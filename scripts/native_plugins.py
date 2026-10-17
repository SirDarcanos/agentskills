#!/usr/bin/env python3
"""Maintain instruction-only native metadata; no installs, tags, or releases.

Run from any directory with Python 3.10+. Only prepare/select write metadata.
"""

import argparse
import base64
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "SirDarcanos/agentskills"
URL = f"https://github.com/{REPOSITORY}"
GROUPS = ("models", "workflow", "writing")
CLAUDE = Path(".claude-plugin/plugin.json")
CODEX = Path(".codex-plugin/plugin.json")
CATALOGS = (Path(".claude-plugin/marketplace.json"), Path(".agents/plugins/marketplace.json"))
DESCRIPTION = "Reusable coding-agent workflows, writing guidance, and bounded model skills."


def require(condition, message):
    if not condition:
        raise ValueError(message)


def version(value):
    require(isinstance(value, str) and re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", value),
            f"Expected a stable MAJOR.MINOR.PATCH version, got {value!r}")
    return tuple(map(int, value.split(".")))


def load(root, path):
    return json.loads((root / path).read_text())


def save(root, path, value):
    (root / path).parent.mkdir(parents=True, exist_ok=True)
    (root / path).write_text(json.dumps(value, indent=2) + "\n")


def inventory(root):
    paths = sorted(path.parent for group in GROUPS for path in (root / group).glob("*/SKILL.md"))
    require(paths, "No skill packages found")
    names = []
    for path in paths:
        text = (path / "SKILL.md").read_text()
        header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        require(header, f"Missing frontmatter: {path}")
        name = re.search(r"^name: ([a-z0-9-]+)$", header[1], re.M)
        require(name and name[1] == path.name, f"Skill name/directory mismatch: {path}")
        require(re.search(r"^description: .+", header[1], re.M), f"Missing description: {path}")
        require((path / "LICENSE").is_file(), f"Missing package notice: {path}")
        names.append(name[1])
        check_links(path)
        for resource in path.rglob("*"):
            require(not resource.is_symlink(), f"Symlink requires packaging review: {resource}")
            require(resource.is_file() or resource.is_dir(), f"Unsupported resource: {resource}")
    require(len(names) == len(set(names)), "Duplicate skill name")
    return ["./" + path.relative_to(root).as_posix() for path in paths]


def check_links(package):
    """Follow shipped Markdown instructions, never source-history or sibling paths."""
    pending = [package / "SKILL.md"]
    seen = set()
    while pending:
        document = pending.pop()
        if document in seen:
            continue
        seen.add(document)
        text = re.sub(r"^```.*?^```[^\n]*", "", document.read_text(), flags=re.M | re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            linked = (document.parent / unquote(parsed.path)).resolve()
            require(linked.is_relative_to(package.resolve()), f"Non-package instruction link: {document}: {target}")
            require(linked.exists(), f"Missing resource: {document}: {target}")
            if linked.suffix == ".md" and linked.is_file():
                pending.append(linked)


def manifests(root, release):
    version(release)
    common = {
        "name": "agentskills", "version": release, "description": DESCRIPTION,
        "author": {"name": "Nicola Mustone"}, "homepage": URL,
        "repository": URL, "license": "MIT", "skills": inventory(root),
    }
    return ({**common, "displayName": "Agent Skills"},
            {**common, "interface": {"displayName": "Agent Skills", "shortDescription": DESCRIPTION}})


def catalogs(release):
    version(release)
    entry = {"name": "agentskills", "version": release, "description": DESCRIPTION}
    claude = {
        "name": "agentskills", "owner": {"name": "Nicola Mustone"},
        "metadata": {"description": "Agent Skills released collection", "version": release},
        "plugins": [{**entry, "displayName": "Agent Skills", "source": {
            "source": "github", "repo": REPOSITORY, "ref": f"v{release}"}}],
    }
    codex = {
        "name": "agentskills", "interface": {"displayName": "Agent Skills"},
        "plugins": [{**entry, "source": {"source": "url", "url": URL + ".git", "ref": f"v{release}"},
                     "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
                     "category": "Productivity", "interface": {"displayName": "Agent Skills"}}],
    }
    return claude, codex


def selected_version(root):
    plugins = load(root, CATALOGS[0])["plugins"]
    require(len(plugins) == 1, "Expected one collection catalog entry")
    release = plugins[0]["version"]
    version(release)
    return release


def check(root):
    release = load(root, CLAUDE)["version"]
    for path, expected in zip((CLAUDE, CODEX), manifests(root, release)):
        require(load(root, path) == expected, f"Manifest drift (inventory/version/identity/effects): {path}")
    selected = selected_version(root)
    require(version(release) >= version(selected), "Candidate is older than the released catalog")
    for path, expected in zip(CATALOGS, catalogs(selected)):
        require(load(root, path) == expected, f"Catalog drift or non-release source: {path}")
    # These client auto-discovery locations would introduce additional runtime effects
    # or register skills a second time. Supporting files INSIDE skills remain inert.
    for path in ("skills", "commands", "agents", "hooks", ".mcp.json", "mcp.json",
                 ".lsp.json", "lsp.json", "plugin.json", ".app.json", ".claude/settings.json"):
        require(not (root / path).exists(), f"Unexpected plugin auto-discovery path: {path}")
    require((root / "LICENSE").is_file(), "Missing collection license")
    return release, selected


def gh_json(endpoint):
    result = subprocess.run(["gh", "api", f"repos/{REPOSITORY}/{endpoint}"],
                            check=True, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout)


def published(release, request=gh_json):
    """Read-only gate: only the latest public stable GitHub release may be selected."""
    version(release)
    latest = request("releases/latest")
    require(latest.get("tag_name") == f"v{release}" and not latest.get("draft")
            and not latest.get("prerelease") and latest.get("published_at"),
            f"v{release} is not the latest published stable release")
    for path in (CLAUDE, CODEX):
        contents = request(f"contents/{path.as_posix()}?ref=v{release}")
        manifest = json.loads(base64.b64decode(contents["content"]))
        require(manifest.get("name") == "agentskills" and manifest.get("version") == release,
                f"Published manifest/version mismatch: {path}")


def prepare(root, release):
    version(release)
    selected = selected_version(root)
    require(version(release) >= version(selected), "Cannot prepare below selected release")
    for path, value in zip((CLAUDE, CODEX), manifests(root, release)):
        save(root, path, value)
    check(root)  # Catalog selectors deliberately remain on the preceding public release.


def select(root, release, request=gh_json):
    candidate, previous = check(root)
    require(version(previous) <= version(release) <= version(candidate), "Invalid channel transition")
    published(release, request)  # Verify before the first write; no CLI bypass.
    for path, value in zip(CATALOGS, catalogs(release)):
        save(root, path, value)
    check(root)


def export(root, destination):
    """Copy the complete tracked-independent package trees without Git/history/docs."""
    check(root)
    require(not destination.exists(), "Export destination must not exist")
    require(not destination.resolve().is_relative_to(root.resolve()), "Export must be outside the source repository")
    # No partial overwrite or local installation target is ever inferred.
    destination.mkdir(parents=True)
    for group in GROUPS:
        shutil.copytree(root / group, destination / group)
    for path in (CLAUDE, CODEX, *CATALOGS, Path("LICENSE")):
        (destination / path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(root / path, destination / path)
    check(destination)
    compare_resources(root, destination)


def compare_resources(source, packaged):
    """Prove every package byte and executable mode survives a derived copy."""
    for group in GROUPS:
        originals = {p.relative_to(source) for p in (source / group).rglob("*") if p.is_file()}
        copies = {p.relative_to(packaged) for p in (packaged / group).rglob("*") if p.is_file()}
        require(originals == copies, f"Omitted or extra packaged resources: {group}")
        for path in originals:
            a, b = source / path, packaged / path
            require(a.read_bytes() == b.read_bytes(), f"Changed packaged resource: {path}")
            require(a.stat().st_mode & 0o777 == b.stat().st_mode & 0o777, f"Changed resource mode: {path}")
    require((source / "LICENSE").read_bytes() == (packaged / "LICENSE").read_bytes(), "Collection notice drift")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("check")
    validate.add_argument("--published", action="store_true", help="Also verify selected public release via gh")
    sub.add_parser("prepare").add_argument("version")
    sub.add_parser("select").add_argument("version")
    sub.add_parser("export").add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(ROOT, args.version)
        elif args.command == "select":
            select(ROOT, args.version)
        elif args.command == "export":
            export(ROOT, args.destination.resolve())
        candidate, selected = check(ROOT)
        if args.command == "check" and args.published:
            published(selected)
        print(f"Native metadata OK: {len(inventory(ROOT))} skills; candidate {candidate}; catalog v{selected}")
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(f"Native metadata check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
