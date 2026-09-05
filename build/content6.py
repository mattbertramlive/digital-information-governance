# -*- coding: utf-8 -*-
"""content6.py - Tier 8: the agentic extension (framework v1.1, September 2026).
Governing AI that acts (keyboard, mouse, terminal, browser), not only AI that answers.
Spec: audits/2026-09-05-agentic-extension/SPEC.md"""
from templates import defbox, note, deftable

PAGES6 = []

REFS_AGENT = [
    ("NIST AI Risk Management Framework (AI RMF 1.0): Govern, Map, Measure, Manage. National Institute of Standards and Technology, 2023.",
     "https://www.nist.gov/itl/ai-risk-management-framework"),
    ("Deloitte, State of AI in the Enterprise, 2026: roughly 21% of organizations report a mature governance model for agentic AI.",
     "https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html"),
    ("EU AI Act, Regulation (EU) 2024/1689: automatic event logging supporting traceability (Article 12) and human oversight (Article 14) for high-risk systems.",
     "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
    ("OpenAI, Path to Astra: critical capabilities and frontier safeguards, September 1, 2026. Astra is the first OpenAI model designated Critical for cybersecurity under its Preparedness Framework; the post names containing unauthorized, misaligned model actions as a core safeguard goal.",
     "https://openai.com/index/path-to-astra/"),
    ("Anthropic, Claude Fable 5 and Claude Mythos 5, 2026: one frontier model offered as a generally available product with additional safety measures and as a separate trusted-access product for approved organizations.",
     "https://www.anthropic.com/news/claude-fable-5-mythos-5"),
    ("EU Digital Omnibus, in force July 2026: deferral of the AI Act's main high-risk obligations to December 2, 2027 (Annex III stand-alone systems) and August 2, 2028 (Annex I embedded systems).",
     "https://artificialintelligenceact.eu/"),
]

PAGES6.append({
 "path":"ai-agent-governance","nav":None,
 "title":"AI Agent Governance: Governing the Digital Employee (DIG®)",
 "description":"AI agents now operate keyboards, terminals, and browsers. AI agent governance extends Digital Information Governance (DIG®) from what an AI said to what an AI did: authorized access, delegated decisions, execution boundaries, and reconstructable actions.",
 "eyebrow":"Discipline","h1":"AI Agent Governance","byline":True,
 "breadcrumb":[("Home","/"),("AI agent governance","")],
 "toc":[("shift","From answers to actions"),("questions","The five questions"),
        ("frontier","The 2026 frontier context"),("maturity","Maturity at the action layer"),
        ("example","A worked example"),("start","Where to start")],
 "infobox":{"title":"AI agent governance","sub":"The action layer of DIG®","rows":[
    ("Governs","What an AI was authorized to see, decide, and do"),
    ("Extends","The four DIG® pillars, unchanged"),
    ("Why now","Frontier models act through keyboards, terminals, and browsers"),
    ("Maturity","Same five levels, applied to actions"),
    ("Framework","DIG® v1.1")]},
 "body":
   defbox("AI agent governance is the discipline of keeping AI-executed actions defensible and auditable: what an agent was authorized to see, what it was authorized to decide, what it was authorized to do, who approved that authority, and whether the organization can reconstruct exactly what happened afterward. It applies the four DIG® pillars at the action layer.", label="AI agent governance") +
   '<p class="lead" id="shift">For the first years of enterprise AI, governance meant governing answers. What did the model say, was it accurate, was it biased, did it leak. That era is ending. Frontier models now operate a keyboard, a mouse, a terminal, and a browser. They are becoming digital employees, and the vendors themselves say so: OpenAI\'s launch material for its newest model describes safeguards for containing "unauthorized, misaligned actions," not just wrong answers.<sup><a href="#r4">[4]</a></sup> Once an AI acts on enterprise information rather than merely reading it, the governance question changes shape.</p>'
   '<p>An employee\'s actions are governed by identity, permission, and audit. A digital employee deserves nothing less. Today most get nothing at all: agents borrowing human credentials, acting at machine speed, leaving logs built for people. Roughly one in five organizations reports a mature governance model for agentic AI.<sup><a href="#r2">[2]</a></sup></p>'
   '<h2 id="questions">The five questions</h2>'
   '<p>When an AI can act, a defensible posture answers five questions, and they map onto the four DIG® pillars without adding a fifth. The pillars hold; the record simply has to run one step further, from the decision to the act.</p>' +
   deftable([
     ("What was it authorized to see?","Information Provenance. Access scope is provenance in reverse: a record of what information the agent could reach, not only where a decision\'s inputs came from."),
     ("What was it authorized to decide?","Decision Traceability. Which decisions are delegated to agents, at what thresholds, and on what basis."),
     ("Who approved that authority?","Decision Traceability. Delegation is itself a decision; the grant, the grantor, and the revocation path belong in the record."),
     ("What was it authorized to do?","Representation Integrity. An agent that sends, posts, publishes, configures, or transacts is representing the company by action. Execution boundaries are representation controls."),
     ("Can you reconstruct what happened?","Audit Readiness. Action-level trails: tool calls, page loads, commands, and approvals, replayable end to end."),
   ], head=("Question","Pillar it belongs to")) +
   '<h2 id="frontier">The 2026 frontier context</h2>'
   '<p>Two developments in 2026 made the action layer impossible to defer. First, OpenAI designated its Astra model Critical for cybersecurity under its Preparedness Framework, the first model at that level: in OpenAI\'s words, with the right tools and access it can find previously unknown security flaws and develop exploits "without a person guiding each step," and access to its most advanced capabilities is gated to approved defensive users.<sup><a href="#r4">[4]</a></sup> Second, Anthropic split one frontier model into two products, a generally available version with additional safety measures and a trusted-access version for approved organizations.<sup><a href="#r5">[5]</a></sup> Capability tiering by the vendor is now a fact of procurement, which means the enterprise question is no longer only which model, but which authority.</p>'
   '<p>Regulation is moving on its own clock. The EU AI Act already makes event logging and human oversight legal duties for high-risk systems,<sup><a href="#r3">[3]</a></sup> and the 2026 Digital Omnibus moved the main high-risk deadlines to late 2027 and 2028.<sup><a href="#r6">[6]</a></sup> A deferred deadline is not a deferred risk: the agents are being deployed now, and the record either exists when the question comes or it does not.</p>'
   '<h2 id="maturity">The maturity model at the action layer</h2>'
   '<p>The <a href="/dig-maturity-model">DIG Maturity Model</a> keeps its five levels. At the action layer, each level has a concrete marker.</p>' +
   deftable([
     ("Level 1, Ad hoc","Agents run under human credentials. No inventory of what agents exist or what they touch. Agent actions are indistinguishable from employee actions in every log."),
     ("Level 2, Aware","Agent activity is known to exist and partially logged. Scopes are informal and undocumented."),
     ("Level 3, Defined","Agents hold their own identities with scoped access. Delegated-decision thresholds are written. Actions are logged and attributable on request."),
     ("Level 4, Managed","Execution boundaries are tested: what the agent cannot do is verified, not assumed. Approvals are recorded at grant time. Agent representation is monitored."),
     ("Level 5, Defensible by default","Authorization is captured at execution time. Every action is replayable. Containment (pause, revoke, roll back) is a rehearsed control, not a hope."),
   ], head=("Level","Action-layer marker")) +
   '<h2 id="example">A worked example, from our own analytics</h2>'
   '<p>This failure class is easy to picture because we measured it on ourselves. In mid-2026, a browsing agent in our own tooling loaded pages of one of our sites for ten weeks under default settings. Nobody had decided it should be visible to analytics; nobody had decided anything. It ended up generating 59% of the site\'s recorded sessions, and reconstructing what had happened took weeks of forensic work that still could not name the exact machine with certainty. The domain was harmless, web analytics. The governance failure, an agent acting with no authorization record and no reconstructable trail, is exactly the one that matters when the domain is lending, operations, or safety.</p>' +
   note('<strong>The one-line version:</strong> DIG governed what the AI said. Now it governs what the AI does.') +
   '<h2 id="start">Where to start</h2>'
   '<p>Three moves create the floor. First, inventory: list every agent, tool, and automation that can act on enterprise systems, and what credentials each one holds. Second, delegation: write down which decisions and actions are delegated to agents, at what thresholds, and who approved each grant. Third, reconstruction: pick one recent agent action and try to replay it end to end from your logs. Where the replay breaks is where your governance actually stands, and the <a href="/dig-maturity-self-assessment">self-assessment</a> will place the result on the maturity scale.</p>',
 "faqs":[
   ("What is AI agent governance?","<p>The discipline of keeping AI-executed actions defensible and auditable: what an agent was authorized to see, decide, and do, who approved that authority, and whether the action can be reconstructed afterward. It applies the four DIG® pillars at the action layer.</p>"),
   ("Does agentic AI need a new governance framework?","<p>No. The four DIG® pillars (Information Provenance, Decision Traceability, Representation Integrity, Audit Readiness) already decompose the problem. What changes is where the record stops: not at the decision, but at the act.</p>"),
   ("What changed with the 2026 frontier models?","<p>Frontier models began operating real interfaces (terminals, browsers) and vendors began tiering access to their most capable versions: OpenAI gates Astra\'s advanced cybersecurity capability to approved defensive users, and Anthropic offers its frontier model as both a generally available product and a trusted-access product. Enterprise governance now has to record which authority an agent held, not just which model it used.</p>"),
 ],
 "refs":REFS_AGENT,
 "related":[("/ai-decision-governance","AI decision governance"),("/framework","The framework"),
            ("/dig-maturity-model","Maturity model"),("/regulations/eu-ai-act","EU AI Act"),
            ("/dig-maturity-self-assessment","Free self-assessment")],
})
