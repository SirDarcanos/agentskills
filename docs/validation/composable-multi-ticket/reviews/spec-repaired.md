# Independent Spec inspection — #72 repaired-source delivery

## Scope, independence and identities

Fresh read-only inspection of the repaired source and neutral retained evidence. No edits, commands, tests, network calls, optional assessments or delegation were performed. Excluded reviewer reports, ledger, README and delivery narratives were not read.

Comparison selector: fixed base `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`.

The supplied `repaired-source-scope.json` identifies:
- Branch: `test/composable-multi-ticket-recovery`.
- HEAD: the fixed base above.
- New delivery files as included actual files despite empty committed/staged/unstaged patch fingerprints.
- Maintained workflow SHA-256: `72922a2cb2f1da9e8ea32b03e320862086a488165a28f255795d2656c494376e`.
- Historical workflow SHA-256: `18620d4312dd5ee4144cbdec0c527a774bcccff0e3750b75a62c4595340cc867`.
- Gate test SHA-256: `0fbe28da103b3ff3123ab85072815332ff10ec9e69c927f783e5ded56ab6939e`.

These hashes are supplied snapshot identities, not independently recomputed here. The root owns the declared freeze, initial/final fingerprint comparisons and retained source-checkpoint count. This reviewer consumes one reserved 600-second context in the existing shared pool; no allowance reset is inferred.

## Inspected paths and criteria

Paths below are relative to `docs/validation/composable-multi-ticket/` unless otherwise stated.

**Complete source reads:** `review-packet.md`, `plan.md`, `trial-workflow.js`, `source-history/trial-workflow.executed.txt`, `test_gate.py`, `run_fixture.py`, `check_evidence.py`, `export_evidence.py`, `test_harness.py`, `test_export.py`.

**Primary policy/contracts:** supplied repository AGENTS instructions; `docs/agents/{project,workflow,issue-tracker,triage-labels}.md`; accepted `docs/design/composable-delivery.md`; Work On Spec, Work On and Review Delivery entries; Work On execution contracts; Work On Spec dispatch/recovery/aggregate references; Review Delivery handoff/scope/report references.

**Neutral retained data:** lifecycle and tool audit; initial/final state; B failure snapshot, partial source, resume-before manifest, failed/final checks and resume patch; A/B/D/C integration records; interim/final scopes and checks; all seven retained target sources. The manifest was inspected partially.

**Launch-local inputs:** repaired-source scope, gate-repair patch, repaired-source/evidence-source/package check logs, repair pins; the earlier evidence-source delta’s historical workflow section and selected helper-source content.

Criteria: #72 bounded writable execution, dependency/interface eligibility, root-only decisions, partial failure/resume, preserved work and counters, serial integration and refreshed aggregate evidence; bounded #48 AC2, AC3, AC4, AC10, AC11, AC13 and AC15.

## Review

### Correct: repaired approval gate fails closed

`trial-workflow.js:10–18` preserves root-only decision ownership while changing gate output binding to `false` and requiring:
1. `result.ok === true`;
2. string output;
3. trimmed output exactly equal to `ROOT_APPROVED_NEXT_STAGE`.

The previous substring test is absent from the maintained source. Every stage-transition gate uses this same assertion (`trial-workflow.js:25–43`), so denial text containing the token cannot authorize the next writer.

`test_gate.py:45–80` exercises the actual workflow source with offline Node stubs. Its denial cases include embedded, quoted, negated and suffixed tokens, failed/nonboolean success status, and missing/null output. Assertions require termination before B resume. Positive cases require exact or surrounding-whitespace approval and verify disabled gate output binding.

The retained historical source accepts the embedded denial in the sensitivity test. This is meaningful regression sensitivity, **not agent execution**.

### Correct: historical source remains distinct

The historical file retains the old `${key}.md` binding and substring assertion at `source-history/trial-workflow.executed.txt:10–17`. The supplied `gate-repair.patch` changes only that binding and assertion.

The earlier source delta identifies historical blob `e5c6d1b2280efc8de2d812f206ace6644d5f48c8`; the repair patch uses the same old blob identity. Actual historical text is consistent with that delta. It is preserved separately as `.txt`, not substituted into the maintained launch route.

The repair does not rewrite retained lifecycle, integrations, fixture source or checks, and does not claim the repaired workflow was live-executed.

### Correct: bounded execution and eligibility evidence

`trial-workflow.js:19–43` maps the approved sequence to:
- Initial independent A/B work.
- Root reconciliation before B resume.
- B completion before D’s shared-interface ownership.
- Both prerequisite review contexts and root gate before C.
- Root integration/check refresh before final review.

The retained lifecycle records fourteen terminal children under workflow `533be31d-f8e9-4717-98f6-a29043c7c5c1`, with at most two concurrent children. B partial settled before B resume; B resume settled before D; both interim reviewers and the dependent-dispatch gate settled before C. Final reviewers start after the aggregate gate.

No duplicate A build or parent P implementation appears. Tool-count summaries contain no recursive delegation or optional-assessment tool starts. These summaries are not syscall attestation.

### Correct: retained partial work, integration and budgets

B’s retained partial source is trim-only. `executed/evidence/B-final.log` records both rejection failure and nonstring error, exit 1. The resume-before manifest identifies the same partial-source digest; the resume patch preserves trimming and adds validation. Resume checks record three passing tests, exit 0.

Integration records form the serial chain:

`418383fc… → 835f269f… → 62d02770… → 98aeea57… → ea5046c2…`

They identify scoped modules and source-content equivalence. Interim scope is at `98aeea57515a3906f9e2aa33acc57526c56f3acd`; final scope is at `ea5046c2ebaf5aa450095d564284003bc0098347`. Rendering and normalization identities remain unchanged between those scopes; pipeline changes.

Initial/final protected-state fingerprints match. Final state retains `B-reject` spent **2/2**, optional allowance/reservations/attempts **0/0/0**, and no active trial children. Workflow prompts expressly prohibit duplicate analysis and budget resets. The repair adds no launch/retry loop or allowance.

### Correct: bounded behavioral coverage

Actual retained target source implements rendering, trimmed/rejected names, keyword-only uppercase behavior and receipt composition. `executed/target/test_trial.py:6–34` covers those behaviors, including composed rejection.

Interim raw checks report five passing prerequisite tests. Final raw checks report seven passing integrated tests at the final snapshot. This supports the synthetic fixture’s bounded behavior, not general production or GitHub execution claims.

**No issues found.**

**Merge verdict: OK with notes** for the inspected repaired-source/evidence boundary only. Acceptance and publication remain parent-owned.

## Evidence classification and limitations

- **Static inspection:** repaired/historical code, tests, plan, contracts and retained target behavior.
- **Supplied raw-executed evidence:** repaired-source log reports eight offline helper/export/gate tests and four retained-evidence checks passing; evidence-source and package logs report their corresponding passing suites.
- **Historical agent execution:** supported by retained child identities/timestamps, artifacts and checks; not rerun.
- **Not run by this reviewer:** every executable check, fingerprint calculation and live assignment.

The offline gate tests inject denial at the first gate. Later gates share the inspected assertion but were not independently denial-injected in the supplied suite.

Excluded root dispositions and original reviewer conclusions prevent independently certifying historical prerequisite acceptance. Lifecycle ordering proves sequencing, not the semantic contents of root approval messages. Historical source identity is consistent across supplied artifacts; its original runtime copy was not independently authenticated here.

Analysis reuse and zero-call evidence are bounded by prompts, retained manifests/state and tool summaries—not complete observation of internal reasoning or system activity. No process-kill recovery, positive/unknown-charge model transport, live GitHub fixture mutation or installed migration is demonstrated.

## Next action

The root should complete the frozen scope/path comparison, retain this original report separately, and disposition both fresh axes using existing checkpoint history. Preserve historical evidence and label repaired-gate validation as offline-only. No new live replay or optional allowance is warranted by this inspection.