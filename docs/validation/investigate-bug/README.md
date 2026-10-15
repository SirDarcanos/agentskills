# Investigate Bug delivery evidence

For [#64](https://github.com/SirDarcanos/agentskills/issues/64), under the accepted [#50 design](../../design/composable-delivery.md) and [#48 agreement](https://github.com/SirDarcanos/agentskills/issues/48). Input: clean `main` at `8142ef6`; native blocked-by returned closed #60 and #63. Their merged PRs #85 (`ab540d5`) and #88 (`8142ef6`) are ancestors of the input, and the accepted design is present. Branch `feat/investigate-bug`, PR target `main`.

## Scope and traceability

- AC1: independent discoverable entry, ordinary/bounded invocation, semantic non-sibling companion discovery, complete/partial/blocked returns and missing-helper behavior.
- AC4/AC7: bounded confirmation/cause investigation, full implementation-ready ticket input, prior evidence reuse, targeted deciding-input invalidation, duplicate reconciliation and investigation-only stop with artifact accountability.
- AC8: Analyze/Research only for material gaps; unchanged domain definitions read directly, actual domain decisions retain the modeling gate.
- AC15: runnable synthetic reproduction and persisted safe tracker cases, package/isolation checks, direct procedure inspection, with limits stated below.

Write Tickets remains the publication/graph owner. This change clarifies its unresolved-investigation route: exact approval can persist a draft as investigation-only with diagnostic acceptance, not implementation readiness. No duplicate tracker algorithm is introduced. No existing Work On diagnosis body needed extraction; its general routing stays intact until #67. The current explicit Work On gate is honored rather than pretending an investigation can automatically invoke delivery.

## Executable cases

Run [package validation commands](../../../workflow/investigate-bug/references/validation.md). `test_investigation.py` creates only temporary synthetic code and JSON tracker state, reusing #63's `FakeTracker`. Exact local caller choices are authored tests, not a new production diagnosis service or automatic authorization mechanism.

The confirmed fixture's contract is that a discount fraction applies to subtotal. For `[40, 60]` and `.10`, the actual module returns `99.9`, not `90`; zero returns `100`, `.20` returns `99.8`. Source inspection establishes subtraction of the raw fraction rather than subtotal times fraction. A meaningful reproduction assertion fails; the complete ticket records the causal evidence, identities, fix boundary, constraints, exclusions, risks, acceptance/regression and TDD recommendation. A harmless owned probe is restored and a reproduction file retained in the temporary approved home. Persisted issue/body/labels are read back, no parent is invented, and product plus unrelated bytes remain unchanged: the investigation-only test never repairs the defect.

Other executed fixture branches:

- Intermittent observations: a scheduled synthetic input sequence has one failing and two passing observations; the caller trigger is unresolved, so the ticket remains investigation-only. This is controlled synthetic intermittency, not a real timing/race claim.
- Unconfirmed: three passing attempts plus a wrong-type harness error do not establish a defect; the ticket names missing failing inputs/environment and next diagnostic action.
- Confirmed/unresolved cause: symptom observed but decisive source access deliberately withheld for that case; persisted work has no asserted cause or ready fix scope.
- Duplicate: inspected matching input identities and cause select one existing issue, approved body-only reconciliation preserves labels/graph and read-back confirms no second issue.
- Current handoff: receiver checks source and input identities and reads the complete persisted evidence without another reproduction, analysis or fix. This is receiver inspection, not a Work On implementation trial.
- Dirty caller staleness: caller units change with product bytes unchanged; targeted reproduction returns `90` for amount `10`. Old caller reproduction/cause applicability/fix scope are stale, agreement/impact and old-state ticket history survive. No claim that unchanged HEAD means current evidence.

The tests demonstrate actual code observations and JSON persistence with authored caller decisions. They do not prove agent adherence, native live API behavior, real bug diagnosis, installed discovery or an investigation-and-fix agent run. Broader delivery handoff execution belongs to #71 after #67.

## Direct procedure inspection

Read the integrated entries and inspected these returns against the accepted design: complete ready investigation, unconfirmed/unresolved draft or approved investigation-only publication, canonical duplicate, current reuse and changed-input gap. Checked finite bounds, each ticket field, cleanup authority, non-blocking versus material uncertainty, exact publication through Write Tickets and final freshness comparison. For missing/incompatible Write Tickets or native procedure, only a draft/capability blocker is possible; ambiguous candidates require disambiguation. Missing Analyze/Research blocks only its material gap; no automatic rerun or legacy fallback. A later fix needs its own compatible delivery invocation and current evidence check. These are direct/static walkthroughs, not independent review or autonomous workflow trials.

## Actual checks

Executed directly on macOS, Python 3.14.7 and Git 2.54.0:

- All seven new investigation unittest methods passed; the confirmed case executed `python3 reproduction.py` in its scratch directory, observed `AssertionError`, persisted that evidence and retained unchanged buggy product bytes.
- All ten existing Write Tickets persisted-tracker unittest methods passed unchanged.
- Investigate Bug source and non-sibling isolated-package checks passed (four internal links); Write Tickets source/isolated checks passed (five links), along with the unchanged Work On package checks (110 links). Both root/evidence checks passed with 30 links. The new package license exactly matches the root MIT notice; fixtures parsed at Python 3.9 syntax level, not a Python 3.9 runtime claim.
- Existing Node/Marked rendered all nine changed runtime/index/evidence Markdown documents (64 headings, three tables); inspected new-entry HTML/table/list/code structure. This is structural Markdown inspection, not browser visual validation.
- `git diff --check` and staged whitespace checks passed. Direct integrated diff review checked approved boundaries, companion compatibility, complete ticket fields, retention, notices, private-data/local-path exclusions and no unrelated work.

No independent reviewer, autonomous agent trial, live API mutation, installed discovery/migration or actual later product fix was run. Missing-helper and permission routes have direct/static walkthrough evidence only. No model calls or service actions occurred.

## Documentation and provenance

Updated Investigate Bug entry/README/license/validation, Write Tickets entry/README/validation for unresolved publication, root skill index/delivery note and one Unreleased Added entry. Original instructions derive from #48 and accepted #50; no installed diagnosis body or external template imported. The package ships Nicola Mustone's complete MIT notice. Existing Write Tickets attribution/notices remain unchanged.

No domain meaning, architectural decision or operating authority changed: CONTEXT, ADRs and accepted/historical design records remain intact. No llms index or shared CI/build exists. New tests add seven unittest methods against a zero-test investigation-fixture baseline; no existing methods removed or modified. No production executable script changed. Merging adds repository source only; no deployment, release or installed-skill retirement follows. Source reversal does not retract tickets a future authorized consumer might publish. #64 remains open until accepted and merged.
