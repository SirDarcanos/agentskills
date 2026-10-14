# #70 repair — independent Spec review

## Scope and method

- **Agreement:** bounded validation repair supplied in the assignment: preserve Work On invocation/authority, correct shared/extraction expectations, restore skipped coverage, add sensitive regressions, rerun checks and retain initial failures. No public procedure, installation, product-scope or approval-policy change.
- **Snapshot:** `the private frozen repair snapshot`; supplied base and HEAD `bc48d2a3aee1b341da666b908290ca8ec00d359b`, plus dirty repair.
- **Inspection:** actual seven-file diff, new untracked regression file, all supplied repaired raw logs, and authorized contracts. Initial and final working-tree inventories matched.
- **Independence:** assigned read-only Spec context; no other reviewer conclusions inspected. No files changed, scripts executed, delegation, publication or assessments.
- **Limits:** snapshot hashes were inspected, not independently recomputed. Executed results below mean retained author-run evidence, not reviewer execution. Earlier result directories and original-trial sources were intentionally excluded.

## Review

### Correct

| Repair requirement | Source and evidence | Assessment |
|---|---|---|
| Remove stale command-only expectation without broadening authority | `docs/validation/delivery-coverage/check_packages.py:17,67,79–85`; `work-on/SKILL.md:10–12`; `work-on/references/validation.md:9` | Shared metadata expectation now matches current Work On. New assertions retain explicit delivery, bounded authorized assignment and investigation-only no-fix-authority wording. Actual unchanged entry preserves the consequential permission exclusions. |
| Repair all three extraction callers | `docs/validation/shape-work/check.py:27–35`; `docs/validation/write-spec/check.py:30–35`; `docs/validation/write-tickets/check.py:23–28` | Each now expects metadata invocation and still checks source and isolated Work On copies. No Work On skip remains in these callers. |
| Reinstate runner coverage | `docs/validation/discovery-spec-tickets/check.py:30–31,55–57` | Runner adds regression/shared-check commands and restores its direct Work On check. Shared checker separately exercises source and isolated copies (`check_packages.py:101–107`). |
| Preserve procedures and policy | Actual diff; `work-on/SKILL.md:10–12` | Changes are validation, regressions and evidence documentation only. No public skill entry/procedure or approval-policy edit appears. |
| Retain historical failures | Actual diff; runner’s new-directory behavior at `check.py:21` | No historical evidence deletion/modification appears in the repair diff. Documentation distinguishes historical failures from current repaired results. Historical contents themselves were not inspected. |

### Regression sensitivity

`docs/validation/delivery-coverage/test_package_invocation.py:33–38` verifies each mutation target occurs exactly once, changes a disposable copy and requires rejection. The positive baseline helps distinguish intentional mutation sensitivity from a generally broken checker.

| Case | Source | Protected failure |
|---|---|---|
| Positive current package | Lines 40–42 | Current isolated package passes; package configuration is not command-only. |
| Negative metadata | Lines 44–45 | Reinserting `disable-model-invocation: true` fails. |
| Negative user route | Lines 47–48 | Replacing explicit delivery with “any user request” fails. |
| Negative assignment route | Lines 50–51 | Replacing bounded authorization with “any assignment” fails. |
| Negative investigation authority | Lines 53–55 | Changing “no fix authority” to “fix authority” fails. |

These are credible **structural mutation tests**, not invocation simulations or proof that an agent obeys the instructions. Their module documentation states that limit; `work-on/references/single-change-validation.md:26` makes the same distinction.

### Raw rerun evidence

All locators below are under `docs/validation/discovery-spec-tickets/results/checks-repaired/`.

- `checks.json:3–40` records exit 0 for all eight subprocess commands.
- `shape-extraction.txt`, `spec-extraction.txt`, `ticket-extraction.txt` each contain source and isolated Work On passes; Shape also records three baseline tests passing.
- `package-invocation-tests.txt` records five tests, `OK`, without skips.
- `shared-package-checks.txt:1–2` records both Work On copies passing; lines 29–31 record 13 snapshot tests passing.
- The only recorded skips are isolated Setup companion-presence tests (`shared-package-checks.txt:50–58`). Source Setup records all 22 passing in `setup-tests.txt`; these are not residual skipped Work On coverage.
- `ticket-tests.txt` records ten passing tests; `helper-help.txt` contains successful CLI help.
- `checks.json:43–49` records the inline structural checks and whitespace check passing; `git-diff.txt` is empty.

The changed checks and supplied raw results support correction of the stale failures. Passing totals alone were not used to establish contract preservation.

### Finding: P2 — repaired replay claim lacks supplied raw support

**Location:** `docs/validation/discovery-spec-tickets/README.md:54`; `docs/validation/discovery-spec-tickets/walkthrough.md:40`.

The changed documentation groups fixture replay with current repaired results, and the walkthrough says raw corrected results are retained in `results/checks-repaired/`. However:

- The runner’s complete command list (`check.py:23–32`) does not execute `run_fixture.py`.
- `results/checks-repaired/checks.json` contains no replay outcome.
- The supplied repaired artifacts contain no replay log or replay input/output identity.

This does **not** establish that replay failed or was never run. It establishes that the claimed current replay is not substantiated by the authorized repair evidence.

**Smallest correction:** distinguish unchanged historical fixture evidence from the repaired checker rerun, or supply a separately inspectable replay command/result and input identity. Nonblocking for the demonstrated checker correction; the replay verification claim remains partial.

### Documentation and evidence limits

The no-changelog explanation is consistent with repository-local validation maintenance and the absence of public behavior changes. Initial failure history is not treated as an unresolved current exception.

Original-trial acceptance, live APIs, installed behavior, autonomous instruction-following and historical replay fidelity were not reviewed. The repaired logs also lack execution environment/input fingerprints tying their generation cryptographically to this frozen snapshot; source/log consistency was inspected, but independent freshness certification remains the caller’s responsibility.

- **Fixed:** none; read-only review.
- **Blocking findings:** none established within the bounded repair.
- **Merge verdict: OK with notes.**

The checker repair is supported by inspected source and retained executable evidence. Review of the additional current replay claim is **partial** pending clarification or raw evidence; this report does not accept the full original trial or authorize merge.