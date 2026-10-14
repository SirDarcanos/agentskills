# #72 evidence-delivery Standards review

## Scope and independence

Independent, read-only Standards review of the new `docs/validation/composable-multi-ticket/` delivery—not a repeat fixture-behavior verdict.

- Agreement: #72 body SHA-256 `13ed5c7632663e063c2ea0d65ae7a3078abd509cea43575adc6362cace42c456`; bounded parent #48 body SHA-256 `a9171d6dbc63530e1ab33acb4aa8ac08653ea17abecd59d4564d6a38454f9f4e`.
- Criteria considered: bounded AC2/AC3/AC4/AC10/AC11/AC13/AC15, especially authority, safe isolation/integration, negative checks, retention, independent review and evidence classification.
- No edits, shell execution, tests, staging, network, optional assessments or delegation performed.
- Excluded reports, ledger, narrative dispositions, historical validation and the other axis’s conclusions were not read. Their hashes/path metadata were not treated as access permission.
- Root owns final freshness comparison, disposition and publication. This report has no acceptance or merge authority.

## Inspected inputs

Paths below use `V = docs/validation/composable-multi-ticket/`.

**Delivered sources, read fully:**  
`V/review-packet.md`, `plan.md`, `run_fixture.py`, `trial-workflow.js`, `export_evidence.py`, `check_evidence.py`, `test_harness.py`, `test_export.py`; supplied `evidence-source-delta.patch`, read through its final line.

**Policy and execution contracts:**  
`AGENTS.md`; `docs/agents/{project,workflow,issue-tracker,triage-labels}.md`; `docs/design/composable-delivery.md`; complete Work On, Work On Spec and Review Delivery entries; Work On contracts/build/verification/completion/recovery; Work On Spec dispatch/aggregate/recovery; Review Delivery handoff/scope/report; Implementation Preflight and Build and Check entries.

**Neutral retained evidence inspected directly:**

- `V/executed/{lifecycle,tool-audit,manifest}.json`
- All seven `executed/target/` files
- `evidence/{initial,final-state,B-failure-scope,B-resume-before,B-resume-after,interim-scope,final-scope,final-support}.json`
- `evidence/B-partial.py`
- A/B/D/C integration records and patches
- `evidence/{final-delivered.patch,B-final.log,D-interface.log,interim-checks.log,final-checks.log}`
- Supplied `evidence-source-scope.json`, `evidence-source-checks.log` and `package-checks.log`

This is not an exhaustive content audit of every allowlisted artifact.

## Snapshot identities

### Repository delivery

The supplied pin identifies:

- Fixed base and HEAD: `c3bd79eb42918ccdb41b126f48a5b8b15a1bdd12`
- Branch: `test/composable-multi-ticket-recovery`
- Committed, staged and unstaged tracked deltas: empty
- New source content: untracked, inspected directly—not dismissed as an empty delivery

Source SHA-256 identities recorded in that pin:

| Source | SHA-256 |
|---|---|
| `run_fixture.py` | `d6f2ba914faa98d852822131e104adf1def6c6852e378761da9b5be265d6a3bc` |
| `trial-workflow.js` | `18620d4312dd5ee4144cbdec0c527a774bcccff0e3750b75a62c4595340cc867` |
| `export_evidence.py` | `da25cd23b889a04468d6ecdfd50bb5e5b892a56ad6dc1f5071a6bdf368da0635` |
| `check_evidence.py` | `d0b49eddd221b6ee55ca2fd2affcf1ce7c13b521c1dfc7fd98b1332d4ccf14e0` |
| `test_harness.py` | `a6bcd566d07727322e088a41d39d5c55df7f9c9cdf781cc1e789301bc0bab581` |
| `test_export.py` | `d5dd1edf2aabec20fb7fe775149b883c1b276c198624075cbcc9c92a0a62fcc5` |

These are supplied identities, not reviewer-computed hashes.

### Executed fixture

- Workflow: `533be31d-f8e9-4717-98f6-a29043c7c5c1`
- Fixture base: `418383fcddb2d32426a9967d655e48774bbd1073`
- Integration chain: base → A `835f269f4069279a577d78da741cdf41407ccb43` → B `62d027704c60ec789e96bb177b6705fe69572d2d` → D/interim `98aeea57515a3906f9e2aa33acc57526c56f3acd` → C/final `ea5046c2ebaf5aa450095d564284003bc0098347`
- Final delivered-patch SHA-256: `2a8cb7a4bd0da1a55db75cd577f3e35f32c09b19d28341176fccca402d8e3af5`

The final-support scope hash references the original snapshot bytes. The export manifest explicitly distinguishes original and path-sanitized retained scope hashes; that difference is not evidence of unexplained drift.

## Evidence classification

### Static inspection

- Git fixture operations remove inherited `GIT_*` controls, disable system/global Git configuration and hooks, and seed with an empty template (`run_fixture.py:20–28, 142–153`).
- Integration is module-scoped, checks worker path inventory, checks indexed patch application, commits only the module and compares protected fingerprints before/after (`run_fixture.py:207–233`).
- Workflow assignments have exclusive modules, fresh contexts, 600-second bounds, no recursive launches and explicit zero optional-assessment authority.
- Negative tests cover unexpected worker edits, consumed-patch reapplication, preserved failed checks, unresolved workstation paths and export overwrite prevention.
- Export records original/retained hashes and selects lifecycle fields/tool counts rather than publishing raw sessions. It is explicitly path-only sanitization, not a general secret scrubber or syscall attestation.
- Replay verifies retained consistency; it does not rerun agents or independently establish every recorded history assertion.

### Raw-executed evidence read

- Lifecycle contains fourteen started/settled children, peak concurrency two, terminal outcomes before later ownership stages, and durations below 600 seconds.
- B’s partial log records an actual rejection failure and nonstring error with exit 1. Its preserved source is trim-only; resumed manifests retain that starting increment and show only `normalize.py` changed with the index unchanged.
- Initial/final protected fingerprints match. Recorded optional allowance/reservations/attempts remain zero; `B-reject` finishes at spent 2/limit 2.
- Integration records form the serial chain above. Final scope changes pipeline content while retaining interim rendering/normalization identities.
- Interim log records five passing tests; final log records seven passing integrated tests, command, environment, checked base/HEAD and exit 0.
- Supplied source-check log records four replay checks and six helper/export checks passing. Package-check output is separately classified as offline/static evidence, not runtime-adherence proof.

None of these checks was rerun by this reviewer.

## Review

### Correct

The delivery is narrowly separated from production skills and installed copies. Manual fixture tooling, authorized agent execution, retained replay and offline tests have distinct purposes. Protected dirty/index/link state, failed partial work, serial integration and refreshed review snapshots have inspectable evidence rather than only narrative claims.

### Finding ES-01 — P1, blocking: denied gate text can authorize the next stage

**Source:** `V/trial-workflow.js:13–17`, used before writable resume/D/C stages at lines 24, 27 and 39.

**Observed static behavior:** The gate contract requires explicit root approval; otherwise the child returns `BLOCKED` with the reason. However, `assertGate` accepts any successful child output containing the approval token:

```text
result.ok = true
result.output = "BLOCKED: parent did not send ROOT_APPROVED_NEXT_STAGE"
```

That output satisfies the current substring test and does not throw.

**Rationale:** Successful child execution is distinct from approval. A compliant denial that quotes the expected token can therefore advance scheduling despite the root withholding permission. In particular, the dependent-dispatch gate can launch C without accepted prerequisite integration. This contradicts the workflow’s own gate contract and the root-owned eligibility/authority requirements in Work On Spec dispatch and the shared execution contract.

**Evidence boundary:** This is a source-proven failure path, not a claim that it occurred in the retained trial. Prior gate conclusions were not inspected.

**Smallest correction:** Require the complete normalized output to equal `ROOT_APPROVED_NEXT_STAGE`, rather than contain it. Add an offline negative check rejecting `BLOCKED` text containing the token, quoted/negated tokens and unsuccessful child results.

**Renewal:** Refresh source tests/pin and review the changed gate. No repeat live-agent trial is needed merely to demonstrate this string-validation failure.

- **Fixed:** None; review-only.
- **Merge verdict:** **BLOCK** on ES-01. Root retains disposition authority.

## Gaps and next action

- Root’s final source/support fingerprint and path-discovery comparison remains pending; this reviewer cannot certify freshness after returning.
- Tool counts do not prove shell argument safety, absence of network/syscall effects or every required source read. Endpoint booleans do not independently reconstruct the entire repair/model ledger.
- Full privacy inspection of excluded reports and ledger is outside this review. Their manifest entries establish metadata, not content safety.
- Process-kill recovery, positive/unknown-charge model transport, live GitHub mutation and installed migration remain expressly untested. Portability beyond the recorded macOS/Python/Git environment was not executed.
- No production mutation was observed in the inspected sources/artifacts; absolute zero-effects attestation is unavailable from summarized tool records.
- No public skill behavior, domain meaning or release source changes are indicated; a changelog change is not established as necessary.

**Next action:** Root should correct ES-01, run the bounded offline gate-negative checks, refresh affected source evidence, obtain the necessary renewed inspection, and perform the final freshness comparison before disposition/publication.
