---
name: acceptance-first
description: Implement agreed workflows from executable observable acceptance examples. Use for acceptance-first requests or bounded method handoffs covering cross-component behavior, with criterion-level evidence and explicit product-decision or environment blockers.
---

# Acceptance First

Own executable examples and small implementation increments for one agreed workflow, not independent review or delivery acceptance. Use directly for matching requests or inline through an authorized handoff. Read [validation](references/validation.md) when changing or validating this package.

## 1. Bound the workflow and authority

Read target instructions, authoritative agreement/revision and acceptance IDs, exclusions, affected components/callers, existing checks and supplied readiness evidence. Compare deciding source, dirty files, tests, configuration and environment identities; reuse current evidence and reassess only dependent gaps. Ordinary request/context can supply these facts without a form.

Identify one owner, protected work, permitted file/run effects, data/retention constraints, expected return and material integration boundaries. Plan-only authority returns an example/check plan without writes. This method grants no installation, service startup, disclosure, spending, delegation, tracker publication, merge or release permission.

Discover conditional companions through the runtime catalog or an explicit approved location, not sibling paths. Read the complete entry and relevant references, record source/revision or digest and check semantic capability. Ambiguous, missing or incompatible helpers block the dependent route without installation or legacy fallback:

- Before Git writes, consume compatible `implementation-preflight` or inspect a current caller-supplied result for this scope/state. Outside Git retain a before/after manifest.
- Changed meanings or qualifying decisions use discovered `domain-modeling`; reading definitions alone needs no invocation.
- Delegation or correction of recorded acceptance findings consumes discovered `work-on`'s execution/repair library without invoking delivery. Preserve root ownership, ledger, bounds and finding lineage; workers request additional work from the root. Ordinary planned development increments do not require that companion.

**Complete when:** agreement, scope, authority, ownership, deciding inputs and dependencies are known, or affected blockers are recorded with protected work intact.

## 2. Translate commitments into executable examples

Map every in-scope acceptance criterion to representative setup/input, action and externally observable outcome: returned data, persisted state, failure, side effects or workflow transition. Include relevant rejection/recovery paths and cross-component risks. Use the smallest real boundary that can demonstrate the commitment; reuse adequate existing checks. The lead chooses routine harnesses and seams, not the maintainer.

Record each example's criterion ID, authoritative intent source, relevant components, expected result, command/environment, data/setup/cleanup authority and finite run/timeout bounds. Technical fixture values illustrate an approved rule; they must not invent new product requirements. If the agreement permits several materially different outcomes, stop the affected example and recommend a concrete clarification to the product owner. Preserve unaffected work; approval of revised intent precedes implementation and updates to its authoritative record.

Mark mocked boundaries and what they cannot prove. Missing material infrastructure, access, dependency or representative environment leaves that criterion blocked/unverified; a stubbed pass cannot establish real integration. Do not silently replace a material check or install/start services to make it runnable.

**Complete when:** every scoped criterion has executable examples or an explicit intent/environment gap, and expectations trace to the agreement rather than current implementation.

## 3. Establish a meaningful failure before implementing

Run relevant existing checks to identify baseline failures where useful. Execute the acceptance examples before production changes and inspect raw output, exit status and observable state. A useful failing example reaches the intended behavior and fails on the agreed expectation; import, syntax, credentials and harness failures are environment/harness gaps, not acceptance failures.

For behavior already satisfied, retain current passing evidence rather than manufacture a production defect. Where sensitivity needs demonstration, use an authorized reversible perturbation in an isolated copy, restore and rerun; label this sensitivity evidence separately from missing-behavior red. If no meaningful failure or sensitivity can safely be observed, report that limitation instead of claiming it happened.

**Complete when:** each runnable example has an observed baseline tied to its checked state, failures have classified causes, and affected unavailable checks remain explicit.

## 4. Implement and check small increments

Choose a bounded vertical slice of the workflow. Implement only its authorized behavior across the necessary components, then run its acceptance examples and relevant lower-level, integration and regression checks before the next slice. Inspect outcomes and side effects, not only a success summary. Keep completed examples green; refactor within scope while relevant checks pass.

A failed expectation prompts diagnosis of implementation, harness or missing decision. Preserve approved expectations: never weaken assertions, skip a material example or edit acceptance to fit the code. A genuine product change returns to its owner with evidence and a recommended bounded decision; pause dependent work until approved. Record pre-existing/environment failures separately. Material failed/unrun checks block the affected completion claim and unsafe dependent progress, not unrelated safe work.

Ordinary planned failing-example increments are development, not a reset of recorded finding repairs. For corrective work retain the shared checkpoint/lineage and spent repair budget across method switches or resume. Unknown authority or exhausted correction allowance stops the affected route.

After implementation or intervening edits, refresh checks dependent on changed code/callers/configuration/environment or agreement. Keep evidence for its original state; HEAD alone does not identify dirty work. Update authoritative owned documentation/changelog under target policy or justify no change.

**Complete when:** scoped increments have current criterion/risk evidence, or partial work and failed, stale or blocked checks are preserved without a false pass.

## 5. Return criterion-level evidence and stop

Inspect the actual diff/manifest against scope and protected bytes, index work, modes and links. Account for all probes, test data and temporary perturbations; remove only authorized unchanged owned scratch, preserving uncertain/interveningly changed artifacts.

Return **complete**, **partial** or **blocked**, including:

- Agreement/revision, acceptance IDs, exclusions, authority/owner and companion/preflight sources; branch/base/PR target or non-Git manifest.
- Per criterion: examples/commands, observed baseline failure or existing-pass/sensitivity evidence, implementation increments, final result and evidence pointers, checked source/test/config/environment identities, and remaining failure-path/integration limits.
- Explicit failed, not-run, stale, ambiguous and unavailable material boundaries; proposed owner decision or smallest next action. Distinguish implemented from verified, deferred and blocked scope.
- Changed/retained/restored artifacts, protected work, documentation disposition and shared finding/ledger state when applicable.

**Method completion:** all scoped commitments have current local observable evidence, or the return clearly preserves partial/blocking work. Passing examples do not replace broader risk checks, independent review or final integrated acceptance. Return to the caller for those gates; do not recursively launch another method or open a PR.
