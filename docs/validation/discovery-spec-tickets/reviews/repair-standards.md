# Standards review — #70 validation repair

## Scope and authority

Reviewed the dirty repair against supplied base/HEAD `bc48d2a3aee1b341da666b908290ca8ec00d359b` and frozen manifest `the private frozen repair snapshot`.

Inspected all seven tracked diffs, the new invocation test, every `results/checks-repaired/` artifact, and the allowed project, Work On and Review Delivery contracts. No files modified, scripts executed, assessments called, publishing performed or delegation initiated. Earlier results and reviewer reports were not inspected.

## Review

- **Correct — current invocation contract preserved.** `work-on/SKILL.md:10–12` requires explicit delivery or a bounded authorized assignment and denies investigation-only fix authority. The shared checker now matches those boundaries and removes the obsolete command-only expectation (`docs/validation/delivery-coverage/check_packages.py:17,67,79–85`). No public skill-procedure or approval-policy changes appear in the diff.

- **Correct — stale extraction checks repaired minimally.** Only the Work On metadata expectation changes in `docs/validation/shape-work/check.py:27`, `write-spec/check.py:30` and `write-tickets/check.py:23`. Existing source and isolated-copy checks remain intact.

- **Correct — skipped coverage reinstated.** `docs/validation/discovery-spec-tickets/check.py:30–31,57` adds invocation regressions and the full shared checker, and restores the direct Work On check. Command failures remain individually recorded and contribute to the runner’s unsuccessful exit.

- **Correct — sensitive structural regressions added.** `docs/validation/delivery-coverage/test_package_invocation.py:21–55` checks a disposable, non-sibling package copy and rejects command-only metadata, unrestricted request/assignment substitutions and investigation-only fix authority. Mutations are restricted to temporary copies. These tests protect structural assertions, not agent compliance.

- **Correct — scope and documentation remain bounded.** The changed README and walkthrough distinguish historical failures from repaired results. The actual diff contains no deletion or alteration of initial evidence. The no-changelog rationale at `docs/validation/discovery-spec-tickets/README.md:58` fits workflow policy: repository-local validation changes, without public behavior or installation changes.

**No issues found.**

## Raw evidence coverage

Inspected evidence, rather than relying on README totals:

| Artifact under `results/checks-repaired/` | Observed result |
|---|---|
| `checks.json` | All recorded exits are zero |
| `shape-extraction.txt` | Source/isolated checks and 3 baseline tests pass |
| `spec-extraction.txt`, `ticket-extraction.txt` | Source/isolated checks pass |
| `package-invocation-tests.txt` | 5 tests pass |
| `ticket-tests.txt`, `setup-tests.txt` | 10 and 22 tests pass |
| `shared-package-checks.txt` | Package checks, 13 snapshot tests and isolated Setup suite pass; 2 companion-presence tests skip |
| `helper-help.txt` | Read-only/default and explicit `--apply` interface shown |
| `git-diff.txt` | Empty output, consistent with recorded successful whitespace check |

## Limits and missing evidence

- This review was **static inspection plus examination of retained execution logs**; no checks were independently rerun.
- The repair bundle contains no fixture-replay result. Replay, Markdown-rendering and original digest-verification claims in README line 54 were not independently verified or used to justify this repair verdict. Broader original-trial acceptance remains outside scope.
- Supplied snapshot fingerprints were read, not independently recomputed. Initial and final working-tree inventories match; the caller still owns final full fingerprint/freshness verification.
- Literal text guards do not prove equivalent authorization behavior across every possible wording change or runtime.
- This is the independent **Standards** result only, not Spec acceptance, merge approval or full #70/#48 acceptance.

**Merge verdict: OK with notes** for the bounded repair. Integrated acceptance remains subject to the separate Spec result and final freshness verification.