# Spec review — #71 / `bug-to-fix-71`

## Identity, scope and independence

- **Reviewer:** independent read-only Spec subagent, context `3a9386d5-80b8-4092-94dd-df25e2efa52c`.
- **Relationship:** did not author or modify the reviewed changes; did not inspect another reviewer’s conclusions.
- **Authority:** requested review and workflow standing permission; five-minute bound. No modifications, execution, remote access, models or delegation performed.
- **Checkpoint:** root #71, `bug-to-fix-71`. Root declared both scopes frozen.

**Scope A:** supplied synthetic target on `fix/fractional-discount`, base = HEAD = `5fbaa7f0ea2c5f8a5be8f80655848cf2cbf5447a`. Inspected all six included files, `../scope.json`, original ticket, investigation-stop record and raw commands. Did not open `protected.txt` or `protected-link`.

**Scope B:** current untracked `docs/validation/bug-to-fix/{agreement.md,run_fixture.py,run_checks.py,test_handoffs.py,results/}`, against supplied absence at main `c532dc6`. Inspected all listed sources and retained results, including actual patches, target/direct sources and individual check outputs—not totals alone.

Also inspected the permitted repository instructions, composable-delivery design/validation mapping, review contract and delivery execution contract. No searches outside authorized roots.

## Evidence and limitations

- Scope A’s pin identifies staged, unstaged, included untracked and supporting files. The exported patches separately show the staged arithmetic correction and unstaged refactor.
- Final synthetic sources and retained command-input identities are consistent with the supplied pin.
- **No fresh tests, Git inspection or fingerprint calculation were executed by this reviewer.** Live layer identities and final freshness remain the root’s responsibility. Exported patches are supporting evidence, not independently refreshed live Git evidence.
- Package check implementations outside the allowlist were not inspected. Their retained outputs establish reported test executions, not independent verification of their underlying assertions or current source identity.
- Harness phase flags, counters and authorization booleans are authored fixture actions. They do **not** enforce or prove agent behavior.
- This report neither establishes acceptance/merge readiness nor claims live inference or installed changes.

## A — Dirty synthetic fixture: R1/R2

### Correct

- **R1:** `target/pricing.py:1–3` computes subtotal multiplied by the remaining fraction. `target/caller.py:2` retains `.10` fraction units and the original signature, satisfying `target/AGREEMENT.md:2,5`.
- **R2:** zero discount preserves subtotal; empty prices produce zero, including at `.10`. Relevant assertions are in `target/test_existing.py:4–5` and `target/test_discount.py:4–5`, matching `target/AGREEMENT.md:3`.
- **Meaningful red/green:** `../commands.json`, entries “TDD meaningful red,” “TDD minimal green” and “TDD refactor green,” records failures of `99.9 != 90` and `-0.1 != 0`, followed by all four checks passing. “Integrated reproduction passes” records `90.0`.
- **Bounded change:** the staged patch replaces raw subtraction; the unstaged patch only names `subtotal`. No rounding, invalid-input, persistence or API behavior was added.
- **Investigation stop:** original ticket evidence records expected/actual behavior, impact, environment, reproduction, controls, cause, rejected hypothesis, deciding-input hashes, bounded scope, exclusions, risks and regression strategy. `../investigation-stop.json` retains the original product identity and explicitly records no shipped fix.

**No issues found.**

This is an evidence-bounded R1/R2 conclusion, not a complete two-axis acceptance result.

## B — Repository #71 criterion trace

Primary requirements: `docs/validation/bug-to-fix/agreement.md:9–17`.

| Criterion | Inspected evidence and disposition |
|---|---|
| Confirmed investigation stops at complete ticket | `run_fixture.py:139–180` publishes/readbacks local evidence, checks product identity and records the stop. `test_handoffs.py:24–34` checks unchanged bug source, denied fix and absent regression file. **Covered as authored harness behavior.** |
| Authorized fix reuses same evidence without analysis rerun | `run_fixture.py:183–212` requires separate fixture authorization, compares persisted deciding inputs, then builds directly. `test_handoffs.py:36–47` checks unchanged ticket bytes. No diagnostic rerun appears in this delivery function; counters alone are not proof of agent behavior. |
| Real red/green | `results/commands.json` retains specific arithmetic failures and subsequent green runs with input hashes. Actual target assertions and patches were inspected. **Covered.** |
| Clear direct change | `run_fixture.py:216–230`, `results/direct/{display.py,check.py}` and `results/direct.json` show D1 formatting changed with the same check retained; baseline fails and immediate increment passes. **Covered locally.** |
| Useful composition | Characterization preserves intended controls, isolated sensitivity fails for the intended reason, then TDD changes R1/R2. Raw commands substantiate this sequence. **Covered as an authored sequence.** |
| All five methods | Retained outputs show TDD red/green/refactor; prototype cancellation observations and nonproduction disposition; characterization’s intended/defect/unknown separation; acceptance-first workflow/persistence checks and blocked boundaries; build-and-check immediate checks and stopped dependent progress. **Five examples are represented; underlying external assertions were outside this review’s access.** |
| Stale deciding code | `run_fixture.py:233–255` changes pricing, verifies delivery stops before additional checks, then records targeted reproduction at `100.9`. `results/branches.json` retains old-state evidence and affected stale findings. **Covered locally.** |
| Duplicate ticket | `run_fixture.py:256–278` matches retained inputs/cause, reconciles the existing body, preserves identity, labels and graph. Corresponding readback was inspected. **Covered locally; not remote tracker evidence.** |
| Unresolved diagnosis | `results/checks/investigation.txt:2,6` reports unresolved-cause tests passing. **Partial evidence:** deciding implementation/assertions were outside authorized roots. The local trial itself only creates implementation-ready evidence. |
| Allowed/denied mocked model paths | All four retained `ask-*` outputs report named allowance, denial, exhaustion, revocation and fallback tests. **Partial evidence:** no underlying transport-mock assertions inspected; no agent compliance or live-call conclusion follows. |
| Independent dirty review | This assignment supplies actual dirty sources and a pin for independent Spec review. Other axis and root final freshness are not inspected here. **Current Spec evidence only.** |
| PR impact and test/CI/post-merge claims | Direct fixture counts and target test baseline are available, but an admissible decision-ready PR-impact artifact is not present in the scoped results. **Gap; finding S71-1.** |

## Findings

### S71-1 — P1, blocking evidence gap: PR-impact reporting is not established

- **Requirement:** `agreement.md:11,17` requires PR-impact reporting and checking test/CI/post-merge claims against fixture data. The design’s AC12 mapping requires a stated counting baseline, qualified CI evidence, actual merge effects and reversal limits.
- **Evidence:** `run_fixture.py:281–298` exports fixture state, checks, patches and sources; `run_checks.py:13–31` collects method/investigation/model checks. The inspected `results/` inventory contains no PR-impact artifact. `results/direct.json` only counts direct-fixture tests and disclaims delivery acceptance.
- **Impact:** these artifacts cannot establish the requested PR-reporting exercise or validate its CI/post-merge claims.
- **Smallest correction:** provide a source-backed impact record covering the stated baseline, retained/added/changed tests, CI absent/unknown/measured status, effects and reversibility, limitations and documentation disposition. No remote PR action is required.
- **Boundary:** this is missing admissible review evidence, not a claim that an excluded PR draft does not exist.

### S71-2 — P1, fix before publication: retained checks contain workstation paths

- **Requirement:** `docs/agents/project.md:15` prohibits workstation-specific paths in public examples and retained artifacts. `run_checks.py:24` itself states that raw output must exclude them.
- **Evidence:** `run_checks.py:25` only replaces the repository path. Absolute temporary workstation paths remain in `results/checks/tdd.txt:28,75` and `results/checks/build-and-check.txt:8`.
- **Impact:** the newly retained repository evidence violates the portability/disclosure constraint.
- **Smallest correction:** sanitize temporary workspace prefixes when retaining output, regenerate the affected artifacts, and assert retained output contains neither repository nor resolved temporary-root paths. Preserve assertion details and exit results.

### S71-3 — P2, nonblocking evidence-quality note: package checks lack checked-input provenance

- **Requirement:** `agreement.md:12` asks for revisions and evidence; freshness is tied to deciding inputs.
- **Evidence:** `run_checks.py:27–29` records command, cwd, exit and output filename, but no checked package revision, dirty-input fingerprints or environment. `results/checks/summary.json` consequently cannot bind these external package executions to the current sources.
- **Smallest correction:** retain compact source/environment identities for collected package checks. This would make subsequent reuse or invalidation inspectable without interpreting test names as proof.

## Review

- **Correct:** synthetic R1/R2 behavior, meaningful arithmetic red/green, complete local ticket evidence, direct D1 change and useful characterization → TDD composition.
- **Fixed:** none; read-only review.
- **Blocking:** S71-1 prevents treating the scoped evidence as complete #71 verification.
- **Nonblocking:** S71-3; S71-2 requires correction before public retention.
- **Decision findings:** none. No live inference or installation expansion is recommended.
- **Merge verdict:** **BLOCK** for claiming complete #71 verification from this packet; no actual merge or acceptance state is inferred.

**Outcome:** fixture Spec review has no qualifying behavior defect; repository #71 review remains partial because of the reporting gap and bounded package-source access. Root should resolve findings, retain the separate Standards result and perform final freshness comparison before consuming either report.