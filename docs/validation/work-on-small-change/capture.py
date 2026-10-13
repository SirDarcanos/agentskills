"""Capture this trial's synthetic files/checks; never launch agents.

Usage: python3 -B capture.py PROJECT OUTPUT [--test]
Outputs portable JSON; source paths in unittest output become <fixture>.
"""

import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys


def manifest(project):
    entries = {}
    for path in sorted(project.iterdir()):
        mode = path.lstat().st_mode
        entry = {"mode": oct(stat.S_IMODE(mode))}
        if stat.S_ISLNK(mode):
            entry.update(kind="symlink", target=os.readlink(path))
        elif stat.S_ISREG(mode):
            entry.update(kind="file", sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        else:
            raise ValueError(f"Unexpected fixture entry: {path.name}")
        entries[path.name] = entry
    return entries


def main():
    project = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2])
    record = {"python": sys.version.split()[0], "before": manifest(project)}
    if len(sys.argv) == 4 and sys.argv[3] == "--test":
        command = [sys.executable, "-B", "-m", "unittest", "-v"]
        result = subprocess.run(command, cwd=project, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, check=False)
        record.update(command="python3 -B -m unittest -v", cwd="<fixture>",
                      exit_code=result.returncode,
                      output=result.stdout.replace(str(project), "<fixture>"))
        record["after"] = manifest(project)
        if record["before"] != record["after"]:
            raise ValueError("Check changed the fixture")
    elif len(sys.argv) != 3:
        raise ValueError("Expected PROJECT OUTPUT [--test]")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(f"Captured {len(record['before'])} entries; check exit: "
          f"{record.get('exit_code', 'not run')}")
    # Capture success is not test success: the record preserves the check exit.


if __name__ == "__main__":
    main()
