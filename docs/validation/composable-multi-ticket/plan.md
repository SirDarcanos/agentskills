# Multi-ticket runtime trial plan

For [#72](https://github.com/SirDarcanos/agentskills/issues/72), under the [accepted design](../../design/composable-delivery.md). This record describes the approved experiment; actual outcomes belong in the evidence README and retained artifacts.

## Authority and sources

The maintainer approved a disposable synthetic Git project, bounded writable Work On assignments, controlled partial failure/resume, serial integration, independent review, sanitized repository evidence and a PR targeting `main`. No production fixture issues/relationships, installed skills, optional assessments, installations, services, merge or release actions are authorized.

Source base: `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`. #68's PR #93 is merged at `5d0f82bdfd2eb3314920d06811f556bb7e323e51`, present in the base. Read-only native inspection confirms #72's blocker #68, its reverse blocking edge and parent #48. Issue closure alone is not the integration proof.

The root uses the repository's complete Work On Spec entry and dispatch/aggregate/recovery procedures. Work On owns shared contracts and common build/verification/completion/local recovery. Review Delivery owns independent scope/report procedures. Companions resolve through explicitly approved repository sources; installed copies are unchanged. The workflow receives those locations as arguments, not sibling-layout assumptions.

The fixture deliberately chooses a local tracker: `graph.json` stores distinct spec/work-ticket roles, parent membership and forward/reverse blocker edges. It exercises persisted local graph reads, not GitHub API/pagination. Existing shipped fixtures remain separate offline coverage.

## Lane board

All writable assignments are single-seam; the overall experiment has multiple seams. Each owns one module in a separate worktree. The interactive root is the separate integration-only owner. Workers may inspect other modules/tests but cannot edit them, stage or commit.

| Ticket | Agreement / owned module | Isolation | Eligibility / next gate |
| --- | --- | --- | --- |
| A | Render a receipt label; `render.py` | A worktree | Independent of B; inspect local return, then root integration/review |
| B | Trim and reject invalid names; `normalize.py` | B worktree | Independent of A; partial failure and resumed correction retain the same checkpoint |
| D | Optional uppercase parameter; `normalize.py` | D worktree from integrated B | No native blocker, but B's shared interface ownership serializes D |
| C | Compose normalization and rendering; `pipeline.py` | C worktree from accepted B/D target | Native local blockers B and D; no launch until accepted integration |
| P | Overall receipt agreement | Root only | Coordination input; never an implementation assignment |

Protected target state: staged and unstaged layers of an unrelated file, its tracked symlink and an untracked synthetic note. Preserve bytes, scoped index entries, modes and symlink target throughout integration. Source worktrees and partial artifacts remain retained; no automatic cleanup.

## Execution and gates

1. Inspect baseline modules, supplied technical readiness, acceptance tests, graph and protected-state fingerprints. Reserve two initial assignments A/B under one root ledger.
2. B deliberately implements trim only, executes rejection tests, returns partial/blocked and stops. This is a failed implementation/check outcome, not an induced runtime crash or timed-out process.
3. After both assignments are terminal, the lead inspects actual artifacts and raw checks. Keep C unlaunched and D serialized; integrate A only. Reconstruct actual failed state before B replacement.
4. Resume B in the same worktree with its trim increment and technical evidence. Checkpoint `B-reject` spends cycle one on the failed attempt and cycle two on resume; the unresolved cause retains its lineage. No fresh allowance, duplicate A build or fresh Analyze/research call.
5. Inspect/integrate B serially, then create and assign D from the new target. Inspect/integrate D. Refresh interface-dependent B/D checks, preserving unrelated A decisions.
6. Freeze and pin the integrated prerequisite scope. Two fresh read-only reviewers inspect Standards and Spec independently with neutral allowlisted sources/checks. The root inspects both original reports, freshness and graph before accepting prerequisites and authorizing C.
7. Inspect/integrate C serially, rerun the full cross-ticket suite, repin the final dirty/supporting scope and renew both aggregate review axes. Old scope reports remain historical, not final acceptance.
8. Inspect final reports/freshness, protected state, lifecycle and budgets. Retain original evidence and limitations. Stop on material findings or exhausted correction allowance; reports cannot manufacture agreement.

One async workflow launches all children. Read-only supervisor gates keep integration and dispatch decisions with the interactive lead because the workflow sandbox has no host shell/filesystem. Gates occupy the same capacity pool, are not reviewers and grant no product acceptance. At most two active non-lead assignments; every child has a 600-second bound and the overall workflow a 3,600-second bound. No recursive delegation. Optional assessment limit/reservations/attempts remain zero across all handoffs and resume.

## Reproduction and limits

`python3 -B docs/validation/composable-multi-ticket/run_fixture.py setup` creates the disposable repository and initial worktrees. Subsequent `inspect`, `check`, `integrate` and `lane` commands require an explicit root and ticket. They are manual fixture operations, not scheduling logic or agent simulations. `trial-workflow.js` requires an authorized compatible Pi runtime and explicit root/source/model arguments; invoking it is not an ordinary offline check. Repeat live agents only under a new applicable runtime approval.

Ordinary offline evidence checks must work without agents, paid services or optional inference. The trial cannot prove real GitHub fixture mutations, process-kill recovery, unknown-charge model accounting, installed discovery/migration or general autonomous adherence. Record executed evidence separately from these planned steps and those limitations.
