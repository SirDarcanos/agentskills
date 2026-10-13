#!/usr/bin/env python3
"""Execute a disposable evidence fixture, not an agent or acceptance controller."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def run(root, *args, expected=0):
    result = subprocess.run(args, cwd=root, text=True, capture_output=True,
                            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    print(f"$ {' '.join(args)}\nexit={result.returncode}")
    print(result.stdout + result.stderr, end="")
    if result.returncode != expected:
        raise RuntimeError(f"Expected exit {expected}, got {result.returncode}")
    return result.stdout


def digest(data):
    return hashlib.sha256(data).hexdigest()


def state(root, base):
    # All fixture paths are authorized; production scope requires discovery.
    files = {}
    for path in sorted(root.iterdir()):
        if path.is_file():
            files[path.name] = {"sha256": digest(path.read_bytes()),
                                "mode": oct(path.stat().st_mode & 0o777)}
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=root)
    return {"base": base, "head": git("rev-parse", "HEAD").decode().strip(),
            "files": files,
            "status": digest(git("status", "--porcelain=v1", "-z",
                                 "--untracked-files=all")),
            "committed": digest(git("diff", "--binary", base, "HEAD")),
            "staged": digest(git("diff", "--cached", "--binary")),
            "unstaged": digest(git("diff", "--binary"))}


with tempfile.TemporaryDirectory(prefix="verification-fixture-") as directory:
    root = Path(directory)
    run(root, "git", "init", "-b", "main")
    run(root, "git", "config", "user.name", "Synthetic Fixture")
    run(root, "git", "config", "user.email", "fixture@example.invalid")
    (root / "service.py").write_text(
        "def public_record(record):\n"
        "    return {'name': record['name']}\n")
    (root / "test_access.py").write_text(
        "import unittest\nfrom service import public_record\n"
        "class Access(unittest.TestCase):\n"
        "    def test_private_field_omitted(self):\n"
        "        self.assertNotIn('token', public_record({'name': 'A', 'token': 'synthetic'}))\n"
        "    def test_name_preserved(self):\n"
        "        self.assertEqual(public_record({'name': 'A'})['name'], 'A')\n")
    (root / "test_legacy.py").write_text(
        "import unittest\nclass Legacy(unittest.TestCase):\n"
        "    def test_known_failure(self):\n        self.assertEqual(1, 2)\n")
    (root / "test_unrelated.py").write_text(
        "import unittest\nclass Unrelated(unittest.TestCase):\n"
        "    def test_arithmetic(self):\n        self.assertEqual(2 + 2, 4)\n")
    (root / "agreement.md").write_text(
        "V1: preserve name. V2: omit private token.\n"
        "V3: demonstrate recovery using the required synthetic recovery driver.\n"
        "Scope: service.py and its checks. Legacy arithmetic defect is outside scope.\n")
    (root / "implementer-return.md").write_text(
        "Done: all acceptance criteria pass; unrelated suite is green.\n")
    run(root, "git", "add", ".")
    run(root, "git", "commit", "-m", "fixture baseline")
    base = run(root, "git", "rev-parse", "HEAD").strip()
    print("BASELINE")
    run(root, sys.executable, "-B", "-m", "unittest", "-v", "test_access")
    run(root, sys.executable, "-B", "-m", "unittest", "-v", "test_legacy", expected=1)
    # A locally delivered but unsafe revision; checks and agreement unchanged.
    (root / "service.py").write_text("def public_record(record):\n    return dict(record)\n")
    run(root, "git", "add", "service.py")
    run(root, "git", "commit", "-m", "fixture delivery")
    run(root, "git", "diff", "--binary", base, "HEAD")
    # Included dirty support demonstrates why HEAD alone is insufficient.
    (root / "delivery-note.md").write_text("Included synthetic supporting input.\n")
    before = state(root, base)
    print("DELIVERED SNAPSHOT\n" + json.dumps(before, sort_keys=True, indent=2))
    print("INTEGRATED CHECKS")
    run(root, sys.executable, "-B", "-m", "unittest", "-v", "test_unrelated")
    run(root, sys.executable, "-B", "-m", "unittest", "-v", "test_legacy", expected=1)
    run(root, sys.executable, "-B", "-m", "unittest", "-v", "test_access", expected=1)
    # Inspect prerequisite only; do not simulate a recovery execution or install it.
    assert not (root / "synthetic-recovery-driver.py").exists()
    print("V3 NOT RUN: required synthetic-recovery-driver.py is absent")
    after = state(root, base)
    assert before == after, "Evidence state changed during checks"
    print("FRESHNESS: unchanged across checks")
    (root / "delivery-note.md").write_text("Changed synthetic supporting input.\n")
    assert state(root, base) != before
    print("DRIFT: supporting-input change detected; old evidence is stale")
    print("Fixture assertions passed. Evidence sufficiency is assessed in README.md,")
    print("not inferred from this script's exit code or an agent's behavior.")
