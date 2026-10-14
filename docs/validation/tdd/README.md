# TDD implementation evidence — #55

## Scope and authority

Agreement: [#55](https://github.com/SirDarcanos/agentskills/issues/55), under [#48](https://github.com/SirDarcanos/agentskills/issues/48), and the accepted [composable-delivery design](../../design/composable-delivery.md). Direct repository implementation was requested; no delegation, model calls or installed-copy changes were authorized or performed.

Input state: clean `main` at `bc22076`, matching fetched `origin/main`. Native #55 blocker read returned #50 only; #50 is closed and its accepted design was integrated by PR #75, merge `a95a9588ff86304f2390cae8d87df4addf7da1d1`, confirmed as an ancestor of the input. Created `feat/tdd-loop` from that state; base and intended PR target are `main`. No pre-existing PR or protected dirty work. This evidence applies to the scoped changes identified by the implementation commit/PR, not future installed sources.

Newly written instructions implement a complete method owner; no external body/template was copied verbatim. Matt Pocock's TDD skill directly informed the behavioral testing, oracle/coupling safeguards and incremental test-first approach. After the maintainer's licensing clarification, the exact upstream entry and full MIT license at `49dd158d1076134a641b33efb035946536778336` were fetched and inspected; the package README records that source and its LICENSE retains Matt Pocock's 2026 notice alongside Nicola Mustone's. The inspected legacy TDD entry excludes refactoring and requires user-confirmed seams, so inspiration does not make it a compatible runtime fallback. Work On's old test-first instruction is replaced by a semantic companion handoff; its broad entry, non-TDD methods, verification, repair and acceptance responsibilities remain in place pending their own tickets.

## Executed checks

Environment: macOS, Python 3.14.7, Node 24.21.0; direct local checks, no agent workers.

| Check | Actual result |
| --- | --- |
| `python3 tdd/scripts/check-fixture.py` | Exit 0; full synthetic sequence passed as detailed below. |
| Isolated complete package copy | Copied TDD and Work On into differently named, non-sibling package locations in a temporary tree; isolated TDD fixture exited 0 without any sibling skills. Temporary copies removed. |
| Markdown/frontmatter/link checks | Local Node/Marked check rendered 26 package/root/evidence Markdown documents, resolved 116 relative file links in isolated copies plus two in this evidence record after the attribution follow-up, and checked TDD's name/description with no command-only gate. Existing Work On frontmatter/invocation remains unchanged. HTML structure and source were inspected directly; this is not browser visual inspection or installed discovery. |
| `git diff --check` | Passed for tracked changes; repeated against the final staged scope before committing. |
| Direct integrated inspection | Inspected scoped changes against #55/AC1, AC3, AC6, AC14 and AC15: one loop owner, independent invocation/handoff, routine lead choices, authorization/dependency blockers, local-only completion, documentation and no automatic installed mutation. No independent reviewer was used. |

The executable fixture's agreement is synthetic checkout behavior: shipping costs 5 below subtotal 50, otherwise it is free. Its observed sequence:

1. Existing qualifying-cart test passed (one test).
2. A self-comparison also passed faulty shipping behavior, demonstrating an insensitive oracle.
3. Adding a small-cart example retained the old test and failed with `AssertionError: 30 != 35` (exit 1, two tests). This is the intended missing shipping fee, not an infrastructure failure.
4. Minimal shipping implementation passed both tests (exit 0).
5. A source-expression probe passed that implementation.
6. Refactoring repeated subtotal calculation into a single local value passed both unchanged behavioral tests (exit 0); the source-expression probe failed despite preserved behavior (exit 1).
7. Both diagnostic anti-examples were removed; the final retained two-test suite passed. The script verifies that behavioral test bytes did not change through green/refactor.

Counting baseline: compared with `bc22076`, one fixture runner is added and no existing repository tests are removed or updated. Within its synthetic target, one behavioral test is reused unchanged and one is added; two temporary diagnostic anti-examples are deliberately discarded, not existing coverage removals. No shared suite or CI workflow exists, none was added, and CI duration was not measured.

## Documentation disposition

Added TDD entry, human README, MIT notice and package-local repeatable validation guidance. Updated root listing, installation/companion guidance, Work On's test-first route and capability declaration, and one Unreleased Added entry. CONTEXT, ADRs, accepted design and historical execution records are unchanged: no new domain meaning or architectural decision was introduced. Maintainer copyright names were corrected in all five repository/package LICENSE files and two documentation references; TypeSafe AI's existing notice is preserved. The project context now records the maintainer-approved package-specific attribution rule. This licensing follow-up changes notices, not historical check outcomes; no additional changelog entry is needed because runtime behavior is unchanged and TDD already has its single Unreleased Added entry. No release or installed migration was performed. Source rollback restores the old caller instruction as well as removing the new package; it cannot restore any independently changed installations. Consumers must stage updated Work On with compatible TDD for the selected test-first route.

## Limits and next action

The fixture is executed code/test evidence, not an autonomous standalone/composed agent trial. Companion discovery compatibility, plan-only, missing-helper, wrong-reason-red, stale evidence and repair/delegation cases were inspected as instruction contracts; their [authored package cases](../../../tdd/references/validation.md) have not been executed as runtime trials. Real installed discovery, other runtimes/Python versions, bounded delegation and independent Standards/Spec review remain unverified. No local package check establishes overall #48 acceptance.

Implementation is locally checked, not accepted. Make the PR available for maintainer inspection, keep #55 open until accepted and merged, and stop before merging. Broader composed/runtime acceptance remains with #71/#73; actual same-name installed replacement remains with separately approved #74.
