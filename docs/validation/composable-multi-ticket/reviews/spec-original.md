# #72 evidence-delivery review — Spec axis

## Agreement, independence and scope

Independent, read-only review of the new evidence delivery, **not a repeat behavioral acceptance verdict**.

- Fixed repository base/HEAD: `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`.
- #72 body digest: `13ed5c7632663e063c2ea0d65ae7a3078abd509cea43575adc6362cace42c456`.
- #48 body digest: `a9171d6dbc63530e1ab33acb4aa8ac08653ea17abecd59d4564d6a38454f9f4e`.
- Criteria: bounded AC2/3/4/10/11/13/15 as supplied in the fully inspected `review-packet.md`.
- Authority: approved disposable local trial; this reviewer has inspection authority only, a 600-second bound and no recursive delegation.
- No edits, shell commands, tests, network, staging or optional assessments performed.
- Excluded reports, ledger, narrative README/dispositions and historical validation were not read or searched. Manifest entries naming them were treated only as metadata.

## Inspected files

Within `docs/validation/composable-multi-ticket/`:

- Complete `review-packet.md`, `plan.md`, `run_fixture.py`, `trial-workflow.js`, `export_evidence.py`, `check_evidence.py`, `test_harness.py`, `test_export.py`.
- `executed/lifecycle.json`, `tool-audit.json`, `manifest.json`.
- All seven retained `executed/target/` files.
- `evidence/initial.json`, `final-state.json`, `B-failure-scope.json`, `B-partial.py`, `B-partial.diff`.
- A/B/D/C integration records and patches; A/B/B-resume/C before/after manifests; D entry/final manifests.
- Interim/final scope, support and delivered patches.
- A baseline/final, B failed/resume baseline/resume final, D baseline/interface/final B/final D, C baseline/full, interim/final checks and target full-suite baseline/final logs.

Supporting contracts inspected:

- Repository `AGENTS.md`; project, workflow, tracker and label guidance.
- Accepted `docs/design/composable-delivery.md`.
- Complete Work On Spec, Work On, Review Delivery, Implementation Preflight and Build and Check entries.
- Work On contracts/build/verification/completion/recovery.
- Work On Spec dispatch/aggregate/recovery.
- Review Delivery handoff/scope/report.

Additional supplied inputs inspected completely: `evidence-source-scope.json`, `evidence-source-delta.patch`, `evidence-source-checks.log`, `package-checks.log`.

## Snapshot identities

The supplied source pin identifies branch `test/composable-multi-ticket-recovery`, unchanged repository HEAD, and empty committed/staged/unstaged patch fingerprints. The supplied addition patch and actual files establish a **new untracked delivery**, not an empty change.

Selected source SHA-256 identities from that pin:

| Source | SHA-256 |
|---|---|
| `run_fixture.py` | `d6f2ba914faa98d852822131e104adf1def6c6852e378761da9b5be265d6a3bc` |
| `trial-workflow.js` | `18620d4312dd5ee4144cbdec0c527a774bcccff0e3750b75a62c4595340cc867` |
| `check_evidence.py` | `d0b49eddd221b6ee55ca2fd2affcf1ce7c13b521c1dfc7fd98b1332d4ccf14e0` |
| `plan.md` | `ed96b3079387ac5b792058b3f395f632a33e45304ebe2881eb561d4ae37166fd` |
| `review-packet.md` | `c9cd772c07ae2c204cc190aabece40a841d72f68f0320f22ad77989a5ee4358d` |

Fixture integration chain, inspected directly:

```text
418383fcddb2d32426a9967d655e48774bbd1073  initial
835f269f4069279a577d78da741cdf41407ccb43  A
62d027704c60ec789e96bb177b6705fe69572d2d  B
98aeea57515a3906f9e2aa33acc57526c56f3acd  D / interim review
ea5046c2ebaf5aa450095d564284003bc0098347  C / final review
```

Retained scope hashes:

- Interim: `39c8e14e3747087ad4186d7fcbd889d8a1fe23a7ea319f4ad521e7d1983cda7f`.
- Final: `11b31a5444b73ba1f04d2fd2c63d0097f444bc182ae8b1070094f8366138f601`.

The support records name **original** scope hashes; `manifest.json` explicitly maps those to different retained hashes after path sanitization. This difference is explained, not evidence of scope drift.

Current review freshness comparison belongs to root. I inspected the supplied pin but did not independently compute hashes or perform its final comparison.

## Criterion trace

| Criterion | Evidence and bounded conclusion |
|---|---|
| **AC2** | `trial-workflow.js:5–9,19–26,39–40` assigns one module per Work On worker. Actual patches and manifests show A→`render.py`, B/resume/D→`normalize.py`, C→`pipeline.py`. The local graph identifies P as a spec; lifecycle contains no P implementation assignment. Root retains overall coordination. |
| **AC3** | Workflow assignments leave compatible method/check selection inline and reserve integration/dispatch decisions to root gates (`trial-workflow.js:11–18,23–28,38–42`). Integration records form one serial target chain, each with one owned path and source-content equivalence. Gate audit entries contain only `contact_supervisor`. |
| **AC4** | Supplied `target/technical.md:1–12` remains identical across manifests. B-resume begins with the same partial content recorded at failure and adds validation rather than rebuilding A. D starts from integrated B; C starts from integrated D. Interim/final scopes preserve render/normalize while changing pipeline; fresh full integrated checks and new reviewer contexts follow C. No duplicate A assignment or specialist launch appears. This supports targeted reuse, not exhaustive attestation of workers’ internal reasoning. |
| **AC10** | Assignments prohibit optional assessments; initial/final optional allowance, reservations and attempts are all zero. Tool audit lists no `ask-*` calls. This establishes the bounded zero-call record, not positive-policy or transport certification. |
| **AC11** | Facts come from actual module patches/tests and retained check outputs, with separate reviewer lifecycle identities. No optional assessment result substitutes for checks. Tool names and zero counters support the stated restriction; shell arguments and syscalls are not retained, so they cannot prove universal absence of disclosure/service activity. |
| **AC13** | Persisted graph contains B/D→C blockers in both directions. Lifecycle confirms terminal B-partial before resume, terminal B-resume before D, and both interim axes plus dependent-dispatch gate terminal before C. Source bases corroborate actual integrated prerequisites. Protected target fingerprints match initially/finally, including bytes, index, modes and link target. B checkpoint remains `B-reject`, ending spent=2/limit=2; assignment text explicitly carries cycle one into cycle two. |
| **AC15** | Helper docs and replay source explicitly separate local fixture operations, runtime assignments and offline replay. Raw failures/passes are retained; plan and final-state limitations explicitly exclude process-kill recovery, live GitHub fixture mutation, positive/unknown-charge transport and installed migration. Existing package checks are not presented here as another agent run. |

### Lifecycle inspection

Trial workflow ID: `533be31d-f8e9-4717-98f6-a29043c7c5c1`.

The 28 retained start/terminal events account for fourteen children: five writable assignments, five coordination gates and four reviewers. Manual event inspection shows:

- Peak active children: two.
- All fourteen terminal outcomes: `completed`.
- Longest recorded child duration: approximately 140.38 seconds, below 600 seconds.
- Workflow first-start to last-terminal: approximately 1,057.59 seconds, below the planned 3,600-second bound.
- B-partial terminal `1791990591370` precedes B-resume start `1791990652772`.
- B-resume terminal `1791990792713` precedes D start `1791990846573`.
- Both interim axes and dependent-dispatch gate terminate before C start `1791991249499`.
- Final reviewers begin after aggregate-review gate terminal `1791991437681`.

`completed` means runtime termination, **not successful implementation or acceptance**: B’s raw check still failed.

## Evidence classification

### Static inspection

- Workflow scope, ownership, timeout and gate instructions.
- Actual helper/test implementation and neutral addition patch.
- Graph roles/edges, module changes and preserved partial implementation.
- Scope relationships and recorded integration equivalence.
- Replay assertions: several verify recorded booleans/counters or report existence; they do not independently establish underlying history or reviewer conclusions.

### Raw executed evidence inspected

- A: missing-behavior baseline failure, then one test passing.
- B partial: trim succeeds; blank rejection fails and nonstring input raises the wrong exception; exit 1.
- B resume: preserved failure baseline, then three tests passing; exit 0.
- D: unsupported `upper` baseline failure; final B and D checks pass.
- C: unimplemented baseline failure; full seven-test local suite passes.
- Integrated prerequisite suite: five tests pass.
- Final integrated suite: seven tests pass at final HEAD, with command, environment and patch retained.
- Supplied source-check log: four evidence replay tests and six exporter/harness tests pass.
- Supplied package log: fixture/package checks pass, explicitly distinguishing static instruction assertions from runtime adherence.

These are inspected execution records, not checks performed by this reviewer. Replay is not an agent run.

### Not run / not independently established

- Any fresh helper, package, replay or runtime execution by this reviewer.
- Process termination/kill recovery.
- Positive optional-model calls, retries or unknown-charge accounting.
- Live GitHub fixture API/pagination/mutation.
- Installed discovery or migration.
- Syscall-level verification of workers or root.
- Current remote issue bodies, native predecessor observations or merge ancestry.
- Original reviewer conclusions and root dispositions, intentionally excluded.

## Review

- **Correct:** Neutral evidence supports the bounded assignment topology, failed partial/resume, serialized shared interface, delayed dependent, serial integration and refreshed aggregate checks/reviewer starts. The source and retained limitations avoid conflating these with stronger excluded claims.
- **Fixed:** None; read-only review.
- **Findings:** No issues found.
- **Merge verdict:** **OK with notes** for this bounded evidence-delivery inspection only; this is not acceptance, publication or merge authority.

## Gaps and next action

1. **Historical disposition remains root-owned.** Lifecycle proves reviewer completion and ordering, not report adequacy, original findings, prerequisite acceptance or final root disposition. Root must inspect the excluded originals separately before relying on acceptance.
2. **Budget history is bounded evidence.** B’s explicit assignments, preserved partial state and final counters support its two-cycle lineage. The neutral record does not explain the final-integration spent=1 lineage in detail; its truth must not be inferred merely from the replay assertion.
3. **Tool audit is deliberately limited.** Counts omit shell arguments and sessions. `analysis_reused` and unchanged-source booleans are supporting declarations, not exhaustive proof of every action.
4. **Predecessor history is supplied, not independently verified here.** `plan.md:9` names #68 integration/native observations; this review performed no network or ancestry check.
5. **Freshness remains pending root comparison.** Preserve this report separately, finish the frozen source/support/path comparison across both current axes, and invalidate affected evidence if anything changed.

No shipped skill behavior, domain meanings or release source changes were inspected in this delivery; no corresponding changelog change is required by the stated scope. Root alone owns disposition and authorized PR publication.
