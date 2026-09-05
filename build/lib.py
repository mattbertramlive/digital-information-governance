"""lib.py - stdlib helpers for the DIG static-site generator.
No third-party deps required for generation (truststore/requests only used by verify/cutover).
"""
import os, re, html, json, unicodedata

SITE_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "site"))

# ---- text ----
def esc(s):
    return html.escape(str(s), quote=True)

def slugify(text, maxlen=90):
    t = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:maxlen].strip("-")

# AI-tell / em-dash de-slop gate (house rule: no em/en dashes, no AI tells)
_AI_TELLS = re.compile(r"\b(delve|leverage|robust|seamless|moreover|furthermore|"
                       r"in today's|in conclusion|it's not just|navigating the|"
                       r"unlock|elevate|in the realm of|tapestry|testament to)\b", re.I)

def deslop(text):
    """Replace em/en dashes; numeric ranges keep a hyphen, clause dashes become commas/spaces."""
    if text is None:
        return text
    s = str(text)
    # numeric range  12 - 34  -> 12-34
    s = re.sub(r"(\d)\s*[–—]\s*(\d)", r"\1-\2", s)
    # spaced clause dash -> comma
    s = re.sub(r"\s*[–—]\s*", ", ", s)
    s = s.replace("–", "-").replace("—", "-")
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    return s

def deslop_warn(text, where=""):
    """Return list of AI-tell hits for QA (does not mutate)."""
    if not text:
        return []
    return [(where, m.group(0)) for m in _AI_TELLS.finditer(str(text))]

# ---- json-ld ----
def jsonld(graph):
    payload = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

# ---- write ----
def write_site(rel_path, content):
    out = os.path.join(SITE_ROOT, rel_path.replace("/", os.sep))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return out
