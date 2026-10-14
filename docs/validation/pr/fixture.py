"""Create disposable PR evidence; no hosted CI, timing benchmark or remote effects."""
import json
import pathlib
import subprocess
import tempfile


def run(root, *args):
    return subprocess.check_output(args, cwd=root, text=True, stderr=subprocess.STDOUT).strip()


def write(root, name, body):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body)


def generate():
    evidence = {}
    for kind in ("measured", "unmeasured", "no-ci"):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            run(root, "git", "init", "-q")
            run(root, "git", "config", "user.name", "Fixture")
            run(root, "git", "config", "user.email", "fixture@example.invalid")
            baseline = "import unittest\nclass Tests(unittest.TestCase):\n"
            baseline += "    def test_keep(self): self.assertEqual(2 + 2, 4)\n"
            baseline += "    def test_duplicate(self): self.assertEqual(2 + 2, 4)\n"
            baseline += "    def test_update(self): self.assertTrue(True)\n"
            write(root, "test_old.py", baseline)
            if kind != "no-ci":
                write(root, ".github/workflows/check.yml", "on: [pull_request]\njobs:\n  checks:\n    runs-on: ubuntu-latest\n    steps:\n      - run: python -m unittest discover -v\n")
            run(root, "git", "add", ".")
            run(root, "git", "commit", "-qm", "baseline")
            before = run(root, "git", "rev-parse", "HEAD")
            before_result = run(root, "python3", "-B", "-m", "unittest", "discover", "-v")
            (root / "test_old.py").unlink()
            candidate = baseline.replace("    def test_duplicate(self): self.assertEqual(2 + 2, 4)\n", "")
            candidate = candidate.replace("self.assertTrue(True)", "self.assertEqual(3 + 3, 6)")
            candidate += "    def test_new(self): self.assertEqual(1 + 1, 2)\n"
            write(root, "test_new.py", candidate)
            # A migration requirement is evidence, not an executed installation.
            write(root, "MIGRATION.md", "After merge, the maintainer must approve and manually refresh installed copies.\nA source revert does not restore installed copies; use the approved backup.\n")
            if kind == "unmeasured":
                with (root / ".github/workflows/check.yml").open("a") as file:
                    file.write("  syntax:\n    runs-on: ubuntu-latest\n    steps:\n      - run: python -m compileall -q .\n")
            run(root, "git", "add", ".")
            run(root, "git", "commit", "-qm", "candidate")
            after = run(root, "git", "rev-parse", "HEAD")
            result = run(root, "python3", "-B", "-m", "unittest", "discover", "-v")
            evidence[kind] = {
                "baseline": before, "candidate": after,
                "diff": run(root, "git", "diff", "--find-renames=40%", before, after),
                "baseline_tests": baseline, "candidate_tests": candidate,
                "baseline_check": before_result, "candidate_check": result,
                "ci": run(root, "git", "ls-files", ".github/workflows/*"),
                "workflow": (root / ".github/workflows/check.yml").read_text() if kind != "no-ci" else None,
                "migration": (root / "MIGRATION.md").read_text(),
                "review": {"Standards": "not supplied", "Spec": "M1 unresolved: restore procedure has not been exercised"},
                "authority": "local report only; no publication, benchmarks or installed migration",
            }
            if kind == "measured":
                evidence[kind]["samples"] = {
                    "provenance": "synthetic CI records, NOT observed hosted runs",
                    "baseline_run": "fixture-B", "candidate_run": "fixture-C",
                    "baseline_revision": before, "candidate_revision": after,
                    "date": "2026-10-14", "workload": "python -m unittest discover -v, three named test functions",
                    "runner": "synthetic ubuntu-latest, 2 vCPU", "cache": "cold in both records",
                    "concurrency": 1, "retries_skips_failures": 0, "samples_per_state": 1,
                    "baseline_elapsed_seconds": 80, "candidate_elapsed_seconds": 60,
                    "baseline_runner_seconds": 70, "candidate_runner_seconds": 50,
                    "billing": None,
                }
    return evidence


if __name__ == "__main__":
    print(json.dumps(generate(), indent=2))
