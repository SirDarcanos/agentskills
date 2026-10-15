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

- If `develop`, `development`, or another documented integration branch exists, new work branches from it and targets it with a pull request.
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

## Requirements

- Git
- GitHub CLI for pull-request detection and creation when using GitHub
- An agent runtime that supports model-invoked skills

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
