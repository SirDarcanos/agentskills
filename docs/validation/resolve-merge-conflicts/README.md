# Merge-conflict skill validation (#110)

## Agreement and scope

[#110](https://github.com/SirDarcanos/agentskills/issues/110) delivers only `workflow/resolve-merge-conflicts/`, covering MC1–MC6 in the authoritative [#109 specification](https://github.com/SirDarcanos/agentskills/issues/109). Native read-back found parent #109 (including child #110 in its paginated children) and no incoming/outgoing blocker edges. No prerequisite integration evidence is required. Existing reference installations are preserved; installation, unrelated Git cleanup and new product behavior are excluded.

Scope: the complete new package, the catalog row in `docs/skills.md`, the `Unreleased` Added entry in `CHANGELOG.md` and this evidence directory. No domain term, enduring architectural decision, project authority or release policy changes. The top-level README already routes to the complete catalog and needs no additional skill-specific entry.

## Method and environment

One lead implemented directly with Build and Check: package instructions/references/license/readme, immediate link/frontmatter inspection; disposable Git fixtures and immediate execution; catalog/changelog edits and immediate link/diff inspection. Companion sources were the discovered installed `work-on`, `implementation-preflight`, `build-and-check` and writing guidance, plus the repository `review-delivery` and `pr` packages. Installed sources were read only; repository companion revision was base `b3d4259bdf2c6ac6e5105e3429d3281883e52863`. Resolved installed entry SHA-256 identities: Work On `56711cbc92ad0b6ca16e3fbe30f86dc8069240ada1eff26d1b92694455afc980`, preflight `ccb940cb60819792947274f1d848636c6461d47ae3856bae80fcd83d1df39d15`, Build and Check `40a72625c2a7eadd3bba41c562879f248feef30fa5a42371396348ac61bd44a2`, writing guidance `551adca942227b44192edba88acd4e8db911f0121ce58ad16944ccf6a896a74a`. Work started from a clean worktree on a branch whose PR was already merged; preflight fetched origin and created `feat/resolve-merge-conflicts` from current `origin/main`, targeting `main`. There was no unrelated dirty work to transfer or modify.

Environment: macOS, Apple Git 2.54.0, Python 3.14.7. No package installation, inference, network fixture operation or global Git configuration change. The fixture uses synthetic identities, temporary repositories, explicit file staging and per-process Git configuration isolation.

## Executed checks

Command: `python3 -B workflow/resolve-merge-conflicts/scripts/check-fixtures.py`.

[Raw successful output](checks.txt) records seven passing named `unittest` cases in the repository and the same seven passing when the complete package was copied and run outside it. Count unit: named test methods; new package baseline is zero, delivered is seven added, zero removed/updated/moved. Existing packages' tests are unchanged. The [package validation mapping](../../../workflow/resolve-merge-conflicts/references/validation.md) ties the assertions/instruction inspections to MC1–MC6.

The first development run had six cases: five passed and the intended multi-commit rebase case failed because its unrelated unstaged tracked sentinel caused `rebase --continue` to stop before the next commit. `REBASE_HEAD` therefore stayed unchanged. This was a fixture assumption failure, not evidence of second-stop handling. The corrected run separates successful two-stop continuation from a seventh explicit dirty-work pause test. The skill now explicitly explains that Git constraint. Both outcomes and the initial failure remain part of the development history; this was development before acceptance, not a spent acceptance-repair cycle.

Static checks executed: package and changed catalog relative targets exist; entry metadata matches the directory name and permits model invocation; balanced Markdown fences; `git diff --check`. Markdown was parsed to HTML using an already available `marked` installation and its headings, ordered workflow, table, code blocks and link structure inspected. No renderer was installed. License notices retain Matt Pocock and Nicola Mustone; the README distinguishes the inspected reference copy from the upstream revision whose license was verified.

## Direct author-agent walkthrough

In a separate disposable repository the author-agent inspected `git status`, recent commit messages and all three conflict stages, then read the actual conflicted file through the file tool. The current side changed `beta=base` to `beta=current`; incoming changed `alpha=base` to `alpha=incoming`. The base had both defaults. Both effects were compatible, so the agent edited only `rules.txt` to retain both, inspected the combined and staged diffs, explicitly staged that file, checked no unmerged entries/staged whitespace errors, and asserted both intended values before continuing the synthetic merge.

`git merge --continue` finished the authorized fixture operation. Post-checks established both merge parents in order, expected integrated content, absent `MERGE_HEAD`, unchanged protected tracked file contents and clean status. Resulting fixture commit: `1309b04b970abe064a797fd543e3fdcb2485fafe`. This is a direct tool walkthrough by the implementation author, not independent review or an autonomous discovery trial. Dirty sentinel preservation, failure pauses and multi-stop rebase behavior were exercised by the scripted fixtures, not this walkthrough.

## Limits and release effects

Instruction inspection and scripted fixtures are distinct from agent adherence. Binary/rename/modify-delete/submodule and empty-commit scenarios, missing-check handling and denied completion authority have instruction-level inspection only; they were not executed agent walkthroughs. Runtime discovery/installation across coding agents is untested. No live consumer project was integrated.

The new standalone package is compatible added functionality (minor release impact), not a replacement of an installed interface. No GitHub Actions configuration is present in the inspected repository; no CI jobs change, and hosted duration/compute impact is unmeasured/inapplicable to configured jobs. External automation is unknown. Merge would add source/catalog/history only; manual installation remains separately approved. A source revert can remove the package/catalog entry but cannot undo future independently installed copies. No release, merge, installation or issue closure is performed by these checks.
