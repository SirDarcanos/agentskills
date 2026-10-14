# Standards review — bug-to-fix-71

## Identity and boundaries

Fresh read-only Standards reviewer, independent of the authors and other review conclusions. Authority: this assignment and `docs/agents/workflow.md`’s standing independent-review permission; five-minute bound.

No files edited, commands executed, delegation launched, assessments invoked, or network/services used. No prior axis reports, retrospective README content, or protected target contents read.

## Agreement and snapshot

- Repository #71 agreement: `docs/validation/bug-to-fix/agreement.md`; repository input revision `c532dc698c68fca7c5496e116ce66ea4af6e325c`.
- Synthetic product agreement: target `AGREEMENT.md`, R1/R2; separate direct-change D1.
- Synthetic base/HEAD: `5fbaa7f0ea2c5f8a5be8f80655848cf2cbf5447a`.
- Inspected all six actual included target files, original private scope pin, portable exported pin, staged/unstaged pricing patches, status, original and exported command records.
- The two pins agree in their listed fields except the intentional root normalization. Root supplies the scoped-write freeze; final freshness remains the root’s responsibility.

Synthetic R1/R2 correctness is not repository #71 acceptance, production payment validation, or permission to merge.

## Inspected coverage and evidence

Inspected the three trial Python sources, both PR reports, named result artifacts and all eleven raw check outputs. Underlying assertion inspection covered all five method fixtures, investigation cases, tracker fixture, Nimble authorization simulation, Clef/Clef Flash authorization seams, and Jev procedure/tests. Standards included project/workflow/tracker guidance, accepted composable-delivery design and validation mapping, review contracts, PR impact accounting, and delivery execution contracts.

### Correct

- **Real behavioral red/green:** actual `test_discount.py:4–5` asserts fraction and empty-fraction outcomes. Raw commands show `99.9 != 90` and `-0.1 != 0` before repair, then four tests and reproduction passing. Actual `pricing.py:1–3` implements the bounded contract without changing the caller’s units or function signature.
- **Investigation stop and reuse:** `run_fixture.py` persists reproduction, cause, deciding-input identities, exclusions and regression strategy before delivery. Its delivery checks authorization and input freshness before writes. Executed harness assertions verify denied delivery adds neither commands nor regression files and that ticket bytes survive the authorized composition unchanged.
- **Branch handling:** stale deciding code stops delivery before checks/writes; retained observation reports `100.9`. Duplicate reconciliation preserves identity, labels and graph, explicitly labeling evidence pre-fix. Underlying investigation assertions keep confirmed-but-unresolved and unconfirmed cases investigation-only.
- **Useful composition and all-five evidence:** characterization protects intended controls, including an isolated sensitivity failure, before meaningful TDD. Separate examples exercise bounded prototype dispositions, acceptance-first SQLite persistence/rejection failures, and immediate build-and-check validation. D1 reuses its unchanged check across failure/pass.
- **Authority:** policy-enabled/denied assessment paths are mock procedure simulations, not approved real consultations. Inspected assertions check zero denied effects, exact allowed payloads, exhausted/revoked authority and retained shared budgets. Reports appropriately disclaim autonomous compliance, live inference, installation and acceptance.
- **Privacy/portability:** `run_checks.py:13–20` replaces repository and both temporary-root spellings. The executed collector regression retains the diagnostic assertion while scrubbing an external temporary path. Retained raw outputs inspected contain placeholders rather than workstation roots. Export uses explicitly named synthetic files and excludes protected target files and `.git`.
- **Impact reporting:** both reports distinguish named-test changes from fixture observations, local timings from unavailable hosted measurements, source reversal from external effects, and report completion from acceptance/merge. Repository-only validation reasonably requires no public skill changelog or release-impact label.
- **Complexity:** the scripts are explicitly authored, phase-separated fixtures—not a new workflow engine, policy parser or installation service.

## Finding

### STD-71-1 — P2 / nonblocking: checked-input records omit an executed dependency

**Location:** `docs/validation/bug-to-fix/run_checks.py:23–31,46–59`.

The collector fingerprints only each job’s selected directory. However:

- `run_fixture.py:103–107` imports `docs/validation/write-tickets/tracker_fixture.py`.
- `docs/validation/investigate-bug/test_investigation.py:12–15` imports that same external fixture.

Consequently, the `handoffs` and `investigation` records in `results/checks/summary.json` omit executed tracker code from both `checked_inputs` and their before/after comparison. Changing that dependency would not make their `inputs_unchanged` false.

**Requirement:** `work-on/references/contracts.md`, “Lead evidence record,” requires the exact checked state; `review-delivery/references/scope.md` requires relevant supporting/check-input fingerprints.

**Smallest correction:** add the explicit tracker dependency to those two jobs’ before/after manifests, then rerun the affected collection. No recursive dependency framework is needed.

**Why nonblocking:** `results/sources.json` separately identifies the tracker fixture at the input revision, its source was available for direct inspection, and the root freezes supporting sources. This is a collector provenance limitation, not evidence that these executions used stale code.

## Limitations and next action

This reviewer inspected retained executions, not reran them. No Git execution or independent hash recomputation was available through the supplied tools. Protected-layer preservation is supported by executed assertions and root freshness evidence, not by inspecting excluded contents. Hosted CI/external automation and complete model transport internals were not independently verified.

Root should perform the final scope/supporting-input freshness comparison, consume the separate Spec report, and retain this original report unchanged. Maintainer acceptance, #71 closure and merge remain separate decisions.

## Review

- **Fixed:** none; read-only.
- **Blocking findings:** none within the inspected Standards scope.
- **Merge verdict:** **OK with notes** — one nonblocking provenance correction; this axis does not establish complete delivery acceptance.