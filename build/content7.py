# -*- coding: utf-8 -*-
"""content7.py - Tier 9: the reference build-out (v1.1, September 2026).
Expanded agentic glossary (overrides /glossary), AI Regulation Tracker,
AI Agent Incident Register, frontier access-tier matrix.
Roadmap: audits/2026-09-05-agentic-extension/REFERENCE-ROADMAP.md"""
import re
from templates import defbox, note, deftable, DOMAIN
from content import GLOSSARY, REFS_CORE
from content6 import REFS_AGENT

PAGES7 = []
TODAY_REVIEW = "September 5, 2026"

# ============ Agentic glossary (the action-layer vocabulary) ============
GLOSSARY_AGENTIC = [
 ("Agentic AI","AI systems that pursue goals by taking actions through tools and interfaces, rather than only generating content for a person to act on."),
 ("AI agent","A software system that uses an AI model to decide on and carry out actions (tool calls, browser use, transactions) toward an assigned objective, with limited or no step-by-step human direction."),
 ("Digital employee","An AI agent doing work a person would otherwise do, operating real interfaces such as a keyboard, mouse, terminal, or browser. The term frames the governance expectation: identity, permission, and audit, like any employee."),
 ("Action layer","The governance layer concerned with what an AI did, extending decision-level governance one step further, from the decision to the act. Added to the DIG framework in v1.1."),
 ("AI agent governance","The discipline of keeping AI-executed actions defensible and auditable: what an agent was authorized to see, decide, and do, who approved that authority, and whether the action can be reconstructed afterward."),
 ("Execution boundary","The written limit of what an agent is permitted to do: the systems it may touch, the actions it may take, the thresholds it may not cross. At maturity Level 4 the boundary is tested, not assumed."),
 ("Delegated authority","Decision rights an organization has formally assigned to an AI agent, including their scope and thresholds."),
 ("Delegation record","The record of a grant of authority to an agent: what was delegated, by whom, when, under what conditions, and how it can be revoked."),
 ("Approval gate","A required human sign-off inserted before an agent action executes, typically for actions past a defined risk threshold."),
 ("Agent identity","A distinct, non-human identity under which an agent authenticates and acts, so that its actions are attributable and separable from any person's."),
 ("Scoped credential","A credential granting an agent only the access its task requires, in contrast to borrowing a person's full access."),
 ("Credential borrowing","An agent operating under a human's credentials, which makes its actions indistinguishable from that person's in every log. The Level 1 marker of agentic maturity."),
 ("Least privilege (for agents)","Granting an agent the minimum access and action rights its task requires, and nothing else."),
 ("Action trail","The action-level record of what an agent did: tool calls, commands, page loads, and the approvals attached to each."),
 ("Replayability","The property that an agent's sequence of actions can be reconstructed end to end from records after the fact."),
 ("Containment","The rehearsed ability to pause, revoke, or roll back an agent and its actions when something goes wrong. At Level 5 it is a tested control, not a hope."),
 ("Kill switch","A control that immediately halts an agent's ability to act. The containment tool of last resort."),
 ("Rollback","Undoing the effects of an agent's actions after execution. Part of containment."),
 ("Human-in-the-loop","An oversight design in which a person approves each consequential action before it executes."),
 ("Human-on-the-loop","An oversight design in which agents act autonomously while a person monitors and can intervene. Oversight attaches to the grant, not to each action."),
 ("Agent inventory","The maintained list of every agent, automation, and tool-using AI in an organization, with the credentials and access each one holds. The Level 3 floor."),
 ("Agent sprawl","The accumulation of agents nobody inventories: deployed independently by teams, each holding credentials and taking actions outside any governance view."),
 ("Machine-speed risk","Risk amplified because agents act far faster and more often than people, so a small authorization error compounds before anyone notices."),
 ("Misaligned action","An action an AI takes that was not authorized, or that does not serve the objective its operator intended. Frontier-lab safety frameworks name containing these actions as a design goal."),
 ("Autonomous action","An action an agent executes without a person approving that specific step."),
 ("Tool call","A single invocation by an AI of an external function, API, or interface. The atomic unit of an action trail."),
 ("Computer use","An AI operating a computer's actual interface (screen, cursor, keyboard) rather than a purpose-built API."),
 ("Model Context Protocol (MCP)","An open protocol for connecting AI systems to tools and data sources. In governance terms, every connection is an access grant that belongs in the agent's scope record."),
 ("Orchestration","Coordinating multiple agents or steps into one workflow. Governance must still attribute each action to the agent and the grant that produced it."),
 ("Sub-agent","An agent spawned by another agent to perform part of a task. Delegation records must cover authority passed downward, or scope widens silently."),
 ("Prompt injection","Content crafted so that an AI processing it treats it as instructions. At the action layer it becomes an authorization attack: injected text steering an agent into actions nobody approved."),
 ("Capability tier","A vendor-defined level of model capability and access, such as a generally available tier and a gated tier for approved users."),
 ("Trusted access","A vendor program granting vetted organizations access to model capabilities that are withheld from general availability."),
 ("Preparedness framework","A frontier lab's published system for evaluating and gating dangerous model capabilities before release. OpenAI's term; Anthropic's analogue is its Responsible Scaling Policy."),
 ("Critical capability","The highest capability designation in OpenAI's Preparedness Framework, first reached for cybersecurity by the Astra model in September 2026."),
]

def _slug(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return s

def _anchored_table(rows):
    out = ['<table class="deftable"><tr><th class="term">Term</th><th>Definition</th></tr>']
    for term, defn in rows:
        out.append('<tr id="%s"><td class="term">%s</td><td>%s</td></tr>' % (_slug(term), term, defn))
    out.append('</table>')
    return "".join(out)

GLOSSARY_ALL = list(GLOSSARY) + GLOSSARY_AGENTIC

OVERRIDES7 = []
OVERRIDES7.append({
 "path":"glossary","nav":"glossary",
 "title":"Digital Information Governance Glossary - DIG® and AI Agent Terms",
 "description":"The DIG® glossary: more than 40 canonical definitions across AI decision governance and the agentic action layer, from information provenance to execution boundaries, delegation records, and containment.",
 "eyebrow":"Reference","h1":"DIG Glossary","byline":True,
 "breadcrumb":[("Home","/"),("Glossary","")],
 "toc":[("core","Core discipline"),("agentic","The action layer (agentic AI)"),("cite","Citing a term")],
 "infobox":{"title":"DIG Glossary","sub":"Canonical definitions","rows":[
    ("Terms", str(len(GLOSSARY_ALL))),
    ("Sections","Core discipline; action layer"),
    ("Added in v1.1","%d agentic terms" % len(GLOSSARY_AGENTIC)),
    ("Schema","DefinedTermSet, one DefinedTerm per entry"),
    ("Stable anchors","Every term links: /glossary#term-name")]},
 "body":
   '<p class="lead">Defined terms used across the Digital Information Governance reference. Each term has a single canonical definition and a stable anchor, so it can be cited directly. Version 1.1 adds the action-layer vocabulary: the terms organizations need once AI systems act on information rather than only reading it.</p>'
   '<h2 id="core">Core discipline</h2>' + _anchored_table(GLOSSARY) +
   '<h2 id="agentic">The action layer: agentic AI terms</h2>'
   '<p>Added in v1.1 (September 2026). These terms describe governing AI that acts, the subject of <a href="/ai-agent-governance">AI agent governance</a>.</p>' + _anchored_table(GLOSSARY_AGENTIC) +
   '<h2 id="cite">Citing a term</h2>'
   '<p>Every entry has a stable anchor: link to /glossary#agent-identity, /glossary#execution-boundary, and so on. The full set is also published as machine-readable structured data on this page (DefinedTermSet), and the cite block below covers the page as a whole.</p>',
 "extra_schema":[{"@type":"DefinedTermSet","@id":DOMAIN+"/glossary#set","name":"Digital Information Governance Glossary",
    "hasDefinedTerm":[{"@type":"DefinedTerm","@id":DOMAIN+"/glossary#"+_slug(t),"name":t,"description":d,
                       "inDefinedTermSet":{"@id":DOMAIN+"/glossary#set"}} for t,d in GLOSSARY_ALL]}],
 "related":[("/ai-agent-governance","AI agent governance"),("/what-is-digital-information-governance","Definition"),("/framework","Framework"),("/faq","FAQ")],
})

# ============ AI Regulation Tracker ============
TRACKER_ROWS = [
 {"regime":"EU AI Act (Regulation 2024/1689)","scope":"All providers and deployers placing AI on the EU market, tiered by risk",
  "status":"In force since August 2024 with staged application. Transparency duties applied in August 2026. The 2026 Digital Omnibus deferred the main high-risk obligations to December 2, 2027 (Annex III stand-alone systems) and August 2, 2028 (AI embedded in Annex I regulated products).",
  "reviewed":TODAY_REVIEW},
 {"regime":"Texas TRAIGA (HB 149)","scope":"AI systems in Texas; Attorney-General enforced",
  "status":"Effective January 1, 2026. Penalties up to 200,000 dollars per uncurable violation and 40,000 dollars per day for continuing violations.",
  "reviewed":TODAY_REVIEW},
 {"regime":"Colorado AI Act (SB 24-205)","scope":"Developers and deployers of high-risk AI making consequential decisions",
  "status":"Enacted 2024; high-risk obligations take effect in 2026, with the exact date amended by the legislature. Confirm the current date before relying on it.",
  "reviewed":TODAY_REVIEW},
 {"regime":"NYC Local Law 144","scope":"Automated employment decision tools used for NYC roles",
  "status":"In effect. Requires annual independent bias audits and candidate notice.",
  "reviewed":TODAY_REVIEW},
 {"regime":"ISO/IEC 42001:2023","scope":"Certifiable AI management system standard (voluntary)",
  "status":"Published December 2023. Certification audits are running; increasingly referenced in procurement.",
  "reviewed":TODAY_REVIEW},
 {"regime":"NIST AI RMF 1.0","scope":"Voluntary US risk-management framework",
  "status":"Published January 2023 (Govern, Map, Measure, Manage). The common vocabulary for US programs; a generative-AI profile followed.",
  "reviewed":TODAY_REVIEW},
]

REFS_TRACKER = [
 ("EU AI Act, Regulation (EU) 2024/1689, Official Journal of the European Union.",
  "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
 ("EU Artificial Intelligence Act tracker (application timeline and the 2026 Digital Omnibus changes).",
  "https://artificialintelligenceact.eu/"),
 ("Texas Responsible Artificial Intelligence Governance Act (TRAIGA), HB 149, 89R.",
  "https://capitol.texas.gov/tlodocs/89R/billtext/pdf/HB00149F.pdf"),
 ("Colorado SB 24-205, Consumer Protections for Artificial Intelligence.",
  "https://leg.colorado.gov/bills/sb24-205"),
 ("NYC Department of Consumer and Worker Protection, Automated Employment Decision Tools (Local Law 144).",
  "https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page"),
 ("ISO/IEC 42001:2023, AI management system standard.",
  "https://www.iso.org/standard/81230.html"),
 ("NIST AI Risk Management Framework (AI RMF 1.0).",
  "https://www.nist.gov/itl/ai-risk-management-framework"),
]

def _tracker_table():
    out = ['<table class="deftable"><tr><th class="term">Regime</th><th>Who it reaches</th><th>Status</th><th>Last reviewed</th></tr>']
    for r in TRACKER_ROWS:
        out.append('<tr id="%s"><td class="term">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %
                   (_slug(r["regime"].split("(")[0]), r["regime"], r["scope"], r["status"], r["reviewed"]))
    out.append('</table>')
    return "".join(out)

PAGES7.append({
 "path":"ai-regulation-tracker","nav":"regulations",
 "title":"AI Regulation Tracker: Current Status by Regime (DIG®)",
 "description":"A dated, source-linked status table for the AI rules that govern AI-influenced decisions and AI agents: EU AI Act (with the 2026 Omnibus deferrals), TRAIGA, Colorado, NYC Local Law 144, ISO/IEC 42001, NIST AI RMF.",
 "eyebrow":"Living reference","h1":"AI Regulation Tracker","byline":True,
 "breadcrumb":[("Home","/"),("Regulations","/regulations"),("Tracker","")],
 "toc":[("method","How this table works"),("table","Status by regime"),("watchlist","Watchlist"),("data","Machine-readable")],
 "infobox":{"title":"AI Regulation Tracker","sub":"As of "+TODAY_REVIEW,"rows":[
    ("Regimes tracked",str(len(TRACKER_ROWS))),
    ("Cadence","Reviewed monthly; each row carries its own date"),
    ("Rule","No row without a primary source"),
    ("Data",'<a href="/data/regulation-tracker.json">regulation-tracker.json</a>'),
    ("Deep dives",'<a href="/regulations">Per-regime pages</a>')]},
 "body":
   defbox("The AI Regulation Tracker is a dated status table for the rules that govern AI-influenced decisions and AI agents. Every row names its scope, its current status, and the date it was last reviewed against primary sources.", label="AI Regulation Tracker") +
   '<h2 id="method">How this table works</h2>'
   '<p>Regulatory summaries rot quietly: a page written in spring states a deadline that a summer amendment moved. This tracker treats status as data. Each row is reviewed against the primary source and stamped with its review date, and rows are corrected the way a living standard is corrected: visibly, with the change noted in the site <a href="/changelog">changelog</a>. A row is only as current as its date says it is.</p>'
   '<h2 id="table">Status by regime</h2>' + _tracker_table() +
   note('<strong>The deferral is not a reprieve.</strong> The Omnibus moved the EU AI Act\'s main high-risk deadlines to 2027 and 2028, but agents are being deployed now, and the logging and oversight the Act expects cannot be reconstructed later. The record either exists when the question comes, or it does not.') +
   '<h2 id="watchlist">Watchlist</h2>'
   '<p>On the watchlist, pending verification against primary sources before they get a row: California frontier-model legislation, Brazil\'s Bill 2338, India\'s AI liability framework, and state bills in progress. A regime moves from the watchlist to the table only when its status can be stated from a primary source with a date.</p>'
   '<h2 id="data">Machine-readable</h2>'
   '<p>The table is published as JSON at <a href="/data/regulation-tracker.json">/data/regulation-tracker.json</a>, and this page carries speakable structured data like every page on this site. Cite the page, or consume the file.</p>',
 "faqs":[
   ("When do the EU AI Act high-risk obligations apply?","<p>Under the 2026 Digital Omnibus, the main high-risk obligations were deferred to December 2, 2027 for stand-alone Annex III systems and August 2, 2028 for AI embedded in Annex I regulated products. Transparency duties applied in August 2026.</p>"),
   ("Which US AI laws are already in effect?","<p>Texas's TRAIGA took effect January 1, 2026, and NYC Local Law 144 has required bias audits for automated employment decision tools since 2023. Colorado's SB 24-205 obligations take effect in 2026 with an amended date.</p>"),
   ("How often is this tracker updated?","<p>Rows are reviewed monthly against primary sources, and each row carries the date it was last reviewed. Changes are noted in the site changelog.</p>"),
 ],
 "refs":REFS_TRACKER,
 "related":[("/regulations","Per-regime deep dives"),("/ai-agent-governance","AI agent governance"),("/framework","The framework"),("/changelog","Changelog")],
})

# ============ AI Agent Incident Register ============
PAGES7.append({
 "path":"ai-agent-incident-register","nav":None,
 "title":"AI Agent Incident Register (DIG®)",
 "description":"A dated register of documented incidents in which an AI agent acted, each classified by which of the five authorization questions failed and which DIG® pillar it maps to.",
 "eyebrow":"Living reference","h1":"AI Agent Incident Register","byline":True,
 "breadcrumb":[("Home","/"),("Incident register","")],
 "toc":[("why","Why an action-layer register"),("criteria","Inclusion criteria"),("entries","Entries"),("submit","Submitting an incident")],
 "infobox":{"title":"Incident Register","sub":"Action-layer incidents","rows":[
    ("Unit","One incident, one entry, one classification"),
    ("Classified by","The five questions + the DIG® pillar that failed"),
    ("Entries","1 (register opened September 2026)"),
    ("Cadence","Reviewed monthly"),
    ("Related",'<a href="/ai-agent-governance">AI agent governance</a>')]},
 "body":
   defbox("The AI Agent Incident Register documents incidents in which an AI agent took actions, classifying each by which of the five authorization questions failed: what the agent was authorized to see, decide, and do, who approved it, and whether the actions could be reconstructed.", label="AI Agent Incident Register") +
   '<h2 id="why">Why an action-layer register</h2>'
   '<p>Existing incident databases catalogue AI harms broadly, and most entries concern what a model said or predicted. As AI systems gain keyboards, terminals, and browsers, a different class of incident appears: an agent acted, and the organization could not answer the authorization questions afterward. This register documents that class specifically, because the lessons are different. A biased answer teaches you about training data. An unauthorized action teaches you about identity, scope, approval, and reconstruction.</p>'
   '<h2 id="criteria">Inclusion criteria</h2>'
   '<p>An entry qualifies when three things hold. An AI system took actions, not merely generated content. The incident is documented, either publicly reported with a source or disclosed first-party by the affected organization. And enough detail exists to classify it against the five questions. Entries state what is known, what is inferred, and what could not be established; an entry that overstates its own reconstruction would fail the discipline it documents.</p>'
   '<h2 id="entries">Entries</h2>'
   '<h3 id="air-2026-001">AIR-2026-001: Self-inflicted analytics pollution by an unmanaged browsing agent (first-party)</h3>' +
   deftable([
     ("Organization","EWR Digital (disclosed first-party by the register\'s maintainers)"),
     ("Window","June 8 to August 20, 2026 (ten weeks)"),
     ("What happened","A headless-browser audit agent, running under default settings, loaded the organization\'s own production website repeatedly. No one had decided the agent should be visible to analytics; no one had decided anything. It generated 59% of all recorded sessions in the final 30-day window, silently distorting channel, engagement, and journey reporting."),
     ("Authorized to see / do","No authorization decision existed in either direction. The agent was doing legitimate audit work; its visibility to production analytics was an unexamined default. (Pillar: Representation Integrity at the action layer.)"),
     ("Who approved","No grant, no record. The tooling defaulted to visible. (Pillar: Decision Traceability.)"),
     ("Reconstruction","Required weeks of forensic analysis of analytics fingerprints. It attributed the traffic to the organization\'s own automation with high confidence but could not name the exact host with certainty. (Pillar: Audit Readiness; maturity Level 1 on the action layer.)"),
     ("Consequence","The analytics window is permanently polluted; the platform cannot delete it retroactively. Remediation: exclusion segments, analytics-blocking defaults in all agent tooling, marker parameters for deliberate test loads."),
     ("Lesson","The domain was harmless. The failure class, an agent acting with no authorization record and no rehearsed reconstruction path, is the one that matters when the domain is lending, operations, or safety."),
   ], head=("Field","AIR-2026-001")) +
   note('This register opens with our own incident, deliberately. A register that only catalogues other people\'s failures invites doubt about what its maintainers are not disclosing.') +
   '<h2 id="submit">Submitting an incident</h2>'
   '<p>Documented incidents that meet the criteria are added on monthly review. Public reports with primary sources qualify; first-party disclosures are welcome and are marked as such. Entries never name an organization that has not either published the incident or consented to be named.</p>',
 "faqs":[
   ("What counts as an AI agent incident?","<p>An incident in which an AI system took actions (not merely generated content), documented publicly or disclosed first-party, with enough detail to classify against the five authorization questions.</p>"),
   ("How is this different from the AI Incident Database?","<p>General AI incident databases catalogue harms of all kinds, mostly at the model and output layer. This register documents the action layer specifically: incidents where the governance failure concerns authorization, identity, scope, approval, or reconstruction of agent actions.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/ai-agent-governance","AI agent governance"),("/dig-maturity-model","Maturity model"),("/ai-regulation-tracker","Regulation tracker")],
})

# ============ Frontier model access tiers (compare) ============
REFS_TIERS = [
 ("OpenAI, Path to Astra: critical capabilities and frontier safeguards, September 1, 2026.",
  "https://openai.com/index/path-to-astra/"),
 ("Anthropic, Claude Fable 5 and Claude Mythos 5, 2026.",
  "https://www.anthropic.com/news/claude-fable-5-mythos-5"),
 ("Anthropic, Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders, 2026.",
  "https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders"),
]

PAGES7.append({
 "path":"compare/frontier-model-access-tiers","nav":None,
 "title":"Frontier Model Access Tiers Compared (DIG®)",
 "description":"How frontier AI vendors tier access to their most capable models: OpenAI's Astra Critical designation and gated defensive access, Anthropic's generally available and trusted-access split, and what capability tiering means for governance and procurement.",
 "eyebrow":"Comparison","h1":"Frontier Model Access Tiers",
 "byline":True,
 "breadcrumb":[("Home","/"),("Compare","/compare"),("Access tiers","")],
 "toc":[("why","Why tiers exist"),("table","The tiers, by vendor"),("governance","What tiering means for governance")],
 "infobox":{"title":"Access tiers","sub":"As of "+TODAY_REVIEW,"rows":[
    ("Pattern","One frontier model, multiple access levels"),
    ("Vendors tracked","OpenAI, Anthropic (more as verifiable)"),
    ("Cadence","Reviewed monthly"),
    ("Governance question","Which authority did procurement grant?")]},
 "body":
   defbox("Frontier AI vendors now ship one model at multiple access levels: a generally available tier with capability restrictions, and gated tiers granting vetted organizations capabilities withheld from the public. Which tier an organization holds is a governance fact, because it determines what its agents can actually do.", label="Frontier model access tiers") +
   '<p class="lead" id="why">Capability tiering became explicit in 2026. When a model\'s abilities cross a vendor\'s own danger thresholds, the vendor no longer chooses between shipping and not shipping; it ships different authorities to different users. That decision used to be internal to labs. Now it is a procurement variable, and a governance record has to capture it.</p>'
   '<h2 id="table">The tiers, by vendor</h2>' +
   deftable([
     ("OpenAI: Astra","First model designated Critical for cybersecurity under OpenAI\'s Preparedness Framework (September 2026). The broadly available tier refuses advanced cyber requests, including proof-of-concept exploits. Advanced cybersecurity capability is limited to an approved group of testers, expanding to defensive users through the Daybreak Blue program.<sup><a href=\"#r1\">[1]</a></sup>"),
     ("Anthropic: Claude Fable 5 / Claude Mythos 5","One underlying frontier model, two products. Fable 5 is generally available with additional safety measures for dual-use capabilities. Mythos 5 is available only to approved organizations under trusted access, with cybersecurity capability extended to defenders through dedicated programs.<sup><a href=\"#r2\">[2]</a></sup><sup><a href=\"#r3\">[3]</a></sup>"),
     ("Other vendors","Added when tiering is announced and verifiable against primary sources. A vendor without published tiering is not listed as untiered; it is listed as unverified."),
   ], head=("Vendor and model","Tiering, as published")) +
   '<h2 id="governance">What tiering means for governance</h2>'
   '<p>Tiering moves a safety decision from the lab into your delegation records. Two organizations running "the same model" may hold different authorities, and an agent built on a gated tier can do things the generally available tier refuses. So the five questions of <a href="/ai-agent-governance">AI agent governance</a> begin one step earlier than most programs expect: before asking what your agent was authorized to do, record which tier of capability your organization was granted, by whom, under what program, and with what conditions attached. That grant is part of the provenance of every action the agent takes.</p>',
 "faqs":[
   ("What is a frontier model access tier?","<p>A vendor-defined level of model capability and access: typically a generally available tier with restrictions, and gated tiers granting vetted organizations capabilities withheld from general availability.</p>"),
   ("Why does the access tier matter for governance?","<p>Because it determines what an organization\'s agents can actually do. The tier grant belongs in the governance record the same way delegated authority does: which tier, granted by whom, under what program, with what conditions.</p>"),
 ],
 "refs":REFS_TIERS,
 "related":[("/ai-agent-governance","AI agent governance"),("/compare","All comparisons"),("/ai-regulation-tracker","Regulation tracker")],
})
