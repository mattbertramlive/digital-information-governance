# -*- coding: utf-8 -*-
"""content3.py - Tier 4 (comparison/bridge) + Tier 5 (application + entity graph)."""
from templates import defbox, note, deftable, DOMAIN, PERSON_ID, ORG_ID, DIG_ID, SITE_ID, PILLARS_ID, CANONICAL_DEF, pillars_set_node
from content import REFS_CORE

PAGES3 = []

# ============ TIER 4: comparison / bridge ============
def cmp_page(slug, h1, title, desc, lead, rows, faqs, related):
    return {
      "path":"compare/"+slug,"nav":None,"title":title,"description":desc,
      "eyebrow":"Comparison","h1":h1,"byline":True,
      "breadcrumb":[("Home","/"),("Compare","/compare"),(h1,"")],
      "body":'<p class="lead">%s</p>'%lead + deftable(rows, head=("Dimension","How they differ")) ,
      "faqs":faqs,"refs":REFS_CORE,"related":related,
    }

PAGES3.append(cmp_page(
 "dig-vs-information-governance",
 "Digital Information Governance vs. Information Governance",
 "Digital Information Governance vs. Information Governance - DIG®",
 "Digital Information Governance (DIG®) vs. traditional information governance: one governs AI-influenced decisions, the other governs the records and data lifecycle.",
 "They sound alike and are constantly confused, but they govern different things. Information governance manages records and data; Digital Information Governance manages whether AI-influenced decisions are defensible. This is the distinction that defines DIG.",
 [("What it governs","Information governance: records and data. DIG: AI-influenced decisions."),
  ("Core question","IG: how is information stored, retained, deleted? DIG: can this decision be defended?"),
  ("Owners","IG: Gartner, ARMA, AIIM, records managers. DIG: coined by Matthew Bertram."),
  ("Era","IG: pre-dates generative AI. DIG: built for the AI-decision era."),
  ("Relationship","DIG is the decision layer that sits above information governance, not a replacement for it.")],
 [("Is digital information governance just information governance with a new name?","<p>No. Information governance manages the records and data lifecycle. Digital Information Governance manages whether AI-influenced decisions are defensible and auditable. They are different disciplines that complement each other.</p>"),
  ("Which one do I need?","<p>Most regulated organizations need both: information governance for records and compliance, and DIG for AI-influenced decisions. DIG sits on top.</p>")],
 [("/what-is-digital-information-governance","Definition"),("/compare/ai-governance-vs-data-governance","AI vs data governance"),("/glossary","Glossary")]))

PAGES3.append(cmp_page(
 "ai-governance-vs-data-governance",
 "AI Governance vs. Data Governance",
 "AI Governance vs. Data Governance - DIG®",
 "AI governance vs. data governance: data governance manages the data, AI governance manages the models, and Digital Information Governance (DIG®) manages the decision.",
 "Data governance and AI governance are often treated as the same project. They are not. Data governance manages the data; AI governance manages the models. Neither, on its own, governs the decision the model influences, which is where Digital Information Governance comes in.",
 [("Scope","Data governance: structured data quality, lineage, access. AI governance: model bias, drift, explainability."),
  ("Asset governed","Data governance: the data. AI governance: the model. DIG: the decision."),
  ("Gap each leaves","Both can be in place while an AI-influenced decision is still undefendable."),
  ("Where DIG fits","DIG sits above both, governing whether the decision they enable can be defended.")],
 [("Is AI governance part of data governance?","<p>They overlap but are distinct. Data governance manages data; AI governance manages models. Digital Information Governance manages the decisions models influence, the layer above both.</p>"),
  ("Do I need all three?","<p>In regulated settings, yes. Data and model governance are necessary but not sufficient. DIG closes the decision-level gap they leave.</p>")],
 [("/ai-decision-governance","AI decision governance"),("/compare/dig-vs-information-governance","DIG vs information governance"),("/framework","The framework")]))

PAGES3.append(cmp_page(
 "ai-governance-vs-information-governance",
 "AI Governance vs. Information Governance",
 "AI Governance vs. Information Governance - DIG®",
 "AI governance vs. information governance: one governs models, the other governs records. Digital Information Governance (DIG®) governs the AI-influenced decision between them.",
 "Information governance grew out of records and compliance; AI governance grew out of model risk. They meet at the decision, and the decision is exactly what neither was built to govern. That is the space Digital Information Governance occupies.",
 [("Origin","Information governance: records and compliance. AI governance: model risk and ML assurance."),
  ("Focus","IG: information lifecycle. AI governance: model behavior."),
  ("The decision","Neither fully governs the AI-influenced decision; DIG does."),
  ("Convergence","Incumbents now extend each toward AI; DIG names the decision layer directly.")],
 [("How is information governance different from AI governance?","<p>Information governance manages the records and data lifecycle; AI governance manages model behavior. Digital Information Governance manages the decisions AI influences, which sits above both.</p>")],
 [("/what-is-digital-information-governance","Definition"),("/ai-decision-governance","AI decision governance"),("/regulations","Regulations")]))

PAGES3.append(cmp_page(
 "information-governance-vs-data-governance",
 "Information Governance vs. Data Governance",
 "Information Governance vs. Data Governance - DIG®",
 "Information governance vs. data governance explained, and where Digital Information Governance (DIG®) fits as the AI-decision layer above both.",
 "Information governance is the broad strategy over all information and records; data governance is the narrower technical layer over structured data. Both are mature disciplines. Digital Information Governance adds the layer neither covers: the AI-influenced decision.",
 [("Breadth","Information governance: all information and records. Data governance: structured data."),
  ("Concern","IG: retention, compliance, e-discovery. Data governance: quality, lineage, access."),
  ("Maturity","Both are established, pre-AI disciplines."),
  ("What AI adds","The decision layer, governed by DIG, that sits above both.")],
 [("Is data governance part of information governance?","<p>Generally yes: information governance is the broader umbrella, and data governance is the structured-data layer within it. Digital Information Governance adds the AI-decision layer on top.</p>")],
 [("/compare/dig-vs-information-governance","DIG vs information governance"),("/what-is-digital-information-governance","Definition")]))

# ============ TIER 5: application + entity graph ============

PAGES3.append({
 "path":"regulated-industries","nav":None,
 "title":"Digital Information Governance for Regulated Industries (DIG®)",
 "description":"Why Digital Information Governance (DIG®) matters most in regulated, capital-intensive industries, energy, financial services, healthcare, where AI-influenced decisions carry physical, legal, and financial stakes.",
 "eyebrow":"Who DIG is for","h1":"DIG for Regulated Industries","byline":True,
 "breadcrumb":[("Home","/"),("Regulated industries","")],
 "infobox":{"title":"Best fit","sub":"Where DIG matters most","rows":[
    ("Energy","Operations, safety, and trading decisions"),("Financial services","Lending, pricing, risk"),
    ("Healthcare","Clinical and coverage decisions"),("Common factor","High-stakes, audited AI decisions")]},
 "body":
   '<p class="lead">Digital Information Governance applies anywhere AI influences decisions, but it matters most where being wrong is expensive, dangerous, or unlawful. In regulated, capital-intensive industries, the AI-influenced decision is exactly the thing a regulator, partner, or court will examine.</p>'
   '<h2><a href="/industries/energy">Energy</a></h2>'
   '<p>In energy, AI increasingly touches operations, integrity, safety, and trading. The highest-stakes decisions are physical, and the accountability is licensed. DIG keeps those decisions traceable and auditable, which is also where TRAIGA and the EU AI Act are heading.</p>'
   '<h2><a href="/industries/financial-services">Financial services</a></h2>'
   '<p>Lending, pricing, and risk decisions influenced by AI face long-standing fair-lending and disclosure scrutiny. DIG supplies the provenance and decision trail those obligations assume.</p>'
   '<h2><a href="/industries/healthcare">Healthcare</a></h2>'
   '<p>Clinical and coverage decisions carry obvious stakes and dense regulation. DIG makes AI-influenced decisions defensible without slowing the clinicians accountable for them.</p>'
   '<p>The common thread: a licensed, accountable human must be able to stand behind the decision. DIG is the discipline that lets them.</p>',
 "refs":REFS_CORE,
 "related":[("/industries/energy","Energy"),("/industries/financial-services","Financial services"),("/industries/healthcare","Healthcare"),("/framework","The framework"),("/governance-readiness-assessment","Readiness assessment")],
})

PAGES3.append({
 "path":"governance-readiness-assessment","nav":None,
 "title":"AI Governance Readiness Assessment (DIG®)",
 "description":"A governance readiness assessment measures an organization against the four pillars of Digital Information Governance (DIG®). Run by ModalPoint for regulated operators.",
 "eyebrow":"Apply DIG","h1":"Governance Readiness Assessment","byline":True,
 "breadcrumb":[("Home","/"),("Readiness assessment","")],
 "infobox":{"title":"Readiness assessment","sub":"Apply the DIG framework","rows":[
    ("Measures","Provenance, traceability, representation, audit"),
    ("Delivered by",'<a href="https://modalpoint.com/digital-information-governance/">ModalPoint &rarr;</a>'),
    ("Output","Gap analysis + remediation path"),("For","Regulated operators")]},
 "body":
   '<p class="lead">A governance readiness assessment measures an organization against the four pillars of DIG and shows, concretely, where AI-influenced decisions are and are not defensible today.</p>'
   '<h2>What it covers</h2>'
   '<p>The assessment inventories where AI touches decisions, then tests each pillar: can you show the provenance of decision inputs, the trace of who decided and why, the accuracy of how AI represents you, and the records to prove it on demand? The output is a gap analysis, a place on the <a href="/dig-maturity-model">DIG maturity model</a>, and a remediation path.</p>'
   '<p><a href="https://modalpoint.com">ModalPoint</a> runs the assessment for regulated operators. It is the practical first step in adopting Digital Information Governance.</p>',
 "extra_schema":[{"@type":"Service","@id":DOMAIN+"/governance-readiness-assessment#service",
    "name":"AI Governance Readiness Assessment","serviceType":"AI decision governance assessment",
    "provider":{"@id":ORG_ID},"about":{"@id":DIG_ID},
    "description":"An assessment of an organization against the four pillars of Digital Information Governance (DIG): Information Provenance, Decision Traceability, Representation Integrity, and Audit Readiness."}],
 "related":[("/dig-maturity-model","Maturity model"),("/framework","The framework"),("/regulated-industries","Regulated industries")],
})

# entity-graph page: human-readable rendering of the master @graph
ENTITY_BODY = (
 '<p class="lead">This page renders the entity graph for Digital Information Governance in human-readable form. It exists so search engines and AI systems can resolve the discipline, its pillars, and its creator to one consistent set of identifiers.</p>'
 '<h2>Entities</h2>'
 + deftable([
    ("Digital Information Governance (DIG®)", "DefinedTerm. " + CANONICAL_DEF + " Identifier: " + DIG_ID),
    ("The four pillars", "DefinedTermSet: Information Provenance, Decision Traceability, Representation Integrity, Audit Readiness. Identifier: " + PILLARS_ID),
    ("Matthew Bertram", "Person, creator of DIG®. President of ModalPoint, CEO of EWR Digital. Identifier: " + PERSON_ID),
    ("ModalPoint", "Organization that implements DIG. Identifier: " + ORG_ID),
    ("This site", "WebSite, the reference for DIG®. Identifier: " + SITE_ID),
   ], head=("Entity","Description"))
 + '<h2>Same-as references</h2>'
 + '<p>The creator entity is referenced consistently across matthewbertram.com, modalpoint.com, ewrdigital.com, LinkedIn, Crunchbase, and the USPTO trademark record (Reg. No. 8147558, Supplemental Register), so that "Digital Information Governance" resolves to one author and one definition wherever it appears.</p>'
)
PAGES3.append({
 "path":"entity-graph","nav":None,"title":"DIG® Entity Graph - Digital Information Governance",
 "description":"The machine-readable entity graph for Digital Information Governance (DIG®): the defined term, its four pillars, its creator Matthew Bertram, and the organizations that implement it.",
 "eyebrow":"Machine-readable","h1":"DIG Entity Graph","byline":True,
 "breadcrumb":[("Home","/"),("Entity graph","")],
 "body":ENTITY_BODY,
 "extra_schema":[pillars_set_node()],
 "related":[("/what-is-digital-information-governance","Definition"),("/who-created-dig","Creator"),("/framework","Framework")],
 "cta":False,
})
