# -*- coding: utf-8 -*-
"""content2.py - Tier 2 (AI-decision-governance category) + Tier 3 (regulatory)."""
from templates import defbox, note, deftable, DOMAIN
from content import REFS_CORE

PAGES2 = []

# ============ TIER 2: the open category ============

PAGES2.append({
 "path":"ai-decision-governance","nav":None,
 "title":"AI Decision Governance - Definition & Framework (DIG®)",
 "description":"AI decision governance is the practice of governing how AI-influenced decisions are made, recorded, and defended. It is the plain-language name for Digital Information Governance (DIG®).",
 "eyebrow":"The category","h1":"AI Decision Governance","byline":True,
 "breadcrumb":[("Home","/"),("AI decision governance","")],
 "toc":[("def","Definition"),("why","Why it is the new frontier"),("vs","Decision vs model governance"),("how","How to govern a decision"),("refs","References")],
 "infobox":{"title":"AI decision governance","sub":"= Digital Information Governance (DIG®)","rows":[
    ("Governs","AI-influenced decisions"),("Versus","Model governance (AI governance)"),
    ("Framework","DIG® four pillars"),("Coined by","Matthew Bertram")]},
 "body":
   defbox("AI decision governance is the practice of governing how AI-influenced decisions are made, recorded, and defended: ensuring an organization can always show what was decided, on what basis, and who is accountable.", label="AI decision governance") +
   '<p class="lead">AI decision governance is the plain-language name for <a href="/what-is-digital-information-governance">Digital Information Governance (DIG®)</a>. Where AI governance asks "is the model fair and accurate?", decision governance asks the harder question: "when this AI-influenced decision is challenged, can we defend it?"</p>'
   '<h2 id="why">Why the decision is the new frontier</h2>'
   '<p>Most AI governance programs stop at the model. But organizations are not sued for owning a model; they are held to account for the decisions the model influenced. As AI moves into hiring, lending, pricing, safety, and operations, the ungoverned gap is the decision itself: the moment a recommendation becomes an action with consequences.<sup><a href="#r1">[1]</a></sup></p>'
   '<h2 id="vs">Decision governance vs. model governance</h2>' +
   deftable([
     ("AI governance (model)","Bias, drift, explainability, model risk. Governs the system."),
     ("AI decision governance","Provenance, traceability, accountability, audit. Governs the decision the system influences."),
   ], head=("Discipline","Focus")) +
   '<h2 id="how">How to govern a decision</h2>'
   '<p>The DIG framework names the four things that must be true for an AI-influenced decision to be defensible: <a href="/pillars/information-provenance">Information Provenance</a>, <a href="/pillars/decision-traceability">Decision Traceability</a>, <a href="/pillars/representation-integrity">Representation Integrity</a>, and <a href="/pillars/audit-readiness">Audit Readiness</a>. Together they turn "the AI decided" into "a named person decided, and here is the record."</p>',
 "faqs":[
   ("Is AI decision governance the same as AI governance?","<p>No. AI governance focuses on the model (bias, drift, explainability). AI decision governance focuses on the decision the model influences, and whether it can be defended. Decision governance sits above model governance.</p>"),
   ("Is AI decision governance the same as Digital Information Governance?","<p>Yes. AI decision governance is the common-language description of the discipline Matthew Bertram named Digital Information Governance (DIG®).</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/ai-agent-governance","AI agent governance"),("/what-is-digital-information-governance","Definition"),("/defensible-ai-decisions","Defensible AI decisions"),("/framework","The framework")],
})

PAGES2.append({
 "path":"defensible-ai-decisions","nav":None,
 "title":"Defensible AI Decisions - What They Are and How to Make Them (DIG®)",
 "description":"A defensible AI decision is one that can be reconstructed, explained, and justified after the fact. How Digital Information Governance (DIG®) makes AI-influenced decisions defensible.",
 "eyebrow":"AI decision governance","h1":"Defensible AI Decisions","byline":True,
 "breadcrumb":[("Home","/"),("Defensible AI decisions","")],
 "infobox":{"title":"Defensible AI decision","sub":"DIG® concept","rows":[
    ("Definition","A decision that can be reconstructed, explained, and justified later."),
    ("Requires","Provenance + traceability + audit readiness"),("Tested by","Regulators, partners, courts")]},
 "body":
   defbox("A defensible AI decision is one that can be reconstructed, explained, and justified after the fact, with a record of its inputs, its reviewers, and the authority under which it was made.", label="Defensible AI decision") +
   '<p class="lead">Defensibility is the practical test of AI governance. It is not whether you used AI, but whether you can stand behind the decision when someone asks you to.</p>'
   '<h2>What makes a decision defensible</h2>'
   '<p>A defensible decision has three things on hand: the provenance of the information it used, a trace of who decided and on what basis, and the ability to produce both on demand. Each maps to a pillar of <a href="/framework">the DIG framework</a>. A decision missing any of them is not indefensible because it was wrong, but because it cannot be explained.</p>'
   '<p>US AI enforcement to date has punished what AI <em>claims</em> more than how it decides, but the trajectory is clear: as the EU AI Act and state laws take effect, "show your work" becomes the standard. Organizations that capture defensibility at decision time win the premium, regulated work; those that do not become the cautionary tales.<sup><a href="#r3">[3]</a></sup></p>',
 "faqs":[
   ("How do you make an AI decision defensible?","<p>Capture the decision's provenance, traceability, and audit trail at the moment it is made: what information was used, what was recommended, who reviewed it, and on what authority it was acted on. This is the discipline of decision integrity within DIG.</p>"),
   ("Why does defensibility matter more than accuracy?","<p>An accurate decision you cannot explain is still a liability when challenged. Defensibility is what lets you justify the decision to a regulator, partner, or court, regardless of outcome.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/auditable-ai-decisions","Auditable AI decisions"),("/decision-integrity","Decision integrity"),("/pillars/decision-traceability","Decision traceability")],
})

PAGES2.append({
 "path":"auditable-ai-decisions","nav":None,
 "title":"Auditable AI Decisions & AI Audit Trails (DIG®)",
 "description":"Auditable AI decisions and AI audit trails: how Digital Information Governance (DIG®) makes AI-influenced decisions provable on demand for regulators and auditors.",
 "eyebrow":"AI decision governance","h1":"Auditable AI Decisions","byline":True,
 "breadcrumb":[("Home","/"),("Auditable AI decisions","")],
 "infobox":{"title":"Auditable AI decision","sub":"DIG® concept","rows":[
    ("Definition","A decision whose record can be produced and verified on demand."),
    ("Mechanism","AI decision logging / audit trail"),("Pillar",'<a href="/pillars/audit-readiness">Audit Readiness</a>')]},
 "body":
   defbox("An auditable AI decision is one whose full record, its inputs, reviewers, and rationale, can be produced and independently verified on demand.", label="Auditable AI decision") +
   '<p class="lead">Auditability is defensibility made routine. A decision is auditable when its trail is not assembled in a panic after a challenge, but captured automatically as the decision is made.</p>'
   '<h2>The AI audit trail</h2>'
   '<p>An AI audit trail records, for each AI-influenced decision: the information that fed it (provenance), what the model recommended, who reviewed and approved it, the authority under which it was acted on, and which controls applied. This is the operational core of <a href="/pillars/audit-readiness">audit readiness</a>, the fourth pillar of DIG.</p>'
   '<p>The EU AI Act requires logging and record-keeping for high-risk systems; ISO/IEC 42001 requires audit; TRAIGA requires documentation. An organization with a standing AI audit trail satisfies all three from one discipline.<sup><a href="#r3">[3]</a></sup></p>',
 "faqs":[
   ("What is an AI audit trail?","<p>A record, captured per decision, of the information used, the recommendation made, the human review, the authority to act, and the controls applied, sufficient to reconstruct and verify the decision later.</p>"),
   ("What regulations require auditable AI?","<p>The EU AI Act (logging/record-keeping for high-risk systems), ISO/IEC 42001 (audit requirements), and Texas's TRAIGA (documentation) all point toward auditable AI decisions.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/pillars/audit-readiness","Audit readiness"),("/defensible-ai-decisions","Defensible AI decisions"),("/regulations","Regulations")],
})

PAGES2.append({
 "path":"decision-integrity","nav":None,
 "title":"Decision Integrity - The Runtime Discipline of DIG®",
 "description":"Decision integrity is the runtime discipline of capturing a decision's attestation at the moment it is made. It is how Digital Information Governance (DIG®) operates in practice.",
 "eyebrow":"AI decision governance","h1":"Decision Integrity","byline":True,
 "breadcrumb":[("Home","/"),("Decision integrity","")],
 "infobox":{"title":"Decision integrity","sub":"DIG® runtime discipline","rows":[
    ("Definition","Capturing a decision's attestation at the moment it is made."),
    ("Relationship","The runtime practice across all four DIG pillars"),("Coined by","Matthew Bertram")]},
 "body":
   defbox("Decision integrity is the runtime discipline of capturing the attestation of a decision, its inputs, reviewers, and rationale, at the moment the decision is made, rather than reconstructing it later.", label="Decision integrity") +
   '<p class="lead">If the four pillars of DIG are what must be true, decision integrity is when you make them true: at decision time, not after the fact.</p>'
   '<h2>Why timing is the whole game</h2>'
   '<p>Most governance failures are not failures of policy but of timing. The record that would have made a decision defensible existed for a moment and was never captured. Decision integrity closes that gap by treating the attestation as part of the decision itself: the decision is not complete until its provenance and trace are recorded.</p>'
   '<p>This is the discipline that turns DIG from a document into a control. It is also the bridge to the runtime work ModalPoint delivers for regulated operators.</p>',
 "faqs":[
   ("What is decision integrity?","<p>The runtime discipline of capturing a decision's attestation, its inputs, reviewers, and rationale, at the moment the decision is made, so it is defensible without later reconstruction.</p>"),
   ("How does decision integrity relate to DIG?","<p>Decision integrity is how the four DIG pillars are satisfied in practice, at decision time. DIG names what must be true; decision integrity is the runtime discipline that makes it true.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/framework","The framework"),("/defensible-ai-decisions","Defensible AI decisions"),("/pillars/decision-traceability","Decision traceability")],
})

PAGES2.append({
 "path":"representation-integrity-ai-search","nav":None,
 "title":"Representation Integrity in AI Search (DIG® Pillar 3)",
 "description":"Representation integrity is keeping a company accurately represented across AI systems and search. How Digital Information Governance (DIG®) treats AI visibility as a governance control.",
 "eyebrow":"AI decision governance","h1":"Representation Integrity in AI Search","byline":True,
 "breadcrumb":[("Home","/"),("Representation integrity in AI search","")],
 "infobox":{"title":"Representation integrity","sub":"DIG® Pillar 3","rows":[
    ("Definition","Keeping a company accurately represented across AI systems and search."),
    ("Risk governed","AI misrepresentation as evidence"),("Connects to","GEO / AEO, governed for accuracy")]},
 "body":
   defbox("Representation integrity is the discipline of keeping a company accurately represented across AI systems, search engines, and the data environments that feed them.", label="Representation integrity") +
   '<p class="lead">AI systems now describe your company to buyers, partners, regulators, and courts, often without your input. Representation integrity governs that description for accuracy.</p>'
   '<h2>Why misrepresentation is a governance problem</h2>'
   '<p>When an AI answer engine states what a company does, how it operates, or what it is permitted to do, that statement carries weight. A confident misrepresentation can mislead a buyer, contradict a disclosure, or become evidence in a dispute. Representation integrity treats the external AI narrative as a control surface to be governed, not a marketing channel to be optimized.<sup><a href="#r1">[1]</a></sup></p>'
   '<h2>The link to AI visibility</h2>'
   '<p>This is where governance meets generative engine optimization and answer engine optimization. The difference is intent: GEO and AEO usually aim to be <em>seen</em>; representation integrity aims to be seen <em>accurately</em>. Within DIG, AI visibility work is governed for truthfulness and consistency, which is also what makes a company more citable to AI engines.</p>',
 "faqs":[
   ("What is representation integrity?","<p>Keeping a company accurately represented across AI systems, search engines, and data environments, so the external AI narrative is accurate and consistent rather than misleading.</p>"),
   ("How is representation integrity different from SEO or GEO?","<p>SEO and GEO aim for visibility. Representation integrity governs that visibility for accuracy, treating AI misrepresentation as a risk to manage, not just a ranking to win.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/pillars/representation-integrity","Pillar: Representation Integrity"),("/framework","The framework"),("/ai-decision-governance","AI decision governance")],
})

# ============ TIER 3: regulatory ============

PAGES2.append({
 "path":"regulations","nav":"regulations",
 "title":"AI Governance Regulations & How DIG® Maps to Them",
 "description":"How Digital Information Governance (DIG®) maps to the NIST AI RMF, the EU AI Act, ISO/IEC 42001, and Texas's TRAIGA. Most obligations across these regimes overlap.",
 "eyebrow":"Regulatory context","h1":"AI Governance Regulations","byline":True,
 "breadcrumb":[("Home","/"),("Regulations","")],
 "toc":[("intro","One binder, not four"),("regimes","The regimes"),("map","How DIG maps"),("refs","References")],
 "body":
   '<p class="lead" id="intro">Four regimes now shape AI governance in regulated industries. Most of their obligations overlap, which means a single, well-built governance discipline can satisfy most of all four. DIG is built to be that binder.</p>'
   '<h2 id="regimes">The regimes</h2>'
   '<div class="grid">'
   '<a class="gcard" href="/regulations/nist-ai-rmf"><h3>NIST AI RMF</h3><p>The US voluntary framework: Govern, Map, Measure, Manage.</p></a>'
   '<a class="gcard" href="/regulations/eu-ai-act"><h3>EU AI Act</h3><p>Risk-tiered obligations for high-risk AI; logging, oversight, conformity.</p></a>'
   '<a class="gcard" href="/regulations/traiga"><h3>TRAIGA (Texas)</h3><p>The Texas Responsible AI Governance Act; documentation and disclosure.</p></a>'
   '<a class="gcard" href="/regulations/iso-42001"><h3>ISO/IEC 42001</h3><p>The international AI management-system standard; auditable controls.</p></a>'
   '<a class="gcard" href="/regulations/colorado-ai-act"><h3>Colorado AI Act</h3><p>SB 24-205: reasonable care against algorithmic discrimination in high-risk decisions.</p></a>'
   '<a class="gcard" href="/regulations/nyc-local-law-144"><h3>NYC Local Law 144</h3><p>Mandatory bias audits for automated employment decision tools.</p></a>'
   '</div>'
   '<h2 id="map">How DIG maps to the regimes</h2>' +
   deftable([
     ("Information Provenance","NIST Map; EU AI Act data governance; ISO 42001 data quality."),
     ("Decision Traceability","NIST Govern/Manage; EU AI Act record-keeping and human oversight."),
     ("Representation Integrity","Consumer-protection and disclosure duties; AI-output accuracy."),
     ("Audit Readiness","EU AI Act conformity/logging; ISO 42001 audit; TRAIGA documentation."),
   ], head=("DIG pillar","Maps to")),
 "faqs":[
   ("Does DIG replace NIST, the EU AI Act, or ISO 42001?","<p>No. DIG is a discipline that helps an organization meet the obligations those regimes define. It maps the four pillars to the controls each regime expects.</p>"),
   ("Why do the regulations overlap?","<p>They target the same underlying risks, such as provenance, oversight, documentation, and auditability. Most obligations recur across regimes, so one governance program can address most of all four.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/ai-governance-statistics","Statistics"),("/framework","The framework"),("/auditable-ai-decisions","Auditable AI decisions")],
})

REG = {
 "regulations/nist-ai-rmf":{
   "h1":"NIST AI Risk Management Framework (AI RMF)","crumb":"NIST AI RMF",
   "title":"NIST AI RMF & Digital Information Governance (DIG®)",
   "desc":"How the NIST AI Risk Management Framework (Govern, Map, Measure, Manage) maps to the four pillars of Digital Information Governance (DIG®).",
   "sub":"AI RMF 1.0 (2023)",
   "body":"<p class=\"lead\">The NIST AI Risk Management Framework is the US voluntary standard for managing AI risk, organized around four functions: Govern, Map, Measure, and Manage.</p>"
          "<p>DIG operationalizes these functions at the decision level. <strong>Map</strong> aligns with Information Provenance (knowing the inputs and context). <strong>Govern</strong> and <strong>Manage</strong> align with Decision Traceability and Audit Readiness (accountability, oversight, and records). <strong>Measure</strong> supports all four pillars by testing whether controls actually hold.</p>"
          "<p>For an organization adopting the AI RMF, DIG provides the decision-level discipline the framework's functions imply but do not prescribe in detail.</p>"},
 "regulations/eu-ai-act":{
   "h1":"The EU AI Act","crumb":"EU AI Act",
   "title":"EU AI Act & Digital Information Governance (DIG®)",
   "desc":"How the EU AI Act's obligations for high-risk AI (logging, human oversight, record-keeping, conformity) map to Digital Information Governance (DIG®).",
   "sub":"Regulation (EU) 2024/1689",
   "body":"<p class=\"lead\">The EU AI Act (Regulation 2024/1689) tiers AI systems by risk and places substantial obligations on high-risk systems, including data governance, record-keeping, human oversight, transparency, and conformity assessment, with obligations phasing in on a staggered timeline: transparency duties arrived in August 2026, while the 2026 Digital Omnibus deferred the main high-risk deadlines to December 2027 for stand-alone Annex III systems and August 2028 for AI embedded in Annex I regulated products.</p>"
          "<p>These obligations map almost directly onto DIG. Record-keeping and human oversight are Decision Traceability; data-governance duties are Information Provenance; logging and conformity are Audit Readiness; transparency duties touch Representation Integrity. An organization running DIG is building the evidence the Act asks for.</p>"
          "<p>For companies with EU exposure, DIG turns the Act's requirements from a checklist into a standing discipline.</p>"},
 "regulations/traiga":{
   "h1":"TRAIGA: The Texas Responsible AI Governance Act","crumb":"TRAIGA",
   "title":"TRAIGA (Texas Responsible AI Governance Act) & DIG®",
   "desc":"How Texas's Responsible AI Governance Act (TRAIGA) maps to Digital Information Governance (DIG®): documentation, disclosure, and accountability for AI-influenced decisions.",
   "sub":"Texas state law",
   "body":"<p class=\"lead\">The Texas Responsible AI Governance Act (TRAIGA, HB 149), signed in June 2025 and effective January 1, 2026, makes Texas one of the first US states with a comprehensive AI governance law. It brings AI accountability into state law with documentation and disclosure duties for organizations deploying AI in consequential settings, and Attorney-General-enforced civil penalties that reach up to $200,000 per uncurable violation.</p>"
          "<p>TRAIGA rewards exactly what DIG produces: a documented account of how an AI-influenced decision was made and overseen. Decision Traceability and Audit Readiness supply the documentation; Representation Integrity addresses disclosure and accurate description. For Texas operators, including the energy sector, TRAIGA makes DIG a practical compliance posture rather than a theory.</p>"
          "<p>Texas is also the home turf for much of this work, which is why DIG treats TRAIGA as a leading indicator of where US state AI law is heading.</p>"},
 "regulations/iso-42001":{
   "h1":"ISO/IEC 42001","crumb":"ISO/IEC 42001",
   "title":"ISO/IEC 42001 & Digital Information Governance (DIG®)",
   "desc":"How ISO/IEC 42001, the AI management system standard, maps to the auditable controls of Digital Information Governance (DIG®).",
   "sub":"ISO/IEC 42001:2023",
   "body":"<p class=\"lead\">ISO/IEC 42001:2023 is the international management-system standard for artificial intelligence, defining auditable controls for governing AI across its lifecycle.</p>"
          "<p>As a management-system standard, ISO 42001 is built around audit and continual improvement, which aligns with DIG's Audit Readiness pillar. Its controls for data, accountability, and transparency map to Information Provenance, Decision Traceability, and Representation Integrity. An organization pursuing ISO 42001 certification can use DIG as the decision-level discipline underneath the management system.</p>"},
}
for slug,info in REG.items():
    PAGES2.append({
      "path":slug,"nav":"regulations","title":info["title"],"description":info["desc"],
      "eyebrow":"Regulatory context","h1":info["h1"],"byline":True,
      "breadcrumb":[("Home","/"),("Regulations","/regulations"),(info["crumb"],"")],
      "infobox":{"title":info["crumb"],"sub":info["sub"],"rows":[
         ("Maps to DIG",'<a href="/framework">All four pillars</a>'),
         ("See also",'<a href="/regulations">All regulations</a>')]},
      "body":info["body"],
      "refs":REFS_CORE,
      "related":[("/regulations","All regulations"),("/ai-risk-management","AI risk management"),("/framework","The framework"),("/auditable-ai-decisions","Auditable AI decisions")],
    })
