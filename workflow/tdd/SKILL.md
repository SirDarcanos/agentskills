---
name: tdd
description: Implement a bounded feature or bug fix test-first with red–green–refactor. Use for test-first requests, red–green–refactor requests, or an authorized delivery handoff selecting TDD.
---

# TDD

Own one small behavioral increment at a time: meaningful red, minimal green implementation, then behavior-preserving refactoring while green. This method supports standalone requests and bounded handoffs. It returns local implementation/check evidence; it does not select the next method, provide independent review, or accept a whole delivery.

Loading this skill grants no effects. Inspection/plan-only requests stop at a proposed increment and checks. Writes and test execution need task authority; delegation, disclosure, installation, service operations, merge and release remain separately authorized.

For package changes or validation, read [validation](references/validation.md). The procedure below is the sole owner of the TDD loop.

## 1. Establish the bounded increment

Inspect the target's instructions, agreement and relevant code, callers, checks, domain vocabulary and ADRs. Consume current analysis or reproduction evidence directly; reassess only facts dependent on changed agreement, code, callers, tests or environment. Record source revisions/content identities, including relevant dirty files, rather than relying on HEAD alone.

Establish the intended observable behavior, acceptance references, exclusions, owned files/interfaces, protected work, approved effects, dependencies and expected return. A direct request supplies these through context; no handoff form is required. Resolve consequential behavior/authority gaps with their owner; the technical lead chooses routine seams and test strategy without a maintainer questionnaire. Standalone execution acts as its own bounded lead.

Discover companions through the runtime catalog or an explicit approved location, never an assumed sibling path. Read each complete entry and relevant references; record the resolved source/revision or digest and inspect semantic capabilities. Ambiguity or incompatibility blocks only the dependent route; installation is not a fallback.

- Before Git implementation writes, use compatible `implementation-preflight`, or inspect a current supplied result for the same scope/state: protected work, branch/base and PR target. Outside Git, retain a before/after manifest.
- Required meaning or qualifying decision-record changes use the target's discovered `domain-modeling` owner. Reading existing definitions requires no invocation.
- Delegated work or correction of recorded acceptance findings requires the discovered `work-on` execution/repair contract as a read-only library, without invoking delivery. Preserve its root ledger, ownership, limits and finding lineage; workers request additional work from the root rather than spawning workers. An unavailable compatible contract blocks that route, not an ordinary direct development loop. Planned red–green increments are development, not failed-acceptance repair episodes.

**Complete when:** behavior, ownership, authority, deciding inputs and required dependencies are known; otherwise return a plan or affected-route blocker with preserved work.

## 2. Select a behavioral check

Inspect existing assertions and target-documented commands. Reuse or extend adequate coverage instead of duplicating it. Choose a small increment at an externally observable boundary: results, errors or effects available to its consumers. Use the project's vocabulary for examples and names. The lead may choose unit, integration or end-to-end checks according to the actual risks and environment; use controlled doubles at external boundaries when necessary.

Derive expected outcomes independently from the agreement or a worked example. Inspect assertions for two rejection cases:

- **Tautological:** the oracle repeats the production calculation or compares a result with itself. Replace it with an independently justified outcome that can disagree with the implementation.
- **Implementation-coupled:** the check requires private helpers, internal call order or representation instead of the agreed behavior. Move the assertion to the consumer boundary so equivalent implementations can pass. Internal probes may help diagnosis but are not retained as behavioral acceptance checks.

Run relevant safe baselines and record command, environment, state and result. An unavailable material check remains a gap, not green; missing tooling grants no installation permission. If current coverage already demonstrates the required failure, reuse that check and its current red evidence. If behavior is already correctly covered and passing, report that no new red increment is needed; do not fabricate a defect or redundant test. Any separately authorized green-only cleanup must be reported as such, not as a completed new TDD cycle.

**Complete when:** one behavioral increment has a sensitive check and independent oracle, existing coverage has a reuse disposition, and baseline failures/gaps are distinguished from the intended red.

## 3. Red: observe the intended failure

Add or adjust only the check for this increment, then execute it before production changes. Inspect the raw result. Red must fail because the specified behavior is absent or wrong, not because of syntax, a missing tool, broken discovery, or an unrelated failure. For a new interface, make the harness load/run far enough to demonstrate the missing contract; infrastructure failure alone is insufficient.

Record the assertion/expected-versus-actual result, command, exit status, environment and checked source state. Repair the harness or revise an insensitive assertion before implementing. Preserve useful existing reproduction evidence; rerun when deciding inputs differ or its failure cause is unclear.

**Complete when:** the intended behavioral failure is actually observed and understood. Wrong-reason failures or unrun checks block the affected green claim.

## 4. Green: implement the increment

Implement only enough of the agreed behavior to pass the check through the real consumer boundary. Keep changes within the owned scope; avoid speculative features or writing a batch of future tests before learning from this increment.

Run the focused check and relevant regression checks. Inspect failures and distinguish regressions from baseline/environment failures. A passing focused test with a material regression is not green. Stop affected progress for missing authority, unsafe execution or unresolved material evidence; preserve partial artifacts and recommend the smallest next action rather than retrying indefinitely.

**Complete when:** the increment's check and relevant regressions are passing at the recorded state, or a truthful partial/blocking result is retained.

## 5. Refactor while green

Inspect the affected design for duplication, unclear responsibilities or naming, and unnecessary complexity. Make a small behavior-preserving improvement where useful, then rerun the focused and relevant regression checks after each refactoring increment. Keep behavioral expectations intact; a test that breaks solely because equivalent implementation changed needs its coupling examined, not its expected behavior weakened. If refactoring reveals a new behavior requirement, return to a new red increment within authority.

Restore green before proceeding. Record the refactor and before/after evidence. If no useful refactor is warranted, record that inspected decision; refactoring is part of the loop, not deferred to independent review.

**Complete when:** the refactor preserves checked behavior and relevant checks remain green, or the no-refactor decision is justified. Repeat steps 2–5 only for remaining approved behavioral increments.

## 6. Return local evidence and stop

Inspect the integrated local diff against the bounded agreement and protected work. Update owned documentation/changelog under target policy, or justify no change. Pin changed artifacts and deciding inputs, including dirty content/modes or link targets, so receivers can inspect and refresh dependent evidence after changes.

Return **complete**, **partial** or **blocked**, with:

- Implemented behavior and acceptance/risk mapping; deferred/excluded scope.
- Red failure cause, green and refactor commands/results, environment and state identities; reused coverage/evidence and rejected-check dispositions.
- Failed, stale and not-run checks, uncertainty, remaining findings and retained ledger/repair lineage when applicable.
- Artifact/state pointers, branch/base/target or manifest, protected work, companion resolutions, documentation disposition and next action.

**Method completion:** all owned increments have meaningful red and current green/refactor evidence, or an explicitly reported already-covered/no-change outcome. Passing local checks are not independent review, integrated delivery acceptance, ticket closure, merge, deployment or release. Return to the caller without automatically launching another method or delivery phase.
