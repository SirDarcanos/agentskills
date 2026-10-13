# Independent-review trial attempt for #24

**Historical first-attempt outcome: blocked at reviewer startup, not a successful independent review.** A later maintainer-requested retry after the runtime update completed the bounded trial; see [current results](trial-results.md). The maintainer authorized the two-reviewer synthetic trial after merged [PR #39](https://github.com/SirDarcanos/agentskills/pull/39). The lead applied the shipped procedure's unavailable-capability gate to an actual runtime failure. No reviewer read sources or produced findings; lead inspection is not substituted for either axis.

## Scope and reproduction

Procedure revision: `95c42ef05baff60e1747f6d6ab2aac742e5565fe` (the merged package). This follow-up adds only evidence and a reusable fixture generator; it does not change the review/runtime contracts or install anything.

From the repository root, with Python and Git available:

```bash
python3 -B review-delivery/scripts/trial_fixture.py
```

The generator reuses the existing offline test fixture and prints a retained temporary target/evidence directory. It never launches agents. The caller owns its retention/cleanup; it is intentionally not deleted on a failed review. `metadata.json` identifies the base, delivered HEAD, exact included paths, protected sentinel hashes and procedure digests. `evidence/` retains separate committed/staged/unstaged patches, the initial scope, index/status/history observations, and separately supplied execution observations. The copied procedure includes only the unchanged entry point and scope/report references: authored validation/test expectations are excluded from reviewer context.

Actual fixture identity from this attempt:

- Fixed comparison base: `cef787b6707038b7806a4eacbca3a6ca691e5441`.
- Delivered HEAD: `b7682d1c55d12e35e8e742a0765ded20ca3a9d24`; branch `main` in the synthetic repository.
- Included: `formatter.py`, `committed.txt`, `staged.txt`, `duplicate.py`, `deleted.txt`, `old name.txt`, `new name.txt`, `note-link`; supporting `AGENTS.md` and `brief.md`.
- Protected/excluded: unrelated `protected.txt` (staged and unstaged) and `private-note.txt` (untracked); no disclosure of their content to reviewers. Git internals and test expectations were excluded.
- Content-manifest SHA-256: `9307635b977d2030862fad9a258cc41ab892a8c3d0cec40c3ae802a6869969e8`.
- Procedure SHA-256: entry `9bf8b7436ba217d1de16eee49da37994375e60312f5862e8cf132865183d15c2`; scope `0c6293e042630a9cf264a917a0707e07fc744137c271a6a07b4ec92e75887f47`; report `c4299ac82e966571f30035eff1fd4b7c51a374fb09c2b43924642aced03a43d3`.

Synthetic agreement F1 preserves heading case/words while trimming outer whitespace; F2 keeps one behavior owner and preserves unrelated work. Target standard S1 names the formatter as sole normalization owner. The known dirty/untracked findings remain the ones described in [validation](validation.md#executable-fixture-scope); reviewers were not told the expected findings. Lead execution observed baseline `Hello world` versus delivered `HELLO WORLD` for input `'  Hello world  '`, separately labeled direct execution.

## Actual runtime attempt

On 2026-10-13, one async workflow submitted two distinct `reviewer` contexts with `context: fresh`, one Standards and one Spec, identical pinned sources and raw evidence. The builtin reviewer has inspection tools only, no shell/write tools, inherits no global context or skills, and neither assignment receives the other's conclusions. Each assignment had a 15-minute deadline and 70-call tool limit; the outer workflow had a 16-minute bound. Two slots maximum; no nested delegation.

The planned phase boundary asked each reviewer to send its initial report and wait for the lead to finish the unchanged-scope check before the lead would mutate the untracked file. That boundary was never reached.

| Execution pointer | Actual outcome |
| --- | --- |
| Workflow `c13f5708-2584-42df-810e-e7a314f716ae` | Terminal with two failed children; zero reviewer token/tool execution evidence, no report artifacts or resumable sessions. A completed workflow container is not successful review. |
| Standards startup `622fe788-7238-4633-a831-8f3266879ff7` | Failed before child session started; no Standards findings. |
| Spec startup `bae97da9-aa25-4012-ab09-3f66a9ea1208` | Failed before child session started; no Spec findings. |

Both startup errors reported: **background children require the host npm package `@earendil-works/pi-coding-agent` with its dependencies; it does not provide `@earendil-works/chord`, `@earendil-works/chord/context`.** This is observed launcher evidence, not a diagnosed root cause or an instruction to install a particular package.

The lead inspected the terminal workflow state and failure artifacts, confirmed zero active async capacity and no resumable reviewer sessions, and stopped the delegated route. No alternate runner, foreground fallback, repeated launch, runtime repair, model assessment, acceptance claim or fabricated axis report was used. Local raw failure artifacts retain the workflow IDs under the runtime's retention policy; workstation paths/private parent-session metadata are intentionally not copied into this public record.

## Verification status

| Check/claim | Status and actual evidence |
| --- | --- |
| Pinned dirty scope and actual defect observability | **Executed:** initial scoped capture matched immediately before submission; direct public-interface observation above. This is not agent finding detection. |
| Preserve source/protected state on infrastructure failure | **Executed:** after both failed submissions, assertions confirmed identical scope fingerprints, complete status/index/history, protected bytes and copied procedure digests. Fixture retained unchanged. |
| Offline validation support | **Executed:** `python3 -B review-delivery/scripts/test_snapshot.py` exited 0 (11 checks); a separately generated fixture matched its initial capture and excluded validation/test expectations from the reviewer packet. Python 3.14.7 / Git 2.54.0. |
| Document checks | **Executed:** 13 package-relative links/anchors resolved; `git diff --cached --check` passed before commit. Direct author inspection only; HTML rendering and independent review of this follow-up are not executed. |
| Unavailable independent-review capability | **Executed lead gate:** real startup failures caused an explicit acceptance blocker; self-review was not called independent. No child-level blocker interpretation was executed because no child started. |
| Standards/Spec finding detection and separate actionable reports | **Blocked / not run:** no reviewer session. Permission is now granted, but capability is unavailable. |
| Change after initial reports; stale-review disposition | **Not run:** no initial reports exist. The lead did not mutate the preserved fixture; existing offline helper drift tests remain separate evidence. |
| Successful fresh review, renewed review, timeout and non-Git branches | **Not run:** this attempt establishes none of those behaviors or cross-runtime certification. |

## Historical next action and documentation impact

The recommendation below describes the first attempt's blocked state; the later update/retry is recorded separately in the current results.

Keep #24 open. Recommend a bounded runtime diagnosis/repair under separate approval, or an explicitly approved compatible execution-mode alternative. After capability is restored, repin and rerun the initial Standards/Spec trial in fresh contexts, then execute the post-report drift phase and record actual findings/outcomes. Do not resume nonexistent child sessions or treat this failure record as satisfying successful review acceptance.

[Validation](validation.md) links this partial execution record. The fixture generator is validation support, not a new review behavior or installation contract, so no additional changelog entry or release-impact label is needed. Domain vocabulary, ADR decisions, lead completion/repair integration, native tracker relationships, installed skills and runtime configuration remain unchanged. No merge, release or issue closure is implied.
