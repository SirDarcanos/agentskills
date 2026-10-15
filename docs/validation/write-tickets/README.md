# Write Tickets extraction evidence

For [#63](https://github.com/SirDarcanos/agentskills/issues/63), under accepted [#50 design](../../design/composable-delivery.md) and [#48 agreement](https://github.com/SirDarcanos/agentskills/issues/48). Input was clean `main` at `4efaf08`; native #63 blocked-by read returned only closed #50, and merged PR #75 plus accepted design established integration rather than closure alone. Working branch: `feat/standalone-write-tickets`, target `main`.

## Delivered scope and mapping

- AC1/AC5: independently discoverable package, ordinary/bounded input, cohesive acceptance-linked decomposition and exact publication/graph approval; Work On now has a thin adapter to the sole procedure owner.
- AC4/AC7: complete current bounded bug evidence can be reused directly; changed deciding inputs invalidate affected findings, incomplete/unconfirmed cause returns investigation work, duplicate reconciliation and standalone bug publication need no fake hierarchy.
- AC13: discovered maintained tracker library retains native algorithm ownership, exact IDs, pagination, both-direction read-back, additive preservation and partial-write recovery. Spec/work-ticket roles remain distinct from independently authorized readiness; standalone publication never schedules work.
- AC15: package checks, isolated copies and persisted fake tracker exercise useful failure modes. These are authored executable checks and direct inspection, not an autonomous or independent agent trial.

## Reproduction and limitations

Run the commands in [package validation](../../../workflow/write-tickets/references/validation.md). `tracker_fixture.py` writes only a disposable JSON store, supports native parent/blocker endpoints and page-size-one observations, and keeps issue numbers distinct from database IDs. `test_tracker.py` exercises the real Setup Project blocker reconciler through that fixture. Parent writes/conflicts, ticket creation and labels are fixture mechanics with authored caller decisions; this is neither an additional production graph algorithm nor proof of live API behavior or authorization enforcement.

Covered: persisted parent/blocker read-back in both directions, no-op rerun, preserved unrelated labels/edges, pagination, combined blocker cycle, parent ancestry cycle/conflicting parent, number-as-ID rejection, wrong-ID read-back in both blocker directions, failed parent read, partial blocker write inspected before retry, interrupted creation searched before retry, duplicate ambiguity, standalone bug and plan-only/publication without automatic readiness.

Direct caller inspection: Work On discovers Write Tickets through catalogs/approved locations, supplies its pinned envelope, inspects actual artifacts/native evidence, and only then chooses build/dispatch within the existing request and prerequisite integration policy. Missing/incompatible specialist blocks that route; standalone Write Tickets returns without continuation. This is a direct procedure walkthrough, not an executed delegated workflow or installed slash-command test.

## Actual checks

Executed directly on macOS with Python 3.14.7 and Git 2.54.0:

- Initial package/isolation/frontmatter/license/link checks passed: 5 new-package links and 110 Work On links in both source and isolated copies. Both notices matched the complete MIT text. Python fixtures parsed at the 3.9 syntax level; this is not a Python 3.9 execution claim.
- Final rerun passed all 10 persisted-tracker unittest methods and 22 unchanged Setup Project tests. Package/isolation checks passed again, including 29 root/evidence links.
- Dependency helper `--help` and `git diff --check` passed.
- Node/Marked rendered structure inspected for 10 runtime/index/changelog Markdown documents: 63 headings and 6 tables. This is structural inspection, not browser visual validation.
- Direct integrated diff review checked approved ownership, invocation/authority boundaries, preservation, isolated dependencies, standalone bugs, missing helper outcomes and notice portability. No independent reviewer/delegation or model call was used.

Authored procedure cases remain direct/static evidence, not an executed agent workflow. Live GitHub publication, authentication, installed discovery/expansion, cross-runtime behavior and delegated coordination were not run.

## Documentation and provenance

Updated the new package entry/README/validation/license, Work On entry/README/contracts/ticketing and validation adapters, root index and one Unreleased Added entry. No shared build or CI exists; no CI changes or timing claim. Ten new unittest methods are added against a zero-test extraction-fixture baseline; existing Setup Project tests are unchanged. Prior scenario guidance is consolidated into the new owner's validation, not counted as deleted tests. No executable production script changed.

The new package reuses Work On ticketing at the input revision and credits Matt Pocock's to-tickets design lineage with the full 2026 MIT copyright/permission notice shipped alongside Nicola Mustone's notice. No new upstream template/body imported. Historical #14 evidence and accepted design/ADRs remain unchanged; no domain meaning or consequential design delta, so CONTEXT/ADRs need no update. No llms index exists. No tracker settings/labels/relationships, installed packages, model services, merges or releases were changed. #63 stays open until accepted and merged; source merge does not perform installed migration.
