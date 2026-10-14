# Checker repair: execution, review and disposition

The initial PR incorrectly left a clear stale-check defect for the maintainer to resolve. The maintainer requested the fix and clarified that routine defects caused by delivered work should be corrected proactively. This bounded repair updates validation to the existing #67 contract; it changes no product agreement, skill procedure, installed copy, model permission or production tracker state.

## Execution and evidence

All three extraction checks now expect non-command-only Work On metadata. The shared checker explicitly guards user delivery, bounded authorized assignments and investigation-only no-fix-authority. Five new sensitivity tests exercise the current isolated package and reject four authorization/metadata regressions. The previously skipped Work On check is restored; no failure is suppressed.

[Repaired individual results](results/checks-repaired/checks.json) all exit 0. Raw logs cover source/isolated extraction checks, 10 ticket tests, 22 source Setup tests, 5 new invocation tests, helper help and the full shared package checker. Shared checking additionally runs 13 isolated snapshot tests and collects 22 isolated Setup tests: 20 pass, 2 companion-presence checks skip as expected.

Background task `bd85ef83c` completed with exit 0. [Its retained output](results/repair-run.txt) contains both the checker run and the subsequent fixture replay's actual PASS output. The executed shell command was:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 docs/validation/discovery-spec-tickets/check.py docs/validation/discovery-spec-tickets/results/checks-repaired && PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import subprocess
import sys
import tempfile
with tempfile.TemporaryDirectory() as directory:
    subprocess.run([sys.executable, '-B', 'docs/validation/discovery-spec-tickets/run_fixture.py', str(Path(directory) / 'replay')], check=True)
PY
```

The replay's deciding script, fixture, agreement and source identities in [original execution evidence](results/execution.json) were reconfirmed unchanged after review. It wrote only a new disposable directory, then removed that directory; the original persisted artifacts remain intact. [Repair evidence identities](results/repair-evidence.json) record environment, repaired source digests, task/context IDs and the private snapshot digest. This is observed execution evidence, not an attestation or an independently executed replay.

## Independent review and freshness

Root launched two fresh read-only `reviewer` contexts under the workflow's standing permission; at most two active workers, 10-minute child bounds, no recursive delegation or optional assessments. Frozen comparison: full base/HEAD `bc48d2a3aee1b341da666b908290ca8ec00d359b` plus the dirty repair, including seven tracked differences, the new regression test and raw repaired results. Both reviewers received the same explicit sources/standards/agreement, with earlier verdicts/results and each other's conclusions excluded. Original full trial acceptance was outside their assignment.

Original reports, retained separately:

- [Standards](reviews/repair-standards.md), context `b32f2543-6ef6-4ff0-a48b-aa47c3710112`: no issues, OK with notes.
- [Spec](reviews/repair-spec.md), context `f59fd97e-e9cf-4c5d-b1aa-25ee66d14340`: no blocking findings, OK with notes; one nonblocking evidence gap described below.

Reports are unchanged except that the transient private snapshot filename is normalized for public retention. Both performed static inspection and read author-run raw logs, not independent test execution. Both completed before final full fingerprint check returned `matching-listed-paths` with no changed fields; final path discovery matched the pinned repair inventory. This freshness check occurred before retaining reports and adding this administrative record. No reviewed checker, regression, skill contract or original repaired log changed afterward.

## Finding disposition and final state

Spec P2: the current replay claim lacked raw support in the supplied `checks-repaired/` bundle. **Resolved by evidence retention**, not by claiming the reviewer verified it: the separately executed replay already existed in task `bd85ef83c`; its actual output, exact command and deciding identities are now separately inspectable above. The runner still does not pretend to include replay in its own command list. That reviewer report retains its original partial-claim limitation. No code repair or further test rerun was required for this reporting correction.

Standards' replay/rendering/original-pin limitations remain accurately scoped: those checks are lead-executed/direct observations, not independent review. The two Setup skips are isolated-companion-presence checks, not skipped Work On validation. Initial failed logs remain historical evidence, not waived current failures.

Repair history: one initial harness adjustment, followed by this bounded checker correction after maintainer feedback. No additional behavioral repair followed the independent reports; only report/log retention and evidence clarification. No current material checker-repair finding remains. The full original shaping trial still has its stated direct-author/synthetic-input limits. #70 and PR #94 remain unmerged and pending maintainer acceptance; no deployment, release or installed migration occurred.
