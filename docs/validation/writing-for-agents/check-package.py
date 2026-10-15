#!/usr/bin/env python3
"""Offline packaging checks, not an agent-behavior or Markdown-rendering test."""
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "writing/writing-for-agents"


def check_links(path, boundary):
    text = path.read_text()
    # Current package uses inline links, ATX headings, and fenced code only.
    # This intentionally is not a general Markdown parser.
    assert text.count("```") % 2 == 0, f"Unclosed fence: {path}"
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for raw in re.findall(r"\]\(([^\s)]+)\)", prose):
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            continue  # No network: external links remain outside this check.
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(boundary.resolve()), f"Escaping link: {raw}"
        assert target.exists(), f"Missing link: {path}: {raw}"
        if url.fragment:
            headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
            anchors = [re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-")
                       for h in headings]
            assert unquote(url.fragment) in anchors, f"Missing anchor: {raw}"


def check_package(package):
    for name in ("SKILL.md", "README.md", "LICENSE", "references/structure.md",
                 "references/validation.md"):
        assert (package / name).is_file(), f"Missing shipped file: {name}"
    skill = (package / "SKILL.md").read_text()
    assert skill.startswith("---\nname: writing-for-agents\ndescription: ")
    metadata, body = skill[4:].split("\n---\n", 1)
    assert len(metadata.splitlines()) == 2  # Restricted scalar shape, not YAML parsing.
    assert len(re.findall(r"^## [1-4]\. ", body, re.M)) == 4
    assert body.count("**Complete when:**") == 4
    for path in package.rglob("*.md"):
        check_links(path, package)


def main():
    check_package(PACKAGE)
    print("PASS: shipped files, scalar metadata shape, steps, fences, internal links")
    with tempfile.TemporaryDirectory(prefix="writing-for-agents-") as temp:
        copied = Path(temp) / "writing-for-agents"
        shutil.copytree(PACKAGE, copied)
        check_package(copied)
        print("PASS: isolated package copy with no sibling skills")
        probe = copied / "probe.md"
        for link in ("missing.md", "SKILL.md#missing-heading", "../outside.md"):
            probe.write_text(f"[broken]({link})\n")
            try:
                check_links(probe, copied)
            except AssertionError:
                print(f"PASS: checker rejects {link}")
            else:
                raise AssertionError(f"Checker missed {link}")
    check_links(ROOT / "docs/skills.md", ROOT)
    print("PASS: catalog relative links")
    print("LIMIT: no agent execution, runtime invocation, external fetch or rendered preview")


if __name__ == "__main__":
    main()
