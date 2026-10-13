# #28 recovery evidence

Repository-local evidence outside the installable package. [Recovery](../../../work-on/references/recovery.md) owns runtime behavior; [recovery validation](../../../work-on/references/recovery-validation.md) owns authored cases and the execution boundary.

## Reproduction and executed checks

From the repository root with Python 3.9+ and Git:

```sh
python3 -B docs/validation/work-on-recovery/exercise.py
```

Executed and inspected with Python 3.14.7 and Git 2.54.0: final run exit 0. [Source](exercise.py) creates an explicitly disposable Git target, performs local operations and assertions and disposes only that fixture at the end. No agents, installation, live tracker mutation, production merge or global update. Fixture policy explicitly permits these local operations; repository PR-only policy remains unchanged.

Actual disposable revisions from this run (vary on rerun): baseline `708c8d7d71f7cb87590b1448fb25894a036d8849`; uncertain-but-applied source/target `0d44787f02632720dc9dc022b93c46a6b00304ea`; resumed correction `e078698dfc8620a3d9eaa8d704c693bfb53a3b0f`; conflict source `760d7b7c8dd1bf18188871d969c2cb22350e7e16`; conflict target `7094af79dccbefed98112d3344468d6a426fd75a`. Package revision is the containing PR commit, not these temporary revisions.

| Actual observation | Direct lead walkthrough against procedure |
| --- | --- |
| Retained integration outcome says unknown; target HEAD equals source and ancestry succeeds | Step 2 records actual applied result; no second integration is performed. This exercises local outcome inspection, not a remote timeout. |
| Old revision/content differs; old assertion exits 1; current value-2 and value-3 checks exit 0 | Step 3 rejects stale evidence and refreshes checks at actual state. No review freshness or renewed independent review is claimed. |
| Partial value-3 patch inspected; mock lifecycle says stopped; scoped direct correction committed; count advances 1 to 2 | Steps 2–3 justify safe direct resume under fixture authority, retaining the checkpoint. Lifecycle is synthetic, not a killed-worker runtime test. |
| Staged and unstaged sentinel diffs, bytes/mode, untracked note and symlink target remain identical through all operations | Steps 1/4 preservation checks pass. Unrelated index state remains staged; commits explicitly include only owned `core.py`. |
| Actual merge conflict in separate worktree leaves MERGE_HEAD, unmerged index and both source sides intact | Steps 1/3 preserve conflict and both sides with a resolution owner/action. No abort/reset/retry or forced conflict resolution. |
| Synthetic closed predecessor lacks acceptance; required tool unavailable; owner unknown; count two | Step 3 authored dispositions: dependent waiting, check/replacement blocked, repair reassessment. Assertions inspect starting facts/preservation, not a recovery engine's decisions. |
| Source branches, conflict worktree/state and sentinels remain at protocol end | Step 4 retains useful recovery pointers until the fixture's explicit disposable disposition. No production cleanup permission inferred. |

Initial fixture runs failed: the generic commit consumed the unrelated staged sentinel; switching it to an owned-path-only commit fixed preservation. A subsequent merge was correctly refused by Git because of the dirty index; conflict execution moved to a separate worktree without transferring/stashing target work. Final successful run includes both protections. These were fixture-authoring errors, not observed skill-agent behavior or repair-budget evidence.

## Scope, gates and limitations

Preflight: clean `main`, equal to fetched `origin/main`, at `d6b1adbd95638b1f0f3aa8a6aa465c49f101a053`; created `feat/delivery-recovery` from that base, PR target `main`, no existing PR/unrelated work. Native #28 blocked-by read returned #27, closed completed; merged PR #43 at the base above supplies accepted integration evidence. Read #14, accepted delivery design, linked inventory/design validation, actual entry/shared/dispatch/completion procedures and predecessor execution evidence. No native relationships or labels changed.

Build readiness: approved bounded #28 behavior and integrated predecessor, safe preflight, one direct author. Implemented: recovery procedure, reusable validation and routing/documentation. Locally verified: disposable Git tools/assertions and direct structural/semantic inspection. Unverified: independent Standards/Spec review and autonomous instruction execution. Acceptance remains outstanding; #28 stays open pending maintainer acceptance and authorized merge. Ready-to-report is an honest partial/blocked report, not whole-delivery acceptance.

Executed structural checks passed: 150 relative Markdown links/anchors across Work On and affected repository documents, 110 in an isolated package copy, Python 3.9 syntax parsing, entry frontmatter/invocation inspection and `git diff --check`. The installed `marked` renderer rendered entry, package overview, recovery and validation; generated headings/tables/prose were inspected directly (without installing tools). Initial bare `require.resolve('marked')` was unavailable; the existing runtime dependency was used instead.

All 11 authored cases received direct static walkthroughs against recovery steps. Those walkthroughs are not executed agent scenarios. Not executed: real failed-worker lifecycle, remote uncertain writes/read-back, native graph API failure, squash equivalence, renewed review, non-Git resume or autonomous integrated multi-ticket/failure trial (#30). Missing independent review remains explicit; no delegation authority was inferred.

Documentation updated: recovery/validation, entry/shared/dispatch/completion pointers, package/repository overviews, design implementation pointer and Unreleased changelog. No domain meaning, ADR/package boundary, project authority, tracker vocabulary/relationships, legacy command or installed copy changed; those homes need no changes. Compatible new functionality has minor release impact; no release or label mutation requested.
