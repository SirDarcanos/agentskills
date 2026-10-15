# Portable required-review authority

## Agreement and scope

The maintainer requested a source-skill correction: explicit Work On delivery should include its required read-only reviews wherever the skill is used, not depend on this repository's operating policy. Reusable-skill fixes must change tracked package behavior rather than substitute local policy or update installed copies.

This follows the repository-local permission recorded under #65 / PR #90. Historical evidence remains unchanged. The private diagnostic session is neither copied nor linked here. No new issue, tracker relationship, installation, service, optional assessment, merge or release is part of this change. Issue #125 is the separate PR-readability request and is not implemented here.

Base: `df7877b` (`origin/main` at preflight). Branch: `fix/required-review-authority`. The tree was clean before changes. One root lead implements directly; at most two read-only reviewers may run under the existing shared execution limit. Acceptance checkpoint: `portable-review-authority`; repair cycles initially 0/2.

## Acceptance and source mapping

| ID | Required outcome | Deciding source/check |
| --- | --- | --- |
| RA1 | Explicit Work On / Work On Spec delivery supplies bounded required-review authority without another delegation prompt or a local standing policy | Work On entry and `references/contracts.md` required-review authority; Review Delivery entry/handoff; portable source guards |
| RA2 | Explicit restrictions, independent read-only axes, root launch ownership, finite bounds and shared capacity remain binding | Required-review authority plus unchanged execution limits; authored positive/negative cases |
| RA3 | No added authority for optional workers/assessments, new disclosure/spending, installation, library-only execution, merge or release | Required-review authority exclusions; Review Delivery handoff and source guards |
| RA4 | Requested reusable-skill corrections target tracked package sources, not local policy or installed copies | Work On context step, README and source-target guard; actual diff |
| RA5 | Independently copied packages retain links and the authority contract without host-repository policy | Internal-link/anchor checks in source and isolated copies; copied Work On source guards |

The shared authority rule has one home in Work On's execution library. Review Delivery discovers that library and consumes the original delivery authority; loading a library does not originate permission. Work On Spec already discovers the same complete contract; no new coordinator or standalone-review permission is introduced.

## Executed checks and limits

- Before the instruction changes, the two new static source-contract tests failed because portable required-review authority and the tracked-source targeting rule were absent. An initial missing-heading failure appeared as an IndexError; the guard now asserts heading presence first. A later case-sensitive assertion was corrected to match the capitalized source text. Both guards now pass, including in an isolated Work On package copy.
- Existing package link checking from `docs/validation/writing-for-agents/check-package.py` was reused for every Markdown file in Work On and Review Delivery, then repeated on separate temporary package copies without sibling skills. All local links and anchors resolved. Ruby/Psych parsed both unchanged frontmatters successfully.
- Existing Marked rendered all nine changed Markdown inputs and HTML heading/table structure was inspected. The first harness assumed Marked emits heading IDs; it does not by default. That harness assumption was corrected to inspect the rendered heading text; source-anchor validation passed separately. No graphical preview was run.
- Regression suites passed: Work On 10 methods (including the two new source guards), Review Delivery snapshot 13 methods, Work On Spec coordination 8 methods. Full raw output is retained by the delivery runtime. Expected synthetic red checks and the modeled missing-integration failure are asserted by their fixtures; the suites exited 0. The source guards inspect instructions; they are not an executable authorization controller or proof of autonomous compliance.

Environment: macOS, Python 3.14.7, Ruby/Psych 2.6.10, Node 24.21.0, existing Git and Marked. No dependencies were installed. Temporary package copies are removed by their owning `TemporaryDirectory` scopes; fixture scripts clean up only their own synthetic targets.

### Regression commands

From the repository root:

```sh
python3 -B workflow/work-on/scripts/check-single-change-fixture.py
python3 -B workflow/review-delivery/scripts/test_snapshot.py
python3 -B workflow/work-on-spec/scripts/check-coordination-fixture.py
```

Baseline test unit: named `unittest` methods in those scripts. This change adds two Work On source-contract methods; no existing method is removed, moved or weakened. The remaining added cases are authored validation scenarios, not executed agent trials.

## Authored decision cases — not agent executions

1. Explicit single-change delivery in a project with no local permission policy: the request supplies required review authority; do not request separate delegation approval.
2. Whole-spec delivery with a ticket worker: the same shared contract applies; the ticket worker requests reviewers from the existing root, without a second pool.
3. Explicit user, project or runtime prohibition: restriction wins; no unauthorized launches and independent acceptance remains blocked.
4. One slot: sequence axes. Missing bounded runtime: report a capability blocker, not a missing local permission policy.
5. New sensitive disclosure or extra spending, optional implementation/exploration or model assessment: retain separate approval gates.
6. Library-only read or investigation-only request: no delivery execution authority is originated; standalone review must establish its own permission.
7. Skill correction in a skill repository: inspect actual tracked package changes; repository-local permission alone cannot satisfy acceptance, and installed copies remain protected.

These source-level expectations were checked directly against the instructions. No autonomous replay of the private session or cross-runtime adherence experiment was performed. Independent source review is recorded separately in the delivery runtime, not represented as an end-to-end behavioral test.

## Documentation and effects

Updated Work On's entry, shared contract, overview, validation cases and guards; reconciled Review Delivery's entry, handoff, overview and validation. The two unreleased Added changelog entries describe the portable behavior. Repository operating policy, historical design/ADR records, domain meanings and installed copies remain unchanged; existing discovery/catalog descriptions need no update. This is an approved narrow authorization change, not a new architecture or domain model.

Inspected repository sources contain no CI workflows or automatic installation/deployment/release hooks; no jobs change. Hosted timing/compute is unmeasured. Source merge makes the correction available to consumers, but updating separately installed copies requires its own approval. A source revert restores prior instructions, not actions consumers already took; rollback was not executed.
