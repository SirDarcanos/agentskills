#!/usr/bin/env python3
"""Offline tool exercises and instruction regressions; not an agent controller/test."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

PACKAGE = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SingleChange(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="work-on-change-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.put("formatter.py", "def heading(text):\n    return text.strip()\n")
        self.put("check.py", "from formatter import heading\nassert heading('  Hello world  ') == 'Hello world'\n")
        self.put("staged.txt", "original staged\n")
        self.put("unstaged.txt", "original unstaged\n")
        self.git("init", "--template=", "-b", "main")
        self.git("add", "formatter.py", "check.py", "staged.txt", "unstaged.txt")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "fixture baseline")
        self.put("staged.txt", "protected staged edit\n")
        self.git("add", "staged.txt")
        self.put("unstaged.txt", "protected unstaged edit\n")
        self.put("note.txt", "protected untracked\n")
        (self.root / "note-link").symlink_to("note.txt")
        self.protected = self.manifest()
        # One caller-owned ledger passed unchanged between synthetic method/phase steps.
        self.ledger = {"run": "synthetic-change", "active": [], "checkpoint": "F1",
                       "lineage": ["normalization"], "repairs_spent": 1,
                       "model_reserved": 0, "model_attempted": 0}

    def put(self, name, content):
        (self.root / name).write_text(content, encoding="utf-8")

    def git(self, *args, cwd=None):
        # cwd alone does not isolate Git's repository/index/config overrides.
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        p = subprocess.run(["git", "-c", f"core.hooksPath={os.devnull}",
                            "-c", "init.templateDir=", *args],
                           cwd=cwd or self.root, env=env, capture_output=True, timeout=10)
        if p.returncode:
            raise AssertionError(p.stderr.decode())
        return p.stdout

    def manifest(self):
        files = {}
        for name in ("staged.txt", "unstaged.txt", "note.txt", "note-link"):
            p = self.root / name
            files[name] = (p.lstat().st_mode, os.readlink(p) if p.is_symlink() else digest(p))
        paths = list(files)
        return (files, self.git("ls-files", "--stage", "--", *paths),
                self.git("status", "--porcelain=v1", "-z", "--", *paths),
                self.git("rev-list", "main"))

    def check(self, script="check.py"):
        p = subprocess.run([sys.executable, "-B", script], cwd=self.root,
                           capture_output=True, text=True, timeout=5)
        print(f"{self._testMethodName}: {script} exit={p.returncode}")
        return p

    def preserve(self):
        self.assertEqual(self.protected, self.manifest())

    def regression(self):
        self.put("check.py", "from formatter import heading\nassert heading('  Hello world  ') == 'Hello world'\nassert heading('  Hello\\t\\n world ') == 'Hello world'\nassert heading(' \\t\\n ') == ''\n")

    def implement(self):
        self.put("formatter.py", "def heading(text):\n    return ' '.join(text.split())\n")

    def test_direct_change(self):
        # Explicit synthetic-owner authority covers this local branch operation.
        self.git("switch", "-c", "fix/heading-normalization")
        self.assertEqual(self.check().returncode, 0)
        self.regression()
        red = self.check()
        self.assertEqual(red.returncode, 1)
        self.assertIn("AssertionError", red.stderr)
        self.implement()
        self.assertEqual(self.check().returncode, 0)
        self.preserve()

    def test_ready_bug_ticket_reuses_current_evidence(self):
        self.regression()
        observed = self.check()
        self.assertIn("AssertionError", observed.stderr)
        ticket = {"acceptance": ["F1", "F2"], "cause": "strip leaves internal whitespace",
                  "expected": "Hello world", "actual": "Hello\\t\\n world",
                  "environment": sys.version.split()[0], "scope": ["formatter.py", "check.py"],
                  "method": "tdd", "source": digest(self.root / "formatter.py"),
                  "reproduction": observed.stderr, "exit": observed.returncode}
        self.put("ticket.json", json.dumps(ticket))
        retained = json.loads((self.root / "ticket.json").read_text())
        self.assertEqual(retained["source"], digest(self.root / "formatter.py"))
        self.assertEqual(retained["exit"], 1)
        # Direct cause inspection/evidence reuse: no second diagnostic owner is invoked.
        self.assertIn("return text.strip()", (self.root / "formatter.py").read_text())
        self.implement()
        self.assertEqual(self.check().returncode, 0)
        self.preserve()

    def test_stale_evidence_refreshes_only_dependent_claim(self):
        self.assertEqual(self.check().returncode, 0)
        old = digest(self.root / "formatter.py")
        unrelated_claim = digest(self.root / "note.txt")
        self.put("formatter.py", "def heading(text):\n    return text\n")
        self.assertNotEqual(old, digest(self.root / "formatter.py"))
        stale_run = self.check()
        self.assertIn("AssertionError", stale_run.stderr)
        self.assertEqual(unrelated_claim, digest(self.root / "note.txt"))
        self.implement()
        self.assertEqual(self.check().returncode, 0)
        self.preserve()

    def test_method_composition_retains_baseline_and_ledger(self):
        self.put("capture.py", "from formatter import heading\nassert heading('  Hello world  ') == 'Hello world'\n")
        self.assertEqual(self.check("capture.py").returncode, 0)
        captured = digest(self.root / "capture.py")
        ledger_before = json.dumps(self.ledger, sort_keys=True)
        # Baseline protection then test-first production increment, not a new run.
        self.regression()
        self.assertIn("AssertionError", self.check().stderr)
        self.implement()
        self.assertEqual(self.check().returncode, 0)
        self.assertEqual(self.check("capture.py").returncode, 0)
        self.assertEqual(captured, digest(self.root / "capture.py"))
        self.assertEqual(ledger_before, json.dumps(self.ledger, sort_keys=True))
        self.preserve()

    def test_missing_optional_model_uses_zero_calls(self):
        # Explicit none policy and absent endpoint: ordinary checks remain usable.
        policy = {"allowed": False, "endpoint": None}
        self.assertFalse(policy["allowed"])
        self.assertIsNone(policy["endpoint"])
        self.implement()
        self.regression()
        self.assertEqual(self.check().returncode, 0)
        self.assertEqual(self.ledger["model_attempted"], 0)
        self.preserve()

    def test_material_check_blocker_is_not_green(self):
        self.implement()
        self.assertEqual(self.check().returncode, 0)
        missing = self.check("required-integration-check.py")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("No such file", missing.stderr)
        self.assertFalse((self.root / "required-integration-check.py").exists())
        self.assertEqual(self.ledger["repairs_spent"], 1)
        self.preserve()
        print("material integration evidence unavailable: acceptance BLOCKED; no installation/retry")

    def test_inherited_git_controls_cannot_escape_fixture(self):
        # All hostile paths are sacrificial local sandboxes, never a user's repo.
        with tempfile.TemporaryDirectory(prefix="work-on-git-controls-") as tmp:
            outside = Path(tmp)
            sacrificial = outside / "sacrificial"
            sacrificial.mkdir()
            self.git("init", "--template=", "-b", "main", cwd=sacrificial)
            target = sacrificial / "sentinel.txt"
            target.write_text("protected outside work\n")
            self.git("add", "sentinel.txt", cwd=sacrificial)
            self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                     "commit", "-m", "outside baseline", cwd=sacrificial)
            index = outside / "external-index"
            index.write_bytes((sacrificial / ".git/index").read_bytes())
            marker = outside / "hook-ran"
            hooks = outside / "hooks"
            hooks.mkdir()
            template = outside / "template"
            (template / "hooks").mkdir(parents=True)
            for home in (hooks, template / "hooks"):
                hook = home / "pre-commit"
                hook.write_text(f'#!/bin/sh\nprintf executed > "{marker}"\n')
                hook.chmod(0o755)
            before = {str(p.relative_to(outside)): (digest(p), p.stat().st_mode)
                      for p in outside.rglob("*") if p.is_file()}
            head = self.git("rev-parse", "HEAD", cwd=sacrificial)
            probe = self.root / "isolated-probe"
            probe.mkdir()
            overrides = {"GIT_DIR": str(sacrificial / ".git"),
                         "GIT_WORK_TREE": str(sacrificial),
                         "GIT_INDEX_FILE": str(index),
                         "GIT_TEMPLATE_DIR": str(template),
                         "GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "core.hooksPath",
                         "GIT_CONFIG_VALUE_0": str(hooks)}
            with patch.dict(os.environ, overrides):
                self.git("init", "--template=", "-b", "main", cwd=probe)
                (probe / "owned.txt").write_text("owned fixture\n")
                self.git("add", "owned.txt", cwd=probe)
                self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                         "commit", "-m", "isolated commit", cwd=probe)
                self.assertTrue((probe / ".git/index").is_file())
                self.assertEqual(self.git("show", "HEAD:owned.txt", cwd=probe), b"owned fixture\n")
                self.assertFalse((probe / ".git/hooks").exists())
            after = {str(p.relative_to(outside)): (digest(p), p.stat().st_mode)
                     for p in outside.rglob("*") if p.is_file()}
            self.assertEqual(before, after)
            self.assertEqual(head, self.git("rev-parse", "HEAD", cwd=sacrificial))
            self.assertFalse(marker.exists())
        self.preserve()
        print("Git dir/worktree/index/template/config overrides: isolated; no external hook/state effects")

    def test_instruction_gates_and_no_nested_pool(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        contract = (PACKAGE / "references/contracts.md").read_text()
        build = (PACKAGE / "references/build.md").read_text()
        self.assertNotIn("disable-model-invocation:", entry)
        for clause in ("one change", "investigation-only", "without reinvestigation",
                       "without a maintainer method/seam questionnaire", "whole-spec",
                       "lead inspection or optional model agreement cannot substitute"):
            self.assertIn(clause, entry.lower())
        for clause in ("root lead chooses and adjusts concurrency", "root lead alone", "two automatic repair cycles",
                       "zero autonomous calls", "without replenishing", "service/model substitution"):
            self.assertIn(clause, contract.lower())
        for obsolete in ("at most **two active non-lead workers**", "at most two active non-lead workers"):
            self.assertNotIn(obsolete, contract.lower())
        for clause in ("no universal worker ceiling", "rolling scheduling", "explicit user/project restrictions",
                       "finite timeout/turn bounds", "does not override an existing consumer-project"):
            self.assertIn(clause, contract.lower())
        self.assertIn("compatibility pointer only", contract)
        adapter = (PACKAGE / "references/dispatch.md").read_text()
        self.assertNotIn("## 1.", adapter)
        self.assertIn("work-on-spec", adapter)
        self.assertIn("retain", build)
        self.assertIn("without invoking Analyze again", build)
        self.assertEqual(self.ledger["repairs_spent"], 1)
        self.preserve()
        print("instruction guard assertions: PASS (static, not agent-adherence proof)")


class PortableAuthorityInstructions(unittest.TestCase):
    """Source-contract guards, not execution of agent authorization decisions."""

    def test_required_reviews_have_portable_bounded_authority(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        contract = (PACKAGE / "references/contracts.md").read_text()
        self.assertIn("## Required-review authority\n", contract)
        authority = contract.split("## Required-review authority\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("contracts.md#required-review-authority", entry)
        self.assertNotIn("Delegation is optional and separately authorized.", entry)
        self.assertNotIn("destructive operations, delegation, account changes", entry)
        for clause in ("explicit user delivery request", "`work-on` or `work-on-spec`",
                       "read-only Standards and Spec", "without another permission prompt",
                       "no repository-local standing permission", "Explicit user/project/runtime restrictions",
                       "configured agent runtime", "root", "lead-chosen concurrency",
                       "New sensitive disclosure", "additional spending", "optional model assessments",
                       "library grants no execution authority", "implemented-but-unaccepted"):
            with self.subTest(clause=clause):
                self.assertIn(clause, authority)

    def test_reusable_package_fix_targets_sources_not_local_policy(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("tracked package sources", "repository-local operating policy",
                       "not a substitute", "Installed copies remain unchanged"):
            with self.subTest(clause=clause):
                self.assertIn(clause, entry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
