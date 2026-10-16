---
name: analyze
description: Assess codebase-informed technical readiness, recommend an implementation method and meaningful checks, or refresh analysis after deciding inputs change. Use for matching technical-analysis requests and authorized bounded handoffs; stop at recommendations rather than building.
---

# Analyze

Recommend the smallest adequate design, method and check strategy from inspected evidence. Ordinary requests and bounded handoffs use this procedure. The technical lead selects routine engineering choices; in standalone use that is the caller, without spawning an agent or asking the maintainer to choose techniques.

## Prerequisites and companions

Check applicable project instructions and agreement once per context, reusing guidance already read. Follow relevant context/authority and directory/runtime pointers; compare decision/effect authority, safety, verification, documentation and continuation responsibilities with this task. Equivalent existing layouts need no Setup provenance or template. Identify absent, conflicting or unverifiable guidance and recommend explicit setup/reconciliation without starting it or rewriting policy. Missing common guidance blocks dependent project analysis; missing tracker/model/domain detail blocks only that capability. Continue authorized inspection and conversation returns where supported.

Discover companions through runtime/project catalogs or approved locations, not assumed siblings. Read complete entries and required references; recover truncated reads before dependent work and resolve links from their containing source. For a conditional library, inspect the documented pointer and read the complete relevant library without invoking its unrelated procedure. Record source/revision or digest and semantic compatibility; ambiguity blocks that route. Recheck changed sources/task/authority. Missing helpers grant no installation or legacy fallback.

- Use `research` only for unresolved source/API/version questions; require cited applicable findings, uncertainty and freshness.
- For actual meaning/model changes or potentially qualifying enduring decisions, read [domain handoff](references/domain.md). Reading unchanged definitions needs no invocation. Domain writes require authorized deltas; ADRs need explicit agreement and permission.
- Before optional delegation, establish actual permission and read [delegation](references/delegation.md). Otherwise analyze directly; no worker or model assessment is required.
- Inspect method capabilities in step 4; missing packages do not invalidate supported recommendations.

## 1. Bound the question

Identify scope, deciding questions, acceptance/confirmed decisions, exclusions, limitations, authority, protected state and a finite inspection bound from the request or caller evidence. Keep commitments traceable; no mandatory form or spec hierarchy. Assess proposals as proposed. Return missing commitments to their owner with consequences and a recommendation; continue unaffected inspection.

**Done:** deciding questions and stop boundary are clear, without invented commitments.

## 2. Reuse evidence and fill material gaps

Compare prior findings with deciding agreement, implementation, callers, tests/configuration and environment identities, including dirty content digests. Inspect cited support: HEAD, labels and summaries alone do not prove freshness. Reuse current investigation/research. Refresh only findings invalidated by changed, conflicting or newly relevant inputs; retain unaffected evidence and old-state history. If impact cannot be isolated, mark the relevant set stale and explain expanded inspection. A new phase alone triggers no rerun.

Inspect sources and assertions, not names or counts:

- State/behavior/side-effect ownership, invariants, data/control flow and suitable structure to reuse.
- Interfaces and consumers: inputs, outputs, errors, access, compatibility, persistence and recovery.
- Domain definitions, accepted ADRs, constraints and consequential decisions.
- Shared boundaries, dependencies, partial work, coherent ownership and integration/serialization needs. Ticket boundaries need not become modules.
- Existing check commands/assertions, covered behavior, baseline failures, missing failure paths and environment limits.

For non-code/new targets inspect analogous artifacts and constraints; mark absent implementation/coverage. Run only authorized safe relevant baselines and retain commands, environment, observed results or not-run reasons. For source gaps hand Research the bounded question, prior findings and authority; inspect returned claim/source support and conflicts. Inaccessible deciding sources remain gaps.

**Done:** reuse, responsibilities, interfaces and coverage have inspected support or material gaps with owner/next action.

## 3. Form the technical brief

Extend suitable existing structure using the least complicated adequate design. Justify substantial complexity by a current requirement or credible risk, why the simpler alternative fails and maintenance cost. Reject speculative frameworks and shortcuts that lose safety or domain invariants.

Prepare one brief in conversation or the approved task/plan home:

| Item | Required content when applicable |
| --- | --- |
| Agreement/evidence | Acceptance references, deciding identities; reused/refreshed/stale findings and reasons |
| Design | Retained/extended/replaced structure, responsibilities, state, side effects, invariants, interfaces/consumers/errors/compatibility and protected scope |
| Dependencies/risks | Shared ownership, sequencing/integration constraints, credible failure modes, exclusions, assumptions and unresolved decisions with owner/next action |
| Checks | Acceptance/risk → sufficient existing coverage or needed check; command/environment, expected result, actual baseline versus planned/failed/not-run checks and limits |
| Documentation | Authoritative homes, owner/approval status, domain disposition or justified no-change decision |

Propose new checks only for gaps. Cover material security/privacy, destructive effects, persistence/recovery and domain failure paths. Planned checks are not executed evidence; an unrun baseline is unknown. Apply the conditional domain handoff when triggered; unresolved domain capability/meaning/approval blocks only dependent design.

**Done:** actionable structure and risk/check mapping preserve settled commitments; consequential changes return to their authority owner.

## 4. Recommend a method and inspect availability

Honor binding target method/check policy; otherwise select the smallest useful capability or sequence justified by uncertainty and risk:

| Need | Candidate capability and minimum return |
| --- | --- |
| Behavioral increment with useful test seam | `tdd`: meaningful behavioral red, minimal green, green refactoring and current local evidence |
| Uncertain design/UX/state model/feasibility | `prototype`: bounded experiment, observations, recommendation and artifact disposition; no production-readiness claim |
| Legacy behavior at risk | `characterize`: baseline protection, intended/unknown/defect distinctions, sensitivity and limits |
| Observable cross-component workflow | `acceptance-first`: executable agreed examples, checked increments, criterion results and explicit environment/intent gaps |
| Straightforward change, documentation/configuration | `build-and-check`: small increments, immediate relevant validation and coverage reuse |

For sequences specify transitions and remaining checks; methods return to the lead, not recursively invoke successors. No universal TDD, test quota, user seam questionnaire or automatic prototype promotion.

Separate recommended capability from available compatible package. Inspect entries needed for availability claims and record source identity/compatibility, not names alone. Missing/ambiguous/incompatible packages block execution, not supported recommendations. An available equivalent needs evidence and policy fit, never silent substitution. Label synthetic fixtures as such, not real discovery.

**Done:** recommendation, rationale, transitions, checks and actual/fixture availability support the lead's decision.

## 5. Inspect the return, then stop

Recheck the brief and specialist artifacts against current deciding sources; invalidate only dependent claims. Return the brief plus method recommendation/availability, domain/documentation disposition and remaining uncertainty/blockers with owner/next action. The lead retains method selection.

Report **complete** for a supported conclusion with material readiness questions resolved; **partial** when coverage/bounds limit useful findings; **blocked** when a deciding fact, consequential commitment, required domain capability or authority is unresolved. Distinguish actionable design from execution authority, native eligibility, Git preflight and independent delivery acceptance: analysis establishes none of those gates.

Keep findings in conversation or the selected artifact home; ordinary inactive findings need no ledger, durable handoff or future-session storage. Retain live delegation/correction state when applicable. Standalone use stops without implementation, tickets, PRs or delivery invocation. A bounded caller inspects support and resumes its already-authorized responsibility; unchanged inputs need no repeated prompt or reassessment. Recommend a next stage without starting it or granting new commitments/effects.

## Validation

For package changes or routing/freshness exercises read [validation](references/validation.md). Fixtures/static checks do not prove agent adherence or installed discovery.
