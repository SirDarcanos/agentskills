# Session-workflow coverage and remaining acceptance

Reusable coverage map for [#143](https://github.com/SirDarcanos/agentskills/issues/143), against the authoritative [#132 WF-01–14 agreement](https://github.com/SirDarcanos/agentskills/issues/132) and [accepted design](../../design/session-oriented-workflow.md). The [human guide](../../workflow-guide.md) teaches the intended paths. This map describes what the checks cover, not a committed execution report or a claim of aggregate behavioral acceptance.

The implementation baseline for this work is integrated source `7c11b56` (#134–#142 and reading-path follow-ups #155/#156 merged). Reading comparisons use the agreement's pinned `45e5a24` baseline. Source delivery changes no installed copy. Historical reports, including the old `ask-nico` evidence directory and composable-delivery trials, retain their original identities and results.

## Reproduce offline checks

From the repository root with Python 3 and Git available:

```sh
python3 -B docs/validation/session-workflow/check.py
python3 -B -m unittest discover -s docs/validation/session-workflow -p 'test_*.py' -v
python3 -B docs/validation/session-delivery/measure_reading.py --base 45e5a24
```

The runner reuses [package isolation/notices/link checks](../composable-acceptance/check_packages.py) and documented package-local suites. Each package is copied alone to an arbitrary directory. Source-development suites run from a separate disposable source copy. Python/Git fixture operations are real local operations; authored stage decisions and instruction substring assertions are not an agent executor. Commands print raw outcomes and input identities; retain results in conversation or a user-selected destination, not routine committed run reports. A nonzero exit or unavailable job is a gap to inspect, not a waived pass. No installation, live tracker writes, model inference, new service or agent launch is performed.

The reused helper constrains ambient Git configuration/hooks, not arbitrary process/network access. Only the inspected, allowlisted offline suites run; this is not an OS sandbox for untrusted code. Isolation means disposable file copies, not proof of runtime security confinement.

## Criterion-to-evidence map

All source rows are inspectable current contracts. **Offline coverage** below means static assertions and authored synthetic fixtures unless an actual local operation is explicitly named. Actual agent observations, outcomes, interventions and gaps belong with the pinned delivery evidence, separately from this reusable map. The behavioral routes below state what to observe; no table row turns its expected outcome into a pass, and a bounded observation does not establish untested branches or universal runtime adherence.

| Criterion | Current source / reusable check | Evidence boundary and remaining observation |
| --- | --- | --- |
| WF-01 shared project agreement | [Setup contract](../../../workflow/setup-project/references/documentation-contract.md), [Setup tests](../../../workflow/setup-project/tests/test_package.py) | Static responsibility/layout checks, including existing non-template guidance; observe explicit new setup approval, approved writes/read-back and unchanged rerun |
| WF-02 prerequisites | Same Setup tests; [method fixtures](../../../workflow/build-and-check/scripts/check-fixture.py); [advisor check](../ask-nico/check-package.py) | Inspect compatibility and missing-common versus capability-only gaps; observe compatible reuse and missing/conflicting guidance without automatic setup or policy writes |
| WF-03 engineering ownership | [Analyze fixture](../../../workflow/analyze/scripts/check-fixture.py), [single-change fixture](../../../workflow/work-on/scripts/check-single-change-fixture.py) | Actual local Git/check/protected-work operations plus authored owner choices; observe small delivery without a technical questionnaire |
| WF-04 stage control | [Selected stages](../discovery-spec-tickets/test_selected_stages.py), [bug handoffs](../bug-to-fix/test_handoffs.py) | Persisted JSON tracker fixture and static continuation assertions; observe shaping-only and compound investigation/fix with zero unselected effects |
| WF-05 shaping completion | [Shape validation](../../../workflow/shape-work/references/validation.md), selected-stage suite | Confirmed-plan terminal clause inspected; observe real questions, feasibility reuse, owner confirmation and no automatic artifact |
| WF-06 selected artifact publication | [Write Spec checks](../write-spec/check.py), [ticket tracker tests](../write-tickets/test_tracker.py), selected-stage suite | Fixture writes/read-back, role/readiness/graph integrity, draft overrides and concise return examples; observe direct spec publication without full-text reapproval and concise real ticket results in an authorized test runtime |
| WF-07 diagnosis without ticket | [Investigation checks](../investigate-bug/test_investigation.py), [bug handoffs](../bug-to-fix/test_handoffs.py), [ticket-stage adapter](../../../workflow/investigate-bug/references/ticket-stage.md) | Source checks plus synthetic reproduction/cause and tracker persistence tests; observe diagnosis without tracker, then separately direct work or selected tickets; compound fix must reuse current cause evidence |
| WF-08 delivery before PR | [Single-change fixture](../../../workflow/work-on/scripts/check-single-change-fixture.py), [whole-spec fixture](../../../workflow/work-on-spec/scripts/check-coordination-fixture.py), [PR contract tests](../../../workflow/pr/scripts/test_contract.py) | Actual local checks, Git integration and fault sensitivity; no-PR returns/feedback/selected publication decisions are authored. Observe both delivery scopes without PR, adjustment with refreshed evidence, then explicitly selected PR/read-back |
| WF-09 selected persistence | [Handoff fixture](../../../workflow/handoff/scripts/check-handoff-fixture.py), whole-spec fixture | Actual exclusive file creation/read-back, retained owner/spent state and no-overwrite; receiver decisions are authored. Observe explicit handoff and fresh-session resume, including missing/stale history and uncertain operation without blind retry |
| WF-10 domain/ADR authority | [Domain tests](../../../workflow/domain-modeling/tests/test_package.py), [domain validation](../../../workflow/domain-modeling/references/validation.md) | Static plan-only/write/ADR/history boundaries; observe authorized meaning maintenance, unapproved ADR refusal and approved reciprocal supersession without rewriting history |
| WF-11 reading overhead | [Full-file counter](../session-delivery/measure_reading.py), [arithmetic tests](test_reading.py), accepted [counting rules](../../design/session-oriented-reading-paths.md#measurement-boundary) | Static per-context words with full manifests, shared project docs and required companions; no tokens/timing or intervention measurements. Diagnose-only and before-PR endpoint differences are separately labeled; equivalent published routes are also reported. Nonreductions remain visible |
| WF-12 reconciliation | Setup tests and [reconciliation](../../../workflow/setup-project/references/reconciliation.md) | Compatibility/customization/no-permission-import clauses inspected; observe unchanged rerun and explicit approval before incompatible policy delta |
| WF-13 advisor rename | [What Now entry](../../../workflow/what-now/SKILL.md), advisor check | Routing/body gates and package identity inspected; observe explicit advice before setup with no execution. No installed rename is claimed |
| WF-14 safeguards | All isolated package notices/links, review snapshot tests, model authorization suites, [migration fixture](../installed-skill-migration/test_fixture.py), ticket tracker tests | Actual snapshot drift/protected sentinels and synthetic role/readiness/cycle/partial-write cases; model suites use no inference. Observe forbidden effects remaining absent in agent routes; preserve repair lineage, independent axes, no permission widening or installed effects |

The runner additionally checks source-development Writing for Agents and isolated Research, conflict-resolution and model packages. License checks retain the maintainer's MIT notice and TDD's upstream Matt Pocock attribution. No optional-model policy is approved in this repository: model authorization tests are offline checks, not permission to call models. Ordinary authorized independent reviewer agents are distinct from optional assessments.

## Reading comparison interpretation

The counter counts UTF-8 text with Python `str.split()`, full files once per context, as the design specifies. Planning includes inline Analyze and inspection of the Build and Check candidate. Investigation includes current cause evidence with no extra technical/domain gap. Bounded delivery uses Build and Check, a root coordination read and two neutral reviewer contexts; no recovery or recorded repair branch is selected.

Project instructions are charged in every context. The fixed-project column holds the baseline common docs identical for accounting control; actual-project columns additionally expose growth or extraction into current common docs. Both comparison tables are emitted; the arithmetic tests require the three equivalent complete outcomes to reduce with actual project guidance included. Tracker policy/library loads are included when a ticket outcome is selected. Both published-PR manifests also include the project's tracker-completion and release-label policies, as required by PR's reporting contract; the common workflow file already supplies the release procedure. The current path uses Setup's directly readable native-tracker library; only the baseline loads the bootstrap entry and label-audit reference. Analyze's domain/delegation detail remains conditional on those branches, not part of ordinary planning. Maintenance instructions, README/license, task evidence and automatic harness prompts are excluded equally. Full manifests are emitted rather than hiding required companions behind a subtotal.

Compare `investigation_selected_ticket` and `bounded_delivery_with_PR` for equivalent complete artifact outcomes. `investigation_diagnosis_only` exposes removal of the former compulsory ticket outcome, not an equivalent published endpoint. `bounded_delivery_before_PR` is a baseline intermediate boundary, not its former completion. A separate fresh PR context shows the cost when publication happens in a later session. Repeated reads within one context deduplicate; different reviewer/publisher contexts each pay for their own guidance.

Shorter text does not prove correctness, runtime efficiency or reduced human intervention. Report increases as increases; the spec sets no arbitrary reduction quota. If an equivalent complete path does not reduce aggregate reading, record a WF-11 gap rather than using only the fixed-project or changed-endpoint column to declare success. Further package optimization needs its own approved scope; #143's documentation/acceptance scope does not authorize silently changing specialist behavior. Do not use the earlier design-sketch counts as achieved source counts.

## Comparing later instruction simplifications

For two post-session-workflow revisions, use identical current route manifests on both sides instead of charging the historical compulsory ticket/PR endpoints to a modern baseline:

```sh
python3 -B docs/validation/session-delivery/measure_reading.py --base b608804 --baseline-layout current
```

`b608804` is the integrated source before #163. The default `historical` layout and `45e5a24` comparison remain available unchanged in meaning. Inspect the baseline's actual instructions before selecting either layout; this flag does not discover required reads. The counter emits complete per-file/per-context manifests, fixed and actual project costs, unchanged paths and increases. Retain that output in conversation or the user-selected evidence destination, not as a routine committed run report. Neither mode measures tokens, elapsed time, reliability or human interventions.

The #163 simplifications preserve ownership and required reads; their reusable regression rationale is:

| Simplified instruction | Coverage retained at the existing owner |
| --- | --- |
| Analyze companion-discovery narration and repeated return fields | Prerequisite discovery gates remain inline; steps 3–4 own brief fields and method availability; step 5 returns those results and retains stage/active-state boundaries |
| Investigation cleanup narration and repeated diagnosis/continuation fields | Step 4 still owns probe identity/cleanup and diagnosis fields; step 5 returns them with failed checks and preserves explicit fix authority, freshness and compatible-delivery gates |
| Direct-build repeated readiness, handoff fields and method narration | Entry evidence is compared with actual source; build steps 1–2 retain preflight, ownership, native dependencies and check/method choice; step 3 retains actual-return inspection and correction lineage |
| Review entry's duplicate snapshot, axis and drift details | Mandatory complete `handoff`, `scope` and `report` reads remain; those existing owners retain dirty-layer capture, neutral packets, findings and freshness mechanics; entry keeps two independent axes, authority and failure boundaries |

No new shared contract, companion dependency, stage, policy value or installed-copy change is introduced. Package-local guards, isolated links/notices, snapshot fixtures and the reading arithmetic suite cover static and synthetic regressions. They do not execute an autonomous planning, diagnosis, delivery or PR route. Ordinary independent delivery review is also not such an exercise. Any representative runtime exercise still needs a bounded target, effects and execution permission as described below; unavailable authority/capability must remain a reported gap, not a claimed runtime improvement.

## Bounded behavioral follow-up

Aggregate acceptance remains blocked while material agent routes above are unrun. Required next evidence is an explicitly authorized disposable-runtime exercise covering the listed transitions, using pinned current packages and a compatible project agreement. Bound attempts/time and exact writable fixture scope before launch; retain raw actions, current/dirty identities, observed user interventions, checks, independent reports and before/after protected-state/effect inventories. Include negative cases, not just happy paths. Do not mutate a live tracker, call optional models or replace installations to obtain this evidence without separate exact authority.

A fixture-host tracker can test agent publication behavior only if the actual agent uses it and its limits are labeled; direct Python fixture replay is not that observation. Independent delivery review is not a replacement for an agent walkthrough. Unavailable writable whole-spec capability or inaccessible previous-session history remains an explicit blocker. The current source can be documented and offline-checked while aggregate acceptance stays open; no universal runtime adherence or installed migration is implied.
