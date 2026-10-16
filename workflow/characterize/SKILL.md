---
name: characterize
description: Protect relevant existing behavior before risky legacy changes with characterization checks and provenance. Use for characterization-first requests or bounded method handoffs where intended behavior, unknown intent and known defects must be separated.
---

# Characterize

Capture a baseline before change; own behavior protection, not the subsequent implementation or delivery acceptance. Use directly for matching requests or inline through authorized handoffs. Read [validation](references/validation.md) when changing or validating this package.

## 1. Establish the boundary

Reuse applicable project guidance and relevant context/authority pointers once per context, including directory/runtime restrictions. Check decision/effect authority, safety, verification/review, documentation and continuation responsibilities. Direct and bounded use accept equivalent layouts. Missing/conflicting common guidance blocks dependent work: name the gap and recommend explicit setup/reconciliation without starting it or inventing policy. Conditional gaps block only that capability.

Identify the risky change and relevant observable boundaries: inputs, outputs, failures, side effects and state transitions. Inspect affected code/callers/checks and supplied evidence against current source, dirty content, configuration and environment; reuse current evidence. Bound owned checks/probes and protected work. Capture authority does not authorize a production fix or broad refactor; plan-only requests return a capture plan.

Use compatible `implementation-preflight` before Git writes, or inspect a current supplied result for the same scope/state; outside Git retain a before/after manifest. Actual meaning/decision-record changes use discovered `domain-modeling`; reading definitions alone needs no invocation. Missing/incompatible companions block their dependent route.

Only delegated work or recorded acceptance correction loads Work On's documented conditional coordination/repair library, without invoking delivery. Retain root ownership/bounds and checkpoint/lineage/spent cycles; method switches/resume reset nothing. An old universal-contract-only package blocks that route, not ordinary development.

**Complete when:** scope, ownership, deciding sources and capture authority are actionable, or specific affected blockers preserve work.

## 2. Classify observations before protecting them

For each relevant boundary, record representative inputs, observed behavior, provenance (source/caller, command, environment, revision/content identity), intent evidence and one disposition:

| Disposition | Evidence and treatment |
| --- | --- |
| Intended invariant | Agreement, documented contract or confirmed owner decision establishes intent. Protect it with a behavioral check. |
| Unknown intent | Observation alone establishes what happens, not what should happen. Preserve it as an explicitly provisional baseline, identify the missing decision and whether changing it is safe. |
| Confirmed defect | Record actual versus intended behavior and authoritative defect evidence. Keep reproduction separate from desired acceptance; never require the bug to persist. |

A suspected defect with unresolved intent remains unknown, with the suspicion recorded. Existing assertions and snapshots are evidence, not automatic product authority. For mixed snapshots, split intended assertions from defect observations; avoid approving a whole golden file just because it matches. A known-defect diagnostic may describe or reproduce old behavior, but label it non-protecting and exclude it from preservation gates. Its later correction can legitimately change that observation.

Select cases for the proposed change's meaningful risks, including relevant error paths and side effects. Bound case count, repeat count and command timeout before execution. Avoid broad coverage drives or copying real private data into fixtures. Unknown material intent blocks permission to change that boundary, not capture of observations elsewhere.

**Complete when:** each selected boundary has provenance, an explicit disposition, a protecting or diagnostic check plan and any unresolved intent decision.

## 3. Capture and test the baseline

Run existing relevant checks before changing production behavior. Add the smallest behavioral harness at the real boundary, following target conventions. Temporary seams/instrumentation need exact authority and an accounted disposition; keep production behavior unchanged. Run the capture checks against the current legacy state and inspect raw outputs, failures, side effects and exit status. Record pre-existing failures separately from harness/environment errors; an unrun check has no baseline result.

Handle nondeterminism explicitly. Identify sources such as time, randomness, generated IDs, ordering or concurrency. Where justified, control inputs at the boundary or compare meaningful stable properties. Record each normalization and why the removed field is irrelevant to this change. Preserve ordering, identity or timing when it is itself the contract. Use bounded repeated runs to expose variation; one seed or passing repetition cannot prove stability. Retain raw observations under retention authority; unresolved variation is a limit or blocker, not a silently updated snapshot or a flaky check retried until green.

Demonstrate sensitivity to a relevant invariant change: run a reversible, authorized perturbation in an isolated copy or bounded controlled input, observe the check fail for the intended reason, restore the original and rerun green. A missing import or syntax error is not sensitivity. If perturbation is unsafe/unavailable, report sensitivity unverified and its consequence; never mutate unrelated/user work to prove it. Ensure normalization does not hide the relevant change.

**Complete when:** baseline checks have observed results and identities, sensitivity is evidenced or explicitly unverified, nondeterminism is accounted for, and original behavior/protected work is preserved.

## 4. Return protected boundaries and stop

Inspect the actual diff/manifest: only authorized tests/probes/documentation changed, temporary perturbations restored, unrelated bytes/modes/link targets and index work preserved. Retain useful checks and evidence at the approved location; remove only explicitly authorized unchanged owned scratch. Preserve uncertain/interveningly changed artifacts and record their disposition. Update owned documentation/changelog under target policy or justify no change.

Return **complete**, **partial** or **blocked**, with:

- Proposed risky change and scoped agreement references; reuse current task/preflight context.
- Protected intended invariants, provisional unknown baselines and separate defect reproductions, each with intent/observation provenance.
- Runnable commands, actual baseline and sensitivity results, raw evidence pointers, source/test/config/environment identities; failed, unrun or stale checks.
- Normalization/controlled inputs, repeat bounds and observed variation; coverage, environment and intent limits.
- Artifact disposition, protected-work comparison and documentation outcome; existing coordination/repair state only when applicable.
- Recommended follow-on scope/checks, including defect acceptance that still needs implementation and unknown boundaries requiring a decision.

**Method completion:** relevant baseline protection and limits are handed back truthfully, or preserved partial/blocking work identifies the smallest next action. Passing characterization is neither approval of a defect nor proof of new behavior, integration or independent review. Return to the caller; it chooses the next implementation method and delivery gates. Do not recursively launch that method or open a PR.
