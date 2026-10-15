# Validation

Read when changing or validating this package. Run `python3 -B workflow/resolve-merge-conflicts/scripts/check-fixtures.py` from the repository root, or run `scripts/check-fixtures.py` relative to a copied package. Python 3.9+ and Git are required; no inference or installation is used.

## Acceptance mapping

| Criterion | Instruction evidence | Executable or inspection check |
| --- | --- | --- |
| MC1 | Entry description and invocation paragraph | Inspect model-invocable frontmatter and authorized-integration trigger; no explicit-only flag. |
| MC2 | Resolve compatible intent; Git side identities | Compatible two-parent merge and two-stop rebase retain both effects; incompatible rule fixture remains unresolved. |
| MC3 | Baseline protection, narrow staging and full-index completion gate | Staged/unstaged/untracked/symlink sentinels keep content, modes, link targets and index entries; unrelated staged content prevents completion. |
| MC4 | Check before continuation and final-state checks | Deliberately failing check leaves merge active; successful combined-content assertions run before/after completion. Unavailable-check reporting is inspected, not a tool-installation test. |
| MC5 | Authorized continuation and repeated reinspection | Merge completes with both parents; rebase stops on two replayed commits, resolves each and finishes with both intended changes. |
| MC6 | Decision pauses and separate permissions | Incompatible intent, failed check and unrelated staged content retain pending operations; inspect that abort/discard/skip/push/main permission is never inferred. |

The harness drives prescribed fixture choices, not a skill interpreter or authorization engine. Passing checks establish Git mechanics and protected-state comparisons for these examples, not that an agent will choose correctly. Authored cases for a future agent walkthrough include missing intent sources, missing checks, denied completion authority, modify/delete, rename, binary, submodule and empty-commit decisions. No pass is claimed for unexecuted cases.

## Package checks

1. Read Markdown as rendered structure: frontmatter, ordered workflow, tables, code fences and conditional routing. Verify the description routes only relevant active integration, not generic Git cleanup.
2. Follow relative Markdown links, including anchors, from every shipped document. Copy only this package and repeat link/frontmatter/script checks without siblings. The harness checks file links and the entry metadata; any future anchor links need anchor validation too.
3. Review commands against Git in a disposable repository. Check narrow path staging, merge/index effects, reversed rebase side meanings and repeated-stop handling. Keep scripted checks distinct from direct agent walkthroughs and independent review.
4. Use `git diff --check`; inspect all included new files too. Review for credentials, personal paths, generated repository internals and unintended global installation changes. Retain applicable source/license notices when copied.

Repository delivery evidence and raw observed results belong in the task's approved report/location, not a new runtime dependency. A direct walkthrough must identify authority, fixture, inspected sources, actual actions, protected before/after comparison and outcome. A static scenario table alone is not executed evidence.
