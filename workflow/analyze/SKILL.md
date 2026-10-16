---
name: analyze
description: Assess codebase-informed technical readiness, recommend an implementation method and meaningful checks, or refresh analysis after deciding inputs change. Use for matching technical-analysis requests and authorized bounded handoffs; stop at recommendations rather than building.
---

# Analyze

Recommend the smallest useful design, method or sequence and check strategy from inspected evidence. Ordinary requests and bounded handoffs use the same procedure. `analyze` recommends; the technical lead decides routine engineering choices. In standalone use the caller is that lead, not a requirement to spawn an agent or ask the maintainer to select a method.

## Authority and companions

Check the project's applicable instructions and agreement once per context, reusing guidance already read. Follow relevant context/authority pointers and directory/runtime restrictions; compare decision/effect authority, safety, verification, documentation and continuation guidance with this analysis. Equivalent existing layouts work without Setup provenance or a template. Identify specific absent, conflicting or unverifiable guidance and recommend explicit setup/reconciliation without starting it or rewriting policy. Missing common guidance blocks dependent project analysis; missing tracker, model or domain detail blocks only that capability. Default to authorized inspection and a conversation return under that agreement.

Discover companions through the runtime/project catalog or an explicit approved location, never assumed sibling paths. For an invokable companion, read its complete entry and required references. For a conditional library, inspect the documented pointer and read the complete relevant library instead; do not execute or load an unrelated delivery procedure. In either case record resolved source/revision or digest and check semantic behavior. Ambiguous candidates block the dependent route. Recheck changed source, task or authority. Missing helpers never authorize installation or legacy substitution.

- `research`: for unresolved source/API/version questions; must return cited, applicable findings with uncertainty and freshness. Direct inspected local evidence needs no research invocation.
- `domain-modeling`: only actual meaning/model changes or potentially qualifying enduring decisions; must support bounded plan-only/approved effects and preserve decision history. Reading unchanged definitions needs no run.
- Methods: assess the capabilities in step 4 before execution, not by name alone. Missing methods do not prevent a supported recommendation.
- Optional delegation: only with actual permission, discover `work-on`'s conditional coordination library through its documented pointers, without invoking delivery or loading its unrelated entry procedure. Require root-owned allocation, finite bounds, protected ownership and inspectable results. A package exposing only the old universal contract is incompatible for this route; report delegation unavailable and continue direct analysis when equivalent. Workers request assignments from the existing root, never recursively delegate. Recorded acceptance corrections additionally use that lead's repair procedure and retained finding/budget history; analysis alone performs no repairs. No model assessment is required.

## 1. Bound the analysis

Use the request or caller's existing scope, authority, protected state and evidence to identify the deciding questions and a finite inspection bound. Keep acceptance, confirmed decisions, exclusions and limitations traceable to their source. No mandatory form or spec hierarchy is needed. Assess proposed outcomes as proposed; return missing commitments to their owner with consequences and a recommendation, while continuing unaffected inspection.

**Done:** scope, deciding questions, authority and stop boundary are clear; missing commitments are identified rather than silently invented.

## 2. Reuse evidence and inspect only material gaps

Compare prior findings with their deciding agreement, implementation, callers, tests/configuration and environment identities, including dirty content digests. Inspect cited support; neither HEAD, a ready label nor a summary proves freshness. Reuse current investigation and research directly. Refresh only missing or invalidated findings when deciding inputs change, conflict or gain relevant paths; preserve unaffected evidence and old-state history. If impact cannot be isolated, mark the relevant evidence set stale and explain the expanded inspection. Starting another phase alone triggers no complete analysis rerun.

Inspect relevant implementation and callers, not just names or directory listings:

- Ownership of state, behavior, side effects and invariants; data/control flow and suitable designs to retain or extend.
- Interfaces and consumers: inputs/outputs/errors, access rules and material compatibility, persistence or recovery obligations.
- Domain definitions and accepted ADR evidence; existing constraints and consequential decisions.
- Shared interfaces, cross-component dependencies, partial work and integration/serialization requirements. Ticket boundaries need not become module boundaries.
- Existing assertions and documented check commands: behavior covered, baseline failures, missing failure paths and environment limits. Counts are not coverage evidence.

For non-code/new targets inspect analogous artifacts and applicable constraints; mark absent code or coverage explicitly. Run only authorized safe relevant baseline checks, reporting command/environment and observed results or not-run reasons. Use discovered `research` for actual source gaps, supplying the bounded question, prior findings and authority; inspect its claim/source support and conflicts on return. Inaccessible decisive sources remain gaps, not inferred facts.

**Done:** affected responsibilities, interfaces, reuse and coverage have inspected evidence or specific material gaps with owner/next action; prior evidence is explicitly reused, refreshed or stale.

## 3. Form the technical brief and domain disposition

Prefer the least complicated adequate design, extending suitable existing structure. For substantial complexity name the current requirement or credible risk, why the simpler alternative fails and ongoing maintenance cost. Challenge speculative frameworks as well as shortcuts that lose access, persistence, recovery or domain invariants.

Return a brief at the approved task/plan home, or in conversation, covering applicable items:

| Item | Evidence or recommendation |
| --- | --- |
| Agreement/reuse | Acceptance references and deciding identities; retained/extended/replaced modules and reasons |
| Responsibilities/interfaces | State, side effects, invariants, producers/consumers, error and compatibility behavior; protected scope |
| Dependencies | Shared boundaries, coherent ownership, sequencing and integration constraints |
| Risks | Credible failure modes, exclusions, assumptions, unresolved decisions with owner/next action |
| Checks | Acceptance/risk → sufficient existing coverage or needed check; command/environment, meaningful expected result, actual baseline and gaps |
| Documentation | Existing authoritative homes, responsible owner and approval status, or justified no-change decision |

Reuse sufficient checks; propose new ones only for identified gaps. Include meaningful failure-path coverage for material security/privacy, destructive effects, persistence/recovery and domain rules. Planned checks are not executed evidence; an unrun baseline is unknown.

If domain work is actually needed, discover `domain-modeling` and give it the bounded subject, evidence, document mapping, confirmed decisions, contradictions, protected work, authority and expected return. Use **plan-only**, including no draft writes, unless the project agreement and task authorize the confirmed record delta. An approved handoff names exact files/sections/operations and approval evidence. Confirmed authorized glossary/context-map maintenance belongs to this work, not optional session storage. ADR creation or change needs explicit agreement and permission; routine design does not automatically require an ADR. Inspect actual returned plans/documents, applied versus proposed status, per-operation outcomes, rationale/history/links and caller-owned pointers; update only authorized pointers. Missing capability, unresolved meaning/decision or approval blocks the dependent design, not unaffected analysis. Never author a duplicate glossary/ADR procedure as fallback.

**Done:** structure and risk/check mapping are actionable; required domain work has an inspected disposition or explicit affected blocker. Routine refinements preserve settled commitments; consequential changes return to their authority owner.

## 4. Recommend a method and check availability

Honor binding target method/check requirements. Otherwise use the smallest useful capability or sequence justified by the deciding uncertainty and risks. These are selection cues, not method-loop instructions or a mandatory pipeline:

| Evidence/need | Candidate capability and minimum compatible return |
| --- | --- |
| Clear behavioral increment with useful test seam | `tdd`: meaningful behavioral red, minimal green and green refactoring, current local evidence |
| Uncertain design/UX/state model/feasibility | `prototype`: bounded experiment, actual observations, recommendation and artifact disposition; no production-readiness claim |
| Poorly understood legacy behavior at risk | `characterize`: baseline protection with intended/unknown/defect distinctions, sensitivity and limitations |
| Observable acceptance across a workflow/components | `acceptance-first`: executable agreed examples, checked increments and criterion-level results, with environment/intent gaps explicit |
| Straightforward bounded change or documentation/configuration | `build-and-check`: small increment with immediate relevant validation and coverage reuse |

Cues may compose: characterize then TDD, or prototype then a production method. Specify the transition condition and remaining checks; methods return to the lead rather than recursively invoke the next method. No universal TDD, test quota, forced user seam selection or automatic prototype promotion.

Separate **recommended capability** from **available compatible package**. Inspect only method entries needed to support a capability claim; record source identity and compatibility, not names alone. Missing/ambiguous/incompatible methods block execution, not supported recommendations. An available equivalent needs an evidence-backed reason and policy fit. Label fixture availability as synthetic, never real discovery; return the smallest next action without a technique questionnaire or silent substitution.

**Done:** recommendation/sequence, rationale, transitions, meaningful checks and actual or fixture availability are explicit; the lead can decide without an engineering questionnaire.

## 5. Inspect and return, then stop

Compare the brief and specialist artifacts with current deciding sources again; invalidate only dependent claims. Return the technical brief and recommendation with complete/partial/blocked status, source identities, reused/refreshed/stale evidence, actual versus planned/failed/not-run checks and environment limits. The lead retains method selection. Identify companion availability, domain/documentation disposition, uncertainty and affected blockers with owner/next action.

Keep findings in conversation or the selected artifact location, and live delegation/recorded correction state when applicable; ordinary inactive findings need no run ledger, durable handoff or future-session storage. A useful next-step recommendation is allowed without invoking that stage.

**Complete:** the requested technical conclusion is supported and all material readiness questions resolved. **Partial:** supported findings remain useful but scoped coverage/bounds limit the answer. **Blocked:** a deciding fact, consequential commitment, required domain capability or authority is unresolved. Distinguish technically actionable design from method availability and delivery's build/accept/report gates: execution authority, native dependency eligibility, Git preflight and later independent review are not established by analysis.

Standalone use stops at findings, without implementation, tickets, PRs or delivery invocation. In a bounded handoff, return to the caller, which inspects support, decides routine engineering and resumes its already-authorized responsibility. No repeated permission prompt or automatic reassessment is needed for unchanged inputs. Keep specific permission/capability or consequential uncertainty blockers explicit; continuation grants no new commitments or effects.

## Validation

For package changes or routing/freshness exercises read [validation](references/validation.md). Fixtures and static checks do not prove agent adherence or installed runtime discovery.
