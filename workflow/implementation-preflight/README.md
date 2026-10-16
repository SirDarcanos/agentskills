# Implementation Preflight

A companion skill that selects or creates the correct Git branch before an implementation workflow modifies files.

## When to use it

The skill is model-invoked when implementation is about to begin in a Git repository, including work started with:

```text
/implement
```

It does not replace or invoke `/implement`. You continue using the upstream implementation skill normally, so its updates remain independent. Implementation Preflight contributes only the Git branch and pull-request policy to the same task.

## Branch strategy

The skill follows the repository's existing workflow:

- Explicit project branch policy wins, including a documented no-integration-branch policy. Otherwise `develop` or `development` is a candidate; unresolved ambiguity pauses preparation.
- Otherwise, new work branches from the default branch and targets the default branch.
- It never introduces a development branch.

It continues a current feature branch when its work and active pull request match the request. It creates a new short-lived branch when work begins from a default or integration branch, the previous pull request is finished, or the request is a separate reviewable change.

Ambiguous or unrelated work causes the skill to ask before stashing, resetting, rebasing, transferring, or discarding anything.

## How it works

Before implementation, the skill:

1. inspects the working tree, branches, remotes, repository conventions, commits, diffs, and pull requests;
2. selects the existing branch, integration branch, or default branch as the correct route;
3. creates a typed short-lived branch when needed;
4. reports the working branch, base, and intended pull-request target;
5. yields to the active implementation workflow.

After implementation, it only reports the resulting branch and offers to open or update the pull request. Validation, documentation, changelog updates, review, and commits remain owned by their existing workflows.

## Project prerequisite

Direct and bounded use consume established project guidance or a meaningful equivalent. Missing/conflicting common guidance allows safe inspection, not branch writes; return the specific gap and recommend explicit setup/reconciliation. Do not invoke Setup or manufacture policy. Protected work includes bytes, modes, symlink targets and index entries.

## Requirements

- Git
- GitHub CLI for pull-request detection and creation when using GitHub
- An agent runtime that supports model-invoked skills

## Validate package changes

Check frontmatter, rendered structure, isolated-package links and `git diff --check`. In disposable repositories, inspect direct and bounded entry with equivalent project guidance, missing/conflicting authority, explicit no-integration policy despite an incidental `develop`, continuation of related work and a finished-PR/new-branch route. Compare protected staged/unstaged/untracked bytes, modes, symlink targets and index entries before/after preparation; uncertain ownership must block conflicting operations. Record actual commands/results separately from these authored cases. Read-only inspection without guidance does not authorize branch preparation. These checks need no tracker writes, installation or model calls.

## Files

```text
implementation-preflight/
├── SKILL.md
└── README.md
```

[`SKILL.md`](SKILL.md) contains the branch-selection rules, safety boundaries, and handoff procedure.

## Install

```bash
npx skills add SirDarcanos/agentskills --skill implementation-preflight
```

You can also copy the `implementation-preflight` directory into your agent's skill discovery path.
