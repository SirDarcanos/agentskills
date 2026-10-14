# Acceptance First: #58 evidence

Scope: [#58](https://github.com/SirDarcanos/agentskills/issues/58), under #48 AC1/AC3/AC6/AC14/AC15 and the accepted #50 design. Input `main`: `3ab5f80efdede0e5a554a47cca9a7d0ae38e9887`; working branch `feat/acceptance-first`, PR target `main`. The PR commit/diff identifies delivered source. This record describes direct author execution and static inspection, not independent review or an autonomous agent trial.

## Eligibility and ownership

Read-only GitHub inspection found #58 open with native parent #48 and sole native blocker #50 closed. PR #75 is merged at `a95a9588ff86304f2390cae8d87df4addf7da1d1`, and design/ADR status records maintainer acceptance. Current main contains that design. The user requested this ticket's implementation. No graph, labels on issues, installed packages or model permissions changed.

The original package owns acceptance examples and implementation increments. Work On gains thin semantic-discovery/caller pointers, not a second loop or early #67 cutover. Package instructions were authored from #48/#50 and repository-owned build/verification conventions; no external package text was imported. The shipped MIT notice names Nicola Mustone.

## Executed fixture

Environment: macOS arm64, Python 3.14.7. Reproduce with:

```sh
python3 acceptance-first/scripts/check-fixture.py
```

The repository run exited 0: five tests passed in 0.317 seconds. Fixture SHA-256: `fb2b055dc0a2b93296b40a6513c2aa29ee09ae773d09638da99f98147f3bd531`.

The synthetic owner agreement is embedded before implementation variants. Five unittest cases exercise:

| Case | Observed evidence |
| --- | --- |
| Workflow red, two increments, green | AC1 initially returns `pending` with no persisted order, failing the agreed receipt assertion. The first implementation saves quantity 2 in real SQLite and returns an accepted receipt; AC1 passes. AC2 then fails because quantity 0 is accepted/persisted. The final increment rejects 0 and -1 without rows; AC1 remains green. |
| Persistence regression sensitivity | Removing save leaves an accepted receipt but no database row; AC1 fails specifically on missing persistence. Restoring implementation passes. |
| Rejection side-effect sensitivity | Persisting before returning rejection fails AC2's empty-row assertion; restoration passes. |
| Ambiguous commitment | AC3 duplicate-request intent is absent; synthetic reporting returns blocked, verified=false, without implementation edits. |
| Material boundary unavailable | AC4 real remote payment has no environment; synthetic reporting returns unverified, verified=false, with no substitute pass or network operation. |

Each case checks protected agreement, storage/harness and unrelated bytes. Meaningful reds are caught expected assertion failures; harness/process errors instead fail the fixture. No private data, user files, live gateway, installation, tracker mutation or model inference is involved. The ambiguity/unavailability cases are reporting-oracle checks, not proof an agent escalates correctly.

## Packaging, inspection and documentation

Executed package checks passed: matching `name`/description frontmatter with no command-only gate; Node/Marked rendering of 11 Markdown files; 70 relative links/anchors; and a complete isolated copy without sibling skills (three Markdown files, four internal links). The isolated fixture exited 0 with five tests passing in 0.272 seconds. `git diff --check` passed. Generated HTML was structurally inspected, not browser-tested. Direct integrated diff inspection found no scope, authority, notice, portable-link or generated/private/local-path leakage issue. The clean input had no unrelated edits, and `CLAUDE.md` retains its `AGENTS.md` symlink. No independent review was requested or performed.

Updated documents: package entry/README/validation, Work On entry/README/build/capability/validation pointers, root listing and one Unreleased Added entry. Existing design/ADR/domain meanings and operating policy remain unchanged because this implements their accepted boundaries, not new ones. Historical trials remain untouched. Release impact is compatible new functionality (minor), not a release or installation.

Against input main, the fixture adds five tests, removes zero and updates zero existing executable tests. Work On's added case and the package workflow table are authored scenarios. CI remains absent/unchanged; no CI timing measurement is claimed.

## Limits and next action

Executed synthetic examples establish local acceptance-first mechanics, not agent adherence, runtime discovery, standalone/composed end-to-end workflow trials, real payment verification, independent Standards/Spec review or cross-runtime certification. Those trials remain with #71/#73 and separately authorized review. No installed-copy migration occurred. Keep #58 open pending maintainer acceptance and merge; merging alone does not deploy, release or update copied skills. Reverting the source change restores prior repository behavior without data migration.
