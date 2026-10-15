#!/usr/bin/env python3
"""Offline synthetic experiment; no installed skills or production target changes."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


PROBE = '''"""PROTOTYPE ONLY: in-memory cancellation transition; not production-ready."""
import json
import sys
state = "idle"
for event in json.loads(sys.argv[1]):
    if event == "start" and state == "idle":
        state = "running"
    elif event == "cancel" and state == "running":
        state = "cancelled"
    elif event == "complete" and state == "running":
        state = "done"
print(json.dumps({"state": state, "production_ready": False}))
'''


def identity(path):
    if path.is_symlink():
        return ("link", str(path.readlink()))
    return ("file", path.stat().st_mode, hashlib.sha256(path.read_bytes()).hexdigest())


def remove_owned(path, manifest, authorized):
    """Conservative fixture cleanup: exact owned, authorized, unchanged path only."""
    if path not in manifest or path not in authorized:
        return "blocked-unowned-or-unauthorized"
    if identity(path) != manifest[path]:
        return "blocked-changed"
    path.unlink()  # Unlinking an owned link never follows its shared target.
    return "removed"


def experiment(probe, cases, bound):
    observations = []
    for events, expected in cases[:bound]:
        run = subprocess.run(
            [sys.executable, str(probe), json.dumps(events)],
            capture_output=True, text=True, timeout=5, check=True,
        )
        actual = json.loads(run.stdout)
        assert actual["production_ready"] is False
        observations.append({"events": events, "expected": expected,
                             "actual": actual["state"], "exit": run.returncode})
    if any(row["actual"] != row["expected"] for row in observations):
        conclusion = "rejected"
    elif len(observations) < len(cases):
        conclusion = "inconclusive"
    else:
        conclusion = "supported"
    return {"bound": bound, "spent": len(observations), "conclusion": conclusion,
            "production_ready": False, "observations": observations}


def main():
    # All writes/removals are inside this owned TemporaryDirectory.
    with tempfile.TemporaryDirectory(prefix="prototype-fixture-") as directory:
        root = Path(directory)
        protected = root / "pre-existing.txt"
        protected.write_text("Synthetic unrelated work: preserve exactly.\n")
        protected_before = identity(protected)
        probe = root / "prototype-transition.py"
        probe.write_text(PROBE)
        cases = [(["start", "cancel", "complete"], "cancelled"),
                 (["start", "complete", "cancel"], "done")]
        print("Question: can an absorbing cancel state ignore a late completion?")
        supported = experiment(probe, cases, bound=2)
        assert supported["conclusion"] == "supported"
        print(json.dumps(supported, sort_keys=True))
        inconclusive = experiment(probe, cases, bound=1)
        assert inconclusive["conclusion"] == "inconclusive"
        print(json.dumps(inconclusive, sort_keys=True))
        rejected = experiment(probe, [(cases[0][0], "done")], bound=1)
        assert rejected["conclusion"] == "rejected"
        print("Counter-hypothesis:", json.dumps(rejected, sort_keys=True))
        print("Recommendation: consider absorbing cancellation for this model only.")
        print("Limitations: no real concurrency, persistence/recovery, integration, "
              "security or load evidence; production implementation needs new scope/checks.")

        manifest = {probe: identity(probe)}
        retained_before = identity(probe)
        assert remove_owned(probe, manifest, set()) == "blocked-unowned-or-unauthorized"
        assert identity(probe) == retained_before
        # Preserve useful runnable learning in the fixture until its owned target ends.
        (root / "learning.json").write_text(json.dumps(supported))
        assert json.loads((root / "learning.json").read_text())["conclusion"] == "supported"
        print("Retained useful probe and learning; no automatic promotion/commit.")

        scratch = root / "owned-scratch.txt"
        scratch.write_text("temporary observation\n")
        manifest[scratch] = identity(scratch)
        assert remove_owned(scratch, manifest, {scratch}) == "removed"
        assert not scratch.exists()
        assert remove_owned(protected, manifest, {protected}) == "blocked-unowned-or-unauthorized"
        changed = root / "owned-but-changed.txt"
        changed.write_text("initial\n")
        manifest[changed] = identity(changed)
        changed.write_text("intervening edit: preserve\n")
        assert remove_owned(changed, manifest, {changed}) == "blocked-changed"
        assert changed.read_text() == "intervening edit: preserve\n"
        link = root / "owned-link"
        link.symlink_to(protected.name)
        manifest[link] = identity(link)
        assert remove_owned(link, manifest, {link}) == "removed"
        assert identity(protected) == protected_before
        assert identity(probe) == retained_before
        print("Disposition checks passed: authorized scratch/link removed; "
              "unowned, changed and useful artifacts protected; shared target intact.")
    print("PASS: synthetic experiment and disposition checks; temporary fixture ended.")


if __name__ == "__main__":
    main()
