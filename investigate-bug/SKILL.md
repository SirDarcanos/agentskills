---
name: investigate-bug
description: Investigate a reported defect, confirm reproduction and cause, and prepare or reconcile an implementation-ready ticket through write-tickets. Use for diagnosis requests and bounded bug-evidence handoffs; investigation alone stops before fixing.
---

# Investigate bug

Own the evidence between a bug report and a workable ticket. Ordinary matching requests and authorized bounded handoffs use this procedure. A complete current investigation is reused, not repeated because delivery starts. Investigation-only ends at the ticket outcome; a separate explicit investigation-and-fix request may authorize a later delivery handoff, never a fix inside this procedure.

## Authority and dependencies

Read target instructions and relevant context, workflow, tracker and domain pointers. Inspection and a conversation return are the default. Confirm authority for diagnostic execution, local probes, retained artifacts and tracker effects separately; source access grants no installation, external disclosure, service startup, model calls or delegation. Protect unrelated work, partial changes, modes and links. Product repair, PRs, closure, merge and release are outside this owner.

Discover companions from the runtime/project catalog or an explicit approved location, not sibling paths. Read complete entries and conditional references; record source/revision or digest and check semantic capabilities. Ambiguous or incompatible candidates block the affected route; recheck changed source, task or authority. Missing helpers permit supported findings/drafts, not installation or a legacy diagnosis fallback.

- `write-tickets` is required for publication/reconciliation: current bounded bug input, duplicate/partial-write handling, exact publication approval, native relationship/role read-back and no automatic readiness/scheduling. It owns all tracker writes and graph procedure discovery. An unresolved case can supply an explicitly investigation-only draft, never a ready fix claim.
- `analyze` is conditional for material technical-readiness/method/check gaps; require current code/caller evidence, targeted reuse and recommendations without implementation. Direct cause inspection and a supported method recommendation need no automatic Analyze run.
- `research` is conditional for unresolved authoritative source/version questions; require cited findings and freshness/disclosure bounds. Reading unchanged domain definitions needs no modeling run; actual meaning/decision work uses discovered `domain-modeling` with its plan-only/approved gate.
- Optional delegation requires separate authorization and the discovered `work-on` read-only execution contract, not delivery invocation. The root reserves shared capacity, exclusive scopes, finite bounds and lineage; workers request work from the root rather than recursively spawning. Missing authority/contract blocks delegation, not direct diagnosis. No model assessment is required.

For changes or validation read [validation](references/validation.md).

## 1. Bound the report and reuse current evidence

Identify the actual target, reported expected/actual behavior, impact and intended contract source. Record agreement/acceptance references, relevant environment, exclusions, protected files, authority/approval source, prior findings and expected return. Clarify only missing consequential intent, access or permissions; investigate discoverable facts directly. A standalone bug needs no spec hierarchy.

Choose a finite diagnostic bound appropriate to the report: named paths/question, maximum attempts or time, and stopping conditions. Each experiment has a hypothesis, deciding observation and permitted effects. Stop earlier on unsafe execution, missing material capability or decisive evidence; exhausting the bound yields an honest partial/investigation result, not an unlimited loop.

Pin deciding implementation, callers, configuration/tests, environment and contract identities, including staged/unstaged/included untracked content digests rather than HEAD alone. Inspect supporting prior artifacts and raw results. Compare those identities on receipt/resume: reuse complete current evidence, fill only missing coverage, invalidate dependent findings when deciding inputs change or conflict. Preserve unaffected findings and old-state history; if dependency impact cannot be isolated, mark the relevant set stale and explain the expanded check. A label, age or prior summary is not freshness proof.

Search matching issues through authorized read-only tracker access before proposing a new ticket. Compare symptom, intended behavior, environment, affected versions and cause rather than title alone. Record candidates and search coverage; incomplete access leaves duplicate status unknown. An ambiguous match needs reconciliation, not automatic creation or closure.

**Done:** scope, expectation source, authority, deciding identities, diagnostic bound and prior/duplicate evidence dispositions are explicit.

## 2. Confirm and minimize reproduction

Inspect relevant existing checks, implementation and callers. Choose the smallest safe reproduction in the reported environment, or clearly label a synthetic/substitute environment and its limits. Record exact steps/command, inputs, dependency/runtime/configuration versions, relevant timing/seed and observed expected-versus-actual results. Redact secrets and private data under retention/disclosure policy; insufficient safe evidence remains a gap.

For intermittent symptoms, record attempts, failures, successes and triggering conditions within the finite bound. A passing attempt does not disprove the report; distinguish observed intermittent reproduction from an unconfirmed report. A failure from missing dependencies, permissions or harness setup is not confirmation of the bug. Minimize inputs only while preserving the deciding behavior; keep baseline/control observations where useful.

Create probes or runnable reproduction artifacts only within approved diagnostic-write scope. Record owned paths, original identities, permitted edits, output home and retention/cleanup disposition before editing. Use isolated scratch copies where possible; never stash/reset unrelated work or turn a diagnostic experiment into product repair. Potentially destructive/load/production checks require exact environment and effects approval. Required unavailable checks are not-run, not passed.

**Done:** the symptom is confirmed with applicable raw observations, or attempts and the confirmation blocker are recorded. Unconfirmed work stays investigation-only.

## 3. Establish cause and bounded readiness

Trace the reproduced behavior through affected implementation and callers. Separate observations, hypotheses and established cause. For each material hypothesis choose a bounded discriminating check or inspection, record its result and rejected alternatives. Evidence must explain the causal path from trigger to actual behavior, not merely a suspicious line or correlation. A safe diagnostic intervention may support the cause, but its changed output is not a shipped fix or delivery acceptance.

Identify affected source locations/revisions and scope of impact. When decisive source/version or readiness gaps remain, use the conditional companions with only the bounded question, current evidence, protected work and exact authority. Inspect their cited support and actual results on return; reuse them directly. Ask the agreement owner about consequential behavior changes rather than inventing expected behavior.

Stop when the cause is sufficiently established to bound a fix and regression strategy, or the diagnostic bound/capability limit is reached. Unresolved cause returns attempted checks, remaining hypotheses, smallest next diagnostic action and owner. Confirmation alone is insufficient for an implementation-ready ticket.

**Done:** cause and readiness have deciding evidence, or the unresolved material gap prevents a ready fix claim.

## 4. Account for artifacts and prepare the ticket

Remove or restore only owned temporary probes under their recorded cleanup authority, comparing current content with owned changes first. Preserve useful reproduction artifacts at an approved home, with runnable instructions and disclosure-safe output; where retention is unapproved, return a proposed location or conversation evidence. Intervening unrelated changes block conflicting cleanup; report remaining instrumentation exactly. Inspect the final scoped diff/state: no unapproved product fix or unexplained temporary change may remain.

Prepare the following input for discovered Write Tickets; planned checks remain distinct from executed observations:

| Ticket content | Required evidence or decision |
| --- | --- |
| Identity/agreement | Target, descriptive title, standalone identity or existing issue, expectation source/revision, acceptance references and approval boundaries |
| Behavior/impact | Confirmed expected/actual behavior, user/data/operational impact and relevant affected environment/versions |
| Reproduction | Exact steps or retained runnable artifact, observed results and attempt counts/intermittency, controls, environment limits |
| Cause | Established causal path, supporting/rejected-hypothesis evidence, affected code/callers and deciding committed/dirty identities |
| Fix boundary | Recommended bounded outcome/owned paths, constraints, exclusions, true dependencies, risks and non-blocking uncertainty |
| Acceptance/checks | Checkable regression acceptance IDs, meaningful failure sensitivity, sufficient existing/needed checks and environment; method or sequence recommendation with rationale, lead retains selection |
| State/reuse | Reused/refreshed/stale findings and input coverage, raw evidence pointers, protected work, probe cleanup and retained-artifact disposition |

For unconfirmed or unresolved cases, replace ready-fix scope with **investigation-only** outcome, attempted evidence, material blocker, diagnostic acceptance and next action. Preserve any supported findings without manufacturing cause or repair scope. Failed artifact cleanup or missing material readiness prevents a complete ready handoff.

**Done:** every applicable field is supported or explicitly unresolved, and owned artifacts/diffs are accounted for.

## 5. Publish/reconcile through Write Tickets, return and stop

Supply the pinned investigation, current candidate issues, exact authority and expected ticket outcome to compatible `write-tickets`. It owns exact title/body/label/graph proposal and approval, persistence, duplicate/partial-write reconciliation and read-back; do not duplicate those steps here. A matching issue receives only an approved scoped update, preserving unrelated body, labels and native edges. No artificial parent, automatic readiness label, duplicate closure or scheduling follows investigation.

Before sending and after return compare deciding inputs again. Changed inputs invalidate only dependent claims; refresh within remaining bounds or return stale/investigation-only. Inspect actual draft/persisted contents, classification, approval and read-back evidence, not just the companion's success label. Missing approval returns a plan-only draft; missing required persistence capability or unknown read-back is blocked/partial, never a published-ready claim. A duplicate result names the canonical issue and what was actually reconciled.

Return complete/partial/blocked status, ticket identity and revision or draft, all deciding evidence/environment pointers, reused/refreshed/stale results, failed/not-run checks, uncertainty, companion identities, artifact/documentation disposition, remaining blockers and owner/next action. Record ledger use when applicable. Separate diagnostic readiness from publication, native eligibility and future delivery acceptance.

**Complete ready:** confirmed symptom, established cause and complete current ticket contract, accounted artifacts, authorized publication/reconciliation and verified ticket read-back. **Complete duplicate reconciliation:** current matching issue inspected and approved reconciliation read back, with diagnostic readiness stated separately. **Partial/blocked:** useful supported draft/findings with missing confirmation, cause, authority, capability, freshness or persistence explicitly identified; any published unresolved work is investigation-only.

Investigation-only stops here. For a separate authorized fix request, return the ready ticket to the lead for its delivery gate. The receiver compares deciding identities, consumes current evidence without re-investigation and fills only actual gaps. Discovery of `work-on` or a ticket is not invocation authority; incompatible delivery entry gates block that route until an authorized compatible lead is available. This procedure never launches delivery automatically.
