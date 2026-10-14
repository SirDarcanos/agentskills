# Local assessment policy validation

Repository evidence for [#52](https://github.com/SirDarcanos/agentskills/issues/52), under [#48](https://github.com/SirDarcanos/agentskills/issues/48) and the [accepted composable-delivery design](../../design/composable-delivery.md). This is not a target project's policy or permission to call models.

## Scope and prerequisite evidence

The source packages `ask-nimble`, `ask-clef` and `ask-clef-flash` now support explicit assessment and exact policy-authorized autonomous handoffs. Each ships its own authorization procedure and test-only simulation; no shared mandatory gateway, policy parser or delivery companion is introduced. Model selection remains fixed per package. Hosted Jev, installed skills and this repository's disabled model-use permission are unchanged.

Read-only GitHub inspection confirmed #52's native blocker is closed #51. Accepted design PR #75 is merged at `a95a9588ff86304f2390cae8d87df4addf7da1d1`; setup-policy PR #76 is merged at `308bb1fb48c43a8db85c5f66cf80dd661027c4a5`. Both are ancestors of this change's base, `308bb1f`. No tracker relationships or issue state were changed.

## Executed checks

Run from each package root, using Python 3 and no network:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 scripts/replay.py
```

| Package | Baseline test methods at `308bb1f` | New methods | Final passing methods | Offline fixture schemas |
| --- | ---: | ---: | ---: | ---: |
| Ask Nimble | 14 | 23 | 37 | 7 |
| Ask Clef | 17 | 23 | 40 | 7 |
| Ask Clef Flash | 17 | 23 | 40 | 7 |
| Total | 48 | 69 | 117 | 21 |

No baseline test, fixture or production replay script was removed or moved. Counts are discovered `unittest` methods, not subtest iterations, model calls or accuracy measurements.

The new tests execute a **test-only model of the prose procedure**, with mock transport, service probe, start/stop and approval callbacks. They use the existing replay request/response validators for actual script-contract checks. Their in-memory permission dictionaries are synthetic resolved facts, not a new policy format. Passing simulations do not prove an agent will follow the prose or constitute production authorization enforcement.

Executed cases cover absent/none/unapproved/noncurrent authority; exact/wrong skill/model/endpoint; purpose/disclosure denial; explicit invocation/project prohibition/generated command text; suitability before probes; shared call/spending exhaustion, outstanding reservations and resume; pre-send revocation/exhaustion; service/model absence, ambiguous probes and denied startup; configured direct fallback versus explicit offer-and-wait; owned stop/leave/pending disposition; failed/unknown attempts without refunds or retries; valid insufficient data; advisory mismatch without verdict-seeking; and one shared evidence correction. Authorized calls assert no redundant approval callback.

Each package's checks also passed for frontmatter contract wording, all relative Markdown file targets and an isolated temporary copy without siblings. Frontmatter was separately parsed with the already available YAML parser. Seventeen changed Markdown documents were rendered with the already available Markdown renderer into temporary HTML; the skill entries and changed authorization/lifecycle material were inspected. `git diff --check` passed. The integrated diff was directly reviewed for scope, credentials/private data, generated artifacts and nonportable paths.

The first run passed 105 methods. Expanding coverage exposed one authored-test error: the mismatch case used `options` rather than the API's `criteria` field. After correcting all three copies, the complete final run passed the 117 methods and 21 fixture schemas above. No inference was used to choose an expected verdict.

## Documentation disposition

Updated the three entry points, package READMEs, authorization/API/testing references, root README listings and the Unreleased changelog. Setup owns policy establishment; its contract, the source repository's AGENTS/workflow permissions, accepted design, domain vocabulary and ADR history did not change. No live permission values were created. Same-package references preserve isolated installation; any separately authorized alternative is discovered by its lead through the runtime catalog or approved location, never inferred from sibling paths.

## Limits and post-merge effects

- No live inference, endpoint probes, real server startup/shutdown, downloads, installation, hosted changes or retained model records were performed.
- Real agent walkthroughs and live model/service behavior remain unrun. Package testing references list authored scenarios separately.
- Review was direct self-inspection, not independent Standards/Spec review or model assessment; neither was separately authorized.
- CI remains absent: no workflow/configuration change or measured CI performance claim.
- Merge updates source instructions/tests only. Separate installed copies still require their own approved update; rollback of source does not revoke target policies or restore installed copies.
- #52 stays open until maintainer acceptance and merge; no merge/release authority is claimed.
