"""#70 validation evidence runner; existing failed checks stay failed in the report.

Python 3.9+. Only new output directories and disposable isolated packages are
written. No installation/network. Instruction compliance is not tested here.
"""
import ast
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def main(output):
    output.mkdir(parents=True, exist_ok=False)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    commands = [
        ("shape-extraction", ["docs/validation/shape-work/check.py"]),
        ("spec-extraction", ["docs/validation/write-spec/check.py"]),
        ("ticket-extraction", ["docs/validation/write-tickets/check.py"]),
        ("ticket-tests", ["-m", "unittest", "discover", "-s", "docs/validation/write-tickets", "-p", "test_*.py"]),
        ("setup-tests", ["-m", "unittest", "discover", "-s", "workflow/setup-project/tests", "-p", "test_*.py"]),
        ("helper-help", ["workflow/setup-project/scripts/dependencies.py", "--help"]),
        ("package-invocation-tests", ["-m", "unittest", "discover", "-s", "docs/validation/delivery-coverage", "-p", "test_package_invocation.py"]),
        ("shared-package-checks", ["docs/validation/delivery-coverage/check_packages.py"]),
    ]
    outcomes = []
    for name, args in commands:
        result = subprocess.run([sys.executable, "-B", *args], cwd=REPO,
                                env=env, capture_output=True, text=True, check=False)
        log = (result.stdout + result.stderr).replace(str(REPO), "<repository>")
        (output / (name + ".txt")).write_text(log)
        outcomes.append({"check": name, "command": "python3 -B " + " ".join(args), "exit": result.returncode})
        print(name + ": exit " + str(result.returncode))
    spec = importlib.util.spec_from_file_location("package_checks", REPO / "docs/validation/delivery-coverage/check_packages.py")
    checks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checks)
    notice = (REPO / "LICENSE").read_bytes()
    expected_adapted = notice.replace(b"Copyright (c) 2026 Nicola Mustone",
                                    b"Copyright (c) 2026 Matt Pocock\nCopyright (c) 2026 Nicola Mustone")
    for name in ("shape-work", "write-spec", "write-tickets"):
        source = REPO / 'workflow' / name
        assert (source / "LICENSE").read_bytes() == (notice if name == "shape-work" else expected_adapted)
        checks.check_package(source, name, False, notice)
        with tempfile.TemporaryDirectory() as tmp:
            isolated = Path(tmp) / "catalog" / "unrelated-location"
            shutil.copytree(source, isolated, symlinks=True)
            checks.check_package(isolated, name, False, notice)
    # Repair #67's stale expectations rather than skip the affected package.
    # Regression tests also reject accidentally broadened invocation authority.
    checks.check_package(REPO / "workflow/work-on", "work-on", checks.PACKAGES["work-on"], notice)
    links = checks.check_links(list(HERE.glob("*.md")), REPO)
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    outcomes.append({"check": "current package source/isolation/license/frontmatter/links and Python 3.9 syntax", "exit": 0, "evidence_links": links})
    diff = subprocess.run(["git", "diff", "--check"], cwd=REPO, capture_output=True, text=True, check=False)
    outcomes.append({"check": "git diff --check", "exit": diff.returncode})
    (output / "git-diff.txt").write_text(diff.stdout + diff.stderr)
    (output / "checks.json").write_text(json.dumps(outcomes, indent=2) + "\n")
    print("Report retains all exit codes; nonzero existing extraction checks are NOT passed.")
    if any(o["exit"] != 0 for o in outcomes):
        return 1
    return 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new check-evidence directory")
    raise SystemExit(main(parser.parse_args().output))
