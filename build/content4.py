# -*- coding: utf-8 -*-
"""content4.py - expansion pages (Tier 6): compare hub, changelog, maturity model,
AI risk management, per-industry pages, and the cited statistics reference page.
Appended after content/content2/content3. Statistics page figures are primary-sourced and
adversarially verified (deep-research 3-0 votes, 2026-06-17)."""
from templates import defbox, note, deftable, maturity_diagram, DOMAIN, PERSON_ID, ORG_ID, DIG_ID, pillars_set_node
from content import REFS_CORE

PAGES4 = []

# ============ Compare hub (also the target of the /compare breadcrumb) ============
PAGES4.append({
 "path":"compare","nav":None,
 "title":"AI Governance Comparisons (DIG®): Data vs Information vs AI vs Decision Governance",
 "description":"How data governance, information governance, AI governance, and Digital Information Governance (DIG®) differ, and where each fits. A reference map of the four governance layers.",
 "eyebrow":"Comparison","h1":"Governance, Compared","byline":True,
 "breadcrumb":[("Home","/"),("Compare","")],
 "toc":[("layers","The governance layers"),("compare","Side-by-side comparisons")],
 "infobox":{"title":"Governance layers","sub":"Where DIG fits","rows":[
    ("Data governance","The data"),("Information governance","Records and information"),
    ("AI governance","The models"),("Digital Information Governance","The decision")]},
 "body":
   '<p class="lead" id="layers">Four governance disciplines now sit in most regulated organizations. They are often confused because their names overlap, but each governs a different asset. Digital Information Governance (DIG®) is the newest layer: it governs the AI-influenced <strong>decision</strong> that the others enable.</p>' +
   deftable([
     ("Data governance","Governs structured data: quality, lineage, access, and cataloging."),
     ("Information governance","Governs records and information: retention, compliance, and e-discovery."),
     ("AI governance","Governs models: bias, drift, explainability, and model risk."),
     ("Digital Information Governance (DIG®)","Governs the decision: whether an AI-influenced decision is defensible and auditable."),
   ], head=("Discipline","What it governs")) +
   '<h2 id="compare">Side-by-side comparisons</h2>'
   '<div class="grid">'
   '<a class="gcard" href="/compare/dig-vs-information-governance"><h3>DIG vs. information governance</h3><p>Decision-centric vs records-centric. The distinction that defines DIG.</p></a>'
   '<a class="gcard" href="/compare/ai-governance-vs-data-governance"><h3>AI vs. data governance</h3><p>The model vs the data, and the decision neither governs.</p></a>'
   '<a class="gcard" href="/compare/ai-governance-vs-information-governance"><h3>AI vs. information governance</h3><p>Model risk vs records, meeting at the decision.</p></a>'
   '<a class="gcard" href="/compare/information-governance-vs-data-governance"><h3>Information vs. data governance</h3><p>The broad umbrella vs the structured-data layer within it.</p></a>'
   '<a class="gcard" href="/compare/dig-vs-ai-trism"><h3>DIG vs. AI TRiSM</h3><p>Gartner governs the AI system; DIG governs the decision it influences.</p></a>'
   '</div>',
 "refs":REFS_CORE,
 "related":[("/what-is-digital-information-governance","Definition"),("/framework","The framework"),("/glossary","Glossary")],
})

# ============ Changelog (living-standard freshness signal) ============
PAGES4.append({
 "path":"changelog","nav":None,
 "title":"DIG® Framework Changelog & Version History",
 "description":"Version history of the Digital Information Governance (DIG®) framework: what changed, when, and why. DIG is maintained as a living reference, with regulatory mappings updated as the law evolves.",
 "eyebrow":"Living standard","h1":"DIG Framework Changelog","byline":True,
 "breadcrumb":[("Home","/"),("Changelog","")],
 "infobox":{"title":"DIG Framework","sub":"Version history","rows":[
    ("Current version","v1.1 (September 2026)"),("Status","Living reference"),
    ("Maintainer","Matthew Bertram"),("Definition","Stable since v1.0")]},
 "body":
   '<p class="lead">Digital Information Governance is maintained as a living reference. The canonical definition and the four pillars are stable; the regulatory mappings are updated as the underlying laws and standards evolve. Material changes are dated here.</p>'
   '<h2>v1.1, September 2026: the agentic extension</h2>'
   '<ul>'
   '<li>Extended the framework to the action layer: <a href="/ai-agent-governance">AI agent governance</a>, covering what an AI was authorized to see, decide, and do, who approved that authority, and whether the action can be reconstructed. The five questions map onto the existing four pillars; the canonical definition is unchanged.</li>'
   '<li>Added action-layer maturity markers for all five levels of the DIG Maturity Model.</li>'
   '<li>Updated the EU AI Act mapping for the 2026 Digital Omnibus deferral of high-risk deadlines (Annex III systems to December 2027, Annex I embedded systems to August 2028).</li>'
   '<li>Context for the revision: OpenAI designated Astra the first Critical-tier cybersecurity model under its Preparedness Framework, and Anthropic split its frontier model into generally available and trusted-access products.</li>'
   '<li>Opened the living reference layer: the <a href="/ai-regulation-tracker">AI Regulation Tracker</a>, the <a href="/ai-agent-incident-register">AI Agent Incident Register</a>, and the <a href="/compare/frontier-model-access-tiers">frontier access-tier comparison</a>. Expanded the glossary from 9 to 44 anchored terms. Added cite-this-page blocks and machine-readable JSON under /data/.</li>'
   '</ul>'
   '<h2>v1.0, June 2026</h2>'
   '<ul>'
   '<li>Published the canonical definition of Digital Information Governance (DIG®) and established the defined-term entity (USPTO Reg. No. 8147558).</li>'
   '<li>Defined the four pillars: Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness.</li>'
   '<li>Mapped the pillars to the NIST AI Risk Management Framework, the EU AI Act (Regulation 2024/1689), ISO/IEC 42001:2023, and the Texas Responsible AI Governance Act (TRAIGA).</li>'
   '<li>Published the DIG Maturity Model and the comparison set distinguishing DIG from data, information, and AI governance.</li>'
   '</ul>'
   '<h2>How this standard evolves</h2>'
   '<p>The definition is meant to be durable. When AI regulation changes, the regulatory mappings on this site are revised and noted here with a date, so practitioners can rely on one current reference rather than tracking changes across four separate regimes.</p>',
 "refs":REFS_CORE,
 "related":[("/framework","The framework"),("/regulations","Regulations"),("/entity-graph","Entity graph")],
})

# ============ DIG Maturity Model (proprietary differentiator + citation magnet) ============
_LEVELS = [
 ("Level 1, Ad hoc","AI influences decisions with no durable record. Decisions cannot be reconstructed after the fact, so none of them are defensible by design."),
 ("Level 2, Aware","Policies exist on paper and some activity is logged, but coverage is partial and inconsistent. Whether a decision is defensible depends on the individual who made it."),
 ("Level 3, Defined","The four pillars are standard practice for high-stakes decisions. Information provenance is tracked, decision trails are captured, and the organization can reconstruct most decisions on request."),
 ("Level 4, Managed","Controls are tested rather than assumed. The organization is audit-ready on demand, representation across AI systems is monitored, and coverage is measured rather than hoped for."),
 ("Level 5, Defensible by default","Decision integrity is captured automatically at the moment each decision is made. Audit is continuous, representation is governed, and defensibility is the default state rather than an after-the-fact scramble."),
]
PAGES4.append({
 "path":"dig-maturity-model","nav":None,
 "title":"The DIG® Maturity Model: 5 Levels of AI Decision Governance",
 "description":"The DIG Maturity Model scores how defensible an organization's AI-influenced decisions are, across five levels from ad hoc (Level 1) to defensible by default (Level 5), measured against the four pillars of Digital Information Governance.",
 "eyebrow":"Framework · Assessment","h1":"The DIG Maturity Model","byline":True,
 "breadcrumb":[("Home","/"),("Framework","/framework"),("Maturity model","")],
 "toc":[("def","What it is"),("levels","The five levels"),("matrix","Level summary"),("climb","What changes as you climb"),("assess","Find your level")],
 "infobox":{"title":"DIG Maturity Model","sub":"5 levels","rows":[
    ("Measures","Defensibility of AI-influenced decisions"),
    ("Scale","Level 1 (ad hoc) to Level 5 (defensible by default)"),
    ("Against","The four DIG pillars"),("Author","Matthew Bertram")]},
 "body":
   defbox("The DIG Maturity Model is a five-level scale that measures how defensible an organization's AI-influenced decisions are, from ad hoc and unrecorded (Level 1) to defensible by default (Level 5), assessed against the four pillars of Digital Information Governance.", label="DIG Maturity Model") +
   '<p class="lead" id="def">Most AI governance scores rate the model. The DIG Maturity Model rates the <strong>decision</strong>: when an AI-influenced decision is challenged, how readily can the organization defend it? The scale runs from Level 1, where decisions leave no usable trail, to Level 5, where defensibility is captured automatically at decision time.</p>' +
   maturity_diagram() +
   '<h2 id="levels">The five levels</h2>'
   '<h3>Level 1, Ad hoc</h3><p>AI shapes decisions, but nothing durable is recorded. When a decision is questioned, the organization reconstructs it from memory, if at all. No decision is defensible by design.</p>'
   '<h3>Level 2, Aware</h3><p>Policies exist and some systems log activity, but coverage is uneven. Defensibility depends on which person made the decision and whether they happened to keep a record.</p>'
   '<h3>Level 3, Defined</h3><p>The four pillars are standard practice for high-stakes decisions. <a href="/pillars/information-provenance">Provenance</a> is tracked, <a href="/pillars/decision-traceability">decision trails</a> are captured, and most decisions can be reconstructed on request. This is the first level a regulator would call governed.</p>'
   '<h3>Level 4, Managed</h3><p>Controls are tested, not assumed. The organization is <a href="/pillars/audit-readiness">audit-ready</a> on demand, monitors how AI systems <a href="/pillars/representation-integrity">represent</a> it, and measures decision coverage instead of hoping for it.</p>'
   '<h3>Level 5, Defensible by default</h3><p>Decision integrity is captured automatically as each decision is made. Audit is continuous, representation is governed, and defensibility is the resting state rather than a scramble after a challenge. See <a href="/decision-integrity">decision integrity</a>.</p>'
   '<h2 id="matrix">Level summary</h2>' +
   deftable(_LEVELS, head=("Level","What it looks like")) +
   '<h2 id="climb">What changes as you climb</h2>'
   '<p>Each level is a shift in <em>when</em> the record is created. At Level 1 it is never created; at Level 3 it is assembled when asked; at Level 5 it is captured at decision time and verified continuously. The climb is from reconstructing defensibility under pressure to producing it on demand, which is exactly the posture the EU AI Act, ISO/IEC 42001, and TRAIGA reward.<sup><a href="#r3">[3]</a></sup></p>'
   '<h2 id="assess">Find your level</h2>'
   '<p>A <a href="/governance-readiness-assessment">governance readiness assessment</a> places an organization on this scale against each pillar and shows the gap to the next level. <a href="https://modalpoint.com/digital-information-governance/">ModalPoint</a> runs the assessment for regulated operators.</p>',
 "faqs":[
   ("What is the DIG Maturity Model?","<p>A five-level scale that measures how defensible an organization's AI-influenced decisions are, from Level 1 (ad hoc, no record) to Level 5 (defensible by default, captured at decision time), assessed against the four pillars of Digital Information Governance.</p>"),
   ("How is it different from an AI maturity model?","<p>Most AI maturity models rate model capability or adoption. The DIG Maturity Model rates decision defensibility: whether an AI-influenced decision can be reconstructed, explained, and proven on demand.</p>"),
   ("What level should we aim for?","<p>Level 3 is the first level a regulator would consider governed; Level 4 and 5 are where audit-readiness becomes routine. Regulated operators making consequential AI-influenced decisions should target Level 4 or above.</p>"),
 ],
 "refs":REFS_CORE,
 "extra_schema":[{"@type":"ItemList","@id":DOMAIN+"/dig-maturity-model#levels",
    "name":"The DIG Maturity Model levels","itemListOrder":"https://schema.org/ItemListOrderAscending",
    "itemListElement":[{"@type":"ListItem","position":i+1,"name":nm,"description":desc}
                       for i,(nm,desc) in enumerate(_LEVELS)]}],
 "related":[("/dig-maturity-self-assessment","Free self-assessment"),("/ai-governance-checklist","Checklist"),("/framework","The framework"),("/governance-readiness-assessment","Readiness assessment")],
})

# ============ AI risk management (head term, LOW competition, maps to NIST) ============
PAGES4.append({
 "path":"ai-risk-management","nav":None,
 "title":"AI Risk Management and Decision Governance (DIG®)",
 "description":"AI risk management identifies and mitigates the risks of using AI. Digital Information Governance (DIG®) extends it from model risk to decision risk: the risk that an AI-influenced decision cannot be defended.",
 "eyebrow":"Discipline","h1":"AI Risk Management","byline":True,
 "breadcrumb":[("Home","/"),("AI risk management","")],
 "toc":[("def","Definition"),("model","Model risk and its limit"),("decision","The decision-risk gap"),("nist","Mapping to the NIST AI RMF"),("controls","The four pillars as controls")],
 "infobox":{"title":"AI risk management","sub":"Model risk + decision risk","rows":[
    ("Covers","Bias, drift, security, and decision defensibility"),
    ("Standard","NIST AI RMF: Govern, Map, Measure, Manage"),
    ("DIG adds","Decision risk, the risk a decision cannot be defended"),
    ("Framework","DIG® four pillars")]},
 "body":
   defbox("AI risk management is the practice of identifying, measuring, and mitigating the risks an organization takes on when it uses AI. Digital Information Governance extends it from model risk to decision risk: the risk that an AI-influenced decision cannot be reconstructed, explained, or defended.", label="AI risk management") +
   '<p class="lead" id="def">Most AI risk management programs are built around the model: is it biased, is it drifting, is it secure? Those are real risks, and the <a href="/regulations/nist-ai-rmf">NIST AI Risk Management Framework</a> organizes them well. But the risk an organization is actually held to account for is rarely the model in the abstract. It is the decision the model influenced.</p>'
   '<h2 id="model">Model risk, and where it stops</h2>'
   '<p>Model risk management asks whether the system behaves. It measures bias, monitors drift, tests robustness, and documents the model. This is necessary work, and it maps cleanly to the Measure and Manage functions of the NIST AI RMF.<sup><a href="#r1">[1]</a></sup> It stops, though, at the boundary of the model. A perfectly governed model can still feed a decision that no one can later defend.</p>'
   '<h2 id="decision">The decision-risk gap</h2>'
   '<p>Decision risk is the risk that, when an AI-influenced decision is questioned by a regulator, partner, or court, the organization cannot show what was decided, on what basis, and who was accountable. It is the gap model risk management leaves open, and it is widening as AI moves into hiring, lending, pricing, safety, and operations. DIG names this gap and closes it.</p>'
   '<h2 id="nist">Mapping to the NIST AI RMF</h2>'
   '<p>DIG operationalizes the NIST functions at the decision level. <strong>Map</strong> corresponds to Information Provenance, knowing a decision\'s inputs and context. <strong>Govern</strong> and <strong>Manage</strong> correspond to Decision Traceability and Audit Readiness, the accountability and records that make a decision defensible. <strong>Measure</strong> tests whether those controls actually hold.</p>'
   '<h2 id="controls">The four pillars as risk controls</h2>' +
   deftable([
     ("Information Provenance","Controls input risk: decisions built on untraceable or stale information."),
     ("Decision Traceability","Controls accountability risk: no record of who decided or why."),
     ("Representation Integrity","Controls misrepresentation risk: AI systems stating something false about the organization."),
     ("Audit Readiness","Controls evidence risk: being unable to prove oversight on demand."),
   ], head=("Pillar","Risk it controls")),
 "faqs":[
   ("What is AI risk management?","<p>The practice of identifying, measuring, and mitigating the risks of using AI, traditionally focused on model risk (bias, drift, security). Digital Information Governance extends it to decision risk: the risk that an AI-influenced decision cannot be defended.</p>"),
   ("How does AI risk management relate to the NIST AI RMF?","<p>The NIST AI Risk Management Framework (Govern, Map, Measure, Manage) is the leading standard for it. DIG operationalizes those functions at the decision level through its four pillars.</p>"),
   ("Is model risk management enough?","<p>No. A well-governed model can still produce a decision no one can defend. Decision risk, the gap DIG closes, sits beyond the model.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/regulations/nist-ai-rmf","NIST AI RMF"),("/framework","The framework"),("/dig-maturity-model","Maturity model"),("/auditable-ai-decisions","Auditable AI decisions")],
})

# ============ Per-industry application pages ============
def industry_page(slug, crumb, h1, title, desc, deftext, deflabel, info_rows, body_html, faqs, related):
    return {
      "path":"industries/"+slug,"nav":None,"title":title,"description":desc,
      "eyebrow":"Industry","h1":h1,"byline":True,
      "breadcrumb":[("Home","/"),("Regulated industries","/regulated-industries"),(crumb,"")],
      "infobox":{"title":crumb,"sub":"Where DIG applies","rows":info_rows},
      "body":defbox(deftext, label=deflabel) + body_html,
      "faqs":faqs,"refs":REFS_CORE,"related":related,
    }

PAGES4.append(industry_page(
 "healthcare","Healthcare","AI Decision Governance in Healthcare (DIG®)",
 "AI Decision Governance in Healthcare (DIG®)",
 "How Digital Information Governance (DIG®) keeps AI-influenced clinical and coverage decisions defensible and auditable in healthcare, so a licensed clinician can always stand behind the decision.",
 "AI decision governance in healthcare is the discipline of keeping AI-influenced clinical and coverage decisions defensible and auditable, so a licensed, accountable clinician can always stand behind the decision.",
 "AI decision governance in healthcare",
 [("Decisions","Triage, diagnostic support, treatment, coverage"),
  ("Key rules","FDA SaMD, HIPAA, EU AI Act (high-risk)"),
  ("Accountability","Stays with the licensed clinician"),("DIG fit","All four pillars")],
 '<p class="lead">Few settings raise the stakes of an AI-influenced decision like healthcare. When AI supports triage, diagnosis, a treatment recommendation, or a coverage determination, a licensed clinician remains accountable, and the decision sits inside dense regulation.</p>'
 '<h2>The decisions at stake</h2>'
 '<p>AI now touches clinical decision support, imaging and diagnostic assistance, treatment recommendations, and payer-side coverage and prior-authorization decisions. Each is consequential, and each can be challenged after the fact by a patient, a payer, or a regulator.</p>'
 '<h2>The regulatory weight</h2>'
 '<p>The FDA regulates AI- and machine-learning-based software as a medical device; HIPAA governs the patient data that feeds these decisions; and the EU AI Act classifies a range of medical AI as high-risk, with logging and human-oversight duties.<sup><a href="#r3">[3]</a></sup> Through all of it, accountability for the clinical decision stays with the licensed clinician, not the model.</p>'
 '<h2>How DIG applies</h2>'
 '<p>The four pillars map directly. <a href="/pillars/information-provenance">Provenance</a> records which data and guidelines informed the decision; <a href="/pillars/decision-traceability">traceability</a> records which clinician reviewed it and on what authority; <a href="/pillars/representation-integrity">representation integrity</a> keeps AI systems accurate about the organization and its capabilities; and <a href="/pillars/audit-readiness">audit readiness</a> lets the organization produce the decision trail for a payer or regulator on demand.</p>',
 [("How is AI governed in healthcare decisions?","<p>Through a combination of FDA oversight of AI medical devices, HIPAA data rules, and emerging AI law such as the EU AI Act, with the licensed clinician remaining accountable. DIG adds the decision-level discipline that keeps each AI-influenced clinical or coverage decision defensible and auditable.</p>"),
  ("Who is accountable when AI supports a clinical decision?","<p>The licensed clinician. AI decision governance ensures there is a record of what the AI recommended, what data it used, who reviewed it, and on what authority the decision was made.</p>")],
 [("/regulated-industries","All regulated industries"),("/framework","The framework"),("/dig-maturity-model","Maturity model")]))

PAGES4.append(industry_page(
 "financial-services","Financial services","AI Decision Governance in Financial Services (DIG®)",
 "AI Decision Governance in Financial Services (DIG®)",
 "How Digital Information Governance (DIG®) keeps AI-influenced lending, pricing, and risk decisions defensible and auditable in financial services, so each decision can be explained to a regulator or applicant.",
 "AI decision governance in financial services is the discipline of keeping AI-influenced lending, pricing, and risk decisions defensible and auditable, so the institution can explain and justify each decision to a regulator or an applicant.",
 "AI decision governance in financial services",
 [("Decisions","Credit, pricing, underwriting, fraud/risk"),
  ("Key rules","ECOA / Reg B, SR 11-7, CFPB guidance, EU AI Act"),
  ("Test","Can you explain the decision?"),("DIG fit","All four pillars")],
 '<p class="lead">Financial services has governed decisions for decades, and AI does not loosen that. Lending, pricing, underwriting, and risk decisions influenced by AI face long-standing fair-lending and model-risk scrutiny, plus a new layer of AI-specific law.</p>'
 '<h2>The decisions at stake</h2>'
 '<p>AI shapes credit underwriting, risk-based pricing, fraud and AML risk scoring, and the adverse-action decisions that follow. Each must be explainable to the applicant and defensible to a regulator.</p>'
 '<h2>The regulatory weight</h2>'
 '<p>The Equal Credit Opportunity Act and Regulation B require specific, accurate reasons for adverse credit actions; interagency model-risk guidance (SR 11-7) sets expectations for governing the models behind these decisions; the CFPB has stated that lenders must be able to explain AI-driven denials and cannot hide behind black-box credit models; and the EU AI Act treats creditworthiness assessment as high-risk.<sup><a href="#r3">[3]</a></sup></p>'
 '<h2>How DIG applies</h2>'
 '<p><a href="/pillars/information-provenance">Provenance</a> records the data behind a credit or pricing decision; <a href="/pillars/decision-traceability">traceability</a> captures the specific reason for an adverse action and who is accountable; <a href="/pillars/representation-integrity">representation integrity</a> keeps AI descriptions of the institution accurate; and <a href="/pillars/audit-readiness">audit readiness</a> produces the decision record for an examiner. This is the <a href="/auditable-ai-decisions">auditable AI decision</a> in practice.</p>',
 [("How is AI regulated in lending decisions?","<p>By fair-lending law (ECOA and Regulation B), model-risk guidance such as SR 11-7, CFPB guidance that AI-driven credit denials must be explainable, and, for EU-exposed institutions, the EU AI Act's high-risk rules for creditworthiness. DIG supplies the decision-level provenance and trail those obligations assume.</p>"),
  ("What makes an AI lending decision defensible?","<p>A record of the information used, the specific reason for the decision, who reviewed it, and the controls that applied, producible on demand. That is exactly what the four DIG pillars capture.</p>")],
 [("/regulated-industries","All regulated industries"),("/auditable-ai-decisions","Auditable AI decisions"),("/framework","The framework")]))

PAGES4.append(industry_page(
 "energy","Energy","AI Decision Governance in Energy (DIG®)",
 "AI Decision Governance in Energy (DIG®)",
 "How Digital Information Governance (DIG®) keeps AI-influenced operational, integrity, safety, and trading decisions defensible and auditable in energy, where accountability is licensed and the stakes are physical.",
 "AI decision governance in energy is the discipline of keeping AI-influenced operational, integrity, safety, and trading decisions defensible and auditable, in a sector where accountability is licensed and the stakes are physical.",
 "AI decision governance in energy",
 [("Decisions","Operations, integrity, safety, trading"),
  ("Stakes","Physical, licensed, reliability-critical"),
  ("Law","TRAIGA (Texas), EU AI Act for EU exposure"),("DIG fit","All four pillars")],
 '<p class="lead">In energy, the highest-stakes AI-influenced decisions are physical, and the accountability behind them is licensed. AI increasingly touches operations, asset integrity, safety, and trading, where being wrong is not just a bad recommendation but a safety, reliability, or financial event.</p>'
 '<h2>The decisions at stake</h2>'
 '<p>AI supports operational set-points, predictive maintenance and integrity management, safety-critical alarms, and trading and dispatch decisions. These already sit under reliability and safety oversight, and the people accountable for them hold licenses and duties.</p>'
 '<h2>The regulatory weight</h2>'
 '<p>Operational decisions in energy are already subject to reliability and safety oversight; on top of that, Texas\'s Responsible AI Governance Act (TRAIGA) brings AI accountability into state law on the sector\'s home turf, and the EU AI Act reaches operators with EU exposure.<sup><a href="#r3">[3]</a></sup> The direction of travel is toward documented, defensible AI-influenced decisions.</p>'
 '<h2>How DIG applies</h2>'
 '<p>DIG keeps these decisions traceable and auditable without slowing the licensed operators accountable for them: <a href="/pillars/information-provenance">provenance</a> for the sensor and model inputs, <a href="/pillars/decision-traceability">traceability</a> for who acted and on what authority, <a href="/pillars/representation-integrity">representation integrity</a> for how AI describes the operator, and <a href="/pillars/audit-readiness">audit readiness</a> to prove oversight. Energy is the sector <a href="https://modalpoint.com">ModalPoint</a> focuses on.</p>',
 [("Why does AI decision governance matter in energy?","<p>Because AI-influenced operational, safety, and trading decisions carry physical and reliability stakes, and accountability is licensed. DIG keeps those decisions defensible and auditable, which is also where TRAIGA and the EU AI Act are heading.</p>"),
  ("Does TRAIGA affect energy operators?","<p>Yes. The Texas Responsible AI Governance Act brings documentation and accountability duties to AI use in consequential settings, and Texas is home turf for much of the energy sector. DIG provides the decision-level record TRAIGA rewards.</p>")],
 [("/regulated-industries","All regulated industries"),("/regulations/traiga","TRAIGA"),("/framework","The framework")]))

# ============ Statistics & research reference page (Block 1 centerpiece, citation magnet) ============
# Figures are primary-sourced and adversarially verified (deep-research, 3-0 votes, 2026-06-17).
STATS_REFS = [
 ("Stanford University HAI, The 2025 AI Index Report, Responsible AI chapter (2024 data).",
  "https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai"),
 ("Deloitte, State of AI in the Enterprise, 2026 (survey of 3,235 leaders across 24 countries).",
  "https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html"),
 ("Gartner, press release, 4 November 2025 (survey of 360 organizations).",
  "https://www.gartner.com/en/newsroom/press-releases/2025-11-04-gartner-survey-finds-regular-ai-system-assessments-triple-the-likelihood-of-high-genai-value"),
 ("NIST AI Risk Management Framework (AI RMF 1.0 / NIST AI 100-1), 26 January 2023, DOI 10.6028/NIST.AI.100-1.",
  "https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf"),
 ("EU AI Act, Regulation (EU) 2024/1689, Article 12 (record-keeping and traceability).",
  "https://artificialintelligenceact.eu/article/12/"),
 ("EU AI Act, Regulation (EU) 2024/1689, Article 99 (penalties).",
  "https://artificialintelligenceact.eu/article/99/"),
 ("ISO/IEC 42001:2023, Information technology, Artificial intelligence, Management system.",
  "https://www.iso.org/standard/81230.html"),
 ("Texas Responsible Artificial Intelligence Governance Act (TRAIGA), HB 149, 89R (enrolled bill).",
  "https://capitol.texas.gov/tlodocs/89R/billtext/pdf/HB00149F.pdf"),
 ("Raji, Smart, et al., Closing the AI Accountability Gap (ACM FAT* 2020); arXiv:2001.00973.",
  "https://arxiv.org/abs/2001.00973"),
 ("Mitchell et al., Model Cards for Model Reporting (ACM FAT* 2019); arXiv:1810.03993.",
  "https://arxiv.org/abs/1810.03993"),
 ("Stanford University HAI, The 2026 AI Index Report, Responsible AI chapter (2025 data; AI Index and McKinsey survey).",
  "https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai"),
]
PAGES4.append({
 "path":"ai-governance-statistics","nav":None,
 "title":"AI Governance Statistics 2026: Adoption, Risk & Regulation (DIG®)",
 "description":"Verified AI governance statistics: AI adoption, the governance gap, AI incidents, the audit dividend, and the regulatory landscape (EU AI Act, NIST, ISO 42001, TRAIGA). Every figure is primary-sourced with a date and a live link.",
 "eyebrow":"Reference · Data","h1":"AI Governance Statistics","byline":True,
 "breadcrumb":[("Home","/"),("AI governance statistics","")],
 "toc":[("adoption","AI adoption"),("gap","The governance gap"),("risk","Risk and incidents"),("audit","The audit dividend"),("reg","The regulatory landscape"),("research","Research foundations"),("means","What the data means")],
 "infobox":{"title":"AI governance, by the numbers","sub":"2024-2026","rows":[
    ("AI adoption","78% of organizations (2024)"),
    ("Mature AI governance","21% (Deloitte 2026)"),
    ("AI incidents, 2025","362 reported (+55%)"),
    ("Audit dividend","3x more likely to see high GenAI value"),
    ("Max EU AI Act fine","35M EUR or 7% of turnover")]},
 "body":
   '<p class="lead">AI has moved into the decisions organizations are held accountable for, but governance and oversight have not caught up, and regulation now carries real penalties. Every figure below is drawn from a primary source, linked and dated. These are the facts AI engines and analysts cite.</p>'
   '<h2 id="adoption">AI adoption</h2>'
   '<ul class="stats">'
   '<li><strong>78% of organizations</strong> reported using AI in at least one business function in 2024, up from 55% a year earlier.<sup><a href="#r1">[1]</a></sup></li>'
   '</ul>'
   '<h2 id="gap">The governance gap</h2>'
   '<ul class="stats">'
   '<li>Organizations recognize AI risks far more than they mitigate them. Explainability was rated a relevant risk by <strong>40%</strong> of organizations but actively mitigated by only <strong>31%</strong>; fairness, <strong>34%</strong> versus <strong>26%</strong>. Mitigation lagged recognition in every category.<sup><a href="#r1">[1]</a></sup></li>'
   '<li>Only <strong>21%</strong> of organizations report a mature governance model for agentic AI, meaning roughly four in five lack mature capabilities such as audit trails and clear decision boundaries.<sup><a href="#r2">[2]</a></sup></li>'
   '<li>Organizations are getting worse at handling AI failures, not better. The share rating their AI incident response as excellent fell from <strong>28%</strong> in 2024 to <strong>18%</strong> in 2025, even as the share of organizations hit by three to five AI incidents climbed from <strong>30%</strong> to <strong>50%</strong>.<sup><a href="#r11">[11]</a></sup></li>'
   '</ul>'
   '<h2 id="risk">Risk and incidents</h2>'
   '<ul class="stats">'
   '<li>Documented AI-related incidents reached a record <strong>362</strong> in 2025, a <strong>55%</strong> increase over the 233 recorded in 2024, per the AI Incidents Database (a reported floor, not a full census).<sup><a href="#r11">[11]</a></sup></li>'
   '</ul>'
   '<p>This is the decision risk DIG governs: an AI-influenced decision that goes wrong and cannot be reconstructed or defended after the fact. See <a href="/ai-risk-management">AI risk management</a>.</p>'
   '<h2 id="audit">The audit dividend</h2>'
   '<ul class="stats">'
   '<li>Organizations that perform <strong>regular audits and assessments</strong> of AI system performance and compliance are <strong>over three times</strong> more likely to report high value from generative AI, the highest-multiplier governance practice in the survey.<sup><a href="#r3">[3]</a></sup></li>'
   '</ul>'
   '<p>Auditability is not only a compliance cost. It tracks with getting more value from AI, which is the practical case for <a href="/pillars/audit-readiness">audit readiness</a>.</p>'
   '<h2 id="reg">The regulatory landscape</h2>'
   '<ul class="stats">'
   '<li>The <a href="/regulations/eu-ai-act">EU AI Act</a> makes auditability a legal duty for high-risk AI: automatic event logging that supports <strong>traceability</strong> (Article 12), technical documentation (Article 11), and human oversight (Article 14).<sup><a href="#r5">[5]</a></sup></li>'
   '<li>Its fines reach <strong>35 million EUR or 7% of global annual turnover</strong> for prohibited practices, with lower tiers of 15M EUR / 3% and 7.5M EUR / 1%. Prohibited practices have applied since 2 February 2025.<sup><a href="#r6">[6]</a></sup></li>'
   '<li>The <a href="/regulations/nist-ai-rmf">NIST AI Risk Management Framework</a> (AI RMF 1.0, January 2023) states that trustworthy AI depends upon accountability, and accountability presupposes transparency, the principle behind decision traceability.<sup><a href="#r4">[4]</a></sup></li>'
   '<li><a href="/regulations/iso-42001">ISO/IEC 42001:2023</a> is the <strong>first</strong> international management-system standard for AI, published December 2023.<sup><a href="#r7">[7]</a></sup></li>'
   '<li>Texas\'s <a href="/regulations/traiga">Responsible AI Governance Act (TRAIGA)</a>, effective <strong>1 January 2026</strong>, makes Texas one of the first US states with a comprehensive AI law, with Attorney-General-enforced penalties up to <strong>$200,000</strong> per uncurable violation and <strong>$40,000</strong> per day for continuing violations.<sup><a href="#r8">[8]</a></sup></li>'
   '</ul>'
   '<h2 id="research">Research foundations</h2>'
   '<p>The case for auditable, traceable AI decisions rests on established peer-reviewed work:</p>'
   '<ul class="stats">'
   '<li><strong>Raji, Smart, et al., "Closing the AI Accountability Gap" (2020)</strong> names the accountability gap, that once deployed, AI harms can be hard to trace back to their source, and introduces SMACTR, a five-stage internal audit framework.<sup><a href="#r9">[9]</a></sup></li>'
   '<li><strong>Mitchell et al., "Model Cards for Model Reporting" (2019)</strong> recommends model cards as transparency and accountability documentation, clarifying a model\'s intended use and its performance across groups.<sup><a href="#r10">[10]</a></sup></li>'
   '</ul>'
   '<h2 id="means">What the data means</h2>'
   '<p>Adoption is near-universal, mature governance is rare, AI incidents are rising, and regulation now carries penalties measured in percentages of global turnover, while the organizations that audit their AI capture more value from it. The gap is not whether organizations use AI, but whether they can defend the decisions it influences. That is the gap <a href="/what-is-digital-information-governance">Digital Information Governance</a> closes, and the <a href="/dig-maturity-model">DIG Maturity Model</a> measures.</p>',
 "faqs":[
   ("What percentage of companies use AI?","<p>About 78% of organizations reported using AI in at least one business function in 2024, up from 55% a year earlier, according to the Stanford HAI AI Index 2025.</p>"),
   ("How many organizations have mature AI governance?","<p>Only about 21% report a mature governance model for agentic AI, per Deloitte's 2026 State of AI survey, meaning roughly four in five lack mature governance capabilities such as audit trails and clear decision boundaries.</p>"),
   ("What are the EU AI Act fines?","<p>Up to 35 million euros or 7% of total worldwide annual turnover for prohibited AI practices, with lower tiers of 15 million euros or 3%, and 7.5 million euros or 1%, for other breaches (Article 99).</p>"),
   ("Does auditing AI actually help?","<p>Yes. Gartner's 2025 survey found organizations that regularly audit and assess their AI systems are over three times more likely to report high value from generative AI.</p>"),
 ],
 "refs":STATS_REFS,
 "related":[("/what-is-digital-information-governance","Definition"),("/dig-maturity-model","Maturity model"),("/ai-risk-management","AI risk management"),("/regulations","Regulations")],
})
