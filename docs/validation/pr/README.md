# #66 PR reporting evidence

Agreement: [#66](https://github.com/SirDarcanos/agentskills/issues/66), accepted [#48 design](../../design/composable-delivery.md), AC1/AC4/AC12/AC14/AC15. Input `main`: `e2f02b4a91e87aebea6a1830d0384d6c737ad881`; native #66 blocker was #65, integrated through merged PR #90 at that commit. Worktree was clean and synchronized before creating `feat/plain-language-pr`, targeting `main`.

## Executed direct walkthroughs and checks

On macOS, Python 3.14.7 and Git 2.54.0:

```sh
python3 -B docs/validation/pr/fixture.py > /tmp/pr-fixture-evidence.json
python3 -B -m unittest discover -s docs/validation/pr -p 'test_*.py' -v
git diff --check
```

The fixture creates three disposable repositories, commits baseline/candidate files, runs local baseline/candidate checks and captures diffs/identities/configuration. [Retained raw evidence](evidence.json) comes from that execution. All three baseline/candidate local runs passed three trivial fixture functions each. No CI host, installation, remote PR, benchmark or model was invoked. Supplied timing records and unresolved review findings are explicitly synthetic; they are not measured hosted performance or independent review.

The lead then inspected the raw sources/diffs/results and followed `pr` directly to generate [three reports](reports.md), including measured-record arithmetic, missing timing, no CI, test rename/update/redundant deletion, unresolved findings, manual migration and no configured automatic deployment. Authority was local reporting only. No automatic review/analysis restart, publication, merge, closure or migration followed. These are direct agent walkthroughs, not autonomous subprocess-agent execution. The script cannot establish agent compliance.

Six named regression tests passed: actual local results; identity/rename/redundancy accounting; CI distinctions; synthetic measured/unmeasured/inapplicable reporting; retained source identities and findings; migration/report-only fixture boundaries. Report checks compare generated prose with source facts and selected guardrails, not every possible prose error. Fixture arithmetic is not application protection.

## Scope and documentation

New runtime owner: `pr` entry, README, impact/publication/validation references and repository MIT notice. Original instructions derive from #48/#66 and maintained repository contracts; the installed PR/show-me template was inspected as an incompatible candidate, not imported or adapted. Work On retains acceptance/repair/tracker/status ownership and gains only the discovered PR route/capability; its broad entry remains until #67. Root listing and one Unreleased Added entry describe actual new behavior. No glossary/ADR/operating-policy change is needed: accepted ownership and authority are unchanged. No historical #14 evidence, CI configuration, native relationships or installed copies change. Compatible added functionality has minor impact.

The actual delivery PR records final rendered/frontmatter/link/isolated-package checks, freshness, integrated inspection, separately inspectable independent review results when available, and publication read-back. Later results are not implied by this walkthrough record.

## Limits / unrun routes

No live CI duration/compute/billing or live deployment was measured. Fixture workflows are text inputs, not executed hosted YAML. No fixture performs authorized remote create/update, interrupted host mutation, restore or installed-copy replacement. Live publication of this implementation, if authorized by repository policy, is separate from fixture evidence. Missing/incompatible companions, stale evidence and interrupted publication routes are authored validation expectations with direct instruction inspection, not executed end-to-end fixture claims. Cross-runtime installation/discovery and #67/#68 integrated leads remain later work. No paid assessment or benchmark is required for ordinary checks.
