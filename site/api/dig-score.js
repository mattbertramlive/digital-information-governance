// site/api/dig-score.js
// DIG Maturity Scorer - public, deterministic, SSRF-hardened serverless function.
// Reads a small fixed set of the user's OWN public pages and scores AI decision-governance
// maturity (DIG Levels 1-5 across 4 pillars) from concrete, checkable public signals.
// No npm deps: Node stdlib + globals only (Node 22.x on Vercel).
//
// SECURITY: the only untrusted input is `domain`. Everything else (paths, weights, CTA, webhook)
// is server-controlled. The function never fetches an arbitrary user-supplied URL. It resolves DNS
// once, blocks private/reserved/loopback/link-local/metadata IPs, pins the validated IP at connect
// (closing the DNS-rebinding TOCTOU window), handles redirects manually and re-validates every hop,
// caps fetch count/bytes/per-fetch and total time, and escapes all reflected output.

'use strict';

const dns = require('node:dns/promises');
const net = require('node:net');
const http = require('node:http');
const https = require('node:https');

// Node runtime (NOT Edge: Edge has no node:dns/net, which the resolve-then-pin SSRF defense needs).
// maxDuration is the platform hard-kill backing the in-process 10s budget.
const config = { runtime: 'nodejs', maxDuration: 15 };
module.exports.config = config;

// -------------------- policy constants (server-controlled) --------------------
const UA = 'DIG-MaturityScorer/1.0 (+https://digitalinformationgovernance.com/dig-maturity-scorer; indicative public-signal read; contact: hello@modalpoint.com)';
const MAX_URLS = 6;
const PER_FETCH_TIMEOUT_MS = 4000;
const TOTAL_TIMEOUT_MS = 10000;
const MAX_BYTES = 524288;        // 512 KB decoded
const MAX_REDIRECTS = 3;
const CTA_BASE = 'https://modalpoint.com/digital-information-governance/';

// Server-defined fixed allowlist of well-known governance paths. The user NEVER supplies a path.
// Homepage + robots.txt + the canonical security.txt always run; the rest are probed up to MAX_URLS.
// GOVERNANCE_PATHS is ordered so the first few give one strong page per pillar inside the 6-URL budget:
// /privacy (provenance), /responsible-ai (traceability), /security (audit readiness). Deeper variants
// (/privacy-policy, /terms, /trust, /ai-policy, /compliance, etc.) only run if budget remains.
const ALWAYS_PATHS = ['/', '/robots.txt', '/.well-known/security.txt'];
const GOVERNANCE_PATHS = [
  '/privacy', '/responsible-ai', '/security',
  '/privacy-policy', '/legal/privacy',
  '/terms', '/terms-of-service', '/tos', '/legal/terms',
  '/trust', '/trust-center', '/compliance',
  '/ai', '/ai-policy', '/ai-governance', '/trust/ai', '/ai-principles',
  '/about', '/leadership', '/team', '/company',
  '/security.txt', '/llms.txt',
];

// Reserved / non-public TLDs and labels rejected before DNS.
const RESERVED_TLDS = new Set(['local', 'internal', 'lan', 'home', 'corp', 'test', 'example', 'invalid', 'onion', 'localhost']);

// Blocked CIDRs (IPv4 + IPv6). Checked against the NORMALIZED binary address from dns.lookup,
// never against strings, so alternate notations collapse to their real range.
const BLOCKED_V4 = [
  ['0.0.0.0', 8], ['10.0.0.0', 8], ['100.64.0.0', 10], ['127.0.0.0', 8],
  ['169.254.0.0', 16], ['172.16.0.0', 12], ['192.0.0.0', 24], ['192.0.2.0', 24],
  ['192.88.99.0', 24], ['192.168.0.0', 16], ['198.18.0.0', 15], ['198.51.100.0', 24],
  ['203.0.113.0', 24], ['224.0.0.0', 4], ['240.0.0.0', 4], ['255.255.255.255', 32],
];
const BLOCKED_V6 = [
  ['::', 128], ['::1', 128],
  // ::/96 = IPv4-compatible (deprecated) -> blocks ::a.b.c.d carrying a private v4.
  // 2002::/16 = 6to4 (deprecated) -> blocks 2002:<private-v4>:: tunnels. Neither is ever a
  // legitimate public website address; blocking the whole range is simpler and safer than
  // recursing into the embedded v4, and closes the SSRF bypass the adversarial review flagged.
  ['::', 96], ['2002::', 16],
  ['64:ff9b::', 96], ['100::', 64],
  ['2001:db8::', 32], ['fc00::', 7], ['fe80::', 10], ['ff00::', 8],
];

// -------------------- low-level IP helpers --------------------
function ipv4ToInt(ip) {
  const p = ip.split('.');
  if (p.length !== 4) return null;
  let n = 0;
  for (const part of p) {
    const o = Number(part);
    if (!Number.isInteger(o) || o < 0 || o > 255 || !/^\d+$/.test(part)) return null;
    n = (n * 256) + o;
  }
  return n >>> 0;
}
function inV4Cidr(ipInt, baseIp, bits) {
  const baseInt = ipv4ToInt(baseIp);
  if (baseInt === null) return false;
  if (bits === 0) return true;
  const mask = (0xffffffff << (32 - bits)) >>> 0;
  return (ipInt & mask) === (baseInt & mask);
}
// Expand an IPv6 address to a 16-byte buffer (uses net.isIPv6 + manual parse; handles :: and embedded v4).
function ipv6ToBytes(ip) {
  if (!net.isIPv6(ip)) return null;
  let s = ip;
  // embedded IPv4 (e.g. ::ffff:127.0.0.1 or ::127.0.0.1)
  const v4m = s.match(/^([0-9a-fA-F:]*:)((\d{1,3}\.){3}\d{1,3})$/);
  if (v4m) {
    const v4 = ipv4ToInt(v4m[2]);
    if (v4 === null) return null;
    const hex = v4.toString(16).padStart(8, '0');
    s = v4m[1] + hex.slice(0, 4) + ':' + hex.slice(4);
  }
  const halves = s.split('::');
  if (halves.length > 2) return null;
  const head = halves[0] ? halves[0].split(':') : [];
  const tail = halves.length === 2 ? (halves[1] ? halves[1].split(':') : []) : [];
  let groups;
  if (halves.length === 2) {
    const fill = 8 - head.length - tail.length;
    if (fill < 0) return null;
    groups = head.concat(Array(fill).fill('0'), tail);
  } else {
    groups = head;
  }
  if (groups.length !== 8) return null;
  const bytes = Buffer.alloc(16);
  for (let i = 0; i < 8; i++) {
    const g = groups[i] === '' ? '0' : groups[i];
    if (!/^[0-9a-fA-F]{1,4}$/.test(g)) return null;
    const v = parseInt(g, 16);
    bytes[i * 2] = (v >> 8) & 0xff;
    bytes[i * 2 + 1] = v & 0xff;
  }
  return bytes;
}
function inV6Cidr(bytes, baseIp, bits) {
  const base = ipv6ToBytes(baseIp);
  if (!base) return false;
  let remaining = bits;
  for (let i = 0; i < 16 && remaining > 0; i++) {
    const take = Math.min(8, remaining);
    const mask = take === 8 ? 0xff : (0xff << (8 - take)) & 0xff;
    if ((bytes[i] & mask) !== (base[i] & mask)) return false;
    remaining -= take;
  }
  return true;
}
// Returns true only for a normal global-unicast public address; false (blocked) for anything reserved.
function isPublicIp(ip, family) {
  if (family === 4 || net.isIPv4(ip)) {
    const n = ipv4ToInt(ip);
    if (n === null) return false;
    for (const [base, bits] of BLOCKED_V4) if (inV4Cidr(n, base, bits)) return false;
    return true;
  }
  if (net.isIPv6(ip)) {
    const bytes = ipv6ToBytes(ip);
    if (!bytes) return false;
    // IPv4-mapped (::ffff:0:0/96): re-check the embedded v4 against v4 rules.
    const isMapped = bytes.slice(0, 10).every((b) => b === 0) && bytes[10] === 0xff && bytes[11] === 0xff;
    if (isMapped) {
      const v4 = `${bytes[12]}.${bytes[13]}.${bytes[14]}.${bytes[15]}`;
      return isPublicIp(v4, 4);
    }
    for (const [base, bits] of BLOCKED_V6) if (inV6Cidr(bytes, base, bits)) return false;
    return true;
  }
  return false;
}

// -------------------- input validation --------------------
function validateEmail(raw) {
  if (typeof raw !== 'string') return null;
  const e = raw.trim();
  if (e.length === 0 || e.length > 254) return null;
  if (/[\r\n\0]/.test(e)) return null;
  // conservative RFC-lite, single @
  if ((e.match(/@/g) || []).length !== 1) return null;
  if (!/^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$/.test(e)) return null;
  return e.toLowerCase();
}
class ValidationError extends Error {}
// Normalize + validate the domain into a single registrable public DNS hostname, or throw.
function normalizeDomain(raw) {
  if (typeof raw !== 'string') throw new ValidationError('missing domain');
  let d = raw.trim().toLowerCase();
  if (d.length === 0) throw new ValidationError('missing domain');
  if (/[\r\n\0\t]/.test(d)) throw new ValidationError('invalid domain');
  // strip a single leading scheme
  d = d.replace(/^https?:\/\//, '');
  // strip path/query/fragment and anything after first '/'
  d = d.split('/')[0];
  // reject userinfo and explicit ports/scheme leftovers
  if (d.includes('@')) throw new ValidationError('invalid domain');
  if (d.includes(':')) throw new ValidationError('invalid domain'); // no port, no v6 literal, no scheme
  if (d.includes('?') || d.includes('#') || d.includes('\\') || d.includes(' ')) throw new ValidationError('invalid domain');
  // strip a single leading www. and a trailing dot
  d = d.replace(/^www\./, '').replace(/\.$/, '');
  if (d.length === 0) throw new ValidationError('invalid domain');
  // IDN / unicode -> ASCII (punycode) via the WHATWG URL parser. node:punycode is deprecated, and
  // URL host parsing also normalizes obfuscated IPv4 (hex/octal/decimal) to dotted form, which the
  // net.isIP() reject below then catches. d is already scheme/path/port/userinfo-free at this point.
  let ascii;
  try { ascii = new URL('http://' + d + '/').hostname; } catch { throw new ValidationError('invalid domain'); }
  ascii = ascii.toLowerCase();
  // reject IP literals outright (only DNS hostnames proceed)
  if (net.isIP(ascii) !== 0) throw new ValidationError('invalid domain');
  // also reject bare decimal/hex IPv4-ish all-numeric single labels (e.g. 2130706433, 0x7f000001)
  if (/^[0-9]+$/.test(ascii) || /^0x[0-9a-f]+$/i.test(ascii)) throw new ValidationError('invalid domain');
  // grammar: only a-z0-9.- after punycode
  if (!/^[a-z0-9.-]+$/.test(ascii)) throw new ValidationError('invalid domain');
  if (ascii.length < 1 || ascii.length > 253) throw new ValidationError('invalid domain');
  if (ascii.startsWith('.') || ascii.endsWith('.') || ascii.includes('..')) throw new ValidationError('invalid domain');
  if (ascii.startsWith('-') || ascii.endsWith('-')) throw new ValidationError('invalid domain');
  const labels = ascii.split('.');
  if (labels.length < 2) throw new ValidationError('invalid domain'); // require a dot + TLD
  for (const lbl of labels) {
    if (lbl.length < 1 || lbl.length > 63) throw new ValidationError('invalid domain');
    if (lbl.startsWith('-') || lbl.endsWith('-')) throw new ValidationError('invalid domain');
  }
  const tld = labels[labels.length - 1];
  // TLD must be >=2 letters or a valid xn-- label
  if (!(/^[a-z]{2,}$/.test(tld) || /^xn--[a-z0-9-]+$/.test(tld))) throw new ValidationError('invalid domain');
  // reject localhost and reserved TLDs / *.localhost
  if (ascii === 'localhost' || ascii.endsWith('.localhost')) throw new ValidationError('invalid domain');
  if (RESERVED_TLDS.has(tld)) throw new ValidationError('invalid domain');
  return ascii;
}

// -------------------- resolve + validate all IPs once --------------------
async function resolveAndValidate(host) {
  let addrs;
  try {
    addrs = await dns.lookup(host, { all: true, verbatim: true });
  } catch {
    throw new ValidationError('unresolvable');
  }
  if (!addrs || addrs.length === 0) throw new ValidationError('unresolvable');
  // Reject the WHOLE request if ANY resolved address is non-public (blocks split-horizon / partial rebind).
  for (const a of addrs) {
    if (!isPublicIp(a.address, a.family)) throw new ValidationError('blocked');
  }
  return addrs;
}

// -------------------- pinned fetch (IP locked at connect) --------------------
// One raw request to a SINGLE pinned URL (no redirect following here). Uses node:https / node:http
// (NOT global fetch) so the IP can be truly pinned via the `lookup` option, which the Node http layer
// honors. `servername` sets SNI and the explicit Host header keeps virtual hosts serving correctly,
// so a name is never re-resolved between the validation gate and the socket connect.
// Returns {status, location, body} or throws. Streams + caps bytes (decompression/large-body safe).
function rawRequest(u, pinnedAddr, pinnedFamily, totalSignal) {
  return new Promise((resolve, reject) => {
    const isHttps = u.protocol === 'https:';
    const mod = isHttps ? https : http;
    let settled = false;
    let req;
    const finish = (fn, arg) => { if (settled) return; settled = true; cleanup(); try { if (req) req.destroy(); } catch { /* ignore */ } fn(arg); };

    const onTotalAbort = () => finish(reject, new ValidationError('deadline'));
    const timer = setTimeout(() => finish(reject, new ValidationError('timeout')), PER_FETCH_TIMEOUT_MS);
    function cleanup() {
      clearTimeout(timer);
      if (totalSignal) totalSignal.removeEventListener('abort', onTotalAbort);
    }
    if (totalSignal) {
      if (totalSignal.aborted) { clearTimeout(timer); reject(new ValidationError('deadline')); return; }
      totalSignal.addEventListener('abort', onTotalAbort, { once: true });
    }

    const opts = {
      protocol: u.protocol,
      hostname: u.hostname,
      port: isHttps ? 443 : 80,            // forced standard ports; user port never honored
      path: u.pathname + (u.search || ''),
      method: 'GET',
      // PIN: always hand back the pre-validated IP, never re-resolve the name at connect.
      // Node's http layer calls lookup with {all:true} and expects an array; honor both forms.
      lookup(_hostname, o, cb) {
        if (o && o.all) cb(null, [{ address: pinnedAddr, family: pinnedFamily }]);
        else cb(null, pinnedAddr, pinnedFamily);
      },
      servername: u.hostname,              // SNI for the real hostname
      headers: {
        Host: u.hostname,
        'User-Agent': UA,
        Accept: 'text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.1',
        'Accept-Encoding': 'identity',     // no server-side compression -> byte cap == real bytes
        Connection: 'close',
      },
    };

    try {
      req = mod.request(opts, (res) => {
        const status = res.statusCode || 0;
        const location = res.headers && res.headers.location ? String(res.headers.location) : '';
        if (status >= 300 && status < 400) {
          res.resume(); // drain
          finish(resolve, { status, location, body: '' });
          return;
        }
        const dec = new TextDecoder('utf-8', { fatal: false });
        let text = '';
        let total = 0;
        res.on('data', (chunk) => {
          if (settled) return;
          total += chunk.length;
          if (total > MAX_BYTES) {
            const keep = Math.max(0, MAX_BYTES - (total - chunk.length));
            text += dec.decode(chunk.subarray(0, keep));
            finish(resolve, { status, location: '', body: text });
            return;
          }
          text += dec.decode(chunk, { stream: true });
        });
        res.on('end', () => finish(resolve, { status, location: '', body: text }));
        res.on('error', () => finish(reject, new ValidationError('read')));
      });
      req.on('error', () => finish(reject, new ValidationError('conn')));
      req.on('timeout', () => finish(reject, new ValidationError('timeout')));
      req.setTimeout(PER_FETCH_TIMEOUT_MS);
      req.end();
    } catch (e) {
      finish(reject, new ValidationError('conn'));
    }
  });
}

// Pinned fetch with manual redirect handling. Returns {status, body, finalUrl} or throws.
async function pinnedFetch(urlStr, host, addrs, totalSignal) {
  let currentUrl = urlStr;
  let currentAddrs = addrs;

  for (let hop = 0; hop <= MAX_REDIRECTS; hop++) {
    const u = new URL(currentUrl);
    if (u.protocol !== 'https:' && u.protocol !== 'http:') throw new ValidationError('scheme');
    u.port = '';
    // pin the first validated address (prefer v4, else v6)
    const v4 = currentAddrs.find((a) => a.family === 4);
    const pick = v4 || currentAddrs[0];

    const r = await rawRequest(u, pick.address, pick.family, totalSignal);

    if (r.status >= 300 && r.status < 400) {
      const loc = r.location;
      if (!loc) return { status: r.status, body: '', finalUrl: u.toString() };
      if (/[\r\n\0]/.test(loc)) throw new ValidationError('redirect-crlf');
      let nextUrl;
      try { nextUrl = new URL(loc, u.toString()); } catch { throw new ValidationError('redirect'); }
      if (nextUrl.protocol !== 'https:' && nextUrl.protocol !== 'http:') throw new ValidationError('redirect-scheme');
      // re-run the FULL gate (input + DNS + blocked-CIDR + IP-pin) on the new host before any fetch.
      // normalizeDomain strips a leading www, so the exact-match guard still allows apex<->www and
      // http<->https canonical redirects while refusing any other host (no off-domain / subdomain chasing).
      const nextHost = normalizeDomain(nextUrl.hostname);
      if (nextHost !== host) throw new ValidationError('offdomain');
      const nextAddrs = await resolveAndValidate(nextHost);
      currentUrl = nextUrl.toString();
      currentAddrs = nextAddrs;
      continue;
    }
    return { status: r.status, body: r.body, finalUrl: u.toString() };
  }
  throw new ValidationError('too-many-redirects');
}

// Fetch a single path under host, https first then http fallback on connection error. Never throws to caller.
async function tryFetchPath(host, addrs, path, totalSignal) {
  const schemes = ['https', 'http'];
  for (let i = 0; i < schemes.length; i++) {
    if (totalSignal && totalSignal.aborted) break;
    const scheme = schemes[i];
    const url = `${scheme}://${host}${path}`;
    try {
      const r = await pinnedFetch(url, host, addrs, totalSignal);
      return { ok: true, ...r, path };
    } catch (e) {
      const reason = e instanceof ValidationError ? e.message : 'fetch-error';
      // stop entirely once the global deadline is hit
      if (reason === 'deadline') return { ok: false, error: 'deadline', path };
      // http fallback only on an https connection/timeout failure (not on a security reject like offdomain/blocked)
      const connFail = reason === 'conn' || reason === 'timeout' || reason === 'read' || reason === 'fetch-error';
      if (scheme === 'https' && connFail) continue; // try http
      return { ok: false, error: reason, path };
    }
  }
  return { ok: false, error: 'fetch-error', path };
}

// -------------------- signal scoring (deterministic, no LLM) --------------------
function countHits(hay, phrases) {
  let n = 0;
  for (const p of phrases) if (hay.includes(p)) n++;
  return n;
}
function parseJsonLdOrgs(html) {
  const out = [];
  if (typeof html !== 'string' || html.length === 0) return out;
  // Linear, backtracking-free scan over attacker-controlled HTML. The previous regex
  // (`<script[^>]*type=...[^>]*>([\s\S]*?)</script>` with /g) backtracked catastrophically on
  // crafted input (~6.7s CPU, defeating every timeout). indexOf is O(n) and cannot blow up.
  const hay = html.length > 262144 ? html.slice(0, 262144) : html; // cap scanned bytes
  const lower = hay.toLowerCase();
  let idx = 0;
  let blocks = 0;
  while (blocks < 20) {                       // cap parsed JSON-LD blocks
    const sOpen = lower.indexOf('<script', idx);
    if (sOpen === -1) break;
    const sGt = lower.indexOf('>', sOpen);
    if (sGt === -1) break;
    const openTag = lower.slice(sOpen, sGt);
    idx = sGt + 1;
    if (openTag.indexOf('application/ld+json') === -1) continue;
    const close = lower.indexOf('</script', idx);
    if (close === -1) break;
    const json = hay.slice(sGt + 1, close);
    idx = close + 1;
    if (json.length === 0 || json.length > 65536) continue; // cap per-block JSON size
    blocks++;
    let data;
    try { data = JSON.parse(json.trim()); } catch { continue; } // parse as DATA only, never execute
    const nodes = [];
    const push = (x) => { if (x && typeof x === 'object') nodes.push(x); };
    if (Array.isArray(data)) data.forEach(push);
    else { push(data); if (Array.isArray(data['@graph'])) data['@graph'].forEach(push); }
    for (const node of nodes) {
      let types = node['@type'];
      if (!types) continue;
      if (!Array.isArray(types)) types = [types];
      const t = types.map((x) => String(x).toLowerCase());
      const isOrg = t.some((x) => ['organization', 'corporation', 'localbusiness', 'onlinebusiness', 'ngo', 'educationalorganization', 'governmentorganization'].includes(x));
      if (isOrg && node.name) out.push(node);
    }
  }
  return out;
}

// Each signal: {id, pillar, weight, found(0..1)}. found is fractional credit; contribution = weight*found.
function scoreSignals(pages) {
  // pages: { '/': {status, body}, '/robots.txt': {...}, ... }
  const get = (p) => (pages[p] && pages[p].ok && pages[p].status >= 200 && pages[p].status < 300 ? pages[p] : null);
  const home = get('/');
  const homeBody = home ? home.body.toLowerCase() : '';
  const homeRaw = home ? home.body : '';

  // gather a "fetched text" blob across already-fetched governance pages (no extra fetches)
  const fetchedPaths = Object.keys(pages).filter((p) => get(p));
  const blob = fetchedPaths.map((p) => (pages[p].body || '')).join('\n').toLowerCase();

  const firstHit = (cands, langCheck, minHits) => {
    for (const p of cands) {
      const pg = get(p);
      if (!pg) continue;
      const b = pg.body.toLowerCase();
      if (countHits(b, langCheck) >= minHits) return 1;
    }
    return 0;
  };

  const sig = [];
  const add = (id, label, pillar, weight, found) => sig.push({ id, label, pillar, weight, found: Math.max(0, Math.min(1, found)) });

  // ---- Information Provenance ----
  add('privacy_policy', 'Public privacy policy', 'Information Provenance', 8,
    firstHit(['/privacy', '/privacy-policy', '/legal/privacy'],
      ['personal data', 'data we collect', 'retention', 'data subject', 'gdpr', 'ccpa'], 2));
  add('terms_of_service', 'Public terms of service', 'Information Provenance', 6,
    firstHit(['/terms', '/terms-of-service', '/tos', '/legal/terms'],
      ['terms of service', 'acceptable use', 'liability', 'governing law', 'agreement'], 2));
  {
    const phrases = ['data governance', 'data lineage', 'data provenance', 'source of record', 'data quality', 'master data', 'data classification', 'retention policy', 'records management'];
    const c = countHits(blob, phrases);
    add('data_governance_language', 'Data governance / source-of-record language', 'Information Provenance', 10,
      c >= 2 ? 1 : (c === 1 ? 0.5 : 0));
  }

  // ---- Decision Traceability ----
  add('responsible_ai_policy', 'Responsible-AI / AI usage policy page', 'Decision Traceability', 11,
    firstHit(['/ai', '/ai-policy', '/responsible-ai', '/ai-governance', '/trust/ai', '/ai-principles'],
      ['responsible ai', 'ai governance', 'ai policy', 'human oversight', 'human in the loop', 'model', 'accountability', 'ai principles'], 2));
  {
    const phrases = ['human oversight', 'human in the loop', 'human review', 'accountable for', 'decision owner', 'oversight committee', 'review and approve', 'sign-off', 'audit trail of decisions'];
    const c = countHits(blob, phrases);
    add('human_oversight_accountability', 'Stated human oversight / accountability', 'Decision Traceability', 7,
      c >= 2 ? 1 : (c === 1 ? 0.5 : 0));
  }
  {
    const phrases = ['chief compliance', 'chief risk', 'data protection officer', 'dpo', 'head of governance', 'compliance team', 'risk and compliance', 'governance committee', 'general counsel'];
    const c = countHits(blob, phrases);
    add('governance_or_compliance_role', 'Public governance / compliance / risk function', 'Decision Traceability', 6,
      c >= 1 ? 1 : 0);
  }

  // ---- Representation Integrity ----
  const orgs = home ? parseJsonLdOrgs(homeRaw) : [];
  add('schema_org_organization', 'schema.org Organization structured data', 'Representation Integrity', 9,
    orgs.length > 0 ? 1 : 0);
  {
    let sameAsCount = 0;
    for (const o of orgs) {
      let sa = o.sameAs;
      if (sa) { if (!Array.isArray(sa)) sa = [sa]; sameAsCount += sa.filter(Boolean).length; }
    }
    if (sameAsCount === 0) {
      // fallback: scan homepage for identity links
      const idHosts = ['linkedin.com/company', 'crunchbase.com/organization', 'wikipedia.org', 'wikidata.org', 'twitter.com', 'x.com/', 'facebook.com', 'youtube.com/'];
      sameAsCount = idHosts.filter((h) => homeBody.includes(h)).length;
    }
    add('entity_sameas_links', 'Self-describing entity links (sameAs)', 'Representation Integrity', 6,
      sameAsCount >= 2 ? 1 : (sameAsCount === 1 ? 0.5 : 0));
  }
  {
    const robots = get('/robots.txt');
    const llms = get('/llms.txt');
    let found = 0;
    if (llms && llms.body.trim().length > 0) found = 1;
    else if (robots) {
      const rb = robots.body.toLowerCase();
      const aiAgents = ['gptbot', 'claudebot', 'perplexitybot', 'google-extended', 'ccbot', 'oai-searchbot', 'applebot-extended'];
      if (aiAgents.some((a) => rb.includes(a))) found = 1;
    }
    add('llms_txt_or_ai_directives', 'llms.txt or explicit AI-crawler directives', 'Representation Integrity', 5, found);
  }
  {
    let found = 0;
    if (home) {
      const hasCanon = /<link[^>]+rel=["']canonical["']/i.test(homeRaw);
      const hasTitle = /<title>\s*\S[\s\S]*?<\/title>/i.test(homeRaw);
      const hasDesc = /<meta[^>]+name=["']description["'][^>]+content=["']\s*\S/i.test(homeRaw);
      if (hasCanon && hasTitle && hasDesc) found = 1;
      else if (hasCanon && (hasTitle || hasDesc)) found = 0.5;
    }
    add('canonical_and_metadata_hygiene', 'Canonical tags and clean page metadata', 'Representation Integrity', 4, found);
  }

  // ---- Audit Readiness ----
  {
    let found = 0;
    for (const p of ['/.well-known/security.txt', '/security.txt']) {
      const pg = get(p);
      if (pg && /(^|\n)\s*contact\s*:/i.test(pg.body)) { found = 1; break; }
    }
    add('security_txt', 'security.txt vulnerability-disclosure file', 'Audit Readiness', 6, found);
  }
  add('trust_center_or_security_page', 'Trust center / security page', 'Audit Readiness', 9,
    firstHit(['/security', '/trust', '/trust-center', '/compliance'],
      ['security', 'compliance', 'controls', 'audit', 'encryption', 'access control', 'incident response', 'trust center'], 2));
  {
    const phrases = ['iso/iec 42001', 'iso 42001', 'nist ai rmf', 'ai risk management framework', 'eu ai act', 'traiga'];
    const c = countHits(blob, phrases);
    add('ai_standards_mentions', 'Named AI / governance standards', 'Audit Readiness', 8,
      c >= 2 ? 1 : (c === 1 ? 0.5 : 0));
  }
  {
    const phrases = ['soc 2', 'soc2', 'iso 27001', 'iso/iec 27001', 'hipaa', 'pci dss', 'gdpr compliant', 'fedramp'];
    const c = countHits(blob, phrases);
    add('compliance_certifications', 'Compliance certifications (claimed)', 'Audit Readiness', 5,
      c >= 2 ? 1 : (c === 1 ? 0.5 : 0));
  }

  return sig;
}

const LEVELS = [
  { level: 1, name: 'Ad hoc', min: 0, max: 15 },
  { level: 2, name: 'Aware', min: 15, max: 35 },
  { level: 3, name: 'Defined', min: 35, max: 60 },
  { level: 4, name: 'Managed', min: 60, max: 82 },
  { level: 5, name: 'Defensible by default', min: 82, max: 100 },
];
function levelForPct(pct) {
  for (const L of LEVELS) {
    if (pct >= L.min && pct < L.max) return L;
  }
  return LEVELS[LEVELS.length - 1]; // 100 -> Level 5
}
const PILLAR_KEYS = ['Information Provenance', 'Decision Traceability', 'Representation Integrity', 'Audit Readiness'];

function buildResult(domain, signals) {
  const totalWeight = signals.reduce((s, x) => s + x.weight, 0); // = 100 by design
  const earned = signals.reduce((s, x) => s + x.weight * x.found, 0);
  const pct = totalWeight > 0 ? Math.round((earned / totalWeight) * 100) : 0;
  const L = levelForPct(pct);

  const pillars = {};
  for (const key of PILLAR_KEYS) {
    const ps = signals.filter((s) => s.pillar === key);
    const pw = ps.reduce((s, x) => s + x.weight, 0);
    const pe = ps.reduce((s, x) => s + x.weight * x.found, 0);
    const ppct = pw > 0 ? Math.round((pe / pw) * 100) : 0;
    pillars[key] = { pct: ppct, level: levelForPct(ppct).level };
  }

  const encDomain = encodeURIComponent(domain);
  const cta = `${CTA_BASE}?domain=${encDomain}&level=${L.level}&src=dig-scorer`;

  return {
    ok: true,
    domain, // safe: validated to [a-z0-9.-]; JSON.stringify escapes it regardless
    level: L.level,
    levelName: L.name,
    score: Math.round(earned),
    pct,
    pillars,
    signals: signals.map((s) => ({ id: s.id, label: s.label, pillar: s.pillar, weight: s.weight, found: s.found > 0 })),
    cta,
    disclaimer: 'Indicative read of your public footprint, not an audit. It reads only public pages on your own domain and cannot see internal policies, contracts, or decision logs. A missing public signal is not proof a control is absent.',
  };
}

// -------------------- abuse controls (best-effort, in-memory) --------------------
// NOTE: in-memory limits do NOT hold across Vercel instances. They are a second layer only.
// The real per-deployment ceiling is a Vercel WAF / Firewall rate-limit rule on /api/dig-score
// (documented in the deploy notes) plus the hard per-request caps (MAX_URLS, byte/time limits).
const buckets = new Map(); // ip -> {tokens, ts}
const RL_BURST = 5, RL_REFILL_MS = 4000, RL_MAX = 5;
function rateLimited(ip) {
  const now = Date.now();
  let b = buckets.get(ip);
  if (!b) { b = { tokens: RL_BURST, ts: now }; buckets.set(ip, b); }
  const refill = Math.floor((now - b.ts) / RL_REFILL_MS);
  if (refill > 0) { b.tokens = Math.min(RL_MAX, b.tokens + refill); b.ts = now; }
  if (b.tokens <= 0) return true;
  b.tokens -= 1;
  if (buckets.size > 5000) { const oldest = buckets.keys().next().value; buckets.delete(oldest); } // bounded growth (Map is insertion-ordered)
  return false;
}
let inFlight = 0;
const MAX_INFLIGHT = 6;

// Short per-domain result cache. Repeated scans of the SAME domain (the cheapest amplification
// vector) return a cached body instead of re-fanning-out 6 fetches. Bypassed when an email is
// supplied (POST lead capture must run fresh).
const resultCache = new Map(); // domain -> {body, exp}
const CACHE_TTL_MS = 60000, CACHE_MAX = 1000;
function cacheGet(domain) {
  const e = resultCache.get(domain);
  if (!e) return null;
  if (Date.now() > e.exp) { resultCache.delete(domain); return null; }
  return e.body;
}
function cacheSet(domain, body) {
  if (resultCache.size > CACHE_MAX) { const k = resultCache.keys().next().value; resultCache.delete(k); }
  resultCache.set(domain, { body, exp: Date.now() + CACHE_TTL_MS });
}

// validate the optional lead webhook destination once at boot (env-only, never user input)
let WEBHOOK_OK = false;
let WEBHOOK_URL = '';
(function initWebhook() {
  const u = process.env.LEAD_WEBHOOK_URL;
  if (!u) return;
  try {
    const parsed = new URL(u);
    if (parsed.protocol === 'https:') { WEBHOOK_OK = true; WEBHOOK_URL = u; }
  } catch { /* leave disabled */ }
})();

async function postLead(payload) {
  if (!WEBHOOK_OK) return;
  try {
    const ac = new AbortController();
    const t = setTimeout(() => ac.abort(), 3000);
    await fetch(WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'User-Agent': UA },
      body: JSON.stringify(payload),
      signal: ac.signal,
    });
    clearTimeout(t);
  } catch { /* never let webhook failure affect the user response */ }
}

// -------------------- handler --------------------
function sendJson(res, status, obj) {
  const body = JSON.stringify(obj);
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.end(body);
}
// single generic error envelope: no internal IP / host / timing detail leaked
function sendError(res, status) {
  sendJson(res, status, { ok: false, error: 'Could not score this domain. Check it is a public website and try again.' });
}

function getQueryParam(req, name) {
  if (req.query && typeof req.query[name] !== 'undefined') {
    const v = req.query[name];
    return Array.isArray(v) ? v[0] : v;
  }
  try {
    const u = new URL(req.url, 'http://x');
    return u.searchParams.get(name);
  } catch { return null; }
}
async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') { try { return JSON.parse(req.body); } catch { return {}; } }
  return await new Promise((resolve) => {
    let data = ''; let size = 0;
    req.on('data', (c) => { size += c.length; if (size > 8192) { data = '{}'; req.destroy(); } else data += c; });
    req.on('end', () => { try { resolve(JSON.parse(data || '{}')); } catch { resolve({}); } });
    req.on('error', () => resolve({}));
  });
}

module.exports = async function handler(req, res) {
  // env kill-switch (cut the endpoint without a redeploy)
  if (process.env.DIG_SCORER_DISABLED) { sendJson(res, 503, { ok: false, error: 'Temporarily unavailable.' }); return; }

  // method gate
  const method = (req.method || 'GET').toUpperCase();
  if (method !== 'GET' && method !== 'POST') { res.setHeader('Allow', 'GET, POST'); sendError(res, 405); return; }

  // per-IP rate limit (best-effort, first XFF hop)
  const xff = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  if (rateLimited(xff)) { res.setHeader('Retry-After', '4'); sendJson(res, 429, { ok: false, error: 'Too many requests. Please wait a moment.' }); return; }
  if (inFlight >= MAX_INFLIGHT) { res.setHeader('Retry-After', '2'); sendJson(res, 429, { ok: false, error: 'Busy. Please retry shortly.' }); return; }

  let rawDomain = null;
  let email = null;
  if (method === 'GET') {
    rawDomain = getQueryParam(req, 'domain');
  } else {
    const body = await readBody(req);
    rawDomain = (body && body.domain) || getQueryParam(req, 'domain');
    if (body && body.email) email = validateEmail(body.email);
  }

  let domain;
  try {
    domain = normalizeDomain(rawDomain);
  } catch {
    sendError(res, 400);
    return;
  }

  // serve a fresh-enough cached body for repeat scans of the same domain (skip when capturing a lead)
  if (!email) {
    const cached = cacheGet(domain);
    if (cached) { sendJson(res, 200, cached); return; }
  }

  inFlight++;
  const totalAC = new AbortController();
  const totalTimer = setTimeout(() => totalAC.abort(), TOTAL_TIMEOUT_MS);
  try {
    // resolve + validate ALL IPs once (fail closed on any private/reserved hit)
    let addrs;
    try {
      addrs = await resolveAndValidate(domain);
    } catch {
      sendError(res, 400);
      return;
    }

    // build the fetch set: always-paths first, then governance paths up to MAX_URLS
    const pathSet = [];
    for (const p of ALWAYS_PATHS) { if (pathSet.length < MAX_URLS) pathSet.push(p); }
    for (const p of GOVERNANCE_PATHS) { if (pathSet.length >= MAX_URLS) break; pathSet.push(p); }

    // fetch sequentially under the shared total deadline; stop early if deadline hit
    const pages = {};
    for (const p of pathSet) {
      if (totalAC.signal.aborted) break;
      const r = await tryFetchPath(domain, addrs, p, totalAC.signal);
      pages[p] = r;
    }

    // Honesty gate: if we could not actually read the homepage, do NOT emit a confident "Level 1".
    // A 403/JS-wall/timeout on the home page means we saw nothing, which is not a governance finding.
    const homePage = pages['/'];
    const isOk = (pg) => pg && pg.ok && pg.status >= 200 && pg.status < 300;
    const fetchedOk = Object.keys(pages).filter((p) => isOk(pages[p])).length;

    if (!isOk(homePage)) {
      const honest = {
        ok: true,
        reachable: false,
        domain,
        message: "We could not read this site's public pages from our scanner. That usually means it blocks automated requests, needs JavaScript to render, or was briefly unreachable. It is not itself a governance finding. Try a domain that serves static HTML, or book a hands-on review.",
        cta: `${CTA_BASE}?domain=${encodeURIComponent(domain)}&src=dig-scorer&reachable=0`,
        disclaimer: 'Indicative read of your public footprint, not an audit.',
      };
      if (!email) cacheSet(domain, honest);
      sendJson(res, 200, honest);
      return;
    }

    // Score from whatever we gathered (graceful partial result if some governance pages failed).
    const signals = scoreSignals(pages);
    const result = buildResult(domain, signals);
    result.reachable = true;
    result.coverage = { pagesRead: fetchedOk, pagesAttempted: pathSet.length };
    if (fetchedOk <= 2) result.lowConfidence = true; // homepage read but little else -> flag low confidence

    if (!email) cacheSet(domain, result);

    // optional lead webhook (only after a successful score; never on validation failures).
    // awaited so the lead survives the function freeze after the response (it has its own 3s timeout
    // and swallows all errors, so it can neither hang nor break the user response).
    if (WEBHOOK_OK) {
      await postLead({ domain: result.domain, level: result.level, score: result.score, signals: result.signals, email: email || undefined });
    }

    sendJson(res, 200, result);
  } catch (e) {
    sendError(res, 502);
  } finally {
    clearTimeout(totalTimer);
    inFlight = Math.max(0, inFlight - 1);
  }
};
module.exports.config = config;

// test-only hooks: inert in production, enabled with DIG_TEST=1 so the smoke test can exercise the
// internal SSRF / parsing logic directly. Never referenced by the request handler.
if (process.env.DIG_TEST) {
  module.exports._test = { parseJsonLdOrgs, isPublicIp, normalizeDomain, ipv6ToBytes, scoreSignals, buildResult, levelForPct };
}