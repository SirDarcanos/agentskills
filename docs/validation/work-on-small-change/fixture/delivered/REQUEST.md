# Trial request and lightweight agreement

Synthetic request authored for #29 under the maintainer's approved trial scope:
“Recognize .md filenames regardless of extension case; keep the filtering API
and all other filename behavior unchanged.”

This file is the fixture's authoritative agreement, not a claim that a real
customer made this request. Its acceptance oracle is fixed before building.

| ID | Observable acceptance |
| --- | --- |
| F1 | `is_markdown("notes.MD")` and `is_markdown("notes.mD")` return true, as does existing lowercase `.md`. |
| F2 | Only the final `.md` suffix matches: `.markdown`, `.md.bak`, empty names and names without an extension return false. No trimming: `"notes.md "` returns false. |
| F3 | `markdown_files` returns matching original strings in input order without altering casing or duplicates; existing lowercase behavior remains. |
| F4 | Only code, relevant tests and README behavior text change; unrelated note bytes/mode and link target remain unchanged. |

Required now: case-insensitive ASCII extension recognition and regression
checks for F1–F4. Worth considering later: additional extensions, only if a
future request needs them. Explicitly unnecessary: CLI, file-system access,
ticket hierarchy, configuration and a domain/ADR record. Accepted trial
limitation: string inputs only and no claim of file existence, path validation
or content detection; these are fixed fixture boundaries selected under #29,
not waived material requirements. No consequential product uncertainty remains.
