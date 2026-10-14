# Installed-skill migration preparation: #69

Evidence for [#69](https://github.com/SirDarcanos/agentskills/issues/69), under [#48](https://github.com/SirDarcanos/agentskills/issues/48)'s AC14–AC16 and the [accepted design](../../design/composable-delivery.md). The [migration runbook](../../agents/installed-skill-migration.md) owns the operational procedure. This directory owns its offline fixture and evidence, not a second operational implementation.

## Scope and eligibility

Input `origin/main`: `d90f0e709157b82788bd11288ac1bcc0413bd157`; clean preflight, branch `test/installed-skill-migration`, PR target `main`. A read-only native blocker query for #69 returned #50 closed. Acceptance is recorded in the design; PR #75 merged design commit `a95a9588ff86304f2390cae8d87df4addf7da1d1` on 2026-10-14. This establishes accepted integration, not just closure. The user approved the documentation outline before drafting.

Only repository documentation and synthetic validation are in scope. No real installed inventory, removal, activation, registration, discovery refresh, model call or service operation ran. Fixture approval is authored test input; it is not maintainer approval to migrate actual targets. #74 remains responsible for private inventory, exact-target approval and real runtime/installer read-back after #73 acceptance.

## What ran

Direct Python disk tests on macOS (`Darwin`), Python 3.14.7:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 docs/validation/installed-skill-migration/test_fixture.py
```

[Test driver](test_fixture.py) has no target/output path arguments or production installer integration. It creates a fresh owned temporary root for each case, then audits the file mutation events used by the fixture against that root. Unlink/rename check link locations without following leaf targets; writes resolve targets. Dir-fd mutations and subprocesses are refused. Bootstrap creates the temporary root before enabling the guard; all subsequent fixture writes and cleanup are inside it. The explicit outside-path and symlink-write attempts are rejected before mutation. This is a guard for these inspectable Python operations, not an OS sandbox against arbitrary native code or a concurrent hostile process.

The model persists a private JSON record and ordered intent/outcome operations, immutable old package manifest, package backup, staged new package and a restored rehearsal copy. Packages contain entry points, locally modified references, executable scripts, binary assets, hidden additions, empty directories and an internal symlink. A separate registration JSON models installation metadata. Discovery enumerates two synthetic roots; the companion is deliberately in the other root, not beside the replacement. No runtime API is mocked as though it were live.

The [initial run](results/initial-tests.txt) failed (14 test methods, 1 failure and 16 errors including subtests): the audit guard read `os.utime`'s nanoseconds field as a dir-fd argument. The guard was corrected to use the event-specific argument positions and include extended-attribute mutations used by `shutil`. No outside write was observed. The [rerun](results/tests.txt) passed **14 test methods**, including six interruption-boundary subtests, with 4,441 audited mutations in 0.475 seconds. Runtime is local test elapsed time, not a CI measurement. Initial logs substitute `<repository>` and `<python-stdlib>` for machine-specific prefixes; no real installation paths or contents are retained.

## Acceptance and failure evidence

| Requirement | Executed fixture evidence | Limit |
| --- | --- | --- |
| AC14 procedure/documentation | Runbook specifies standalone/handoff inputs, exact authority, private records, completion/blocked states; root README links it. | Document inspection, not real execution of every runtime-specific step. |
| AC16 full package backup/restore | `test_full_package_restore` compares complete path/type/mode/byte/link manifests and registration metadata after activation and rollback; retained backup verified. | POSIX modes/bytes/links, not certification of ownership, ACLs or xattrs. |
| Same-name replacement | `test_same_name_new_source` proves `tdd` resolves to different intended content, not just the same catalog name. | Synthetic directory discovery. |
| Shared-source ownership | `test_shared_symlink_retirement_and_restore` retires only the runtime link, preserves source and another consumer, then restores the raw relative link and old contents. | Local synthetic source; external link chains remain real-inventory obligations. |
| Duplicates | `test_duplicate_discovery_blocks_success` detects the unapproved second-root installation, preserves it and reports incomplete rollback discovery. | Two modeled roots, no platform precedence assumptions. |
| Invalid backups/replacements | Backup corruption, missing staged reference and missing companion each block retirement, leaving the old copy intact. | Staged validation is manifest/entry/companion presence; full semantic/frontmatter/link checks are required by runbook, not simulated certification. |
| Activation failure | Injected refresh failure, reopened disk record and rollback restore old content/registration and discovery, retain backup. | Real refresh mechanism unrun. |
| Resume | Six before/after retirement, copy activation and registration intent boundaries reopen the record, reconcile actual disk state, finish migration and preserve original backup; backing up replacement as old is rejected. | Completed-operation boundary interruption, not torn filesystem copy/power-loss durability testing. Partial copy would be conflicting/unknown, not blindly deleted. |
| Conflict/recovery protection | Intervening replacement edit, changed shared source and unknown retirement outcome block recovery/resume without overwriting conflicts; shared source and backup retained. | Rollback interruption itself and disk-full recovery remain unrun. |
| Approval/preservation | Missing exact approval leaves target untouched; every case compares unrelated and companion-root manifests in teardown. | Synthetic approval only. |
| AC15 owned temporary writes | Every used mutation audited; outside-path and link-target writes rejected. | No arbitrary-code sandbox or hostile concurrency claim. |

## Reproduce and remaining checks

Run the command above from the repository root with Python 3.9+ (only 3.14.7 executed). Use a normal private OS temporary directory outside public source and active discovery roots; do not point `TMPDIR` into a skill root. No dependencies, network or retained real data are needed. Each owned fixture directory is deleted after testing; retained public logs contain only synthetic test names/results and sanitized tracebacks. Replaying these tests does not repeat an agent walkthrough or migrate installed packages.

Direct source review and document/link checks are recorded in delivery evidence. Independent review results, if obtained, are separate from these executed tests. Package frontmatter/isolated-package checks are inapplicable: no skill package changed or was introduced. The fixture is deliberately not shipped as a local migration helper: runtime/installer effects differ and must be inspected under exact approval, so a generic mutation CLI would add unjustified risk and scope.

Documentation disposition: added the operational runbook and this evidence home; root README now points to them. Historical design/inventory/ADR evidence, skill entry points, notices, CONTEXT and policy remain unchanged. No changelog entry: this preparation adds repository documentation/tests, not released skill behavior, a production migration helper or new installation authority. Reverting removes repository guidance/evidence only; it cannot restore future installed changes. The runbook requires separate full local restoration for those changes.

Test accounting against input main: one new test file, 14 unittest methods (plus six boundary subtests), zero removed/updated/moved test files. No CI jobs/configuration change; `.github/workflows` is absent and external automation/timing is unknown. Merging neither deploys, releases nor installs anything. Keep #69 open until maintainer acceptance and merge; no fixture success establishes #74 or whole-#48 completion.
