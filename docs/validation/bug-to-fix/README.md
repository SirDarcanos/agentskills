# Bug-to-fix and direct delivery trials

Executed evidence for [#71](https://github.com/SirDarcanos/agentskills/issues/71), under [#48](https://github.com/SirDarcanos/agentskills/issues/48) and the [accepted design](../../design/composable-delivery.md). Audience: maintainer reviewing handoff integrity. This record separates lead actions, authored fixture execution, independent review and unavailable live checks.

## Scope and eligibility

Input repository revision: `c532dc698c68fca7c5496e116ce66ea4af6e325c`. The clean previous branch's PR was merged; this work uses `test/bug-to-fix-handoffs`, based on `main`, targeting `main`. Read-only native observations: #71's parent is #48; its sole blocker is closed #67. Required integration is present: #67's PR [#92](https://github.com/SirDarcanos/agentskills/pull/92) is merged at `330bf0736519b4b96a873050bb542924b1f2fa38`, an ancestor of the input revision. Closure alone was not used as readiness evidence. No issue/label/relationship mutation occurred.

The approved task permits local synthetic artifacts and checks. JSON tracker publication and mock assessment permissions are fixture inputs, not authority to publish real bug tickets or call models. No installed copy, credential, endpoint, service or model-use policy changed. Direct engineering stays with the root lead; only bounded read-only review is delegated under the standing permission. Product meanings/ADRs remain unchanged.

Source procedures were explicitly resolved to this repository, not the older installed names in the runtime catalog: `work-on`, `investigate-bug`, `write-tickets`, all five methods, `review-delivery` and `pr`. Full entries and conditional contracts were inspected. Preflight consumed the installed compatible `implementation-preflight` and the repository's explicit branch policy. [Source identities](results/sources.json) pin the actual shipped entries/references/scripts and task inputs; names alone do not establish compatibility. No missing Analyze or product-intent gap justified a new specialist run.

## Reproduce the trial

Python 3.9+ and Git; no dependencies to install. From repository root, use a **new** disposable directory. The harness refuses to initialize an existing workspace. It strips ambient `GIT_*` routing/configuration and disables Git templates/hooks; no remote is created.

```sh
scratch=$(mktemp -d)
trial="$scratch/run"
python3 -B docs/validation/bug-to-fix/run_fixture.py init "$trial"
python3 -B docs/validation/bug-to-fix/run_fixture.py investigate "$trial"
# Inspect ticket.json, investigation-stop.json and commands.json before continuing.
python3 -B docs/validation/bug-to-fix/run_fixture.py branches "$trial"
# This flag models the separately authorized fixture fix, not real consent detection.
python3 -B docs/validation/bug-to-fix/run_fixture.py deliver "$trial" --authorize-fix
python3 -B docs/validation/bug-to-fix/run_fixture.py direct "$trial"
python3 -B docs/validation/bug-to-fix/run_fixture.py export "$trial" --output "$scratch/export"
python3 -B docs/validation/bug-to-fix/run_checks.py
```

`run_checks.py` refreshes repository evidence under `results/checks/`; it uses the existing package fixtures and mock-only assessment tests. Commands are finite (10 seconds per trial subprocess; 90 seconds per check job). These scripts execute authored actions/assertions; they are **not** another implementation of the skill procedures, an autonomous scheduler, a permission engine or proof that arbitrary agents follow instructions. The lead actually invoked the separated phases, inspected their raw returns and selected the next handoffs in this session.

## Executed handoffs and observations

[Commands and raw outputs](results/commands.json), [persisted original ticket](results/ticket.json), [investigation stop](results/investigation-stop.json), [state](results/state.json), [branch observations](results/branches.json) and [final fixture](results/target/AGREEMENT.md) retain evidence. Original ticket and duplicate read-back remain separate history.

1. **Investigation only:** baseline controls passed. A real call with `[40, 60]` and `.10` failed on `99.9 != 90`, not import/tool setup. The bounded control experiment returned `[100, 99.9, 99.8]` for discounts `[0, .1, .2]`; inspection established raw-fraction subtraction in `pricing.py:2`, rejecting a caller-unit mismatch. The complete local JSON ticket includes contract/environment, cause/input hashes, fix/exclusions/risks, regression acceptance and method recommendation. It was read back with standalone `bug` classification, no artificial hierarchy or ready label. Product digest stayed unchanged; no fix shipped.
2. **Authorized delivery from that evidence:** the lead checked every supplied deciding input and consumed the original ticket. No new cause experiment, Analyze or investigation invocation occurred. The root selected `characterize → tdd` because preserving existing zero/empty behavior is useful before correcting fraction handling. The reproduction retained its old-state failure; new development checks are not repeated investigation.
3. **Characterize:** two existing intended controls passed. An isolated subtotal perturbation failed both controls (`101 != 100`, `1 != 0`), proving sensitivity. The actual product stayed untouched by that experiment. The known discount defect was a non-protecting reproduction, never a preservation requirement. Inputs are deterministic; no normalization or repeat-until-green was used.
4. **TDD:** two new boundary tests failed for fraction and empty-fraction behavior; minimal green passed all four checks. A staged green implementation was then refactored to name `subtotal`; four checks remained green and the original reproduction returned `90.0`. Planned development red/green is not an acceptance-repair episode; zero repair cycles spent.
5. **Clear direct change:** the lead selected `build-and-check` for formatting `90` as `Total: 90.00`. The existing executable assertion failed at baseline, then immediately passed after one implementation-first increment. It was reused unchanged (zero added/removed/updated checks). [Before/after manifest](results/direct.json) supplies non-Git identities. This presentation fixture adds no currency-rounding contract.
6. **Stale deciding code:** a separate workspace changed the implementation itself, not just HEAD/caller metadata. Delivery stopped on the deciding-input mismatch before test additions or a fix. One targeted observation returned `100.9` versus `90`; agreement identity remained current. Dependent reproduction/cause completeness/fix applicability are stale; old evidence and the unaffected contract are retained. The next action is bounded cause reassessment, not complete rediscovery or speculative repair.
7. **Duplicate:** a complete local search matched retained symptom/cause/identities, reconciled the canonical JSON issue body and read it back. One ticket remained, with labels and graph preserved. This matches the original pre-fix evidence, not a claim that the delivered code still reproduces the defect.
8. **Unresolved diagnosis:** reran the existing seven investigation cases. `test_confirmed_unresolved_cause_remains_investigation` confirms the synthetic symptom but supplies no deciding source/cause, persists explicitly investigation-only work with a bounded next action, and asserts unchanged product/protected bytes. Intermittent, unconfirmed and harness-failure cases also ran. These are executed authored branch fixtures, not another live agent investigation.

## All-five method reconciliation

| Method | Actual #71 execution | Result and limits |
| --- | --- | --- |
| `tdd` | New composed pricing trial; existing package script rerun | Meaningful red, minimal green and refactor green; existing reuse and anti-oracle checks passed |
| `characterize` | New pricing baseline/sensitivity before TDD; existing five-case script rerun | Intended invariants protected, defect not preserved; unknown/nondeterminism/sensitivity fixture checks passed |
| `build-and-check` | New direct display change; existing four-case script rerun | Immediate checked increment; package failed-check stop/coverage reuse/non-code examples passed |
| `prototype` | Existing runnable transition experiment rerun and inspected | Two cases support absorbing cancellation; bound-limited result inconclusive; counter-hypothesis rejected. No concurrency/persistence/UX/production acceptance claim; owned artifact disposition assertions passed |
| `acceptance-first` | Existing five-case API→SQLite example rerun and inspected | Receipt/persistence and rejection/no-side-effect examples have red→green observations. Unknown duplicate intent remains blocked; unavailable real payment remains unverified, not a mocked integration pass |

The useful new sequence is characterization followed by TDD under one owner, authority record and checkpoint. The prototype and acceptance-first reruns are separate synthetic examples, **not** a claimed prototype-to-production handoff. [Check summary](results/checks/summary.json) links every command/exit/raw result. Totals: 183 named unittest cases plus the prototype's bounded subprocess experiments; totals are not acceptance evidence by themselves.

## Optional assessment mocks

All four existing named-package suites reran: Nimble 37, Clef 40, Clef Flash 40, Jev 36. Their approved-policy fixture cases exercise exact allowed mocked transport; absent/none/conflicting/expired, wrong-route/disclosure, exhausted/reserved/unknown budget, generated-command and pre-send revocation cases assert no forbidden send. Shared child/resume allowances, retries/correction ceilings, unavailable/insufficient-data and service ownership remain covered by package assertions. See the named test output under [checks](results/checks/summary.json) and pinned source identities, rather than inferring policy from test names alone.

The real repository still has **no approved model-use policy**. Actual optional assessment calls, live inference, service starts, external sensitive payloads, downloads and substitutions: zero. Reviewer-agent execution is separately authorized review, not an optional assessment service. Mock tests establish only their modeled transport and caller-decision cases; they cannot prove behavior of a live provider or every future lead.

## Independent dirty-work review

The root freezes the actual disposable Git target and supporting checks. Scope includes staged `pricing.py`, its unstaged refactor, untracked reproduction/regression tests and unchanged caller/control/contract. The scoped committed diff is empty; that does not erase dirty delivery. Unrelated staged+unstaged content, mode and symlink target are excluded/protected and compared separately by the root. The maintained `review-delivery/scripts/snapshot.py` captures base/HEAD, layers, index, final modes/content and untracked support. Reviewers receive real files/diffs/raw checks, not hashes alone.

Two fresh read-only reviewer contexts cover separate Standards/Spec axes and the same fixture plus new validation source, without author/other-axis conclusions. Root ledger: at most two active workers, five-minute runtime each, no recursive delegation or optional models. A first parallel-call schema rejection launched zero workers; the same runtime was retried with a scripted workflow, not an execution-mode fallback. [Initial original Standards](results/reviews/initial-standards.md) and [Spec](results/reviews/initial-spec.md) reports are retained unchanged. Both found no fixture R1/R2 defect. They identified leaked temporary paths in the collector, missing admissible PR-impact evidence and weak package-source provenance. Root repair cycle 1 for checkpoint `bug-to-fix-71` normalizes scratch paths, adds a collector regression/source fingerprints, and supplies the two PR reports plus underlying package assertions for renewed review. The pricing fixture itself is unchanged; its development repair count remains zero. [Initial freshness](results/initial-freshness.json) confirms helper matching, repeated candidate membership and separately protected index/content/mode/link identities. The [public snapshot](results/dirty-scope.json) replaces only the private root with `<workspace>/target`; its original hash is retained, and this portable copy is not directly executable without relocating that root. Review remains advisory and grants no merge or maintainer acceptance.

### Final review and disposition

[Renewed Standards](results/reviews/final-standards.md) and [Spec](results/reviews/final-spec.md) reports are retained byte-for-byte, with [identity/hash receipts](results/reviews/receipts.json). Neither has a blocking finding. Underlying method/investigation/assessment assertions and both PR-impact reports were supplied in the renewed neutral packet; prior reports and this retrospective narrative were excluded. Worker run identities are separate, with the same shared two-slot root ledger and no nested launches.

[Final freshness and gate record](results/final-freshness.json) compares every reviewed file/membership, package-check inputs and all supporting source hashes, repeats actual Git candidate discovery and scope-helper comparison, and checks protected content/index/mode/link state. All matched. No target writes occurred during either review. Reviewers performed static inspection of root-executed raw checks, not independent test reruns or Git hash calculations; the root performed those freshness calculations.

Standards note `STD-71-1` remains a **nonmaterial collector limitation**: the two per-job manifests omit the imported tracker fixture. Its identity is separately pinned in `sources.json`, was directly inspected by both renewed reviewers and was compared unchanged by the root. This run therefore has no missing deciding source. The narrow future improvement is to include that dependency in each job's manifest; until then, those job records alone must not justify reuse. No new ticket, acceptance change or claim of a general dependency resolver follows this note.

Build gate passed for the approved local trial. All material local checks/review obligations have current evidence, so the root recommends **ready to accept** with the stated nonblocking note; this is not maintainer acceptance or merge. Report gate passed. One automatic repository evidence-repair cycle was spent on the original findings; none on the product fixture. Installed/live/hosted obligations remain excluded/unrun, not passed. Completion appendices/report disposition were added after the review freeze ended; they change no checked source, behavior or assertion and are lead-inspected reporting, not a newly independently reviewed implementation.

## Reporting, documentation and remaining checks

[Fixture PR report](fixture-pr-report.md) accounts for the synthetic two→four named-test baseline, unchanged CI absence, actual merge effects and reversal limits. [Repository PR draft](pr-report.md) accounts for the actual validation-only change. No CI jobs/hooks, deployment, release or installed migration were added. Local elapsed unittest times are not hosted CI/compute measurements; no speedup or billing claim is made.

Documentation affected: this execution record, issue-body input copy, raw results and PR reports. Source skills, public listings, design/ADR/domain vocabulary and operating policies are unchanged. Changelog: no entry because this delivers repository-only validation evidence, not new public skill behavior. Release-impact label: none. Package frontmatter/isolated-copy changes are inapplicable to unchanged packages; assessment suites still execute their existing package checks.

Not run: real GitHub bug-ticket publication, hosted CI, payment integration, participant/visual UX checks, live assessments, installed discovery/migration or multi-ticket scheduling (#72). They are excluded or belong to their designated later trial; synthetic passes are not evidence for them. #71 stays open pending maintainer acceptance and merge. Build/report readiness can be stated separately from review freshness and acceptance.

Final direct document checks rendered eight Markdown files with Marked, resolved 26 relative targets, parsed every retained JSON artifact and scanned public artifacts for personal/workstation paths. No credential/private-data or symlink/history change was found in the scoped diff. A surplus EOF newline in the copied issue body was normalized after review; its content/authority/acceptance are identical, with old/new identities and retained-review rationale recorded in final freshness. The affected seven handoff regressions were refreshed on that exact input. Reporting-only appendices and review receipts do not change the checked implementation or assertions.
