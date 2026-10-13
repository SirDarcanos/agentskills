"""#31 offline package checks; no install, agent launch or network.

Run from the repository root: python3 -B docs/validation/delivery-coverage/check_packages.py
These structural assertions do not execute the instruction workflow.
"""
import ast
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[3]
PACKAGES = {
    "work-on": True,
    "review-delivery": False,
    "implementation-preflight": False,
    "domain-modeling": False,
    "setup-project": True,
}


def prose(text):
    return re.sub(r"^```[^\n]*\n.*?^```[ \t]*$", "", text, flags=re.M | re.S)


def anchors(path):
    result = set()
    counts = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", prose(path.read_text()), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug + ("-" + str(count) if count else ""))
    return result


def check_links(paths, boundary):
    count = 0
    for path in paths:
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose(path.read_text())):
            if re.match(r"[a-z]+://|mailto:", link):
                continue
            target, _, fragment = unquote(link).partition("#")
            resolved = (path.parent / target).resolve() if target else path.resolve()
            assert resolved.is_relative_to(boundary.resolve()), (path, link, "escape")
            assert resolved.exists(), (path, link, "missing")
            if fragment:
                assert resolved.is_file() and fragment in anchors(resolved), (path, link, "anchor")
            count += 1
    return count


def check_package(root, name, command_only, notice):
    entry = (root / "SKILL.md").read_text()
    assert entry.startswith("---\n")
    _, frontmatter, body = entry.split("---", 2)
    fields = {}
    for line in frontmatter.strip().splitlines():
        key, value = line.split(":", 1)
        assert key not in fields
        fields[key] = value.strip()
    assert fields["name"] == name
    assert fields["description"]
    assert (fields.get("disable-model-invocation") == "true") == command_only
    assert re.search(r"^## (?:[1-9]|Workflow)", body, re.M), name
    assert "Complete when:" in body or "complete when" in body or "**Done:" in body, name
    markdown = sorted(root.rglob("*.md"))
    for path in markdown:
        content = path.read_text()
        assert "/Users/" not in content and "BEGIN PRIVATE KEY" not in content, path
    count = check_links(markdown, root)
    for path in root.rglob("*.py"):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    if name in ("work-on", "review-delivery"):
        assert (root / "LICENSE").read_bytes() == notice
    if name == "work-on":
        assert "only when the user explicitly requests" in body
        for target in re.findall(r"`(references/[^`]+\.md)`", body):
            assert (root / target).is_file(), target
    if name == "review-delivery":
        assert "bounded independent-review handoff" in fields["description"]
        assert "Packet complete when:" in (root / "references/report.md").read_text()
    print(name + ": frontmatter, procedure bounds, links/anchors and syntax passed (" + str(count) + " links)", flush=True)


def run(root, *command):
    subprocess.run(command, cwd=root, check=True)


def main():
    notice = (REPO / "LICENSE").read_bytes()
    for name, command_only in PACKAGES.items():
        source = REPO / name
        check_package(source, name, command_only, notice)
        with tempfile.TemporaryDirectory(prefix="delivery-package-check-") as temporary:
            isolated = Path(temporary) / name
            shutil.copytree(source, isolated, symlinks=True)
            check_package(isolated, name, command_only, notice)
            if name == "review-delivery":
                run(isolated, sys.executable, "-B", "scripts/test_snapshot.py")
            elif name == "setup-project":
                run(isolated, sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v")
    docs = [REPO / "README.md", REPO / "CHANGELOG.md"]
    docs += list(Path(__file__).resolve().parent.glob("*.md"))
    print("Repository documentation: " + str(check_links(docs, REPO)) + " relative links/anchors passed")
    print("Isolated copies removed by this explicitly disposable protocol; no installed copies changed.")
    print("Static assertions and helper tests are not agent trials or runtime certification.")


if __name__ == "__main__":
    main()
