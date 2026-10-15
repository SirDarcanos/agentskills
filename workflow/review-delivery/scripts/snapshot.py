#!/usr/bin/env python3
"""Read-only fingerprints for an explicit Git file scope; not a scope discoverer."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    return subprocess.check_output(
        ["git", "--literal-pathspecs", "-c", "core.fsmonitor=false",
         "-C", str(root), *args], env=env,
        stderr=subprocess.PIPE,
    )


def file_state(root, name):
    path = root / name
    # Never traverse an included path's symlinked parent, even within the repo.
    for parent in path.parents:
        if parent == root:
            break
        if parent.is_symlink():
            raise ValueError("symlinked parent: " + name)
    try:
        info = path.lstat()
    except FileNotFoundError:
        return {"kind": "absent"}
    mode = stat.S_IMODE(info.st_mode)
    if stat.S_ISLNK(info.st_mode):
        return {"kind": "symlink", "mode": mode,
                "target_sha256": digest(os.fsencode(os.readlink(path)))}
    if stat.S_ISREG(info.st_mode):
        return {"kind": "file", "mode": mode, "sha256": digest(path.read_bytes())}
    raise ValueError("not a regular file or leaf symlink: " + name)


def capture(root, base, paths):
    root = Path(root).resolve()
    paths = sorted(set(paths))
    if not paths:
        raise ValueError("empty scope")
    for name in paths:
        p = PurePosixPath(name)
        if (not name or p.is_absolute() or ".." in p.parts
                or p.as_posix() != name or ".git" in p.parts or name == "."):
            raise ValueError("noncanonical repository-relative path: " + name)
    base_id = git(root, "rev-parse", "--verify", "--end-of-options",
                  base + "^{commit}").decode().strip()
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode().strip()
    branch = git(root, "rev-parse", "--abbrev-ref", "HEAD").decode().strip()
    index = git(root, "ls-files", "--stage", "-z", "--", *paths)
    for entry in index.split(b"\0"):
        if entry:
            metadata = entry.split(b"\t", 1)[0].split()
            if metadata[0] == b"160000" or metadata[2] != b"0":
                raise ValueError("submodule or unresolved index requires manual capture")
    options = ("--no-ext-diff", "--no-textconv", "--no-renames", "--binary",
               "--full-index", "--no-color", "--src-prefix=a/", "--dst-prefix=b/")
    committed = git(root, "diff", *options, base_id, head, "--", *paths)
    staged = git(root, "diff", *options, "--cached", head, "--", *paths)
    unstaged = git(root, "diff", *options, "--", *paths)
    status = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all",
                 "--", *paths)
    files = {name: file_state(root, name) for name in paths}
    if git(root, "rev-parse", "HEAD").decode().strip() != head:
        raise ValueError("HEAD changed during capture")
    return {"format": 1, "root": str(root), "base": base_id, "head": head,
            "branch": branch, "paths": paths, "files": files,
            "committed_sha256": digest(committed), "staged_sha256": digest(staged),
            "unstaged_sha256": digest(unstaged), "index_sha256": digest(index),
            "status_sha256": digest(status)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    pin = commands.add_parser("pin")
    pin.add_argument("--base", required=True)
    pin.add_argument("paths", nargs="+")
    check = commands.add_parser("check")
    check.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "pin":
            root = git(Path.cwd(), "rev-parse", "--show-toplevel").decode().strip()
            print(json.dumps(capture(root, args.base, args.paths), indent=2, sort_keys=True))
            return 0
        before = json.loads(args.snapshot.read_text())
        if not isinstance(before, dict) or before.get("format") != 1:
            raise ValueError("unsupported snapshot format")
        if (not isinstance(before.get("root"), str)
                or not isinstance(before.get("base"), str)
                or not isinstance(before.get("paths"), list)
                or not all(isinstance(p, str) for p in before["paths"])):
            raise ValueError("invalid snapshot identity or paths")
        after = capture(before["root"], before["base"], before["paths"])
        changed = sorted(key for key in after if before.get(key) != after[key])
        print(json.dumps({"status": "stale" if changed else "matching-listed-paths",
                          "changed_fields": changed}, sort_keys=True))
        return 1 if changed else 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print("snapshot unavailable: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
