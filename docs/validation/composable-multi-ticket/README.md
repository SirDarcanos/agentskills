# Multi-ticket failure and recovery execution

Executed evidence for [#72](https://github.com/SirDarcanos/agentskills/issues/72), under [#48](https://github.com/SirDarcanos/agentskills/issues/48) and the [accepted design](../../design/composable-delivery.md). Source base: `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`; branch `test/composable-multi-ticket-recovery`, PR target `main`. The maintainer approved the [bounded runtime plan](plan.md) before agent execution. #68's merged PR #93 / `5d0f82bdfd2eb3314920d06811f556bb7e323e51` is present in that base; native read-only reads confirmed #72's blocker/reverse edge and parent #48.

## What actually ran

The parent used the repository Work On Spec dispatch/aggregate/recovery procedures and Work On's common execution libraries. Five actual writable Work On assignments implemented four local fixture tickets; they selected Build and Check inline and reused supplied current technical readiness. This was not a Python agent simulation. The root inspected actual code, diffs, raw results and lifecycle before each integration/launch.

| Assignment | Observed outcome / next gate |
| --- | --- |
| A-build | Independent rendering increment; local check passed. Root integrated A while retaining failed B work. |
| B-partial | Trim-only increment; blank rejection failed and nonstring input errored. Partial/blocked return; no accepted integration and no C launch. |
| B-resume | Reconstructed the stopped owner's same worktree and retained trim increment; added missing validation. Three tests passed; root integrated B. |
| D-build | No native prerequisite, but waited for B's exclusive normalization interface. Added the keyword-only uppercase option without changing validation/default behavior; B/D checks passed; root integrated D. |
| C-build | Started only after B/D integrated checks, separate prerequisite review and root acceptance. Composed the interfaces; seven local tests passed; root inspected/integrated C and refreshed aggregate verification/review. |

The executed workflow's exact source is retained in `source-history/trial-workflow.executed.txt`. Source review later found a denial-token substring flaw in that version; no denial occurred in this retained run. The maintained workflow now requires a successful result containing only the normalized approval token and disables gate output-file binding, so file-save metadata cannot become approval text. Offline negative tests demonstrate the old bypass and the corrected stop-before-next-writer behavior. No completed live assignment was rerun or rewritten to claim it used the repaired source.

One root integrated serially at these actual disposable target revisions:

`418383fcddb2d32426a9967d655e48774bbd1073` → A `835f269f4069279a577d78da741cdf41407ccb43` → B `62d027704c60ec789e96bb177b6705fe69572d2d` → D `98aeea57515a3906f9e2aa33acc57526c56f3acd` → C `ea5046c2ebaf5aa450095d564284003bc0098347`.

Each [integration record](executed/evidence/A-integration.json) includes actual before/after refs, source base, included module, patch/content hashes and inspected source-content equivalence; B/D/C records have the same naming pattern. Scope patches and final modules are retained, not just commit IDs.

## Bounds, failure and freshness

Workflow `533be31d-f8e9-4717-98f6-a29043c7c5c1`, mission `12d6984a-0474-4c77-a7ee-cb2b79cb1cf0`, completed fourteen children: five writers, five read-only supervisor gates and four independent reviewers. [Lifecycle observations](executed/lifecycle.json) identify starts/terminal outcomes and exact child IDs. Gates occupy the same pool and preserve interactive-root decisions because the workflow sandbox has no shell/filesystem. No recursive fan-out or separate child pool was permitted.

- B checkpoint `B-reject` spent cycle one on the partial attempt and cycle two on resume; final count **2/2**, not reset by replacement, phase or integration. The missing-rejection cause resolved under current tests; any remaining related material defect would require reassessment, not a third automatic attempt.
- The aggregate `final-integration` checkpoint spent **1/2** correcting a real review-input gap: both prerequisite reviewers independently lacked the actual committed patch. They stopped; the root supplied the same neutral raw patch to both under an expanded allowlist, preserving the freeze. Final packets include the actual diff directly with environment/check evidence. No verdict averaging or author-review substitution.
- Optional assessment allowance/reservations/attempts stayed **0/0/0** across parent, children, integration and resume. Ordinary authorized writer/reviewer model execution is distinct from optional `ask-*` assessment calls. [Recorded tool counts](executed/tool-audit.json) and lead inspection of writable command actions found no recursive launch, Analyze/research invocation, optional assessment, service or network operation. This is tool evidence, not syscall/billing attestation.
- Protected root file bytes, separate staged/unstaged state, scoped index entries, modes, tracked symlink target and untracked synthetic note matched their initial fingerprints after every integration and final review. See [initial](executed/evidence/initial.json) and [final](executed/evidence/final-state.json) state.
- A was neither rebuilt nor redispatched on resume. B reused its partial increment and analysis. D's interface change refreshed B/D/C-dependent evidence; unrelated rendering decisions remained reusable. Old failures/checks stay attached to their original content.
- The prerequisite snapshot at `98aeea…` and final snapshot at `ea5046…` have separate committed/index/staged/unstaged/content/mode fingerprints. The root froze sources/supporting inputs, repeated path discovery, checked snapshot helper freshness and compared external check/diff hashes before consuming reviews. Interim reports establish prerequisite scope only, not final C acceptance.

The graph is an explicitly chosen persisted **local fixture**, with spec/work-ticket roles, parent membership and both blocker directions. P was never dispatched. No live GitHub fixture API/pagination or public graph mutation is claimed.

## Verification and review evidence

Python 3.14.7, Git 2.54.0 (Apple Git-157), stdlib-only fixture. Git controls are sanitized and hooks/templates disabled for disposable fixture operations; no dependencies were installed.

- Baseline full target: seven expected missing-behavior errors, exit 1; retained in `executed/evidence/target-all-0.log`.
- Actual B partial state: trim passes, rejection fails/errors, exit 1. [Raw failure](executed/evidence/B-final.log), [partial source](executed/evidence/B-partial.py), dirty failure snapshot and resume baseline/final logs are retained.
- Integrated prerequisite command `python3 -B -m unittest test_trial.A test_trial.B test_trial.D`: five tests passed.
- Integrated final command `python3 -B -m unittest test_trial`: seven tests passed, exit 0. [Final raw packet](executed/evidence/final-checks.log) records command/environment/base/HEAD/source digests and actual committed diff.
- `python3 -B work-on-spec/scripts/check-coordination-fixture.py`: eight offline fixture tests passed, including its expected injected failure. `python3 -B work-on/scripts/check-single-change-fixture.py`: eight passed, retaining expected failure/unavailable-check paths. These are not live agent-adherence evidence.
- New offline harness/export/gate checks and retained-evidence replay have their exact commands/results in the delivery record. The gate checks execute actual JavaScript source with mocked `runs` methods, not agents; denied/quoted/negated/unsuccessful results stop before the next writer, while exact approval proceeds. Offline tooling requires Python 3, Git and Node.js; no installation is performed. Replay checks integrity, lifecycle capacity/order, serial refs/source equivalence, snapshot refresh, partial source, counters, zero allowance and protected-state preservation. A replay pass is not a new agent run.

Original behavioral reviews: [interim Standards](executed/reports/interim-standards.md), [interim Spec](executed/reports/interim-spec.md), [final Standards](executed/reports/final-standards.md), [final Spec](executed/reports/final-spec.md). All are fresh read-only contexts separate from authors/each other's conclusions. They found no behavioral defects within their allowed sources. Their stated limits remain intact: historical lifecycle/ledger/upstream AC definitions were excluded and hashes/environment were not independently recomputed by reviewers. The lead's actual history/freshness inspection is separate; evidence-delivery review inspects the neutral raw history under [its packet](review-packet.md).

## Acceptance mapping and limits

| Criterion | Bounded executed support / remaining boundary |
| --- | --- |
| AC2 / AC3 | Work On Spec root with five Work On assignments; local method choices, shared-interface serialization and sole root integration. |
| AC4 | Current readiness/partial increment reused; A not redispatched; changed interface-dependent checks refreshed and final scope repinned. No fresh Analyze/research invocation. |
| AC10 / AC11 | Zero optional allowance remained zero across handoffs/resume; ordinary delivery required no assessment. Positive/unknown-charge transports, alternative models and all named package gates are not exercised here. |
| AC13 | Local graph eligibility, isolated preflight, actual lifecycle/reservations, failed prerequisite waiting, preserved counters/protected work, serial integration, repinned dirty-layer scope and renewed aggregate review. No live process kill/crashed-parent recovery or GitHub fixture mutation. |
| AC15 | Actual agent artifacts/raw checks/history retained separately from plan/static fixtures; limitations visible. #73 owns broader package/discovery/model-policy acceptance. |

The induced failure is an **observed failed check with partial worker return**, not a forcibly killed worker. Resume is a new stopped-owner assignment in the preserved worktree, not a Pi process/session revival. Shared positive-call or unknown-charge budgets are not proven by the zero-allowance trial; existing offline fixture tests cover additional denial/exhaustion/unknown-history cases separately. Source discovery uses explicit approved repository locations, not globally installed migration or complete isolated-runtime discovery. This one small supervised trial does not establish general autonomous adherence or whole-#48 acceptance.

## Retention, reproduction and documentation

[Run tooling](run_fixture.py) creates disposable repos and exposes explicit lead inspect/check/integrate/lane actions; [workflow](trial-workflow.js) launches real agents only under separate runtime authority. Nothing auto-schedules or launches on an ordinary offline test. [Exporter](export_evidence.py) leaves originals untouched, replaces local path prefixes and retains original/export hashes in [manifest](executed/manifest.json). No raw sessions, credentials, environment dumps or personal roots are published. Original local artifacts/worktrees remain retained; the public copies are path-sanitized, not byte-identical attested originals. Archived snapshots identify their original scope and are not live helper targets after path sanitization.

Offline commands from repository root:

```sh
python3 -B -m unittest discover -s docs/validation/composable-multi-ticket -p 'test_*.py' -v
python3 -B docs/validation/composable-multi-ticket/check_evidence.py -v
```

Independent evidence-source reports, gate-finding disposition, renewed review, exact final checks and publication freshness are recorded in `delivery.md`; original reports and later scope addenda are retained separately under `reviews/`. One known author-generated Python bytecode cache was removed after its review freeze; it is excluded from publication, not an executed artifact.

Documentation changed only in this new evidence directory. No changelog/release-impact label: this adds validation/evidence, not public skill behavior or an installation contract. No skill entry/frontmatter/link/install boundary changed; source package executable fixtures were rerun, while broader isolated/discovery coverage remains #73. No glossary/ADR/operating-policy/tracker/listing/history updates are needed because their facts and decisions are unchanged. No CI jobs are configured or changed; hosted duration/compute impact is unmeasured, not inferred from local timings. Merge would retain source/evidence only, not run agents, deploy, release, migrate installs or clean the disposable worktrees. Reverting the evidence commit does not remove privately retained trial artifacts. Keep #72 open until accepted and merged; this record grants no merge/closure permission.
