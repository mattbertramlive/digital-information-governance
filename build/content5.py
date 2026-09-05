# -*- coding: utf-8 -*-
"""content5.py - Tier 7: interactive tools + content-breadth-blitz pages.
Appended after content4. The self-assessment tool is fully client-side (no backend, no data leaves the browser)."""
import os
from templates import defbox, note, deftable, DOMAIN
from content import REFS_CORE

PAGES5 = []

# Interactive DIG Maturity Scorer front-end (HTML/CSS/JS), kept in its own file so the large blob
# (with literal % and mixed quotes) is embedded verbatim and never %-formatted. The page calls the
# SSRF-hardened serverless function at /api/dig-score (see build/dig-score.js).
_SCORER_BODY = open(os.path.join(os.path.dirname(__file__), "dig-scorer-body.html"), encoding="utf-8").read()

# ============ Free DIG Maturity self-assessment tool (client-side, lead-gen) ============
_Q = [
 "Can you trace where the information behind an AI-influenced decision came from?",
 "Do you know whether that information was current and authoritative when the decision was made?",
 "Is there a record of who reviewed and approved each AI-influenced decision?",
 "Can you show the basis for a decision: which recommendation, and on whose authority?",
 "Do you monitor how AI systems and search engines describe your organization?",
 "Could you correct an inaccurate AI-generated statement about your company quickly?",
 "Could you produce the full decision trail for any AI-influenced decision on demand?",
 "Are your AI decision controls tested, rather than assumed to work?",
]
_OPTS = [("0","Not at all"),("1","Somewhat"),("2","Mostly"),("3","Fully")]
def _quiz_html():
    out=['<form class="quiz" id="digQuiz">']
    for i,q in enumerate(_Q,1):
        out.append('<div class="q"><p>%d. %s</p>'%(i,q))
        for val,lab in _OPTS:
            out.append('<label><input type="radio" name="q%d" value="%s"> %s</label>'%(i,val,lab))
        out.append('</div>')
    out.append('</form>')
    return "".join(out)

_QUIZ_STYLE = """<style>
.quiz .q{margin:0 0 1rem;padding:0 0 .8rem;border-bottom:1px solid #e5e7eb}
.quiz .q p{font-weight:700;margin:0 0 .4rem}
.quiz label{display:block;padding:.25rem 0;cursor:pointer}
.quiz input{margin-right:.5rem}
#digScoreBtn{background:#0a5dbd;color:#fff;border:0;padding:.75rem 1.5rem;border-radius:6px;font-size:1rem;font-weight:700;cursor:pointer;margin:.5rem 0 0}
#digResult{display:none;margin-top:1.5rem;padding:1.25rem 1.5rem;border:2px solid #114b73;border-radius:8px;background:#f4f8fc}
#digResult h3{margin:.15rem 0 .5rem;color:#114b73}
#digResult .sub{font-size:.82rem;color:#555;text-transform:uppercase;letter-spacing:.04em}
.lvlbar{height:8px;background:#e5e7eb;border-radius:4px;margin:.4rem 0 .8rem;overflow:hidden}
.lvlfill{height:100%;background:#0a5dbd}
</style>"""

_QUIZ_SCRIPT = """<script>
(function(){
  var btn=document.getElementById('digScoreBtn');
  var out=document.getElementById('digResult');
  var levels=[
   {min:0,max:5,name:'Level 1: Ad hoc',desc:'Your AI-influenced decisions leave little or no usable trail. Few could be reconstructed or defended if challenged today.',next:'Start with Decision Traceability: capture what was decided, by what, and on whose authority, for your highest-stakes AI-influenced decisions.'},
   {min:6,max:11,name:'Level 2: Aware',desc:'You have some policies and logging, but coverage is uneven. Whether a decision is defensible still depends on the individual who made it.',next:'Standardize provenance and decision trails across your high-stakes decisions, so defensibility does not depend on who made the call.'},
   {min:12,max:17,name:'Level 3: Defined',desc:'The four pillars are becoming standard practice and you can reconstruct most decisions on request. This is the first level a regulator would call governed.',next:'Move from reconstructing decisions on request to being audit-ready on demand: test your controls and measure coverage.'},
   {min:18,max:21,name:'Level 4: Managed',desc:'Your controls are tested and you are audit-ready on demand. You monitor how AI systems represent you.',next:'Push toward capturing decision integrity at the moment each decision is made, so defensibility is automatic rather than assembled.'},
   {min:22,max:24,name:'Level 5: Defensible by default',desc:'Defensibility is your resting state. Decision integrity is captured as decisions are made, and audit is continuous.',next:'Maintain it. Use representation-integrity monitoring and continuous audit to hold this level as your AI use expands.'}
  ];
  btn.addEventListener('click',function(){
    var f=document.getElementById('digQuiz'),total=0,answered=0,i,sel;
    for(i=1;i<=8;i++){sel=f.querySelector('input[name=q'+i+']:checked');if(sel){total+=parseInt(sel.value,10);answered++;}}
    if(answered<8){out.style.display='block';out.innerHTML='<p><strong>Please answer all eight questions.</strong></p>';out.scrollIntoView({behavior:'smooth'});return;}
    var lvl=levels[0],k;for(k=0;k<levels.length;k++){if(total>=levels[k].min&&total<=levels[k].max){lvl=levels[k];break;}}
    var pct=Math.round(total/24*100);
    out.style.display='block';
    out.innerHTML='<div class="sub">Your score: '+total+' of 24</div><h3>'+lvl.name+'</h3><div class="lvlbar"><div class="lvlfill" style="width:'+pct+'%"></div></div><p>'+lvl.desc+'</p><p><strong>Your next step:</strong> '+lvl.next+'</p><p>Read the full <a href="/dig-maturity-model">DIG Maturity Model</a>, or get a structured <a href="https://modalpoint.com/digital-information-governance/">governance readiness assessment</a> from ModalPoint.</p>';
    out.scrollIntoView({behavior:'smooth'});
  });
})();
</script>"""

PAGES5.append({
 "path":"dig-maturity-self-assessment","nav":None,
 "title":"DIG Maturity Self-Assessment: Score Your AI Decision Governance",
 "description":"A free self-assessment that scores how defensible your AI-influenced decisions are, on the five-level DIG Maturity Model. Eight questions, instant result, and nothing you enter leaves your browser.",
 "eyebrow":"Free tool","h1":"DIG Maturity Self-Assessment","byline":True,
 "breadcrumb":[("Home","/"),("Maturity model","/dig-maturity-model"),("Self-assessment","")],
 "infobox":{"title":"Self-assessment","sub":"Free, no signup","rows":[
    ("Questions","8"),("Time","About 2 minutes"),
    ("Scores","DIG Maturity Level 1 to 5"),("Privacy","Runs in your browser")]},
 "body":
   '<p class="lead">Answer eight questions to see how defensible your AI-influenced decisions are today, scored on the five-level <a href="/dig-maturity-model">DIG Maturity Model</a>. It takes about two minutes, and nothing you enter leaves your browser.</p>'
   + _QUIZ_STYLE + _quiz_html()
   + '<button id="digScoreBtn" type="button">See my DIG maturity level</button><div id="digResult"></div>'
   + _QUIZ_SCRIPT,
 "faqs":[
   ("Is this assessment free and private?","<p>Yes. It runs entirely in your browser, no answers are sent anywhere, and there is nothing to sign up for.</p>"),
   ("What does my level mean?","<p>It places you on the five-level DIG Maturity Model, from Level 1 (ad hoc, no decision trail) to Level 5 (defensible by default). Each result comes with a recommended next step.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/dig-maturity-scorer","Score your live site"),("/dig-maturity-model","The maturity model"),("/governance-readiness-assessment","Readiness assessment")],
})

# ============ DIG Maturity Scorer (live public-footprint read, backed by /api/dig-score) ============
PAGES5.append({
 "path":"dig-maturity-scorer","nav":None,
 "title":"DIG Maturity Scorer: Read Your Public AI Governance Signals",
 "description":"A free scorer that reads your own public pages for AI decision governance signals, maps them to the four DIG pillars, and places you on the five-level DIG Maturity Model. Indicative public-signal read, not an audit. No login, nothing stored.",
 "eyebrow":"Free tool","h1":"DIG Maturity Scorer","byline":True,
 "breadcrumb":[("Home","/"),("Maturity model","/dig-maturity-model"),("Scorer","")],
 "infobox":{"title":"DIG Maturity Scorer","sub":"Reads public signals","rows":[
    ("Input","Your company domain"),("Reads","Your public pages only"),
    ("Scores","DIG Level 1 to 5, four pillars"),("Privacy","No login, nothing stored")]},
 "body":_SCORER_BODY,
 "faqs":[
   ("Does the scorer store my data or need a login?","<p>No. It reads only public pages on the domain you enter, the same ones any visitor or search engine can reach, and the scan is not stored. There is no login. Sending your email for the full breakdown is optional and only happens if you ask for it.</p>"),
   ("How is this different from the self-assessment?","<p>The <a href=\"/dig-maturity-self-assessment\">self-assessment</a> scores what you know about your own controls from eight questions. The scorer reads what the outside world, including AI systems, can actually see on your public site. A gap between the two is itself a Representation Integrity finding.</p>"),
   ("Is a low score proof we lack controls?","<p>No. The scorer reads public signals only. A missing public page is not proof the control behind it is absent, only that it is not visible from outside. For a real read, book the ModalPoint readiness assessment.</p>"),
 ],
 "refs":REFS_CORE,
 "related":[("/dig-maturity-self-assessment","Self-assessment"),("/dig-maturity-model","Maturity model"),("/framework","The framework")],
})

# ============ Content-breadth blitz: more regulations + comparison + implementation ============

PAGES5.append({
 "path":"regulations/colorado-ai-act","nav":"regulations",
 "title":"The Colorado AI Act (SB 24-205) & Digital Information Governance (DIG®)",
 "description":"How the Colorado AI Act (SB 24-205), which requires reasonable care against algorithmic discrimination in high-risk AI decisions, maps to Digital Information Governance (DIG®).",
 "eyebrow":"Regulatory context","h1":"The Colorado AI Act","byline":True,
 "breadcrumb":[("Home","/"),("Regulations","/regulations"),("Colorado AI Act","")],
 "infobox":{"title":"Colorado AI Act","sub":"SB 24-205","rows":[
    ("Enacted","2024"),("Takes effect","2026 (date amended by the legislature)"),
    ("Targets","Algorithmic discrimination in consequential decisions"),("Enforced by","Colorado Attorney General")]},
 "body":
   defbox("The Colorado AI Act (SB 24-205) requires developers and deployers of high-risk AI systems to use reasonable care to protect consumers from algorithmic discrimination in consequential decisions.", label="Colorado AI Act (SB 24-205)") +
   '<p class="lead">Colorado enacted SB 24-205 in 2024, one of the first comprehensive US state AI laws. Its high-risk-AI obligations take effect in 2026, with the exact date amended by the legislature. It is enforced by the Colorado Attorney General.</p>'
   '<h2>What it covers</h2>'
   '<p>The Act applies to AI used in consequential decisions: employment, lending, housing, education, healthcare, insurance, and legal services. Developers and deployers owe a duty of reasonable care to avoid algorithmic discrimination, and deployers must run risk management and impact assessments, notify consumers, and document their controls.</p>'
   '<h2>How DIG maps</h2>'
   '<p>Reasonable care is provable only if it is documented. <a href="/pillars/information-provenance">Provenance</a> and <a href="/pillars/decision-traceability">traceability</a> supply the record of how a high-risk decision was made; <a href="/pillars/audit-readiness">audit readiness</a> produces the impact assessment and decision trail the Act expects. DIG is the decision-level discipline behind a Colorado compliance posture. It pairs with Texas\'s <a href="/regulations/traiga">TRAIGA</a> as the US state law moves first.</p>',
 "faqs":[
   ("What does the Colorado AI Act require?","<p>Developers and deployers of high-risk AI must use reasonable care to avoid algorithmic discrimination in consequential decisions, run risk management and impact assessments, notify consumers, and document their controls. It is enforced by the state Attorney General.</p>"),
   ("When does the Colorado AI Act take effect?","<p>It was enacted in 2024 and its high-risk-AI obligations take effect in 2026; the legislature amended the effective date, so confirm the current date before relying on it.</p>")],
 "refs":REFS_CORE,
 "related":[("/regulations","All regulations"),("/regulations/traiga","TRAIGA"),("/ai-governance-statistics","Statistics")],
})

PAGES5.append({
 "path":"regulations/nyc-local-law-144","nav":"regulations",
 "title":"NYC Local Law 144 (AI Hiring Bias Audits) & DIG®",
 "description":"How New York City's Local Law 144, which requires bias audits of automated employment decision tools, maps to Digital Information Governance (DIG®).",
 "eyebrow":"Regulatory context","h1":"NYC Local Law 144","byline":True,
 "breadcrumb":[("Home","/"),("Regulations","/regulations"),("NYC Local Law 144","")],
 "infobox":{"title":"NYC Local Law 144","sub":"AEDT bias audits","rows":[
    ("Applies to","Automated employment decision tools"),("Enforced from","5 July 2023"),
    ("Requires","Independent bias audit + notice"),("Decision","Hiring and promotion")]},
 "body":
   defbox("New York City's Local Law 144 requires employers using automated employment decision tools (AEDTs) to conduct an independent bias audit, publish a summary of the results, and notify candidates.", label="NYC Local Law 144") +
   '<p class="lead">Local Law 144 is one of the first US laws to put a hard requirement on an AI-influenced decision. Since enforcement began on 5 July 2023, employers using automated tools to screen or rank candidates in New York City must have an independent bias audit, publish its results, and tell candidates the tool is in use.</p>'
   '<h2>What it requires</h2>'
   '<p>An AEDT (an automated employment decision tool) cannot be used to substantially assist a hiring or promotion decision unless it has had a bias audit within the past year, the audit summary is published, and candidates receive notice. The bias audit is, in effect, a mandated audit-readiness artifact for one class of decision.</p>'
   '<h2>How DIG maps</h2>'
   '<p>A bias audit is exactly what <a href="/pillars/audit-readiness">audit readiness</a> produces: evidence, on demand, that an AI-influenced decision met its obligations. <a href="/pillars/information-provenance">Provenance</a> and <a href="/pillars/decision-traceability">traceability</a> make that audit possible rather than a guess. DIG generalizes the Local Law 144 discipline to every consequential AI-influenced decision, not just hiring.</p>',
 "faqs":[
   ("What is an AEDT under NYC Local Law 144?","<p>An automated employment decision tool: software that uses machine learning or AI to substantially assist a hiring or promotion decision. Using one in New York City requires an annual independent bias audit, published results, and candidate notice.</p>"),
   ("When did NYC Local Law 144 take effect?","<p>Enforcement began on 5 July 2023.</p>")],
 "refs":REFS_CORE,
 "related":[("/regulations","All regulations"),("/auditable-ai-decisions","Auditable AI decisions"),("/industries/financial-services","Financial services")],
})

PAGES5.append({
 "path":"compare/dig-vs-ai-trism","nav":None,
 "title":"Digital Information Governance vs. AI TRiSM - DIG®",
 "description":"Digital Information Governance (DIG®) vs. Gartner's AI TRiSM: one governs the AI system for trust, risk, and security; the other governs whether the AI-influenced decision can be defended.",
 "eyebrow":"Comparison","h1":"Digital Information Governance vs. AI TRiSM","byline":True,
 "breadcrumb":[("Home","/"),("Compare","/compare"),("DIG vs. AI TRiSM","")],
 "body":
   '<p class="lead">AI TRiSM (Trust, Risk and Security Management) is Gartner\'s framework for governing AI systems: model operations, security, privacy, and trust. Digital Information Governance governs something different and downstream: the AI-influenced decision, and whether it can be defended. The two are complementary, and DIG is the decision layer above the system layer TRiSM manages.</p>' +
   deftable([
     ("What it governs","AI TRiSM: the AI system (model ops, security, privacy, trust). DIG: the decision the system influences."),
     ("Core question","TRiSM: is the system trustworthy and secure? DIG: can this decision be defended?"),
     ("Origin","TRiSM: an analyst framework (Gartner). DIG: coined by Matthew Bertram, registered mark."),
     ("Output","TRiSM: model controls, security posture. DIG: a defensible, auditable decision trail."),
     ("Relationship","DIG sits above TRiSM: a well-managed system can still feed an indefensible decision."),
   ], head=("Dimension","How they differ")),
 "faqs":[
   ("Is DIG the same as AI TRiSM?","<p>No. AI TRiSM governs the AI system for trust, risk, and security. Digital Information Governance governs the AI-influenced decision and whether it is defensible and auditable. DIG is the decision layer above the system layer TRiSM manages.</p>"),
   ("Do you need both?","<p>They complement each other. TRiSM keeps the system sound; DIG keeps the decisions the system influences defensible. A secure model can still produce a decision no one can defend.</p>")],
 "refs":REFS_CORE,
 "related":[("/compare","All comparisons"),("/ai-decision-governance","AI decision governance"),("/framework","The framework")],
})

PAGES5.append({
 "path":"ai-governance-checklist","nav":None,
 "title":"AI Governance Checklist: Defensible AI Decisions (DIG®)",
 "description":"A practical AI governance checklist organized by the four pillars of Digital Information Governance (DIG®): the controls that keep AI-influenced decisions defensible and auditable.",
 "eyebrow":"Implementation","h1":"AI Governance Checklist","byline":True,
 "breadcrumb":[("Home","/"),("AI governance checklist","")],
 "infobox":{"title":"AI governance checklist","sub":"By the four pillars","rows":[
    ("Organized by","The four DIG pillars"),("Use","Audit your AI-influenced decisions"),
    ("Pairs with",'<a href="/dig-maturity-self-assessment">Self-assessment</a>'),("Output","A defensible decision")]},
 "body":
   defbox("An AI governance checklist is a practical list of controls for keeping AI-influenced decisions defensible. This one is organized by the four pillars of Digital Information Governance.", label="AI governance checklist") +
   '<p class="lead">Use this checklist to test whether your AI-influenced decisions are defensible today. It is organized by the four pillars of DIG. To score yourself in two minutes, use the <a href="/dig-maturity-self-assessment">DIG maturity self-assessment</a>.</p>'
   '<h2>Information Provenance</h2>'
   '<ul><li>You can trace the source of the information behind each AI-influenced decision.</li>'
   '<li>You know whether that information was authoritative and current when it was used.</li>'
   '<li>You can tell whether inputs were altered between source and decision.</li></ul>'
   '<h2>Decision Traceability</h2>'
   '<ul><li>There is a record of what was recommended, by which system, and on what basis.</li>'
   '<li>You can show who reviewed and approved the decision, and on whose authority.</li>'
   '<li>The record is captured as part of the decision, not reconstructed afterward.</li></ul>'
   '<h2>Representation Integrity</h2>'
   '<ul><li>You monitor how AI systems and search engines describe your organization.</li>'
   '<li>You can correct an inaccurate AI-generated statement about your company quickly.</li></ul>'
   '<h2>Audit Readiness</h2>'
   '<ul><li>You can produce the full decision trail for any AI-influenced decision on demand.</li>'
   '<li>Your controls are tested, not assumed.</li>'
   '<li>Coverage is measured: you know which decisions are governed and which are not.</li></ul>',
 "faqs":[
   ("What should an AI governance checklist cover?","<p>The controls that make an AI-influenced decision defensible: the provenance of its inputs, a trace of who decided and why, accurate representation across AI systems, and the ability to prove all of it on demand. The DIG four pillars organize these.</p>"),
   ("How do I know where we stand?","<p>Run the free <a href=\"/dig-maturity-self-assessment\">DIG maturity self-assessment</a> to score your organization on the five-level scale and get a recommended next step.</p>")],
 "refs":REFS_CORE,
 "related":[("/dig-maturity-self-assessment","Self-assessment"),("/dig-maturity-model","Maturity model"),("/framework","The framework")],
})
