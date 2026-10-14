# Independent Standards inspection — #72 repaired source

## Scope, independence and identities

Fresh, read-only Standards inspection; separate from authors and other reviewers. No edits, shell commands, tests, network calls, assessments or delegation were performed. Prior conclusions and excluded narratives/reports were not read.

**Agreement:** `review-packet.md`, `plan.md`, synthetic target agreement revision 1; bounded #48 AC2/3/4/10/11/13/15 obligations. Issue excerpts were inspected; live issue bodies were not independently retrieved.

**Snapshot:** supplied `repaired-source-scope.json`:
- Fixed repository base and HEAD: `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`.
- Branch: `test/composable-multi-ticket-recovery`.
- Delivery consists of actual new/untracked sources, not an empty delivery inferred from empty committed/staged/unstaged patches.
- Supplied SHA-256 identities:
  - `trial-workflow.js`: `72922a2cb2f1da9e8ea32b03e320862086a488165a28f255795d2656c494376e`
  - `test_gate.py`: `0fbe28da103b3ff3123ab85072815332ff10ec9e69c927f783e5ded56ab6939e`
  - Historical executed source: `18620d4312dd5ee4144cbdec0c527a774bcccff0e3750b75a62c4595340cc867`
- Root owns the included-source/support freeze and final fingerprint comparison. I did not independently compute hashes.

**Historical execution:** workflow `533be31d-f8e9-4717-98f6-a29043c7c5c1`; fixture base `418383fcddb2d32426a9967d655e48774bbd1073`, final HEAD `ea5046c2ebaf5aa450095d564284003bc0098347`.

## Inspected paths and criteria

Under `docs/validation/composable-multi-ticket/`, inspected:
- Complete `trial-workflow.js`, `source-history/trial-workflow.executed.txt`, supplied `gate-repair.patch`.
- Complete `run_fixture.py`, `export_evidence.py`, `check_evidence.py`, `test_gate.py`, `test_harness.py`, `test_export.py`, `plan.md`, `review-packet.md`.
- All seven retained `executed/target/` files.
- `executed/lifecycle.json`, `tool-audit.json`; first 60 lines of `manifest.json`.
- `executed/evidence/initial.json`, `final-state.json`, `final-scope.json`, `final-delivered.patch`, `final-checks.log`, `B-before.json`, `B-final.log`, `B-partial.py`, `B-resume.patch`, and A/B/D/C integration JSON records.
- Supplied neutral `repaired-source-scope.json`, `repaired-source-checks.log`, `evidence-source-checks.log`, `package-checks.log`.

Primary instructions/contracts inspected:
- `AGENTS.md`; project, workflow, tracker and label guidance.
- Accepted `docs/design/composable-delivery.md`.
- Complete Work On, Work On Spec and Review Delivery entries.
- Work On execution contracts; Work On Spec dispatch/aggregate/recovery; Review Delivery handoff/scope/report references.

Criteria: fail-closed approval, strict result/output types, raw-output configuration, denied/quoted/negated/unsuccessful replies before next-writer launch, regression-test sensitivity, ownership/capacity, serial integration, protected state, retained failure and budget lineage, portability and export safety.

## Review

- **Correct — approval parsing:** `trial-workflow.js:10–19` disables gate artifact output binding and requires literal boolean success, primitive string output and exact trimmed approval token. Denial text containing the token, quoted tokens and appended qualifications do not satisfy this condition. Exceptions stop execution before the next writer.
- **Correct — minimal repair:** the supplied patch changes only gate output configuration and approval validation. Direct inspection of both source versions matches those changes; scheduling and assignment boundaries are unchanged.
- **Correct — meaningful sensitivity:** `test_gate.py:46–77` exercises eight malformed/denied/unsuccessful cases against the actual maintained workflow source and checks the exact launch prefix, excluding B resume. It also demonstrates that the retained historical parser accepts the denied-token case. Positive cases verify progression and `output: false` for every gate.
- **Correct — integration safety:** `run_fixture.py:17–26,212–236` removes inherited Git controls, disables hooks/signing, rejects unexpected worker paths, checks patches before applying and commits only the owned module. Harness tests inspect preservation of unrelated staged/unstaged work and rejection of unintended changes.
- **Correct — bounded historical observations:** retained lifecycle records show fourteen terminal assignments with at most two concurrently active; C starts after both interim reviewers and its dispatch gate settle. Integration records form the serial A→B→D→C chain.
- **Correct — failure remains failure:** retained `B-final.log` records blank rejection failure, nonstring error and exit 1. The partial source retains trim-only behavior. Initial/final records preserve protected-state identities and zero optional allowance; B's final checkpoint records spent 2/2.
- **Correct — scope-conscious retention:** `export_evidence.py:17–80` retains original hashes, sanitizes supplied path prefixes, rejects unresolved workstation paths and exports selected lifecycle fields/tool counts instead of raw sessions or tool arguments. Export tests check original preservation, overwrite refusal and unresolved-path rejection.

**No issues found.**

**Merge verdict: OK with notes** for the inspected repaired source, conditional on root's final freshness comparison. This is not delivery acceptance or publication authority.

## Static versus executed evidence

| Evidence | What it establishes |
|---|---|
| My inspection | Static source/patch correctness and consistency with the named contracts |
| `repaired-source-checks.log` | Reports eight helper tests and four retained-evidence checks passing |
| `evidence-source-checks.log` | Reports four evidence checks and six pre-gate helper tests passing |
| `package-checks.log` | Reports four harness, eight coordinator and eight single-change checks passing; explicitly distinguishes static instruction assertions |
| Historical lifecycle/tool records and fixture logs | Retained observations of actual trial children and checks—not a new execution of repaired orchestration |
| `test_gate.py` Node runner | Offline workflow execution with mocked `runs`; **not agent execution** |

No checks were rerun by this reviewer.

## Limitations and next action

- The offline runner checks that `output: false` is requested; it does not emulate or independently validate the Pi runtime's raw-output semantics.
- Historical source is retained separately and its delta was inspected. The inspected neutral execution records do not independently attest that exact historical workflow bytes were the launch input; lifecycle correspondence is supporting evidence, not cryptographic source-to-run provenance.
- Original gate replies, supervisor approval exchanges, reviewer conclusions and delivery dispositions remain outside this inspection. Terminal status alone does not establish prerequisite acceptance.
- Retained-evidence tests check recorded invariants; booleans such as analysis reuse are recorded claims, not independently established merely by passing those tests.
- No process-kill recovery, positive/unknown-charge assessment accounting, live GitHub fixture mutation or installed migration was demonstrated.
- Full export-manifest integrity was reported by supplied raw checks, not independently recomputed here.

**Next action:** root should complete the frozen-source/support comparison, preserve this report separately, and disposition provenance/runtime limitations alongside the other independent axis. Do not rerun completed live assignments or characterize mocked Node runs as agent execution.