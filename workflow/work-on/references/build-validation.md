# Direct-build validation

Use when changing or validating [direct build](build.md). Follow [entry validation](validation.md#reproducible-static-checks) for frontmatter, rendered Markdown, relative links/anchors, isolated package copying and diff hygiene. These are agent instructions, not an executable build controller. This reference separates authored cases from an executed local exercise.

## Authored cases

Walk each case through the actual procedure and record gaps with step references. These expected outcomes are **not executed behavioral evidence**.

| Case | Starting facts | Expected behavior |
| --- | --- | --- |
| Direct existing agreement | Approved small fix, actionable plan, compatible preflight, relevant public-interface checks | Steps 1–3 reuse the agreement, assign one owner, preflight before writes and implement directly. No scheduler, mandatory integration branch or hidden legacy command. |
| Ownership conflict | Partial patch has an active or unknown competing writer; unrelated staged/unstaged/untracked work exists | Step 1 protects work and blocks conflicting writes until ownership is reconciled. No stash, reset, broad staging or implicit transfer. |
| Predecessor unaccepted | Native blocker is closed but required merge/acceptance evidence is absent | Step 1 blocks dependent building and names missing evidence. Readiness labels cannot substitute. |
| Preflight absent or ambiguous | Approved Git change, unavailable compatible preflight | Step 1 blocks Git preparation; inspection/planning may continue. No local duplicate algorithm or automatic installation. Non-Git targets instead record preflight inapplicable and a manifest. |
| Selected TDD companion | Test-first method selected, current agreement/check mapping and preflight result | Step 2 discovers and reads compatible `tdd`, executes its bounded procedure in context, inspects red–green–refactor/local evidence, and retains lead method choice and delivery gates. Missing/ambiguous or legacy-incompatible TDD blocks that route; no duplicated loop or automatic installation. |
| Selected Prototype companion | Approved bounded experimental question, unresolved production design, current evidence and safe preflight | Steps 1–3 treat experiment readiness separately from production build readiness; discover/read compatible `prototype`, inspect bounded observations, limitations and owned-artifact disposition, then return learning to readiness/method selection. No production promotion or automatic acceptance. Missing/incompatible Prototype blocks this route. |
| Selected Characterize companion | Risky legacy change, bounded capture scope, current evidence/preflight | Steps 2–3 discover/read compatible `characterize`, inspect intended/unknown/defect dispositions, baseline provenance, sensitivity and nondeterminism limits, then return protection to readiness/method selection before production changes. The lead selects the next method; missing/incompatible capture blocks the dependent route. |
| Selected Acceptance First companion | Agreed cross-component workflow, acceptance IDs and current evidence/preflight | Steps 2–3 discover/read compatible `acceptance-first`, inspect executable observable examples, meaningful baseline and checked increments, then return criterion-level local evidence for lead verification/review. Ambiguous expectations and missing material environments stay blocked/unverified. Missing/incompatible helper blocks the selected route. |
| Selected Build and Check companion | Bounded implementation-first change, current agreement/check mapping/preflight | Steps 2–3 discover/read compatible `build-and-check`, inspect immediate increment/check order and actual results, then return local evidence for verification/review. Existing adequate coverage is reused; non-code increments receive proportionate checks; failed/material unrun checks stop dependent progress. Missing/incompatible helper blocks the selected route. |
| Relevant existing coverage | Mechanical text correction already covered by focused text/link checks | Step 2 justifies those checks from failure risks without mandatory TDD or a new-test quota. Binding target TDD/check policy still applies. |
| Baseline and unavailable check | Existing unrelated failure; material access check cannot run | Steps 2–4 retain exact failure/not-run evidence and reasons. Safe progress may continue; no passing-baseline or acceptance claim, installation or blanket suite. |
| Green refactor | Routine implementation reveals a simpler existing helper under the same contract | Step 3 refactors with relevant checks green and updates the technical plan. A changed product guarantee or meaningful risk instead pauses affected writes for approval. |
| Persistent findings | Checkpoint already spent two correction cycles, material failure remains | Step 3 applies shared limits and returns preserved artifacts, diagnosis and reassessment; resume or renaming does not reset budget. |
| Truthful handoff | Local checks pass but integrated verification/review has not run | Step 4 identifies dirty delivered state, commands, acceptance/risk mapping and documentation impact. Return implemented-but-unaccepted; keep issue open under target policy. |

## Executed synthetic local exercise

**Boundary:** the implementation author executed one-owner development in a temporary Git fixture using the steps above and the maintained preflight contract. This was a direct tool walkthrough, not a delegated agent, independent review, autonomous routing test or integrated acceptance trial. No live tracker mutations, installs, model services or global skill changes were involved. The synthetic fixture owner explicitly authorized its branch switch with the unrelated sentinel work retained in place; this is not permission to switch an unknown user's dirty repository without the preflight's required clarification.

**Agreement F1:** normalize whitespace in a heading while preserving words; F2: whitespace-only input returns an empty heading; F3: preserve unrelated work. Scope: `formatter.py` and `test_formatter.py`. Exclusions: Unicode normalization, non-string input policy, publication, deployment and final acceptance. The sole formatter owns normalization; its existing public-interface test covers trimming and word preservation. One owner suffices. No domain/ADR change is needed.

Reproduce the fixture with Python and Git only:

1. Initialize a temporary repository on `main`, with local synthetic Git identity. Commit `formatter.py` containing `def heading(text): return text.strip()` and a `unittest` asserting `heading('  Hello world  ') == 'Hello world'`.
2. Commit separate `staged.txt` and `unstaged.txt` baseline files. Stage a sentinel edit to the first, leave a sentinel edit unstaged in the second, and create untracked `note.txt` plus a `note-link` symlink to it. Before changing scope, record their content digests/modes or symlink target, `git ls-files --stage -- <protected paths>`, path-scoped porcelain status and `git rev-list HEAD`.
3. Inspect status, branch/base, remotes and HEAD. With the fixture owner's explicit branch-operation authority, create `fix/heading-normalization` from `main`; no remote exists, so PR state/remote fetch is unavailable and the intended target is local `main`. Preserve all sentinels and index state.
4. Run `python3 -B -m unittest -v` for baseline. Add a regression test asserting `heading('  Hello\t\n world  ') == 'Hello world'` and `heading(' \t\n ') == ''`. Rerun and inspect the assertion failure before fixing implementation.
5. Replace the function body with `return ' '.join(text.split())`; rerun the checks and protected-state comparison. Fingerprint the scoped dirty diff and both included files; retain the actual diff/files for inspection, not only hashes.

Observed evidence (Python 3.14.7, local Git):

| Check | Actual result and relevance |
| --- | --- |
| Preflight inspection and branch selection | `git status --short`, `git branch -avv`, `git remote -v`, `git rev-parse HEAD`; branch created with `git switch -c fix/heading-normalization`. `git rev-parse main HEAD` returned `145cb6161c8b5a3ad441155af43a159f5fed4e10` for both. No remote/PR. |
| `python3 -B -m unittest -v` — baseline | Exit 0, existing trimming/word-preservation test passed; no baseline failure observed. |
| Same command — red | Exit 1, new test failed specifically because actual `Hello\t\n world` retained internal whitespace instead of expected `Hello world`; original test still passed. |
| Same command — green | Exit 0, original and regression tests passed, including whitespace-only input. These cover the agreed normalization and preservation risks; no unrelated suite or new framework was needed. |
| `git diff --check` | Exit 0 after implementation. |
| Python protected-manifest equality assertion | Exit 0: all four sentinels' bytes/modes/target, protected index entries, path-scoped status and existing commit history identical before/after. |

**Local correctness handoff:** F1–F2 implemented with current public-interface checks; F3 verified by manifest equality. Owned files are unstaged on `fix/heading-normalization`, base/HEAD as above. Scoped `git diff -- formatter.py test_formatter.py` SHA-256: `403fecc75fded65ad5573af120d2d3c1310322533028c36b31e5d555ca5dbb7d`; formatter SHA-256: `ef9ff9b755abe5adb072247a49a3189a64511d322dbcede5f911aafcdb59b142`; test file SHA-256: `67a1550f58c4d5e347a9fb5dde4615b6ba9cc05283786c5feb58228856319b17`. Protected sentinels and the local manifest are excluded from delivered scope. No active workers, ticket graph or repair checkpoint applies to this initial synthetic implementation.

The fixture has no product documentation/changelog/release policy, so no such update is needed there. No independent Standards/Spec review or integrated acceptance checks were performed; non-string/Unicode behavior remains outside scope. Next action is integrated verification and independent review when available and authorized. This is locally implemented, not accepted, merged, deployed or released.
