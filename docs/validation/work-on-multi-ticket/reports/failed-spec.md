# Spec review — ticket 101 failed candidate

## Agreement and independence

Scope: synthetic ticket 101 under issue #30; **N1/P1/G1/E1** at the failed-candidate checkpoint. **R1 belongs to pending, unstarted ticket 102**; absent report implementation is not a defect in this review.

Agreement: `docs/validation/work-on-multi-ticket/plan.md` and `fixture/failed/REQUEST.md`. Paths below are relative to `docs/validation/work-on-multi-ticket/` unless stated otherwise.

Recorded agreement SHA-256:
- `REQUEST.md`: `39cd7e04b03a4ed365f38619ae3dfe6be542e3fcbc5b7dae47030d65aae8bc10`
- `AGENTS.md`: `3acf10386081e50326aadc24d4ddf295c887cf6bd744b4aa566882f6183986a9`

Exclusions: coercion, locale/Unicode normalization, production tracker writes, deployment/releases, and protected sentinel/note/link contents.

This is a fresh independent **Spec** context, separate from the author and Standards reviewer, with maintainer-approved read-only authority and a ten-minute bound. No other axis report was consumed. No commands, edits, mutations, delegation, or optional models were run.

## Snapshot and inspected inputs

- Target: synthetic Git project, branch `feature/name-report`.
- Comparison: supplied fixed base → delivered HEAD, not merge-base selection.
- Base: `2c686bb8e1c04c2bcff2b3cccb028b2c9b495d8e`
- HEAD: `93e4d2d2027e1db7c91f0430edc0dd22ece0514c`
- Snapshot: `evidence/failed.json`
- Committed patch: `evidence/failed.diff`; recorded SHA-256 `f456114935796f1e10781ef3b3d6225f458d85e467ad2509766b666a6a4d0cef`
- Included changes: `names.py`, `test_names.py`, `README.md`.
- Included unchanged support: `AGENTS.md`, `REQUEST.md`, `tracker.json`.
- Explicitly absent: `report.py`, `test_report.py`.

Read all six files in `fixture/failed`, their actual baseline counterparts excluding protected content, the required evidence inputs, `baseline-check.json`, `baseline-check.diff`, `protected.json`, and `actions.md`. Also read repository project/workflow instructions and Review Delivery’s complete entry, scope, and report references.

The supplied patch agrees with the inspected baseline and candidate sources. The manifest records empty scoped staged/unstaged/status deltas; unrelated protected work remains present separately.

**Freshness:** the task freezes source and supporting evidence through both reports. A repeated directory listing and reread of candidate implementation/tests/README and `failed.json` showed no observed change. No hashes were independently recomputed. Full post-pair discovery/fingerprint comparison remains the caller’s responsibility.

## Review

- **Correct:** the candidate retains the lowercase regression test, exposes the intended whitespace failure, and leaves ticket 102 unimplemented. The mock records distinguish closure from acceptance.
- **Fixed:** none; review-only assignment.
- **Finding: P1 / blocking — `N1-trim` (Spec).**  
  **Location:** `fixture/failed/names.py:2`; affected promise `fixture/failed/README.md:3`.  
  **Requirement:** `fixture/failed/REQUEST.md:4–5` requires stripping surrounding whitespace and lowercasing strings.  
  **Evidence:** the implementation changes baseline identity behavior to `value.lower()` without stripping. `evidence/commands.jsonl`, record 13, reports exit 1 at `test_names.py:10`: `normalize_name(' A ')` returned `' a '`, not `'a'`. Static inspection also shows whitespace-only input remains whitespace, contrary to `test_names.py:12`.  
  **Materiality:** this violates ticket 101’s central public behavior and makes its README promise false. Intentional failure injection does not satisfy acceptance. It also leaves the prerequisite unsuitable for ticket 102.  
  **Smallest fix:** use `value.strip().lower()`. Rerun the relevant unittest command, repin the repaired snapshot, and renew both independent axes. Preserve this failed evidence and carry the same repair episode forward.
- **Merge verdict: BLOCK** for this synthetic candidate; this report grants no merge or acceptance authority.

## Spec criterion coverage

| Criterion | Coverage and evidence |
|---|---|
| **N1** | **Failed.** Lowercase regression executes successfully at `test_names.py:6–7`; trimming fails at line 10. Empty-string preservation is statically satisfied, but assertions at lines 11–12 are skipped when line 10 fails. Their presence is not executed coverage. |
| **P1** | **Covered through the candidate commit, manifest-bounded.** `baseline-check.json#/protected`, `protected.json`, and `failed.json#/protected` agree on content/mode/link-target, index, staged, unstaged, and status fingerprints. Sentinel executable mode remains recorded as 493; note/link membership remains present. Protected contents were not opened. Preservation through future repair/resume is not yet demonstrated. |
| **G1** | **Covered at this checkpoint.** `tracker-read.json#/reads` records parent 100, forward/reverse 101→102 dependency observations, and closed/ready 101 with null acceptance. `failed.json#/scope/files` records report files absent. `actions.md`, sections 1–2, records 102 waiting for accepted integration/current checks/review. The mock is not production evidence, and closure does not establish acceptance. |
| **E1** | **Partially evidenced; later obligations pending.** Failed source, patch, manifest, and raw check are retained. `actions.md`, section 2, records checkpoint `101-normalization`, finding `N1-trim`, and spent budget 0/2, matching the planned episode. No resume, correction, refreshed check/review, or final integrated acceptance has occurred in this snapshot. Those future obligations are not certified here. |
| **R1** | **Excluded/pending**, not failed: ticket 102 has not started and is not claimed delivered. |

## Checks and limitations

**Executed evidence supplied by the author:** `evidence/commands.jsonl` records Python 3.14 unittest execution; manifests identify version 3.14.7. Record 10 establishes the baseline lowercase test passing. Record 13 proves the candidate whitespace failure. Records 12 and 14 tie the scoped commit/check sequence to the delivered revision.

**Static review:** actual baseline/candidate sources, patch, assertions, documentation, mock graph, and preservation manifests.

**Not run by this reviewer:** any command, fresh test, Git capture, hash calculation, or tracker request. Test totals, authored action claims, and mocked closure were not treated as acceptance proof. No material required input was unreadable.

## Documentation impact

`fixture/failed/README.md:3` promises trimming that the implementation does not provide; the minimal behavior fix resolves that conflict. Line 4 correctly says report support is not built. The fixture policy (`AGENTS.md:11`) requires README behavior documentation and excludes fixture changelog/release publication. No skill contract, domain definition, ADR, or release behavior changes are in scope.

## Outcome and next action

**Current Spec checkpoint review complete; candidate acceptance blocked by `N1-trim`.** Combined two-axis review is not asserted complete here.

After both reports return, the caller should confirm freshness, retain failed evidence, carry the stable repair episode/budget into correction, rerun affected checks, and obtain renewed Standards/Spec reports on the repaired snapshot. Keep ticket 102 waiting until current accepted integration and required evidence actually permit it.