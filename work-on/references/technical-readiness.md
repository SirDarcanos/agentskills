# Technical readiness

Read completely when entry selects missing codebase/design/risk evidence for an actionable brief/spec, or implementation reveals a material design change. Use the inspected context and [handoff contract](contracts.md#handoff-envelope). This is an internal procedure of an explicitly requested Work On run, not a separate command. For changes or validation, read [technical-readiness validation](technical-readiness-validation.md).

## 1. Pin the agreement and inspect the affected system

Identify the approved brief/spec source and revision, acceptance IDs, exclusions, accepted limitations, authority and protected work. Reuse settled product and technical decisions, checking their freshness against actual sources. Route missing or changed product commitments to [product agreement](product-agreement.md); keep safe technical inspection moving without treating proposals as approval.

Before proposing structure, inspect the relevant implementation and its callers, not only a directory listing or prior summary:

- Existing modules and suitable designs to reuse or extend; ownership of state, behavior and side effects; current data/control flow across the affected boundary.
- Interfaces, their consumers and contracts: inputs, outputs, errors, access rules, persistence/recovery and compatibility where material.
- Domain vocabulary, relevant ADRs and their acceptance evidence through the target's existing pointers; constraints and consequential choices already made.
- Cross-cutting dependencies, shared interfaces, related partial work and integration assumptions. Scheduling/ticket boundaries need not become module boundaries.
- Existing verification and documented commands, what behavior they actually cover, known baseline failures and material gaps. Inspect test assertions rather than inferring coverage from names or counts.

Bound inspection by acceptance and credible risks. For a new or non-code target, inspect analogous existing artifacts and applicable constraints; mark absent modules/coverage explicitly rather than inventing them. Record source locations/revisions, observed facts, assumptions and unavailable evidence. Run safe relevant baseline checks when useful and authorized; otherwise label them not-run with reasons.

**Complete when:** each affected responsibility/interface and material constraint has inspected evidence, reuse candidates and current coverage are known, and missing material facts have an owner and next investigation or affected blocker.

## 2. Choose proportionate structure and verification

Prefer the least complicated design that satisfies current requirements and credible risks. Extend a suitable existing design unless evidence explains why it cannot meet this agreement. Keep likely changes local and interfaces small enough to hide meaningful complexity. Routine technical choices stay with the lead within authority; use the target's collaboration preference when a consequential choice needs human approval.

Produce a bounded technical brief in the target's approved task/plan location (a short conversation return can suffice under the shared retention contract). Include only applicable detail:

| Item | Required decision/evidence |
| --- | --- |
| Agreement and reuse | Brief/spec revision and acceptance IDs; existing modules/designs to retain, extend or replace, with source pointers and reasons |
| Responsibilities | Ownership of state, behavior, side effects and invariants; proposed changes and protected scope |
| Interfaces | Producers/consumers, inputs/outputs, error and compatibility behavior; material access, persistence or recovery obligations |
| Dependencies | Shared interfaces and cross-cutting changes; sequencing/integration constraints and coherent ownership, including work that should serialize or stay together |
| Risks and exclusions | Credible failure modes, mitigations, unresolved assumptions/decisions with owner and next action; preserved exclusions, deferrals and accepted limitations |
| Verification | Acceptance/risk → existing coverage or needed check, command/environment where known, meaningful expected result, baseline status and evidence gaps |
| Documentation | Existing authoritative homes needing updates, responsible phase and approval status, or justified no-change decision |

For every substantial complexity choice, name the current requirement or credible risk, why a simpler alternative is insufficient, and the ongoing maintenance cost. Challenge **overengineering** (speculative layers, wrappers, configuration or frameworks) and **underengineering** (lost invariants, unsafe access, fragile persistence/recovery or unsupported compatibility). Reuse needs no new abstraction merely to look organized; an extra boundary earns its cost through the inspected behavior.

Choose checks for distinct meaningful failures and important boundaries. Reuse or extend sufficient coverage; identify necessary failure-path coverage for security/privacy, persistence/recovery, destructive effects and material domain rules. Honor binding project verification requirements. Recommend new tests only for identified gaps, not a quota or mandatory TDD. Separate planned verification from actually executed evidence; an unrun baseline is unknown, not green.

**Complete when:** responsibilities, interfaces, dependencies, risks and verification are actionable against the agreement; substantial complexity has an evidence-backed rationale; any unresolved material design choice is explicitly blocked rather than hidden in a build assignment.

## 3. Resolve needed domain or decision-record work

Reading existing definitions or reusing an unchanged accepted decision requires no modeling run. When evidence indicates needed terminology/model changes or a potentially qualifying enduring architectural record, discover and check `domain-modeling` through [capability checks](contracts.md#capability-checks). Read its complete entry point and relevant handoff/branch references; let that companion own qualification and the glossary/ADR procedure rather than duplicating them here.

Supply the shared envelope plus the exact terms/relationships/decision to examine, inspected code/spec/record evidence, the target's document mapping and maintenance policy, confirmed decisions with authority, contradictions/proposals/deferrals, protected work and expected return. Specify **plan-only** when exact write authority is absent: inspection and proposed file/section deltas only, including no draft writes. An **approved** handoff names approval evidence, exact permitted files/sections and operations, exclusions and preserved history. Follow the procedure in the lead's context unless separately authorized delegation is useful; the handoff itself launches nothing.

Inspect the returned plan or actual documents against evidence and approval: per-operation outcomes, proposed/accepted distinctions, preserved rationale, relevant links, code/document conflicts, omitted records and required caller-owned pointers. Apply only authorized caller-owned pointer updates. Partial/failed writes and plans remain distinguishable from applied results. Reopen only changed facts; an unchanged rerun should not regenerate records.

Missing/incompatible required domain capability, unresolved meanings, missing consequential decisions or required write approval block the affected modeling-dependent design/build scope. Return the smallest next action; continue unaffected analysis without installing, substituting a helper or authoring glossary/ADRs locally as a fallback.

**Complete when:** modeling is explicitly unnecessary with rationale, or the required handoff has an inspected disposition and all material dependent decisions/records are reconciled. A plan-only proposal with unresolved approval is not readiness evidence.

## 4. Inspect the brief and return the next gate

The lead compares the actual technical brief and any specialist artifacts to the current agreement, codebase, coverage and authority. Preserve accepted commitments and history. Routine technical refinements update this brief and affected evidence within authority; consequential changes to behavior, scope, cost/risk commitments or accepted limitations return to product agreement/the approval owner with practical consequences and a recommendation. Update the authoritative product home only after appropriate approval; a technical plan cannot silently supersede it.

Return through [the shared envelope](contracts.md#handoff-envelope): source revisions, technical decisions and evidence, domain disposition, documentation outcomes, executed/planned/not-run checks, remaining uncertainty and specific blockers. If material evidence changed, identify affected stale plans/checks and the reinspection needed.

Report **technically actionable** only when approved product scope and verifiable acceptance, responsibilities/interfaces, dependencies, material risks and required modeling decisions are actionable. Separately assess the [build gate](contracts.md#delivery-gates): sufficient execution authority, native dependency eligibility where applicable and safe Git preflight are still required before ready-to-build. A ready label or finished plan cannot bypass those conditions. Known later acceptance/review gaps stay explicit without falsely blocking equivalent authorized planning/building.

Select ticketing only when decomposition is useful; otherwise select direct build. Inspect the selected package-local destination from entry before loading it, read its complete procedure and check conditional capabilities. If absent, return the technical handoff and report that responsibility unavailable. Do not implement from the route table or invoke a legacy command.

**Technical-readiness completion:** a codebase-informed bounded brief with an evidence-backed gate decision and next action, or an affected blocker with owner/recommendation. This is not verified implementation, accepted delivery, issue closure, merge or release.
