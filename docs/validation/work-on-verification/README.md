# #25 integrated-verification evidence

This repository-local record is not part of the installable Work On package. The runtime procedure is [integrated verification](../../../work-on/references/verification.md); its [validation reference](../../../work-on/references/verification-validation.md) separates authored cases from execution.

## Execution boundary and reproduction

The implementation author ran [exercise.py](exercise.py) directly and inspected its sources, actual diffs, assertions and results against the procedure. This is a disposable synthetic tool walkthrough, **not an autonomous agent run, independent review or end-to-end delivery trial**. No delegation/model assessment, install, live tracker mutation, global skill change, release or real private data was involved. The script creates and removes only its own temporary Git repository; unexpected subprocess results fail the exercise.

From the repository root, with Python 3.9+ and Git:

```sh
python3 -B docs/validation/work-on-verification/exercise.py
```

Actual execution used Python 3.14.7 and Git. The outer command exited 0 because the expected failures and freshness assertions occurred; this does **not** mean the synthetic delivery passed acceptance. Commit IDs vary per rerun; the source recreates the exact contents and prints its complete authorized file/mode manifest, three patch hashes and check output. Raw temporary execution logs were inspected locally, not committed with workstation paths.

## Agreement and inspected state

Fixture agreement: **V1** preserve the public name; **V2** omit the private token; **V3** demonstrate recovery using a required synthetic recovery driver. Scope is the service and its checks; the deliberately broken legacy arithmetic test is excluded from the behavior change but inspected as baseline evidence. The privacy failure is a material domain/access-disclosure violation. Actual recovery is material to V3; destructive behavior is inapplicable to this pure record projection. Recovery failure-path evidence remains unavailable, not inferred from the privacy check.

The fixture's implementer return says “Done: all acceptance criteria pass; unrelated suite is green.” The sole delivery change replaces `return {'name': record['name']}` with `return dict(record)`. Both baseline and delivered revisions keep identical agreement and assertions. Tests run directly in the delivered worktree, not on a worker branch. One direct owner held scoped writes during checks; no active workers or repair episode existed.

Observed snapshot:

- Base: `b1624ae3d4fb8b67383302d2dfc50edaec7a64f2`; delivered HEAD: `e04277d83ef3779ec982abe73f17281426ede600`; branch: `main` in the isolated fixture, not this repository.
- Included files: `service.py` (change), `test_access.py`, `test_legacy.py`, `test_unrelated.py`, `agreement.md`, `implementer-return.md` and untracked `delivery-note.md` (support). All were ordinary mode 0644 files; no external/private scope.
- Base→HEAD patch SHA-256: `705f9d2392e02bbd2df5f6fea3a049a37f579c679ccc71d011d3fa9ebe5a39ac`. Staged and unstaged patches were empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` each.
- Agreement SHA-256: `bd53276f9404b71968f0aef880a2e0adcdaa6ea53cf220bc57c6687ac085a287`; service SHA-256: `3e541254ca625fe95eac870993ee8f9899b62fa1ac9a0e714996bb1d8a5f407f`; access assertions SHA-256: `a15362d612bdf5f6ebbaa31b283ca2fef65fdac60823c608b509b08fece7ee33`.
- Included untracked note SHA-256: `9ea970ebc8ed3331af3506631312907842dff24a1efca42a94323e5ff2bab157`. Before/after checks compared the complete file manifest, scoped status, commits and layer hashes successfully. Changing this supporting input afterward made the comparison fail as expected; old evidence remains for the prior snapshot only.

## Actual checks and lead disposition

Commands below ran with the same Python executable/environment in the fixture. Each row retains its state and cause rather than a blanket suite verdict.

| Command / observation | Baseline | Integrated | Meaning |
| --- | --- | --- | --- |
| `python3 -B -m unittest -v test_access` | Exit 0; name preservation and private-field omission passed | Exit 1; name passed, omission failed: `token` unexpectedly present | V1 verified at the checked snapshot; V2 blocked by a demonstrated new regression. Existing public-interface assertion detects the precise leak without a new-test quota. |
| `python3 -B -m unittest -v test_legacy` | Exit 1: `1 != 2` | Exit 1: identical assertion/cause | Evidenced pre-existing defect, outside the scoped behavior agreement; not silently called green or waived for another acceptance criterion. |
| `python3 -B -m unittest -v test_unrelated` | Not run | Exit 0: `2 + 2 == 4` | No evidence for V1–V3; its pass cannot satisfy privacy or recovery acceptance. |
| Inspect required recovery driver | Not run | `synthetic-recovery-driver.py` absent; recovery check **not run** | V3 blocked by unavailable material check, with no claim of a recovery pass or demonstrated regression sensitivity. |
| Before/after snapshot equality assertion | Inapplicable | Passed after checks; deliberate subsequent note edit detected drift | Evidence was current at completion of checks, then became stale for the changed supporting-input state. |

Following verification steps 1–4, the author rejected the unsupported “done.” Initial handoff: V1 verified, V2/V3 blocked; implementation present but unaccepted. After deliberate drift, retained results identify the old snapshot; renewed claims for the changed state require repinning and affected re-verification. No repairs or final acceptance were attempted.

Recommended bounded next actions: repair the projection under a separate repair checkpoint and rerun the privacy assertion; obtain the authorized recovery driver/environment and execute V3, or request that the agreement owner explicitly revise V3 with its consequence. Until approval, V3 remains required. A green unrelated check supplies neither missing evidence. Independent Standards/Spec review and the completion gate remain separate later requirements.

## Repository checks

- `git diff --check`: exit 0.
- Python relative Markdown link/anchor validation: 98 targets passed across the entire Work On package and changed repository documents; 61 passed again after copying only `work-on` to a temporary directory.
- Frontmatter/body inspection: `name: work-on`, description and `disable-model-invocation: true` remain intact; explicit invocation is still required.
- Direct source review covered headings/tables, criterion mapping, scope boundaries and the integrated diff for credentials, private data, generated artifacts and workstation paths. No Markdown renderer was available; rendered-output inspection was not performed and no renderer was installed.
- Python 3.9 syntax parsing of the fixture: passed; actual execution used 3.14.7, not 3.9.
- Fixture rerun after adding actual diff output: exit 0, same assertions, file fingerprints and patch hashes; new temporary base `688f69d28c4a317d4a1c242b96664c5a5aacde6f` and HEAD `de4e6a36bc3fbef7230d1451e18109037359f933`.

Repository preflight began on clean `main` at `3868e94`; fetched `origin/main` matched it. #25's native blocker read returned #23, and its reverse relationship included #25. #23's accepted direct-build output is present in main through merged PR #38 (`c3d4dcb698b2ae4ebd4d0affd1dbaea7da89b5cc`). Implementation uses `feat/integrated-verification`, base/PR target `main`; no unrelated work or existing PR was present at entry. The PR commit identifies this procedure/fixture revision; the synthetic commit IDs above identify only the exercised target.

## Documentation and limits

Runtime/overview/design pointers and the Unreleased changelog were updated for #25; the reusable validation reference links from the package and this record remains repository-local. Shared policies, domain meanings and the accepted package boundary did not change, so no glossary, ADR, authority or graph update was needed. Release impact is compatible functionality (minor); no publication or global installation is implied. The synthetic target has no separate documentation/changelog convention requiring edits.

The script checks actual fixture results and snapshot drift, not whether a future agent follows the prose. Missing-baseline classification, staged-versus-unstaged reversal, identical-content commits, destructive effects and full persistence/recovery remain authored branches rather than executed trials here. The fixture fingerprint function handles only its known ordinary top-level files; it is not a general snapshot helper and cannot replace the companion's production scope contract. #29/#30 still own integrated workflow trials. No independent review of this implementation was performed.
