"""templates.py - shared shell, canonical @graph, and component renderers for the DIG site."""
from lib import esc, jsonld, deslop

DOMAIN   = "https://digitalinformationgovernance.com"
SITE_NAME = "Digital Information Governance"
TODAY    = "2026-09-05"      # build stamp (passed in; no Date.now in generator runs)

# --- canonical identifiers (entity spine) ---
PERSON_ID  = "https://matthewbertram.com/#person"     # reuse off-domain canonical -> one entity
ORG_ID     = "https://modalpoint.com/#organization"
DIG_ID     = DOMAIN + "/#dig"
PILLARS_ID = DOMAIN + "/#dig-pillars"
SITE_ID    = DOMAIN + "/#website"
USPTO_URL  = "https://uspto.report/TM/99559923"
OG_IMAGE   = DOMAIN + "/og-dig.png"     # branded 1200x630 social card (static asset in site/)

# --- search-console verification (paste tokens to activate; empty = not rendered) ---
GSC_VERIFY  = ""   # Google Search Console: paste the google-site-verification token, then rebuild + redeploy
BING_VERIFY = ""   # Bing Webmaster Tools: paste the msvalidate.01 token, then rebuild + redeploy

CANONICAL_DEF = ("Digital Information Governance (DIG®) is a discipline for keeping "
  "AI-influenced decisions defensible and auditable, ensuring a company's information is "
  "accurately represented, its decisions are traceable, and its AI use is provable to "
  "regulators, partners, and courts.")

PILLARS = [
    ("Information Provenance",  "pillars/information-provenance",
     "Where the information feeding a decision came from, and whether it can be trusted."),
    ("Decision Traceability",   "pillars/decision-traceability",
     "A record of what was decided, by what (human or AI), on what basis, and who is accountable."),
    ("Representation Integrity","pillars/representation-integrity",
     "Keeping the company accurately represented across AI systems, search engines, and data environments."),
    ("Audit Readiness",         "pillars/audit-readiness",
     "Being able to prove, on demand, that AI-influenced decisions met their obligations."),
]

# Canonical weld set (byte-identical to the entity master, verified 2026-06-17 vs live ORCID + Open Library).
# Same @id + same sameAs across every owned property = one resolved entity in the KG and LLMs.
PERSON_SAMEAS = [
    "https://matthewbertram.com/",
    "https://orcid.org/0009-0004-0720-5321",
    "https://doi.org/10.5281/zenodo.17042750",
    "https://openlibrary.org/authors/OL7787306A",
    "https://www.amazon.com/stores/Matthew-Bertram/author/B07FCQXDC7",
    "https://www.crunchbase.com/person/matthew-bertram-c7ef",
    "https://www.linkedin.com/in/mattbertramlive/",
    "https://muckrack.com/matt-bertram",
    "https://www.searchenginejournal.com/author/matt-bertram/",
    "https://www.entrepreneur.com/author/matt-bertram",
    "https://about.me/mattbertram",
    "https://gravatar.com/mattbertramlive",
    "https://www.facebook.com/mattbertramlive1",
    "https://www.instagram.com/matt_bertram_live/",
    "https://www.ewrdigital.com/author/matthew-bertram/",
    "https://bestseopodcast.com/",
    "https://podcasts.apple.com/us/podcast/id303672420",
    USPTO_URL,
]

NAV = [
    ("Definition", "/what-is-digital-information-governance", "definition"),
    ("Framework",  "/framework", "framework"),
    ("White Paper","/white-paper", "whitepaper"),
    ("Pillars",    "/pillars", "pillars"),
    ("Regulations","/regulations", "regulations"),
    ("Glossary",   "/glossary", "glossary"),
    ("FAQ",        "/faq", "faq"),
]

# ---------- shared schema nodes ----------
def person_node():
    return {"@type":"Person","@id":PERSON_ID,"name":"Matthew Bertram",
            "alternateName":["Matt Bertram","Matt Bertram Live"],
            "jobTitle":["AI Keynote Speaker","Owner & CEO of EWR Digital","President of ModalPoint",
                        "Chief Marketing Officer of OGGN"],
            "description":("Matthew (Matt) Bertram is an AI keynote speaker and creator of DIG (Digital Information "
                "Governance). He is owner and CEO of EWR Digital, President of ModalPoint, and CMO of the Oil & Gas "
                "Global Network, and the author of eight books on SEO and growth."),
            "disambiguatingDescription":("Matthew Bertram, Houston-based creator of Digital Information Governance (DIG) "
                "and the LLM Visibility framework; owner and CEO of EWR Digital, President of ModalPoint, host of The Best "
                "SEO Podcast. Not the fractional CTO and AI keynote speaker of the same name."),
            "url":"https://matthewbertram.com/","image":"https://matthewbertram.com/img/mb-otc-headshot.jpg",
            "worksFor":[{"@id":"https://www.ewrdigital.com/#organization"},{"@id":ORG_ID},
                        {"@id":"https://oggn.com/#organization"}],
            "knowsAbout":["AI Search Visibility","Digital Information Governance","AI decision governance",
                          "Generative Engine Optimization","Answer Engine Optimization","Decision Intelligence",
                          "Entity SEO","AI governance"],
            "identifier":[{"@type":"PropertyValue","propertyID":"ORCID","value":"0009-0004-0720-5321"},
                          {"@type":"PropertyValue","propertyID":"Open Library","value":"OL7787306A"},
                          {"@type":"PropertyValue","propertyID":"USPTO Trademark","value":"8147558"}],
            "sameAs":PERSON_SAMEAS}

def org_node():
    # Matt is President of ModalPoint, NOT its founder (entity master rule: never assert a founder edge).
    return {"@type":"Organization","@id":ORG_ID,"name":"ModalPoint","url":"https://modalpoint.com/"}

def dig_node():
    return {"@type":"DefinedTerm","@id":DIG_ID,"name":"Digital Information Governance",
            "alternateName":["DIG","DIG®","AI decision governance"],
            "description":CANONICAL_DEF,
            "disambiguatingDescription":("A decision-centric AI-governance discipline, distinct from "
              "records-management information governance (the storage, retention, and deletion of records)."),
            "termCode":"USPTO Reg. No. 8147558 (Supplemental Register)","creator":{"@id":PERSON_ID},
            "inDefinedTermSet":{"@id":PILLARS_ID},"url":DOMAIN+"/what-is-digital-information-governance",
            "sameAs":[USPTO_URL,"https://modalpoint.com/#dig"]}

def pillars_set_node():
    terms=[{"@type":"DefinedTerm","@id":DOMAIN+"/"+slug+"#term","name":name,"description":desc,
            "inDefinedTermSet":{"@id":PILLARS_ID},"creator":{"@id":PERSON_ID}}
           for name,slug,desc in PILLARS]
    return {"@type":"DefinedTermSet","@id":PILLARS_ID,"name":"The Four Pillars of Digital Information Governance",
            "creator":{"@id":PERSON_ID},"hasDefinedTerm":terms}

def website_node():
    return {"@type":"WebSite","@id":SITE_ID,"url":DOMAIN+"/","name":SITE_NAME,
            "publisher":{"@id":PERSON_ID},"about":{"@id":DIG_ID}}

def shared_nodes():
    return [person_node(), org_node(), dig_node(), website_node()]

def article_node(page, url):
    n={"@type":"Article","@id":url+"#article","headline":page["title"],
       "description":page["description"],"author":{"@id":PERSON_ID},"publisher":{"@id":ORG_ID},
       "datePublished":page.get("datePublished","2026-06-17"),"dateModified":TODAY,"mainEntityOfPage":url,
       "isPartOf":{"@id":SITE_ID},"about":{"@id":DIG_ID},"inLanguage":"en-US",
       "speakable":{"@type":"SpeakableSpecification","cssSelector":[".defbox",".lead"]}}
    return n

def faqpage_node(faqs, url):
    return {"@type":"FAQPage","@id":url+"#faq",
            "mainEntity":[{"@type":"Question","name":deslop(q),
              "acceptedAnswer":{"@type":"Answer","text":deslop(_strip(a))}} for q,a in faqs]}

def breadcrumb_node(crumbs, url):
    items=[{"@type":"ListItem","position":i+1,"name":n,"item":(DOMAIN+u if u else url)}
           for i,(n,u) in enumerate(crumbs)]
    return {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":items}

import re
def _strip(htmlstr):
    return re.sub(r"\s+"," ", re.sub(r"<[^>]+>"," ", htmlstr)).strip()

# ---------- component renderers (for use inside page bodies) ----------
def defbox(text=None, label="Digital Information Governance (DIG®)"):
    text = text or CANONICAL_DEF
    return ('<div class="defbox"><div class="lbl">%s</div><p>%s</p></div>'
            % (esc(label), deslop(text)))

def pillars_grid(link=True):
    out=['<div class="pillars">']
    for i,(name,slug,desc) in enumerate(PILLARS,1):
        h = '<a href="/%s">%s</a>' % (slug,esc(name)) if link else esc(name)
        out.append('<div class="pillar"><div class="n">Pillar %02d</div><h3>%s</h3><p>%s</p></div>'
                   % (i,h,esc(deslop(desc))))
    out.append('</div>')
    return "".join(out)

def pillars_diagram():
    """Inline, crawlable SVG: a classical four-column diagram of the DIG pillars holding up a
    defensible AI-influenced decision. Columns link to the pillar child pages. Hero for /pillars."""
    cols = [
        ("01","Information","Provenance","Where a decision's","inputs came from","/pillars/information-provenance"),
        ("02","Decision","Traceability","Who decided,","and on what basis","/pillars/decision-traceability"),
        ("03","Representation","Integrity","How AI systems","portray the org","/pillars/representation-integrity"),
        ("04","Audit","Readiness","Proof of oversight,","on demand","/pillars/audit-readiness"),
    ]
    cx=[126,282,438,594]
    shafts=[]
    for (num,n1,n2,g1,g2,href),x in zip(cols,cx):
        shafts.append(
          '<a href="%s" aria-label="Pillar %s">' % (href,num) +
          '<rect x="%d" y="110" width="150" height="12" fill="#114b73"/>' % (x-75) +
          '<rect x="%d" y="122" width="138" height="176" fill="#ffffff" stroke="#114b73" stroke-width="1.5"/>' % (x-69) +
          '<line x1="%d" y1="128" x2="%d" y2="292" stroke="#e6e6e6" stroke-width="1"/>' % (x-24,x-24) +
          '<line x1="%d" y1="128" x2="%d" y2="292" stroke="#e6e6e6" stroke-width="1"/>' % (x+24,x+24) +
          '<rect x="%d" y="298" width="150" height="12" fill="#114b73"/>' % (x-75) +
          '<text x="%d" y="151" text-anchor="middle" font-family="Roboto Mono,monospace" font-size="12" font-weight="700" fill="#0a5dbd" letter-spacing="1.5">PILLAR %s</text>' % (x,num) +
          '<text x="%d" y="188" text-anchor="middle" font-family="Merriweather,Georgia,serif" font-size="16" font-weight="700" fill="#1a1a1a">%s</text>' % (x,n1) +
          '<text x="%d" y="208" text-anchor="middle" font-family="Merriweather,Georgia,serif" font-size="16" font-weight="700" fill="#1a1a1a">%s</text>' % (x,n2) +
          '<text x="%d" y="242" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="12" fill="#51565d">%s</text>' % (x,g1) +
          '<text x="%d" y="258" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="12" fill="#51565d">%s</text>' % (x,g2) +
          '</a>')
    svg = (
      '<svg viewBox="0 0 720 372" role="img" aria-labelledby="pil-t pil-d" xmlns="http://www.w3.org/2000/svg">'
      '<title id="pil-t">The four pillars of Digital Information Governance</title>'
      '<desc id="pil-d">Four columns (Information Provenance, Decision Traceability, Representation Integrity, '
      'and Audit Readiness) holding up a defensible, auditable AI-influenced decision on the foundation of the DIG framework.</desc>'
      '<rect x="40" y="44" width="640" height="58" fill="#114b73"/>'
      '<text x="360" y="72" text-anchor="middle" font-family="Merriweather,Georgia,serif" font-size="17" font-weight="700" fill="#ffffff">A defensible, auditable</text>'
      '<text x="360" y="92" text-anchor="middle" font-family="Merriweather,Georgia,serif" font-size="17" font-weight="700" fill="#ffffff">AI-influenced decision</text>'
      '<rect x="40" y="102" width="640" height="4" fill="#f5c636"/>'
      + "".join(shafts) +
      '<rect x="40" y="312" width="640" height="40" fill="#0e3f63"/>'
      '<text x="360" y="337" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="12" font-weight="700" fill="#ffffff" letter-spacing="1">THE FOUR PILLARS OF THE DIG® FRAMEWORK</text>'
      '</svg>')
    return ('<figure class="figure">%s<figcaption>The four pillars of Digital Information Governance (DIG®): '
            'each names a condition an AI-influenced decision must meet to be defensible and auditable.</figcaption></figure>' % svg)

def maturity_diagram():
    """Inline, crawlable SVG: five ascending bars for the DIG Maturity Model (Level 1 ad hoc to
    Level 5 defensible by default), with a dashed trend line. Wired into /dig-maturity-model."""
    bars=[("1","Ad hoc","","58","#8b97a3","#1a1a1a"),
          ("2","Aware","","104","#5f83a3","#ffffff"),
          ("3","Defined","","150","#2f6ea5","#ffffff"),
          ("4","Managed","","196","#114b73","#ffffff"),
          ("5","Defensible","by default","242","#f5c636","#1a1a1a")]
    xs=[40,174,308,442,576]; base=316; frags=[]; tops=[]
    for (num,n1,n2,h,fill,numfill),x in zip(bars,xs):
        h=int(h); top=base-h; cx=x+58; tops.append((cx,top))
        frags.append(
          '<rect x="%d" y="%d" width="116" height="%d" rx="3" fill="%s"/>' % (x,top,h,fill) +
          '<text x="%d" y="%d" text-anchor="middle" font-family="Merriweather,Georgia,serif" font-size="27" font-weight="700" fill="%s">%s</text>' % (cx,top+36,numfill,num) +
          '<text x="%d" y="336" text-anchor="middle" font-family="Roboto Mono,monospace" font-size="11" font-weight="700" fill="#0a5dbd" letter-spacing="1">LEVEL %s</text>' % (cx,num) +
          '<text x="%d" y="353" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="13" font-weight="700" fill="#1a1a1a">%s</text>' % (cx,n1) +
          (('<text x="%d" y="369" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="13" font-weight="700" fill="#1a1a1a">%s</text>' % (cx,n2)) if n2 else ''))
    pts=" ".join("%d,%d" % (cx,top-10) for cx,top in tops)
    svg=(
      '<svg viewBox="0 0 720 384" role="img" aria-labelledby="mat-t mat-d" xmlns="http://www.w3.org/2000/svg">'
      '<title id="mat-t">The DIG Maturity Model</title>'
      '<desc id="mat-d">Five ascending levels of AI decision governance, from Level 1 ad hoc to Level 5 defensible by default, '
      'with decision defensibility increasing at each level.</desc>'
      '<defs><marker id="mk" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0a5dbd"/></marker></defs>'
      '<text x="52" y="40" font-family="Source Sans 3,sans-serif" font-size="12" font-weight="700" fill="#0a5dbd">Increasing decision defensibility &#8594;</text>'
      + "".join(frags) +
      '<line x1="34" y1="%d" x2="700" y2="%d" stroke="#a2a9b1" stroke-width="1.5"/>' % (base,base) +
      '<polyline points="%s" fill="none" stroke="#0a5dbd" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#mk)"/>' % pts +
      '</svg>')
    return ('<figure class="figure">%s<figcaption>The DIG® Maturity Model: five levels of AI decision governance, '
            'from ad hoc (Level 1) to defensible by default (Level 5).</figcaption></figure>' % svg)

def note(html_inner, kind="note"):
    return '<div class="%s">%s</div>' % (kind, html_inner)

def deftable(rows, head=("Term","Definition")):
    out=['<table class="deftable"><tr><th class="term">%s</th><th>%s</th></tr>'%(esc(head[0]),esc(head[1]))]
    for term,defn in rows:
        out.append('<tr><td class="term">%s</td><td>%s</td></tr>'%(esc(term),esc(deslop(defn))))
    out.append('</table>')
    return "".join(out)

# ---------- page shell ----------
def _nav_html(active):
    items=[]
    for label,href,key in NAV:
        cls=' class="on"' if key==active else ''
        items.append('<a%s href="%s">%s</a>'%(cls,href,esc(label)))
    return "".join(items)

def _faq_html(faqs):
    if not faqs: return ""
    out=['<h2 id="faq">Frequently asked questions</h2><div class="faq">']
    for q,a in faqs:
        out.append('<details><summary>%s</summary><div class="a">%s</div></details>'%(esc(deslop(q)),a))
    out.append('</div>')
    return "".join(out)

def _refs_html(refs):
    if not refs: return ""
    lis=[]
    for i,r in enumerate(refs):
        if isinstance(r,(tuple,list)):
            text,url = r[0], r[1]
            lis.append('<li id="r%d">%s <a class="refsrc" href="%s" target="_blank" rel="noopener">View source &#8599;</a></li>'
                       % (i+1, esc(deslop(text)), esc(url)))
        else:
            lis.append('<li id="r%d">%s</li>' % (i+1, esc(deslop(r))))
    return '<div class="refs" id="refs"><h4>References</h4><ol>%s</ol></div>' % "".join(lis)

def _related_html(related):
    if not related: return ""
    links="".join('<a href="%s">%s</a>'%(h,esc(l)) for h,l in related)
    return '<div class="related"><h4>Related</h4>%s</div>'%links

def _cta_html(page):
    if not page.get("cta",True): return ""
    return ('<div class="cta"><b>Put DIG to work in your organization.</b>'
            '<a class="btn" href="https://modalpoint.com/digital-information-governance/">Governance Readiness Assessment &rarr;</a>'
            '<a class="btn ghost" href="https://matthewbertram.com/speaking">Book a keynote on DIG &rarr;</a></div>')

def _toc_html(toc):
    if not toc: return ""
    links="".join('<a href="#%s">%s</a>'%(a,esc(l)) for a,l in toc)
    return '<aside class="toc"><h4>On this page</h4>%s</aside>'%links

def _infobox_html(info):
    if not info: return ""
    rows="".join('<dt>%s</dt><dd>%s</dd>'%(esc(k),v) for k,v in info.get("rows",[]))
    sub='<div class="sub">%s</div>'%esc(info["sub"]) if info.get("sub") else ""
    return '<aside class="infobox"><h4>%s</h4>%s<dl>%s</dl></aside>'%(esc(info.get("title",SITE_NAME)),sub,rows)

def _crumbs_html(crumbs):
    if not crumbs: return ""
    parts=[]
    for n,u in crumbs:
        parts.append('<a href="%s">%s</a>'%(u,esc(n)) if u else esc(n))
    return '<div class="crumbs">%s</div>'%' &rsaquo; '.join(parts)

def _cite_html(page, url):
    if not page.get("byline", True) or page.get("cite", True) is False:
        return ""
    title = page.get("h1", SITE_NAME)
    key = (page["path"] or "home").replace("/", "-")
    apa = ('Bertram, M. (2026). <i>%s</i>. Digital Information Governance (DIG&reg;), '
           'Framework v1.1. %s') % (esc(title), esc(url))
    bib = ("@misc{dig-%s,\n  author = {Bertram, Matthew},\n  title = {%s},\n  year = {2026},\n"
           "  howpublished = {Digital Information Governance (DIG), Framework v1.1},\n"
           "  url = {%s}\n}") % (key, title, url)
    return ('<div class="citebox"><h4>Cite this page</h4><p class="apa">%s</p>'
            '<pre class="bibtex">%s</pre></div>') % (apa, esc(bib))

def render(page):
    path=page["path"]
    url=DOMAIN+"/"+path if path else DOMAIN+"/"
    # schema
    graph=shared_nodes()
    if page.get("article",True): graph.append(article_node(page,url))
    if page.get("faqs"): graph.append(faqpage_node(page["faqs"],url))
    if page.get("breadcrumb"): graph.append(breadcrumb_node(page["breadcrumb"],url))
    graph += page.get("extra_schema",[])
    # body
    has_info = bool(page.get("infobox"))
    has_toc  = bool(page.get("toc"))
    shell_cls = "shell" + ("" if has_toc else " no-toc") + ("" if has_info else " no-info")
    eyebrow='<span class="eyebrow">%s</span>'%esc(page["eyebrow"]) if page.get("eyebrow") else ""
    byline='<p class="byline">Authored by <b>Matthew Bertram</b> &middot; Updated September 2026 &middot; <span class="badge">DIG Framework v1.1</span></p>' if page.get("byline",True) else ""
    main = page["body"] + _faq_html(page.get("faqs")) + _cta_html(page) + _refs_html(page.get("refs")) + _cite_html(page, url) + _related_html(page.get("related"))
    # children order always matches the grid tracks: [toc?] main [infobox?]
    parts = []
    if has_toc: parts.append(_toc_html(page.get("toc")))
    parts.append('<main id="main">%s</main>'%main)
    if has_info: parts.append(_infobox_html(page.get("infobox")))
    cols = "".join(parts)
    canonical = url
    verify = ""
    if GSC_VERIFY:  verify += '<meta name="google-site-verification" content="%s">' % esc(GSC_VERIFY)
    if BING_VERIFY: verify += '<meta name="msvalidate.01" content="%s">' % esc(BING_VERIFY)
    head = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">%(verify)s
<link rel="canonical" href="%(canon)s">
<meta property="og:type" content="article"><meta property="og:site_name" content="%(site)s">
<meta property="og:title" content="%(title)s"><meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:image" content="%(ogimg)s"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%(title)s"><meta name="twitter:description" content="%(desc)s"><meta name="twitter:image" content="%(ogimg)s">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Source+Sans+3:wght@400;600;700&family=Roboto+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='5' fill='%%23114b73'/%%3E%%3Ctext x='16' y='21' font-family='Georgia,serif' font-size='11' font-weight='700' fill='%%23f5c636' text-anchor='middle'%%3EDIG%%3C/text%%3E%%3C/svg%%3E">
%(head_extra)s<script type="application/ld+json">%(schema)s</script>
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast"><div class="in"><a class="wm" href="/" style="color:#fff">Digital Information Governance<small>DIG&reg; &middot; The Standard Reference</small></a><nav>%(nav)s</nav></div></header>
""" % {"title":esc(page["title"]),"desc":esc(page["description"]),"canon":canonical,"site":SITE_NAME,
       "schema":jsonld(graph),"nav":_nav_html(page.get("nav")),"verify":verify,"ogimg":OG_IMAGE,"head_extra":page.get("head_extra","")}
    hero = '<section class="hero"><div class="in">%s%s<h1>%s</h1>%s</div></section>'%(
        _crumbs_html(page.get("breadcrumb")), eyebrow, esc(page["h1"]), byline)
    shell = '<div class="%s">%s</div>'%(shell_cls, cols)
    foot = ('<footer class="foot">&copy; 2026 &middot; Digital Information Governance&reg; is a registered trademark of '
            'Matthew Bertram (USPTO Reg. 8147558). A reference resource, cross-referenced with NIST, the EU AI Act, and ISO/IEC 42001. '
            '&middot; <a href="/">Home</a> &middot; <a href="/glossary">Glossary</a> &middot; <a href="/who-created-dig">About</a> '
            '&middot; <a href="/changelog">Changelog</a> &middot; <a href="https://modalpoint.com">ModalPoint</a></footer>')
    return head + hero + shell + foot + "\n</body></html>\n"
