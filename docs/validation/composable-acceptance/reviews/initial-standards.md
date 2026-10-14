# Standards review — #73

## Review

- **Correct:** The publication distinguishes structural checks, offline fixtures, historical agent actions and unverified live behavior. AC16 remains explicitly pending #74; whole-#48 completion is not claimed (`docs/validation/composable-acceptance/README.md:61–96`).
- **Correct:** All 13 new package-local LICENSE files were read directly and preserve the complete root MIT notice naming Nicola Mustone. TDD’s existing notice also names Matt Pocock (`tdd/LICENSE:3–4`).
- **Correct:** Stay Positive’s revised guidance preserves its conditional companion behavior without requiring sibling installation (`stay-positive/README.md:17`; `stay-positive/SKILL.md:38–40`).
- **Correct:** The collector reuses existing link validation and explicit offline commands rather than introducing another delivery procedure owner (`check_packages.py:17–34`). The Pi checker disables default discovery roots and accurately limits its claims to loader behavior.
- **Fixed:** None; review was read-only.

## Finding S73-01 — P1, blocking: package checks inherit external Git routing

**Location:** `docs/validation/composable-acceptance/check_packages.py:121–124`

The new package collector launches its allowlisted subprocesses without an isolated environment. Its `review-delivery` job executes `scripts/test_snapshot.py`, whose Git helper also inherits the environment (`review-delivery/scripts/test_snapshot.py:53–55`). That suite initializes repositories, stages files and commits (`:21–35`).

Consequently, an inherited absolute `GIT_INDEX_FILE` can redirect fixture staging into an index outside the disposable workspace. Inherited Git configuration or template settings can also cause fixture commits to execute external hooks. Changing `cwd` does not confine these effects. The later source-manifest comparison cannot detect mutation of an external index or hook side effects.

This contradicts the disposable-only execution claim at `docs/validation/composable-acceptance/README.md:28` and the project’s protection of authorized effects and destructive-operation boundaries (`docs/agents/workflow.md:13,39`). It is made reachable by this diff’s new aggregate package-check command.

**Smallest correction:**

1. Pass a sanitized environment to package subprocesses: remove inherited `GIT_*` routing/configuration variables and disable global/system Git configuration, following the existing approach in `run_checks.py:36–37`.
2. Ensure external hooks/templates cannot activate in fixture repositories.
3. Add a collector-level regression using an owned sacrificial external repository/index and hook sentinel. Verify that inherited routing/configuration cannot modify them.
4. Refresh affected receipts after the repair.

**Verification status:** Source-established execution path; not executed during this review. The retained passing receipt does not exercise this collector-level hostile-environment case.

- **Merge verdict: BLOCK** — technical review recommendation for S73-01 only, not an acceptance or merge authorization.

## Inspected files and criteria

Inspected:

- Frozen diff and changed-file inventory; selected identities from the 591-path snapshot.
- #73/#48 archived inputs; project, workflow, tracker and label standards.
- Accepted composable design, inventory, validation and ADR 0002.
- All new collector/checker source files and their regression tests.
- New acceptance README, changed publication text, all 13 new LICENSE files, root/TDD notices and Stay Positive’s complete entry.
- Selected deciding fixture code, migration runbook, mock authorization tests, retained-evidence checker and current command receipts.

The five new checker/document source hashes in `results/checks.json:727–733` match their supplied snapshot identities. Receipt inspection supports the reported selected command outcomes; it does not independently reproduce them.

## Limitations and completeness

This was a bounded Standards review, not exhaustive AC1–AC16 acceptance validation. I did not inspect every package entry, every historical source artifact or every retained result. Historical independent verdicts and excluded retrospective reports were not used as evidence.

No writes, shell commands, tests, network operations, assessments or delegation were performed. Actual installed discovery, migration, live tracker behavior and arbitrary agent adherence remain unverified. Review is complete for the inspected Standards seams; the safety finding requires correction and executable regression evidence.