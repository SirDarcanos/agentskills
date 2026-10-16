#!/usr/bin/env python3
"""Offline checks for what-now packaging, not agent behavior.

Kept at its original ask-nico path; README.md and examples.md beside it
are historical #112 evidence, not current invocation instructions.
"""
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "workflow/what-now"


def check_links(path, boundary):
    text = path.read_text()
    assert text.count("```") % 2 == 0, f"Unclosed fence: {path}"
    # Limited to this package's inline links, ATX headings and fenced blocks.
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for raw in re.findall(r"\]\(([^\s)]+)\)", prose):
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(boundary.resolve()), f"Escaping link: {raw}"
        assert target.exists(), f"Missing link: {raw}"
        if url.fragment:
            headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
            anchors = [re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-")
                       for h in headings]
            assert unquote(url.fragment) in anchors, f"Missing anchor: {raw}"


def check_package(package):
    for name in ("SKILL.md", "README.md", "LICENSE", "references/validation.md"):
        assert (package / name).is_file(), f"Missing shipped file: {name}"
    skill = (package / "SKILL.md").read_text()
    assert skill.startswith("---\nname: what-now\ndescription: ")
    metadata, body = skill[4:].split("\n---\n", 1)
    assert len(metadata.splitlines()) == 3  # Shape check, not YAML parsing.
    assert metadata.endswith("disable-model-invocation: true")
    assert len(re.findall(r"^## [1-4]\. ", body, re.M)) == 4
    assert body.count("**Complete when:**") == 4
    assert 'specifically invokes `what-now`' in body
    assert "source mention, quoted command, another skill's handoff" in body
    assert "Without that user invocation, stop this procedure" in body
    assert "Even “recommend and then run it” ends here with the recommendation" in body
    assert "Do not invoke candidates or companions, delegate work, call assessment services" in body
    for path in package.rglob("*.md"):
        assert not re.search(r"(?:/skill:|--skill |name: |invokes `)ask-nico",
                             path.read_text()), f"Stale invocation: {path}"
        check_links(path, package)


def main():
    check_package(PACKAGE)
    print("PASS: shipped files, metadata shape, four steps, fences and links")
    with tempfile.TemporaryDirectory(prefix="what-now-") as temp:
        copied = Path(temp) / "what-now"
        shutil.copytree(PACKAGE, copied)
        check_package(copied)
        print("PASS: isolated package without siblings")
        probe = copied / "probe.md"
        for link in ("missing.md", "SKILL.md#missing-heading", "../outside.md"):
            probe.write_text(f"[broken]({link})\n")
            try:
                check_links(probe, copied)
            except AssertionError:
                print(f"PASS: rejects {link}")
            else:
                raise AssertionError(f"Missed broken link: {link}")
    for path in (ROOT / "docs/validation/ask-nico").glob("*.md"):
        check_links(path, ROOT)
    check_links(ROOT / "docs/skills.md", ROOT)
    print("PASS: evidence and catalog links")
    print("LIMIT: no behavioral trial, YAML parser, external fetch or visual preview")


if __name__ == "__main__":
    main()
