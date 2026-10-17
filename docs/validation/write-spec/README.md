# #62 specification extraction evidence

Scope: standalone [Write Spec](../../../workflow/write-spec/SKILL.md), its publication/reference gates and Work On's thin product-agreement adapter. Accepted #50 design integrated through PR #75 at `a95a9588`; source baseline `c1465e7` includes #61. Native #62 blocked-by inspection returned only closed #50, and the accepted design status plus merged artifact established eligibility, not closure alone. No graph/issue-label changes were made.

## Current readiness regression checks

Run `python3 -B -m unittest discover -s docs/validation/write-spec -p 'test_*.py'`. [Readiness examples](test_readiness.py) exercise authored agent-ready/human-ready spec creation and failed label read-back using the local CRUD fixture, plus static guards for required classification and independent scheduling gates. [Ticket tracker tests](../write-tickets/test_tracker.py) cover blocked parent specs, preserved graph state and equivalent blocked/unblocked next actors. The existing checker retains the genuinely design-unready publication case. These are executable authored examples, not autonomous agent-adherence or live API evidence. The historical results below describe their original revision.

## Executed evidence

Environment: Pi implementation session on macOS, Python 3.14.7, Git 2.54.0, Node 24.21.0. No delegated/model calls. Working tree began clean; created `feat/standalone-write-spec` from current `origin/main`, targeting `main`.

```sh
python3 -B docs/validation/write-spec/check.py
git diff --check
```

The checker passed for Write Spec, Work On and Shape Work in-source and isolated non-sibling copies: frontmatter, ordered procedure bounds, relative links/anchors and script syntax. Nine Write Spec links after the attribution update, 108 Work On links and five Shape Work links each; root/evidence links checked separately. New Python files parse with the Python 3.9 grammar; this is not a run on Python 3.9. The Write Spec notice preserves both Matt Pocock's and Nicola Mustone's copyright with the full MIT text. The attribution follow-up inspected to-spec and its license at pinned upstream revision `49dd158`; the checker verifies this combined notice rather than incorrectly requiring root-license equality. Temporary copies/stores are disposable; no installed skills changed.

The checker executed fixture-only create/read/list/update/fault operations: exact body/title/mapped roles read back, product-approved/design-unready state, existing identity reused without mutation, post-write timeout inspected before retry, unavailable read reported as failed. One spec, zero tickets or graph edges. The CRUD fixture is not an authorization engine; the caller selects the approved effects. Detailed [direct writing/caller walkthrough](walkthrough.md) separates actual authored spec/fixture operations from direct decision applications and unrun agent trials.

Changed Markdown was rendered using the already available Marked parser and inspected for heading/table/code structure. Direct integrated review checked source fidelity, approval/publication/readiness separation, stable acceptance IDs, owner-only spec procedure, companion boundaries, portable links and no private/local-path leakage. No independent review was authorized or performed.

## #48 mapping and limits

| Criterion | Delivered evidence |
| --- | --- |
| AC1 | Standalone entry, conditional companions, isolated links, useful complete/partial/blocked returns and stop boundary |
| AC4 | Agreement-1 reused with no shaping/analysis/model run; direct selective-invalidation application preserves unaffected product commitments (not autonomous freshness testing) |
| AC5 | Actual spec expression plus local publication/read-back; no ticket creation; role distinct from readiness |
| AC14 | Package README/license, public index, caller entries/contracts/README, Shape Work ownership pointers and changelog reconciled |
| AC15 | Executed checks/fixture operations and direct walkthrough separated from authored cases; unrun checks disclosed |

No live tracker API mutation, installed slash expansion, independent reviewer, cross-runtime agent trial or full discovery→spec→tickets run. #70 owns broader composition; #73 owns final discovery coverage. Fixtures do not prove GitHub permissions/API semantics or autonomous instruction compliance.

Documentation disposition: no domain meanings or new architectural decision changed, so CONTEXT/ADR/design need no rewrite; accepted #50 already assigns this owner. Operating policy and native graphs remain unchanged. Historical #14/#18/#31 and #61 evidence remain historical, not regenerated. Changelog adds one Unreleased Added entry for this new package; Work On's existing unreleased entry already describes its broad delivery behavior. Installation/retirement is excluded and not performed.

Two new executable evidence files (`check.py`, `tracker_fixture.py`) add offline mechanics assertions; no existing executable tests were removed or modified. Two package validation documents changed; these are authored instructions, not executable tests. No CI exists or was added; timing impact is unmeasured. Merge publishes source only, not deployment, release or installed-copy replacement. Stage compatible Work On/Write Spec copies when separately authorized; missing Write Spec blocks the dependent route. Reverting source restores prior ownership but cannot undo a future authorized remote publication.
