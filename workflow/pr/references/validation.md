# PR validation

Use when changing/validating this package. Read the full entry and branch references. Check frontmatter routing for standalone and bounded handoffs; render and inspect Markdown; resolve every relative link/anchor; copy the package alone and repeat link checks without sibling assumptions. Review diffs for private data, generated artifacts and local paths. Inspect the selected Work On PR route so procedure ownership remains here, without an automatic PR stage at delivery completion. Run `python3 -B scripts/test_contract.py` from this package directory (Python 3.9+). These static instruction guards execute offline and do not publish a PR.

## Summary and evidence checks

For routine documentation and executable changes, failed/unrun/stale checks, and migrations, draft a summary and a separate synthetic evidence record. Aim for 100–200 words for routine examples without padding; allow longer consequential explanations. Compare every summary claim with the record. Check that:

1. Before/after outcome and purpose are understandable without code reading.
2. Meaningful checks and review outcomes are summarized plainly; hashes, commands, reviewer IDs, snapshot history, test arithmetic and full reports stay in evidence.
3. Material failures, unrun/stale checks, unresolved findings and uncertainty remain prominent with consequences and next actions; no unsupported blanket verification claim appears.
4. Unchanged tests/CI/deployment/reversal details are omitted from the summary unless decision-relevant; protection changes, migration actions/owners and source-revert limits remain visible when relevant.
5. Intended closure uses `Closes #X`, related-only references use `Refs #X`, and neither `Fixes` nor `Resolves` is used as a closing keyword. Publication preserves target completion policy.
6. Entry, impact guidance and README agree on internal diligence versus the maintainer-facing summary. Evidence links are accessible and disclosure-safe; unavailable storage/publication is reported honestly.

Reusable authored fixtures may live beside repository validation tooling; they are not per-change execution reports. Existing historical reports retain their original results and may illustrate older formatting. Static assertions and authored examples do not demonstrate autonomous runtime behavior.

## Fixture protocol

Use disposable local repositories and synthetic evidence; no public PR, live CI, benchmark, installation or model call is implied. Inspect actual before/after source, test identities, workflow definitions and raw check results. Generate plain-language reports using the entry, then compare claims with those sources. Record direct agent walkthroughs separately from fixture-script assertions and independent review.

| Input | Required report/action |
| --- | --- |
| Measured CI | Baseline/candidate run records, workload/runner/cache/sample/statistic/units, elapsed versus compute distinction, confounders and synthetic versus live evidence labels |
| Unmeasured CI | Job changes established from definitions; missing duration/compute explicit, zero invented savings or unauthorized benchmark |
| No CI | Configuration scope inspected, no jobs found; external unknowns preserved, timing comparison inapplicable |
| Tests renamed/deleted/updated | Declared base/unit; moves not additions/deletions; redundant removals still removed with retained protection evidence; additions/updates explain protection |
| Unresolved or stale review | Findings and dependent acceptance blockers retained, independent versus direct checks distinguished; report can complete without acceptance |
| Migration / no automatic deployment | Manual action/owner/approval, actual merge triggers, source-revert limits and installed-copy effects; no presumed deployment |
| Report only / unauthorized publication | Useful draft and blocked publication, zero remote mutation |
| Authorized update / interrupted write | Preserve unrelated body content, current remote scope, read-back and inspect-before-retry; fixture-host behavior is not live-host evidence |
| Current / changed evidence | Reuse current findings without repeat analysis; dependent stale claims after source change cannot pass |
| Missing/incompatible companion | Route-specific blocker, no sibling/legacy fallback or automatic installation |

Follow the entry's supporting-evidence instructions: retain reproducible inputs, commands/environment, state identities, raw outputs, actual check results and original independent-review reports separately from the short summary, in conversation or a user-selected evidence home. A dedicated PR/issue comment or collapsed **Validation details** is appropriate only when selected publication is authorized. Link it once when useful rather than duplicating it in the summary. Keep material failures, unrun checks, blockers and required actions visible in the short summary. Use temporary local intermediates, not a new committed execution report; reusable checks remain committed. Unrequested persistence is not a storage gap. If selected publication/storage is unavailable, return evidence conversationally and identify that gap without remote writes or publication claims. Active owners, uncertain operations and spent allowances retain their safety accounting. Walk complete copied-package instructions and prompts without the collection's checkout, Git metadata or tracker; target-project evidence remains legitimate. Static checks or expected outcomes are not autonomous agent trials. No test-count quota applies. Report unrun material routes, including unavailable publication/review capabilities, instead of inferring success.
