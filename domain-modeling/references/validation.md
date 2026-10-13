# Validation

From the repository root, using Python 3.9+:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s domain-modeling/tests -p 'test_*.py'
git diff --check
```

For a copied standalone package, run discovery against `tests/`. Tests inspect frontmatter and package-local Markdown links. They require no network or sibling package and do not execute the agent workflow.

## Behavioral scenarios

Use synthetic temporary projects and retain original file hashes, the exact request/handoff, tool actions, resulting diff, and report. An actual agent run is required to claim these observations; authored scenarios or static review are not executed behavioral evidence.

| Input | Required observation |
| --- | --- |
| Direct discussion without write approval | Plan-only result; no files or directories created. |
| Caller plan-only handoff with settled answers | Reuse answers; propose exact delta; preserve every file hash. |
| Approved handoff restricted to one glossary section | Only that section changes; other affected consumers returned to caller. |
| No confirmed terms or qualifying decision | Explain omission; create no empty glossary or ADR directory. |
| Overloaded term and code/spec disagreement | Test meanings with scenarios; resolve through authority or report conflict; no silent code rename. |
| Multi-context map with differing local meanings | Preserve scoped meanings, paths, and relationships rather than a new global glossary. |
| Proposed replacement ADR | Keep current decision active; proposed status and link are clear. |
| Accepted replacement ADR | Retain old rationale; mark supersession and verify both links. |
| Concurrent file change or interrupted supersession | Reinspect, stop stale writes, reconcile remaining approved delta without duplicating records. |
| Unchanged rerun | No substantive delta, duplicate questions, new records, or cosmetic churn. |
| Sensitive source material | Public-safe definitions and rationale; no credentials or unnecessary personal data. |

Review rendered Markdown, frontmatter triggers, all local links, approval boundaries, document ownership, and the diff for private data or nonportable paths. Distinguish packaging checks, direct static review, and agent walkthroughs in the result. No installation, external model call, live project mutation, or deployment is authorized merely to validate this skill.
