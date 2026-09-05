# -*- coding: utf-8 -*-
"""content.py - authored pages for the DIG site (Tier 1: definitional core)."""
from templates import defbox, pillars_grid, pillars_diagram, note, deftable, pillars_set_node, PILLARS, DOMAIN, PERSON_ID, ORG_ID, SITE_ID, DIG_ID, TODAY

# (text, url) tuples -> rendered as live outbound trust links to primary sources.
# Order is load-bearing: page bodies cite #r1=NIST, #r2=IG/records, #r3=EU AI Act/ISO/TRAIGA, #r4=USPTO.
REFS_CORE = [
    ("NIST AI Risk Management Framework (AI RMF 1.0): Govern, Map, Measure, Manage. National Institute of Standards and Technology, 2023.",
     "https://www.nist.gov/itl/ai-risk-management-framework"),
    ("Information governance: the records and data lifecycle discipline (storage, retention, disposition), distinct from AI decision governance. ARMA International, Generally Accepted Recordkeeping Principles; AIIM.",
     "https://www.arma.org/"),
    ("EU AI Act, Regulation (EU) 2024/1689 (Official Journal of the European Union); ISO/IEC 42001:2023; Texas Responsible AI Governance Act (TRAIGA).",
     "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
    ("USPTO Trademark Reg. No. 8147558 (Supplemental Register), Digital Information Governance / DIG, owner Matthew Bertram.",
     "https://uspto.report/TM/99559923"),
]

PAGES = []

# ---------------- 1. HOME / hub ----------------
PAGES.append({
 "path":"", "nav":None, "title":"Digital Information Governance (DIG®) - Definition, Framework & Pillars",
 "description":"Digital Information Governance (DIG®) is the discipline of AI decision governance: keeping AI-influenced decisions defensible and auditable. Definition, the four pillars, and the framework by Matthew Bertram.",
 "eyebrow":"The discipline of AI decision governance", "h1":"Digital Information Governance (DIG®)",
 "byline":True,
 "infobox":{"title":"Digital Information Governance","sub":"DIG®","rows":[
    ("Also called","AI decision governance"),("Type","Governance discipline / framework"),
    ("Coined by","Matthew Bertram"),("Registered mark","DIG® · USPTO Reg. 8147558"),
    ("Framework version","v1.1 (2026)"),
    ("White paper",'<a href="/white-paper">DIG® White Paper (PDF)</a>'),
    ("Pillars",'<a href="/pillars/information-provenance">Provenance</a> · <a href="/pillars/decision-traceability">Traceability</a> · <a href="/pillars/representation-integrity">Representation</a> · <a href="/pillars/audit-readiness">Audit</a>'),
    ("Related",'<a href="/ai-decision-governance">AI decision governance</a>, <a href="/decision-integrity">decision integrity</a>')]},
 "body": defbox() +
   '<p class="lead">In plain terms, DIG is <strong>AI decision governance</strong>: making sure that when AI shapes a decision, an organization can still show what was decided, on what basis, and who is accountable. It is the <strong>decision layer</strong> that sits on top of data governance, information governance, and AI governance.<sup><a href="#r1">[1]</a></sup></p>' +
   note('<b>Not records-management "information governance."</b> Traditional information governance (Gartner, ARMA, AIIM) governs how records and data are stored, retained, and deleted. Digital Information Governance governs how AI-influenced <em>decisions</em> are made defensible. See <a href="/compare/dig-vs-information-governance">DIG vs. information governance</a>.<sup><a href="#r2">[2]</a></sup>') +
   '<h2 id="pillars">The four pillars</h2>'
   '<p>DIG is built on four pillars. Each maps to obligations now appearing across NIST, the EU AI Act, ISO/IEC 42001, and US state law such as Texas\'s TRAIGA.<sup><a href="#r3">[3]</a></sup></p>' +
   pillars_grid() +
   '<h2 id="explore">Explore the reference</h2>'
   '<div class="grid">'
   '<a class="gcard" href="/white-paper"><h3>The white paper</h3><p>The full 42-page DIG standard, free as a PDF: the four pillars, the maturity model, the seven principles, and the operating model.</p></a>'
   '<a class="gcard" href="/what-is-digital-information-governance"><h3>Definition</h3><p>The canonical definition and how DIG differs from records-management information governance.</p></a>'
   '<a class="gcard" href="/framework"><h3>The framework</h3><p>The four pillars as a working system, mapped to the major AI regulations.</p></a>'
   '<a class="gcard" href="/ai-decision-governance"><h3>AI decision governance</h3><p>The category DIG belongs to, and why the decision layer is now the governance frontier.</p></a>'
   '<a class="gcard" href="/ai-agent-governance"><h3>AI agent governance</h3><p>New in v1.1: governing AI that acts. The five questions to ask once an AI holds a keyboard, a terminal, and a browser.</p></a>'
   '<a class="gcard" href="/ai-regulation-tracker"><h3>Regulation tracker</h3><p>Dated status for every regime we track, from the EU AI Act Omnibus deferrals to TRAIGA. Reviewed monthly.</p></a>'
   '<a class="gcard" href="/ai-agent-incident-register"><h3>Incident register</h3><p>Documented AI-agent incidents, classified by which authorization question failed. Opens with one of our own.</p></a>'
   '<a class="gcard" href="/regulations"><h3>Regulations</h3><p>How DIG maps to NIST AI RMF, the EU AI Act, ISO 42001, and TRAIGA.</p></a>'
   '<a class="gcard" href="/glossary"><h3>Glossary</h3><p>Defined terms: provenance, traceability, representation integrity, audit readiness, and more.</p></a>'
   '<a class="gcard" href="/who-created-dig"><h3>Who created DIG</h3><p>Matthew Bertram coined the discipline and holds the DIG® trademark.</p></a>'
   '<a class="gcard" href="/dig-maturity-model"><h3>Maturity model</h3><p>Score how defensible your AI-influenced decisions are, across five levels.</p></a>'
   '<a class="gcard" href="/ai-governance-statistics"><h3>Statistics</h3><p>Verified, primary-sourced figures on AI adoption, the governance gap, and regulation.</p></a>'
   '<a class="gcard" href="/dig-maturity-self-assessment"><h3>Free self-assessment</h3><p>Score your AI decision governance in eight questions. Nothing leaves your browser.</p></a>'
   '<a class="gcard" href="/dig-maturity-scorer"><h3>Score your live site</h3><p>Enter your domain and the scorer reads your public pages for AI governance signals. No login, nothing stored.</p></a>'
   '</div>',
 "faqs":[
   ("What is Digital Information Governance (DIG®)?",
    "<p>Digital Information Governance (DIG®) is a discipline for keeping AI-influenced decisions defensible and auditable, ensuring a company's information is accurately represented, its decisions are traceable, and its AI use is provable to regulators, partners, and courts. It is commonly described as AI decision governance.</p>"),
   ("How is DIG different from information governance?",
    "<p>Traditional information governance governs the storage, retention, and deletion of records and data. DIG is decision-centric: it governs how AI-influenced decisions are made defensible. DIG is the decision layer on top of data, information, and AI governance.</p>"),
   ("Who created Digital Information Governance?",
    "<p>Matthew Bertram, President of ModalPoint and CEO of EWR Digital, coined the discipline and holds the registered trademark DIG® (USPTO Reg. No. 8147558).</p>"),
   ("What are the four pillars of DIG?",
    "<p>Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness.</p>"),
 ],
 "refs":REFS_CORE,
 "extra_schema":[pillars_set_node()],
 "breadcrumb":None,
})

# ---------------- 2. Definition pillar ----------------
PAGES.append({
 "path":"what-is-digital-information-governance","nav":"definition",
 "title":"What Is Digital Information Governance (DIG®)? - Definition",
 "description":"A clear definition of Digital Information Governance (DIG®): the discipline of keeping AI-influenced decisions defensible and auditable. How it differs from records-management information governance.",
 "eyebrow":"Definition","h1":"What is Digital Information Governance?","byline":True,
 "breadcrumb":[("Home","/"),("Definition","")],
 "toc":[("def","Definition"),("plain","In plain terms"),("distinct","How it differs from IG"),("layers","The governance layers"),("pillars","The four pillars"),("refs","References")],
 "infobox":{"title":"Digital Information Governance","sub":"DIG®","rows":[
    ("Short answer","Keeping AI-influenced decisions defensible and auditable."),
    ("Also called","AI decision governance"),("Coined by","Matthew Bertram"),
    ("Registered mark","USPTO Reg. 8147558"),("Distinct from","Records-management information governance")]},
 "body":
   '<h2 id="def">Definition</h2>' + defbox() +
   '<h2 id="plain">In plain terms</h2>'
   '<p class="lead">When AI shapes a decision, who can answer for it later? DIG is the discipline that makes sure the answer is always "we can." It keeps a record of what the AI recommended, what information it used, who reviewed it, and on what authority the decision was made, so the decision can be defended to a regulator, a partner, or a court.<sup><a href="#r1">[1]</a></sup></p>' +
   '<h2 id="distinct">How DIG differs from information governance</h2>'
   '<p>The phrase looks close to "information governance," but the two govern different things. Information governance, as defined by Gartner, ARMA, and AIIM, is about the lifecycle of records and data: how information is created, stored, retained, and deleted.<sup><a href="#r2">[2]</a></sup> Digital Information Governance is about <strong>decisions</strong>: whether an AI-influenced decision can be defended after the fact.</p>' +
   note('Read the full comparison: <a href="/compare/dig-vs-information-governance">DIG vs. information governance</a>.') +
   '<h2 id="layers">The governance layers</h2>'
   '<p>Most organizations already run several governance disciplines. DIG sits at the top of the stack:</p>' +
   deftable([
     ("Data governance","Governs structured data: quality, lineage, access, and cataloging."),
     ("Information governance","Governs all information and records: retention, compliance, e-discovery."),
     ("AI governance","Governs models: bias, drift, explainability, and model risk."),
     ("Digital Information Governance","Governs the decision: whether an AI-influenced decision is defensible and auditable."),
   ], head=("Discipline","What it governs")) +
   '<h2 id="pillars">The four pillars</h2>' + pillars_grid(),
 "faqs":[
   ("Is Digital Information Governance the same as information governance?",
    "<p>No. Information governance manages the records and data lifecycle. Digital Information Governance manages whether AI-influenced decisions are defensible and auditable. DIG is decision-centric; information governance is records-centric.</p>"),
   ("Is DIG a registered trademark?",
    "<p>Yes. DIG® / Digital Information Governance® is a registered trademark of Matthew Bertram (USPTO Reg. No. 8147558).</p>"),
 ],
 "refs":REFS_CORE,
 "extra_schema":[pillars_set_node()],
 "related":[("/framework","The framework"),("/ai-decision-governance","AI decision governance"),("/compare/dig-vs-information-governance","DIG vs. information governance"),("/glossary","Glossary")],
})

# ---------------- 3. Framework ----------------
PAGES.append({
 "path":"framework","nav":"framework",
 "title":"The Digital Information Governance Framework (DIG®) - Four Pillars",
 "description":"The DIG framework: four pillars (Information Provenance, Decision Traceability, Representation Integrity, Audit Readiness) for governing AI-influenced decisions, mapped to NIST, the EU AI Act, and ISO 42001.",
 "eyebrow":"Framework","h1":"The DIG Framework","byline":True,
 "breadcrumb":[("Home","/"),("Framework","")],
 "toc":[("intro","Overview"),("p1","Information Provenance"),("p2","Decision Traceability"),("p3","Representation Integrity"),("p4","Audit Readiness"),("map","Regulatory map"),("refs","References")],
 "infobox":{"title":"DIG Framework","sub":"v1.0 (2026)","rows":[
    ("Pillars","4"),("Maps to","NIST AI RMF, EU AI Act, ISO 42001, TRAIGA"),
    ("Author","Matthew Bertram"),("Use","Assess and govern AI-influenced decisions")]},
 "body":
   '<h2 id="intro">Overview</h2>'
   '<p class="lead">The DIG framework turns a one-line definition into something an organization can act on. It names the four things that have to be true for an AI-influenced decision to be defensible, and gives each one a place in the governance program.</p>' +
   pillars_grid() +
   '<h2 id="p1">Pillar 1: Information Provenance</h2>'
   '<p>Every decision rests on information. Provenance asks where that information came from and whether it can be trusted: the source, the chain of custody, and the freshness. Without provenance, a decision cannot be reconstructed or defended.<sup><a href="#r1">[1]</a></sup></p>'
   '<h2 id="p2">Pillar 2: Decision Traceability</h2>'
   '<p>Traceability is the record of the decision itself: what was recommended, by which system, on what basis, who reviewed it, and on what authority it was acted on. It is the difference between "the AI did it" and "a named person decided, and here is the trail."</p>'
   '<h2 id="p3">Pillar 3: Representation Integrity</h2>'
   '<p>AI systems now describe your company to the outside world. Representation integrity is keeping that description accurate across AI search, models, and data environments, because a misrepresentation becomes evidence a regulator, partner, or court can cite. See <a href="/pillars/representation-integrity">Representation Integrity</a>.</p>'
   '<h2 id="p4">Pillar 4: Audit Readiness</h2>'
   '<p>Audit readiness is the ability to prove, on demand, that the first three pillars held. It is the posture that turns "we have AI policies" into "we can show our oversight worked."</p>'
   '<h2 id="map">How the pillars map to regulation</h2>'
   '<p>The four pillars are not arbitrary. They correspond to controls described across the major AI governance regimes, where most obligations overlap.</p>' +
   deftable([
     ("Information Provenance","NIST AI RMF (Map); EU AI Act data governance; ISO 42001 data quality."),
     ("Decision Traceability","NIST AI RMF (Govern/Manage); EU AI Act record-keeping and human oversight."),
     ("Representation Integrity","Consumer-protection and disclosure rules; AI-search accuracy."),
     ("Audit Readiness","EU AI Act conformity/logging; ISO 42001 audit; TRAIGA documentation."),
   ], head=("Pillar","Maps to")),
 "refs":REFS_CORE,
 "extra_schema":[pillars_set_node()],
 "related":[("/what-is-digital-information-governance","Definition"),("/dig-maturity-model","Maturity model"),("/ai-risk-management","AI risk management"),("/regulations","Regulations"),("/decision-integrity","Decision integrity")],
})

# ---------------- 4-7. Pillar pages ----------------
PILLAR_CONTENT = {
 "pillars/information-provenance":{
   "h1":"Information Provenance","short":"Where the information feeding a decision came from, and whether it can be trusted.",
   "title":"Information Provenance (DIG® Pillar 1) - Definition",
   "desc":"Information Provenance, the first pillar of Digital Information Governance: knowing where the information feeding an AI-influenced decision came from, and whether it can be trusted.",
   "body":"<p>If you cannot say where a decision's inputs came from, you cannot defend the decision. Information provenance is the discipline of recording the source, chain of custody, and freshness of the information that feeds an AI-influenced decision. It is the foundation the other three pillars stand on.</p>"
          "<p>In practice, provenance means tracking which data, documents, and model outputs informed a decision; whether those sources were authoritative and current; and whether they were altered along the way. When a decision is later challenged, provenance is what lets an organization reconstruct it faithfully rather than guess.</p>"
          "<p>Provenance maps to the NIST AI RMF Map function and to the data-governance obligations in the EU AI Act and ISO/IEC 42001.</p>"},
 "pillars/decision-traceability":{
   "h1":"Decision Traceability","short":"A record of what was decided, by what, on what basis, and who is accountable.",
   "title":"Decision Traceability (DIG® Pillar 2) - Definition",
   "desc":"Decision Traceability, the second pillar of Digital Information Governance: a defensible record of what an AI-influenced decision was, who made it, on what basis, and who is accountable.",
   "body":"<p>Decision traceability is the record of the decision itself. It captures what was recommended, by which human or AI system, on what basis, who reviewed it, and on what authority it was acted on. Traceability is what separates a defensible decision from an unaccountable one.</p>"
          "<p>The discipline matters most when an AI recommendation is accepted with little human change. Without a trace, the organization cannot show that a human stayed accountable. With a trace, it can prove who decided and why, which is exactly what regulators and courts ask for.</p>"
          "<p>Traceability maps to the NIST AI RMF Govern and Manage functions and to the record-keeping and human-oversight requirements of the EU AI Act.</p>"},
 "pillars/representation-integrity":{
   "h1":"Representation Integrity","short":"Keeping the company accurately represented across AI systems, search, and data environments.",
   "title":"Representation Integrity (DIG® Pillar 3) - Definition",
   "desc":"Representation Integrity, the third pillar of Digital Information Governance: keeping a company accurately represented across AI systems, search engines, and data environments.",
   "body":"<p>AI systems now describe your company to buyers, partners, regulators, and courts. Representation integrity is the discipline of keeping that description accurate across AI search, large language models, and the data environments that feed them.</p>"
          "<p>This pillar connects governance to AI visibility. When an AI answer engine misstates what a company does, how it operates, or what it is permitted to do, that statement can become evidence. Representation integrity treats the external AI narrative as a governable control surface, not a marketing afterthought.</p>"
          "<p>It is the pillar that links DIG to generative engine optimization and answer engine optimization, governed for accuracy rather than promotion.</p>"},
 "pillars/audit-readiness":{
   "h1":"Audit Readiness","short":"Being able to prove, on demand, that AI-influenced decisions met their obligations.",
   "title":"Audit Readiness (DIG® Pillar 4) - Definition",
   "desc":"Audit Readiness, the fourth pillar of Digital Information Governance: being able to prove, on demand, that AI-influenced decisions met their obligations.",
   "body":"<p>Audit readiness is the posture that turns governance from a policy into proof. It is the ability to show, on demand, that provenance was tracked, decisions were traceable, and representation stayed accurate. It is the pillar regulators test first.</p>"
          "<p>An organization is audit-ready when it can produce the decision trail for any AI-influenced decision without a scramble: the inputs, the reviewers, the authority, and the controls that applied. Audit readiness is becoming a client requirement as well as a regulatory one.</p>"
          "<p>It maps to the EU AI Act conformity and logging obligations, ISO/IEC 42001 audit requirements, and TRAIGA documentation duties.</p>"},
}
for slug,info in PILLAR_CONTENT.items():
    name=info["h1"]
    others=[(("/"+s),n) for n,s,_ in PILLARS if s!=slug]
    PAGES.append({
      "path":slug,"nav":"pillars","title":info["title"],"description":info["desc"],
      "eyebrow":"DIG Framework · Pillar","h1":name,"byline":True,
      "breadcrumb":[("Home","/"),("Framework","/framework"),("Pillars","/pillars"),(name,"")],
      "infobox":{"title":name,"sub":"DIG® Pillar","rows":[
         ("Part of",'<a href="/framework">The DIG framework</a>'),
         ("In one line",info["short"]),("Coined by","Matthew Bertram")]},
      "body":defbox(name+" is "+info["short"][0].lower()+info["short"][1:]) + info["body"],
      "related":[("/framework","The framework"),("/pillars","All four pillars")]+others+[("/glossary","Glossary")],
      "refs":REFS_CORE,
    })

# ---------------- 7b. Pillars hub (parent of the four pillar pages) ----------------
PAGES.append({
 "path":"pillars","nav":"pillars",
 "title":"The Four Pillars of Digital Information Governance (DIG®)",
 "description":"The four pillars of Digital Information Governance (DIG®): Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness. Together they define what makes an AI-influenced decision defensible and auditable.",
 "eyebrow":"DIG Framework","h1":"The Four Pillars of DIG","byline":True,
 "breadcrumb":[("Home","/"),("Framework","/framework"),("Pillars","")],
 "toc":[("diagram","The four pillars"),("pillars","Each pillar"),("together","How they work together")],
 "infobox":{"title":"The Four Pillars","sub":"DIG® Framework","rows":[
    ("Pillar 01",'<a href="/pillars/information-provenance">Information Provenance</a>'),
    ("Pillar 02",'<a href="/pillars/decision-traceability">Decision Traceability</a>'),
    ("Pillar 03",'<a href="/pillars/representation-integrity">Representation Integrity</a>'),
    ("Pillar 04",'<a href="/pillars/audit-readiness">Audit Readiness</a>'),
    ("Coined by","Matthew Bertram")]},
 "body":
   defbox("The four pillars of Digital Information Governance (DIG®) are Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness. Together they define what must be true for an AI-influenced decision to be defensible and auditable.", label="The Four Pillars of DIG®") +
   '<p class="lead" id="diagram">Digital Information Governance rests on four pillars. Each names one thing that must be true for an AI-influenced decision to hold up under scrutiny: you know where its information came from, you can trace who decided and why, the organization is accurately represented to the AI systems around the decision, and you can prove all of it on demand.</p>' +
   pillars_diagram() +
   '<h2 id="pillars">The four pillars</h2>'
   '<p>Each pillar is a standalone discipline with its own definition, controls, and regulatory mapping. Follow any pillar for the full treatment.</p>' +
   pillars_grid(link=True) +
   '<h2 id="together">How the pillars work together</h2>'
   '<p>The pillars are sequential as much as parallel. <a href="/pillars/information-provenance">Information Provenance</a> establishes what a decision was based on; <a href="/pillars/decision-traceability">Decision Traceability</a> records who turned that information into a decision and on what authority; <a href="/pillars/representation-integrity">Representation Integrity</a> keeps the AI systems around that decision accurate about the organization; and <a href="/pillars/audit-readiness">Audit Readiness</a> makes the whole chain provable when a regulator, partner, or court asks. Miss one and the decision has a gap a challenger can open.</p>'
   '<p>The <a href="/framework">DIG framework</a> assembles the four pillars into a single operating model, and the <a href="/dig-maturity-model">DIG Maturity Model</a> scores how reliably an organization applies them, from ad hoc to defensible by default.</p>',
 "faqs":[
   ("What are the four pillars of Digital Information Governance?","<p>Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness. Each names a condition that must hold for an AI-influenced decision to be defensible and auditable.</p>"),
   ("Why four pillars?","<p>Each pillar closes a different gap a challenger could exploit: unknown inputs (provenance), unaccountable decisions (traceability), false external representation (representation integrity), and unprovable oversight (audit readiness). Together they cover the full life of an AI-influenced decision.</p>"),
   ("Which pillar matters most?","<p>They are interdependent, but Audit Readiness is the one regulators test first, and Information Provenance is the foundation the others rest on. A mature program treats all four as standard practice, which the DIG Maturity Model calls Level 3 and above.</p>"),
 ],
 "extra_schema":[pillars_set_node()],
 "refs":REFS_CORE,
 "related":[("/framework","The framework"),("/dig-maturity-model","Maturity model"),("/white-paper","White paper"),("/glossary","Glossary")],
})

# ---------------- 8. Glossary ----------------
GLOSSARY=[
 ("Digital Information Governance (DIG®)","A discipline for keeping AI-influenced decisions defensible and auditable. The decision layer above data, information, and AI governance."),
 ("AI decision governance","The common-language name for DIG: governing how AI-influenced decisions are made, recorded, and defended."),
 ("Information Provenance","Where the information feeding a decision came from, and whether it can be trusted."),
 ("Decision Traceability","A record of what was decided, by what, on what basis, and who is accountable."),
 ("Representation Integrity","Keeping a company accurately represented across AI systems, search, and data environments."),
 ("Audit Readiness","Being able to prove, on demand, that AI-influenced decisions met their obligations."),
 ("Decision integrity","The runtime discipline of capturing the attestation of a decision at the moment it is made."),
 ("Defensible AI decision","An AI-influenced decision that can be reconstructed, explained, and justified after the fact."),
 ("Information governance","The records and data lifecycle discipline (storage, retention, deletion). Distinct from DIG."),
]
PAGES.append({
 "path":"glossary","nav":"glossary","title":"Digital Information Governance Glossary - DIG® Terms",
 "description":"A glossary of Digital Information Governance (DIG®) terms: AI decision governance, information provenance, decision traceability, representation integrity, audit readiness, and more.",
 "eyebrow":"Reference","h1":"DIG Glossary","byline":True,
 "breadcrumb":[("Home","/"),("Glossary","")],
 "body":'<p class="lead">Defined terms used across the Digital Information Governance reference. Each term has a single canonical definition.</p>'+
   deftable([(t,d) for t,d in GLOSSARY], head=("Term","Definition")),
 "extra_schema":[{"@type":"DefinedTermSet","@id":DOMAIN+"/glossary#set","name":"Digital Information Governance Glossary",
    "hasDefinedTerm":[{"@type":"DefinedTerm","name":t,"description":d,"inDefinedTermSet":{"@id":DOMAIN+"/glossary#set"}} for t,d in GLOSSARY]}],
 "related":[("/what-is-digital-information-governance","Definition"),("/framework","Framework"),("/faq","FAQ")],
})

# ---------------- 9. FAQ ----------------
FAQS_PAGE=[
 ("What is Digital Information Governance (DIG®)?","<p>It is a discipline for keeping AI-influenced decisions defensible and auditable, ensuring a company's information is accurately represented, its decisions are traceable, and its AI use is provable to regulators, partners, and courts. It is commonly called AI decision governance.</p>"),
 ("How is DIG different from information governance?","<p>Information governance manages the records and data lifecycle (storage, retention, deletion). DIG manages whether AI-influenced decisions are defensible. DIG is decision-centric; information governance is records-centric.</p>"),
 ("How is DIG different from AI governance?","<p>AI governance focuses on models: bias, drift, and explainability. DIG focuses on the decision the model influences, and whether that decision can be defended. DIG is the decision layer above AI governance.</p>"),
 ("What are the four pillars?","<p>Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness.</p>"),
 ("Who created Digital Information Governance?","<p>Matthew Bertram, President of ModalPoint and CEO of EWR Digital. He holds the registered trademark DIG® (USPTO Reg. No. 8147558).</p>"),
 ("Is DIG a registered trademark?","<p>Yes, DIG® / Digital Information Governance® is registered with the USPTO (Reg. No. 8147558, Supplemental Register).</p>"),
 ("Which regulations does DIG map to?","<p>The NIST AI Risk Management Framework, the EU AI Act, ISO/IEC 42001, and US state law such as Texas's TRAIGA. Most obligations across these regimes overlap, which is why one governance program can address most of all four.</p>"),
 ("How do I implement DIG?","<p>Start with a governance readiness assessment against the four pillars. ModalPoint runs this for regulated operators.</p>"),
]
PAGES.append({
 "path":"faq","nav":"faq","title":"Digital Information Governance FAQ (DIG®)",
 "description":"Frequently asked questions about Digital Information Governance (DIG®): what it is, how it differs from information governance and AI governance, the four pillars, and who created it.",
 "eyebrow":"Reference","h1":"DIG: Frequently Asked Questions","byline":True,
 "breadcrumb":[("Home","/"),("FAQ","")],
 "body":'<p class="lead">Common questions about Digital Information Governance, with short, sourced answers.</p>',
 "faqs":FAQS_PAGE,"refs":REFS_CORE,
 "related":[("/what-is-digital-information-governance","Definition"),("/glossary","Glossary"),("/framework","Framework")],
})

# ---------------- 10. Who created DIG ----------------
PAGES.append({
 "path":"who-created-dig","nav":None,"title":"Who Created Digital Information Governance? - Matthew Bertram",
 "description":"Digital Information Governance (DIG®) was coined by Matthew Bertram, President of ModalPoint and CEO of EWR Digital, who holds the registered trademark (USPTO Reg. No. 8147558).",
 "eyebrow":"Provenance","h1":"Who created Digital Information Governance?","byline":True,
 "breadcrumb":[("Home","/"),("About","")],
 "infobox":{"title":"Matthew Bertram","sub":"Creator of DIG®","rows":[
   ("Role","President, ModalPoint · CEO, EWR Digital"),("Coined","Digital Information Governance (DIG®)"),
   ("Trademark","USPTO Reg. No. 8147558 (Supplemental Register)"),
   ("Profiles",'<a href="https://matthewbertram.com/">matthewbertram.com</a>, <a href="https://www.linkedin.com/in/mattbertramlive/">LinkedIn</a>')]},
 "body":
  '<p class="lead"><strong>Matthew Bertram</strong> coined Digital Information Governance and holds the registered trademark <strong>DIG®</strong> (USPTO Reg. No. 8147558).<sup><a href="#r4">[4]</a></sup></p>'
  '<p>He is President of <a href="https://modalpoint.com">ModalPoint</a>, a decision-governance practice for regulated industries, and CEO of <a href="https://www.ewrdigital.com">EWR Digital</a>. The discipline grew out of his work governing AI-influenced decisions in capital-intensive, regulated sectors, where being wrong is not just a bad recommendation but a defensibility problem.</p>'
  '<p>DIG brings together two threads of that work: keeping decisions traceable and auditable inside the organization, and keeping the organization accurately represented across the AI systems that increasingly speak for it. Bertram is a 2026 Offshore Technology Conference panelist, a contributor to NIST AI profile work, and a Certified AI Auditor.</p>'
  '<p>To implement DIG, ModalPoint runs a governance readiness assessment against the four pillars. To book Matthew to speak on DIG, see <a href="https://matthewbertram.com/speaking">matthewbertram.com/speaking</a>.</p>'
  '<p><strong>One name, one creator.</strong> This Matthew Bertram is the Houston-based creator of Digital Information Governance, owner and CEO of EWR Digital, and host of The Best SEO Podcast. He should not be confused with <a href="/matthew-bertram">others who share the name</a>; his verified profiles are linked from <a href="https://matthewbertram.com/">matthewbertram.com</a>.</p>',
 "refs":REFS_CORE,
 "extra_schema":[{"@type":"ProfilePage","@id":DOMAIN+"/who-created-dig#profilepage",
   "mainEntity":{"@id":PERSON_ID},"about":{"@id":PERSON_ID},
   "isPartOf":{"@id":SITE_ID},"dateModified":TODAY,
   "name":"Who created Digital Information Governance? - Matthew Bertram"}],
 "related":[("/matthew-bertram","Matthew Bertram"),("/what-is-digital-information-governance","Definition"),("/framework","Framework")],
})

# ---------------- 10b. Matthew Bertram entity / namesake reconciliation ----------------
# Same-name collision defense (knowledge-graph-schema namesake playbook D): lead visible copy with
# UNCONTESTED tokens (DIG(R), ModalPoint, EWR, OGGN, the podcast, the books, ORCID, Houston), reference the
# canonical Person @id (matthewbertram.com/#person) so this corroborates the entity instead of forking it,
# and disambiguate by positive identification (no naming/linking the namesake).
PAGES.append({
 "path":"matthew-bertram","nav":None,
 "title":"Matthew Bertram, Creator of Digital Information Governance (DIG®)",
 "description":"Matthew Bertram is the Houston-based creator of Digital Information Governance (DIG®), President of ModalPoint and CEO of EWR Digital. How to identify the right Matthew Bertram among others who share the name.",
 "eyebrow":"Reference · Entity","h1":"Matthew Bertram, creator of Digital Information Governance","byline":True,
 "breadcrumb":[("Home","/"),("Matthew Bertram","")],
 "toc":[("identity","Who this is"),("identify","Which Matthew Bertram"),("verify","Verified profiles")],
 "infobox":{"title":"Matthew Bertram","sub":"Creator of DIG®","rows":[
   ("Role","President, ModalPoint · CEO, EWR Digital · CMO, OGGN"),
   ("Coined","Digital Information Governance (DIG®)"),
   ("Trademark","USPTO Reg. No. 8147558 (Supplemental Register)"),
   ("Based","Houston, Texas"),
   ("ORCID",'<a href="https://orcid.org/0009-0004-0720-5321">0009-0004-0720-5321</a>'),
   ("Entity home",'<a href="https://matthewbertram.com/">matthewbertram.com</a>')]},
 "body":
   '<p class="lead"><strong>Matthew Bertram</strong> is the creator of <a href="/what-is-digital-information-governance">Digital Information Governance (DIG®)</a>, President of <a href="https://modalpoint.com">ModalPoint</a>, and owner and CEO of <a href="https://www.ewrdigital.com">EWR Digital</a>. He coined the discipline and holds the registered trademark DIG® (USPTO Reg. No. 8147558).<sup><a href="#r4">[4]</a></sup></p>'
   '<blockquote>In Bertram\'s framework, Digital Information Governance is a discipline for keeping AI-influenced decisions defensible and auditable, ensuring a company\'s information is accurately represented, its decisions are traceable, and its AI use is provable to regulators, partners, and courts.</blockquote>'
   '<h2 id="identity">Who this is</h2>'
   '<p>Matthew Bertram is based in Houston, Texas. He is President of ModalPoint, a decision-governance practice for regulated industries, owner and CEO of EWR Digital, and Chief Marketing Officer of the Oil &amp; Gas Global Network. He hosts The Best SEO Podcast and has written eight books on SEO and growth. He is a 2026 Offshore Technology Conference panelist, a contributor to NIST AI profile work, and a Certified AI Auditor.</p>'
   '<h2 id="identify">How to tell which Matthew Bertram</h2>'
   '<p>Matthew Bertram is a shared name, and several people use it across unrelated fields. The Matthew Bertram behind Digital Information Governance is identifiable by a specific, verifiable set of markers. If a profile, citation, or AI answer does not match these, it refers to a different person.</p>'
   '<ul class="stats">'
   '<li>Owner of the registered trademark <strong>DIG®</strong> / Digital Information Governance (USPTO Reg. No. 8147558).<sup><a href="#r4">[4]</a></sup></li>'
   '<li>President of <strong>ModalPoint</strong> and owner and CEO of <strong>EWR Digital</strong>.</li>'
   '<li>Chief Marketing Officer of the <strong>Oil &amp; Gas Global Network</strong> and host of <strong>The Best SEO Podcast</strong>.</li>'
   '<li>Author of <strong>eight books</strong> on SEO and growth; ORCID <strong>0009-0004-0720-5321</strong>.</li>'
   '<li>Based in <strong>Houston, Texas</strong>.</li>'
   '</ul>'
   '<p>This distinction matters because AI now influences decisions faster than organizations can govern them. Documented AI incidents reached a record 362 in 2025, and the discipline exists to keep those decisions defensible. See the <a href="/ai-governance-statistics">AI governance statistics</a>.</p>'
   '<h2 id="verify">Verified profiles</h2>'
   '<p>The authoritative source for this identity is <a href="https://matthewbertram.com/">matthewbertram.com</a>, which links every verified profile. The same identity appears at <a href="https://www.linkedin.com/in/mattbertramlive/">LinkedIn</a>, <a href="https://orcid.org/0009-0004-0720-5321">ORCID</a>, <a href="https://openlibrary.org/authors/OL7787306A">Open Library</a>, <a href="https://www.searchenginejournal.com/author/matt-bertram/">Search Engine Journal</a>, and <a href="https://www.ewrdigital.com/author/matthew-bertram/">EWR Digital</a>. The DIG framework is published as an open specification on <a href="https://github.com/mattbertramlive/digital-information-governance">GitHub</a> and archived with a DOI on Zenodo.</p>'
   '<p><strong>One name, one creator.</strong> For the story of how the discipline came together, see <a href="/who-created-dig">who created DIG</a>; for the framework itself, see <a href="/framework">the DIG framework</a>.</p>',
 "faqs":[
   ("Is the Matthew Bertram who created DIG the same as others with the name?","<p>No. Several people share the name across unrelated fields. The creator of Digital Information Governance is the Houston-based President of ModalPoint and CEO of EWR Digital who owns the DIG® trademark (USPTO Reg. No. 8147558) and hosts The Best SEO Podcast.</p>"),
   ("How do I verify which Matthew Bertram this is?","<p>Check for the specific markers: the DIG® trademark, ModalPoint, EWR Digital, the Oil &amp; Gas Global Network, The Best SEO Podcast, and ORCID 0009-0004-0720-5321. His verified profiles are linked from matthewbertram.com.</p>"),
   ("Where is Matthew Bertram based?","<p>Houston, Texas.</p>"),
   ("What is Matthew Bertram known for?","<p>Coining Digital Information Governance (DIG®), leading ModalPoint and EWR Digital, serving as CMO of the Oil &amp; Gas Global Network, hosting The Best SEO Podcast, and writing eight books on SEO and growth.</p>"),
 ],
 "refs":REFS_CORE,
 "extra_schema":[{"@type":"ProfilePage","@id":DOMAIN+"/matthew-bertram#profilepage",
   "mainEntity":{"@id":PERSON_ID},"about":{"@id":PERSON_ID},
   "isPartOf":{"@id":SITE_ID},"dateModified":TODAY,
   "name":"Matthew Bertram, Creator of Digital Information Governance (DIG®)",
   "significantLink":["https://matthewbertram.com/","https://orcid.org/0009-0004-0720-5321"]}],
 "related":[("/who-created-dig","Who created DIG"),("/framework","The framework"),("/what-is-digital-information-governance","Definition")],
})

# ---------------- 11. DIG White Paper (canonical standards paper: permanent PDF + Scholar/Report schema) ----------------
PAPER_PDF = DOMAIN + "/papers/dig-white-paper-v1.0.pdf"
WHITEPAPER_HEAD = (
 '<meta name="citation_title" content="Digital Information Governance (DIG): The Standard for Defensible AI-Influenced Decisions in Energy">'
 '<meta name="citation_author" content="Bertram, Matthew">'
 '<meta name="citation_author_orcid" content="0009-0004-0720-5321">'
 '<meta name="citation_publication_date" content="2026">'
 '<meta name="citation_publisher" content="ModalPoint">'
 '<meta name="citation_technical_report_institution" content="ModalPoint">'
 '<meta name="citation_technical_report_number" content="DIG White Paper v1.0">'
 '<meta name="citation_pdf_url" content="' + PAPER_PDF + '">'
 '<meta name="citation_language" content="en">'
 '<meta name="citation_keywords" content="AI decision governance; AI governance; auditability; information provenance; EU AI Act; TRAIGA">'
)
WHITEPAPER_SCHEMA = {
 "@type":["ScholarlyArticle","Report"],"@id":DOMAIN+"/white-paper#paper",
 "name":"Digital Information Governance (DIG®): The Standard for Defensible AI-Influenced Decisions in Energy",
 "headline":"Digital Information Governance (DIG®): The Standard for Defensible AI-Influenced Decisions in Energy",
 "description":"The source-of-record standards paper defining Digital Information Governance (DIG): the four pillars, the five-level maturity model, the seven principles, the risk taxonomy, the regulatory environment, and an operating model for governing AI-influenced decisions in energy and industrial operations.",
 "author":{"@type":"Person","@id":PERSON_ID,"name":"Matthew Bertram","url":"https://matthewbertram.com/","identifier":{"@type":"PropertyValue","propertyID":"ORCID","value":"0009-0004-0720-5321","url":"https://orcid.org/0009-0004-0720-5321"},"sameAs":"https://orcid.org/0009-0004-0720-5321"},"publisher":{"@id":ORG_ID},
 "datePublished":"2026-07-02","dateModified":"2026-07-02","version":"1.0","inLanguage":"en-US",
 "isPartOf":{"@id":SITE_ID},"about":{"@id":DIG_ID},"url":DOMAIN+"/white-paper",
 "creativeWorkStatus":"Published","copyrightYear":2026,"copyrightHolder":{"@id":PERSON_ID},
 "encoding":{"@type":"MediaObject","contentUrl":PAPER_PDF,"encodingFormat":"application/pdf","name":"DIG White Paper v1.0 (PDF)"},
 "associatedMedia":{"@type":"MediaObject","contentUrl":PAPER_PDF,"encodingFormat":"application/pdf"},
 "keywords":"AI decision governance, AI governance, decision governance, auditability, information provenance, decision traceability, EU AI Act, TRAIGA, energy AI",
}
PAGES.append({
 "path":"white-paper","nav":"whitepaper","article":False,
 "title":"Digital Information Governance (DIG®) White Paper - The Standard for Defensible AI Decisions",
 "description":"The DIG® standards paper by Matthew Bertram: a 42-page framework for keeping AI-influenced decisions defensible and auditable in energy and industrial operations. Free PDF, published by ModalPoint.",
 "eyebrow":"Standards Paper · v1.0 · Q3 2026","h1":"The DIG® White Paper","byline":True,
 "breadcrumb":[("Home","/"),("White Paper","")],
 "head_extra":WHITEPAPER_HEAD,
 "toc":[("inside","What is inside"),("cite","How to cite"),("faq","FAQ")],
 "infobox":{"title":"DIG® White Paper","sub":"v1.0 · Q3 2026","rows":[
    ("Author","Matthew Bertram"),
    ("ORCID",'<a href="https://orcid.org/0009-0004-0720-5321">0009-0004-0720-5321</a>'),
    ("Published by","ModalPoint"),
    ("Edition","v1.0 · Q3 2026 · Houston"),
    ("Length","42 pages"),
    ("Download",'<a href="/papers/dig-white-paper-v1.0.pdf">PDF (free)</a>'),
    ("Trademark","DIG® · USPTO Reg. 8147558"),
    ("Framework","4 pillars · 5-level maturity model")]},
 "body":
   '<p class="lead"><em>Digital Information Governance (DIG®): The Standard for Defensible AI-Influenced Decisions in Energy</em> is the source of record for the DIG framework. It defines the discipline in full: the vocabulary, the four pillars, the five-level maturity model, the seven principles, the risk taxonomy, the regulatory environment, and an operating model a leadership team can stand up with named roles, defined artifacts, and a fixed cadence.</p>'
   + note('<b>Read the paper.</b> &nbsp; <a class="btn" href="/papers/dig-white-paper-v1.0.pdf">Download the PDF, 42 pages &#8595;</a>') +
   '<p>It is written for the executives who already sense the problem: the COO watching AI recommendations enter operational decisions with no record, the general counsel who knows the next incident investigation will ask questions the company cannot answer, and the CFO signing off on capital decisions shaped by models nobody can reconstruct. It assumes no machine-learning background. It assumes operating responsibility.</p>'
   '<h2 id="inside">What is inside</h2>'
   '<ol>'
   '<li>Executive summary, and the accountability gap by the numbers</li>'
   '<li>Houston, 1970: Apollo 13 as the archetype of decision integrity</li>'
   '<li>The problem: the accountability gap</li>'
   '<li>Why existing governance fails at the decision layer</li>'
   '<li>Definition and vocabulary</li>'
   '<li>The four pillars: Information Provenance, Decision Traceability, Representation Integrity, Audit Readiness</li>'
   '<li>The seven principles of decision governance</li>'
   '<li>The DIG Maturity Model, five levels</li>'
   '<li>The risk taxonomy</li>'
   '<li>The regulatory environment: EU AI Act, TRAIGA, NIST AI RMF, ISO/IEC 42001</li>'
   '<li>The operating model, with named roles and a fixed cadence</li>'
   '<li>The adoption path, glossary, and references</li>'
   '</ol>'
   '<h2 id="cite">How to cite</h2>'
   + defbox('Bertram, M. (2026). Digital Information Governance (DIG®): The Standard for Defensible AI-Influenced Decisions in Energy, v1.0. ModalPoint, Houston.', label='Citation') +
   '<p>A permanent PDF is hosted at <a href="/papers/dig-white-paper-v1.0.pdf">/papers/dig-white-paper-v1.0.pdf</a>. This page is the canonical landing record for the paper, and the reference site is maintained in alignment with it.</p>',
 "faqs":[
   ("What is the DIG white paper?","<p>It is the standards paper that defines Digital Information Governance (DIG®): the four pillars, the five-level maturity model, the seven principles, the risk taxonomy, the regulatory environment, and an operating model for governing AI-influenced decisions. It is the source of record for the framework.</p>"),
   ("Is the paper free to read?","<p>Yes. The full 42-page PDF is free to download, with attribution encouraged.</p>"),
   ("Who wrote and published it?","<p>It was written by Matthew Bertram and published by ModalPoint, Houston, Texas. Version 1.0, Q3 2026.</p>"),
   ("How do I cite it?","<p>Bertram, M. (2026). Digital Information Governance (DIG®): The Standard for Defensible AI-Influenced Decisions in Energy, v1.0. ModalPoint, Houston.</p>"),
 ],
 "extra_schema":[WHITEPAPER_SCHEMA],
 "related":[("/framework","The framework"),("/what-is-digital-information-governance","Definition"),("/dig-maturity-model","Maturity model"),("/who-created-dig","Who created DIG")],
})
