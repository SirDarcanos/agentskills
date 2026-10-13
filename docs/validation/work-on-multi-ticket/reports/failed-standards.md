# Standards review — ticket 101 failed candidate

## Agreement and authority

Reviewed issue #30’s synthetic ticket 101 against:

- `docs/validation/work-on-multi-ticket/plan.md`.
- `fixture/failed/REQUEST.md:2–13`: N1, P1, G1 and E1; agreement SHA-256 `39cd7e04b03a4ed365f38619ae3dfe6be542e3fcbc5b7dae47030d65aae8bc10`.
- `fixture/failed/AGENTS.md:3–12`: scoped direct integration, preservation, independent review, read-only reviewers and README ownership.
- Repository project/workflow instructions and `review-delivery/SKILL.md`, `references/scope.md`, and `references/report.md`.

Paths below are relative to `docs/validation/work-on-multi-ticket/` unless otherwise stated.

R1 belongs to dependent ticket 102 and is pending/unstarted, not claimed implemented. Input coercion, locale/Unicode normalization, production tracker operations, deployment and releases are excluded.

## Snapshot and independence

- Target: synthetic repository, branch `feature/name-report`.
- Comparison: fixed supplied base → delivered HEAD, not a branch-relative merge-base.
- Base: `2c686bb8e1c04c2bcff2b3cccb028b2c9b495d8e`.
- HEAD: `93e4d2d2027e1db7c91f0430edc0dd22ece0514c`.
- Snapshot: `evidence/failed.json`; committed patch: `evidence/failed.diff`.
- Committed patch SHA-256: `f456114935796f1e10781ef3b3d6225f458d85e467ad2509766b666a6a4d0cef`.
- Scoped staged/unstaged/status fingerprints are empty-delta fingerprints. Protected unrelated work remains separately represented.

Inspected all six files in `fixture/failed`: `AGENTS.md`, `REQUEST.md`, `README.md`, `names.py`, `test_names.py`, and `tracker.json`. Compared their actual baseline counterparts and the supplied patch. Also inspected `failed.json`, `commands.jsonl`, `tracker-read.json`, `baseline-check.json`, `baseline-check.diff`, and `protected.json`.

Protected sentinel/note/link contents were not opened. `report.py` and `test_report.py` are absent according to the manifest and fixture inventory, consistent with unstarted 102.

This is the independent Standards reviewer context, separate from the author and other axis, authorized for read-only inspection with a ten-minute bound. No other-axis report was consumed; no checks, mutations, delegation or optional assessments were performed.

## Freshness

The assignment supplies a source/support-input freeze through both reports. Observed fixture membership and actual source changes agree with the supplied inventory and patch; baseline and candidate policy/tracker sources are unchanged.

No independent Git capture or cryptographic recomputation was executed. The caller must perform the required final freshness comparison after both reports return. This report applies only to the identified frozen candidate.

## Review

### Correct

- Changes remain within ticket 101’s ownership: normalization implementation, its tests and README. The scoped commit receipt names only those three files (`evidence/commands.jsonl:13`).
- The existing string-returning interface remains simple. No dependency, speculative abstraction, configurability or new state owner was introduced (`fixture/failed/names.py:1–2`).
- The added assertion detects the principal contract failure (`fixture/failed/test_names.py:9–10`); retained execution confirms failure rather than hiding it.
- README correctly identifies report support as unbuilt (`fixture/failed/README.md:4`).
- Mock graph evidence distinguishes issue numbers from database IDs, records both dependency directions, and leaves 101’s acceptance null. Its closed state is not acceptance evidence.

### Finding: N1-trim — P0, blocking

**Locations:** `fixture/failed/names.py:2`; `fixture/failed/README.md:3`; `fixture/failed/test_names.py:10–12`.

**Observed behavior:** The changed implementation calls only `value.lower()`. It preserves surrounding whitespace, so `" A "` becomes `" a "`, not `"a"`. Whitespace-only `" \t "` likewise remains nonempty.

**Evidence:** Static inspection of the actual source and `evidence/failed.diff` establishes the missing operation. The retained unittest execution at `evidence/commands.jsonl:14` reports:

```text
AssertionError: ' a ' != 'a'
FAILED (failures=1)
```

`evidence/failed.json` records `test_exit: 1`.

**Binding requirement:** `fixture/failed/REQUEST.md:3–5` requires stripping surrounding whitespace and lowercasing. README now promises both operations despite implementing only one.

**Materiality:** Ticket 101 does not deliver its central behavior. Accepting it would expose an incorrect normalization interface to dependent 102. Neither a scoped integration commit nor the mocked closed ticket can override the failed requirement/check.

**Smallest correction:** Change the implementation to `return value.strip().lower()`. Keep the failed snapshot/report as history. Rerun relevant checks and renew both review axes against the repaired snapshot before accepting 101 or unlocking 102. The current README wording then matches the approved behavior.

No repairs were applied.

## Criterion coverage

| Criterion | Standards assessment |
|---|---|
| N1 | **Failed.** Lowercasing is implemented; trimming is missing. Empty-string preservation follows statically from `.lower()`. Assertions at lines 11–12 were not reached after line 10 failed. |
| P1 | **Supported by manifest comparison.** Baseline and failed protected manifests match file/link fingerprints, modes, index, staged/unstaged patches and status. Protected contents were intentionally excluded; preservation was not independently recaptured. |
| G1 | **Consistent at this checkpoint.** Parent/child and forward/reverse dependency observations agree. 101 has null acceptance; 102 remains unstarted. Current failed checks prohibit unlocking it. |
| E1 | **Checkpoint evidence retained; later obligations pending.** Failed source, patch and raw check output are preserved. The plan specifies checkpoint `101-normalization`, finding `N1-trim`, budget 0/2. Resume, repair-budget consumption and renewed checks/reviews are not yet evidenced and are not claimed complete. |
| R1 | **Excluded/pending 102.** Its absence is not a ticket 101 defect. |

This is Standards criterion coverage, not a substitute for the independent Spec report.

## Checks and limitations

- **Executed by the author, inspected here:** Python 3.14.7 unittest baseline passed; candidate failed the whitespace assertion. Git receipts identify the baseline and candidate commits.
- **Static here:** actual source/baseline comparison, ownership, interface simplicity, README consistency, graph observations and protected-manifest equality.
- **Not run here:** shell commands, unittest reruns, snapshot helper or final freshness recapture.
- Tracker evidence is explicitly mocked with zero network calls; it does not prove production tracker behavior.

## Documentation impact

README is the fixture’s authoritative behavior documentation and currently contradicts the implementation. Fixing N1 restores consistency without changing the approved README promise. Fixture policy explicitly excludes changelog/publication work (`fixture/failed/AGENTS.md:12`). This candidate changes no reusable skill contract or repository release behavior.

## Outcome and next action

**Standards inspection complete for the supplied snapshot; delivery acceptance blocked by N1-trim. Merge verdict: BLOCK.**

Repair within ticket 101’s scope, preserve historical failure evidence and the repair episode, refresh affected checks and both independent reviews, then perform final freshness comparison. Keep 102 unstarted until current accepted integration evidence permits it. Overall two-axis review completion and acceptance remain the caller’s responsibility.