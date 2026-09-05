# Digital Information Governance (DIG): A Reference Framework for Defensible AI-Influenced Decisions

**Version 1.1** (v1.0 June 2026; v1.1 September 2026 adds Section 9, the action layer)
**Author:** Matthew Bertram, President of ModalPoint, Owner and CEO of EWR Digital, Chief Marketing Officer of the Oil and Gas Global Network. ORCID [0009-0004-0720-5321](https://orcid.org/0009-0004-0720-5321). Houston, Texas.
**Canonical reference:** https://digitalinformationgovernance.com
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Trademark:** DIG® / Digital Information Governance® is a registered trademark of Matthew Bertram (U.S. Reg. No. 8147558, Supplemental Register, registered 17 February 2026; application serial 99559923).

---

## Abstract

Artificial intelligence now influences decisions that organizations are held accountable for, in lending, hiring, clinical care, energy operations, and more. Governance has not kept pace. Most frameworks govern the model: its bias, drift, and explainability. Few govern the decision the model influences, and whether that decision can be defended after the fact. Digital Information Governance (DIG) is a discipline for closing that gap. This document defines DIG, its four pillars, and a five-level maturity model, and maps the framework to the major AI governance regimes (the NIST AI Risk Management Framework, the EU AI Act, ISO/IEC 42001, and the Texas Responsible AI Governance Act).

## 1. The problem: adoption outran defensibility

Adoption of AI is near-universal. Roughly 78% of organizations reported using AI in at least one business function in 2024, up from 55% a year earlier.[1] At the same time, the ability to govern AI-influenced decisions has not kept up. Only about 21% of organizations report a mature governance model for agentic AI, which means roughly four in five lack mature capabilities such as audit trails and clear decision boundaries.[2] Documented AI incidents reached a record 362 in 2025, a 55% increase over the 233 recorded in 2024.[3]

The risk DIG addresses is specific: an AI-influenced decision that goes wrong and cannot be reconstructed or defended after the fact. When a regulator, partner, or court asks how a decision was made, the organization that cannot produce the record is exposed regardless of whether the decision was correct.

## 2. Definition

> Digital Information Governance (DIG) is a discipline for keeping AI-influenced decisions defensible and auditable, ensuring a company's information is accurately represented, its decisions are traceable, and its AI use is provable to regulators, partners, and courts.

DIG is decision-centric. It is distinct from information governance, which manages the records and data lifecycle (storage, retention, and disposition), and from AI governance in its narrow sense, which focuses on the model. DIG sits at the decision layer above model governance: it governs whether the decision an AI system influenced can be defended.

## 3. The four pillars

DIG decomposes a defensible AI-influenced decision into four pillars.

1. **Information Provenance.** Where the information feeding a decision came from, and whether it can be trusted.
2. **Decision Traceability.** A record of what was decided, by what (human or AI), on what basis, and who is accountable.
3. **Representation Integrity.** Keeping the company accurately represented across AI systems, search engines, and data environments.
4. **Audit Readiness.** Being able to prove, on demand, that AI-influenced decisions met their obligations.

A decision is defensible when all four hold: its inputs are traceable to trusted sources, the act of deciding is recorded with accountability, the organization is represented accurately in the systems that speak for it, and the whole record can be produced on request.

## 4. The DIG Maturity Model

The DIG Maturity Model is a five-level scale that measures how defensible an organization's AI-influenced decisions are, assessed against the four pillars. Each level marks a shift in *when* the record is created: at Level 1 it is never created, at Level 3 it is assembled when asked, and at Level 5 it is captured at decision time and verified continuously.

| Level | Name | What it means |
|-------|------|---------------|
| 1 | Ad hoc | AI influences decisions with no durable record. Decisions cannot be reconstructed after the fact, so none are defensible by design. |
| 2 | Aware | Policies exist and some activity is logged, but coverage is partial and inconsistent. Whether a decision is defensible depends on the individual who made it. |
| 3 | Defined | The four pillars are standard practice for high-stakes decisions. Provenance is tracked, decision trails are captured, and the organization can reconstruct most decisions on request. This is the first level a regulator would call governed. |
| 4 | Managed | Controls are tested rather than assumed. The organization is audit-ready on demand, representation across AI systems is monitored, and coverage is measured rather than hoped for. |
| 5 | Defensible by default | Decision integrity is captured automatically at the moment each decision is made. Audit is continuous, representation is governed, and defensibility is the default state rather than an after-the-fact scramble. |

A common self-assessment scores each of the four pillars and places an organization on the scale. Regulated operators making consequential AI-influenced decisions should target Level 4 or above.

## 5. Relationship to existing frameworks

DIG is not a replacement for the established AI governance regimes. It is the decision-level layer that makes their requirements operational, and most of their obligations overlap.

- **NIST AI Risk Management Framework (AI RMF 1.0, 2023).** Organized around Govern, Map, Measure, and Manage. It states that trustworthy AI depends on accountability, and accountability presupposes transparency, which is the principle behind Decision Traceability.[4]
- **EU AI Act (Regulation (EU) 2024/1689).** Makes auditability a legal duty for high-risk AI: automatic event logging that supports traceability (Article 12), technical documentation (Article 11), and human oversight (Article 14).[5] Penalties reach 35 million euros or 7% of global annual turnover for prohibited practices.[6]
- **ISO/IEC 42001:2023.** The first international management-system standard for AI, published December 2023.[7] DIG provides the decision-level evidence an AI management system is expected to produce.
- **Texas Responsible AI Governance Act (TRAIGA, HB 149).** Effective 1 January 2026, with Attorney-General-enforced penalties up to 200,000 dollars per uncurable violation and 40,000 dollars per day for continuing violations.[8]

Across these regimes the recurring demand is the same: show that an AI-influenced decision met its obligations, with a record to prove it. That is what DIG captures.

## 6. Why auditability is also a value lever

Audit readiness is often treated as a compliance cost. The data points the other way. Organizations that regularly audit and assess their AI systems are over three times more likely to report high value from generative AI, the highest-multiplier governance practice in one 2025 survey.[9] The same record that makes a decision defensible also makes the AI program measurable and improvable.

## 7. Applying DIG

Implementation follows a simple arc:

1. **Assess.** Inventory where AI touches decisions, then test each pillar: can you show the provenance of decision inputs, the trace of who decided and why, the accuracy of how AI represents you, and the records to prove it on demand?
2. **Place.** Locate the organization on the DIG Maturity Model and identify the gaps.
3. **Remediate.** Move the record earlier in the decision lifecycle, from reconstructed under pressure (Level 1 to 2), to produced on demand (Level 3 to 4), to captured automatically at decision time (Level 5).

## 8. Research foundations

The case for auditable, traceable AI decisions rests on established peer-reviewed work. Raji, Smart, and colleagues named the AI accountability gap and introduced SMACTR, a five-stage internal audit framework.[10] Mitchell and colleagues proposed model cards as transparency and accountability documentation, clarifying a model's intended use and its performance across groups.[11] DIG extends that lineage from the model to the decision the model influences.

## 9. The action layer: governing AI that acts (added in v1.1, September 2026)

Frontier AI systems now operate real interfaces: a keyboard, a mouse, a terminal, a browser.
They are becoming digital employees, and the vendors say so themselves. OpenAI designated its
Astra model the first at the Critical cybersecurity threshold under its Preparedness Framework,
and names containing "unauthorized, misaligned actions" by the model as a core safeguard
goal.[12] Anthropic offers one frontier model as two products: generally available with
additional safety measures, and trusted-access for approved organizations.[13]

Once an AI acts on enterprise information rather than merely reading it, a defensible posture
answers five questions: What was the AI authorized to see? What was it authorized to decide?
What was it authorized to do? Who approved that authority? And can the organization
reconstruct exactly what happened afterward?

The five questions map onto the four pillars without adding a fifth. Authorized access is
Information Provenance (access scope is provenance in reverse). Delegated decisions and their
approvals are Decision Traceability (delegation is itself a decision, and the grant belongs in
the record). Authorized action is Representation Integrity (an agent that sends, posts,
configures, or transacts represents the company by action). Reconstruction is Audit Readiness
(action-level trails: tool calls, commands, page loads, and approvals, replayable end to end).
The canonical definition is unchanged; the record simply runs one step further, from the
decision to the act.

At the action layer, each maturity level has a concrete marker. Level 1: agents run under
human credentials, with no inventory, indistinguishable from employees in every log. Level 2:
agent activity is known and partially logged; scopes are informal. Level 3: agents hold their
own identities with scoped access, delegation thresholds are written, and actions are
attributable on request. Level 4: execution boundaries are tested rather than assumed, and
approvals are recorded at grant time. Level 5: authorization is captured at execution time,
every action is replayable, and containment is a rehearsed control.

## References

1. Stanford University HAI, The 2025 AI Index Report, Responsible AI chapter (2024 data). https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai
2. Deloitte, State of AI in the Enterprise, 2026. https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html
3. Stanford University HAI, The 2026 AI Index Report, Responsible AI chapter (2025 data; AI Index and McKinsey survey). https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai
4. NIST AI Risk Management Framework (AI RMF 1.0 / NIST AI 100-1), 26 January 2023. https://www.nist.gov/itl/ai-risk-management-framework
5. EU AI Act, Regulation (EU) 2024/1689, Articles 11, 12, 14. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
6. EU AI Act, Regulation (EU) 2024/1689, Article 99 (penalties). https://artificialintelligenceact.eu/article/99/
7. ISO/IEC 42001:2023, Information technology, Artificial intelligence, Management system. https://www.iso.org/standard/81230.html
8. Texas Responsible Artificial Intelligence Governance Act (TRAIGA), HB 149, 89R. https://capitol.texas.gov/tlodocs/89R/billtext/pdf/HB00149F.pdf
9. Gartner, press release, 4 November 2025 (survey of 360 organizations). https://www.gartner.com/en/newsroom/press-releases/2025-11-04-gartner-survey-finds-regular-ai-system-assessments-triple-the-likelihood-of-high-genai-value
10. Raji, Smart, et al., Closing the AI Accountability Gap (ACM FAT* 2020), arXiv:2001.00973. https://arxiv.org/abs/2001.00973
11. Mitchell et al., Model Cards for Model Reporting (ACM FAT* 2019), arXiv:1810.03993. https://arxiv.org/abs/1810.03993
12. OpenAI, Path to Astra: critical capabilities and frontier safeguards, 1 September 2026. https://openai.com/index/path-to-astra/
13. Anthropic, Claude Fable 5 and Claude Mythos 5, 2026. https://www.anthropic.com/news/claude-fable-5-mythos-5

---

## How to cite

Bertram, Matthew. *Digital Information Governance (DIG): A Reference Framework for Defensible AI-Influenced Decisions*, Version 1.1, 2026. https://digitalinformationgovernance.com

A related working paper by the same author is archived at Zenodo: *LLM Visibility Glossary and Frameworks (2025 Edition)*, DOI [10.5281/zenodo.17042750](https://doi.org/10.5281/zenodo.17042750).
