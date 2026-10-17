# Implementation Preflight

A reusable Git preflight that selects or creates the correct branch before authorized implementation modifies files.

## When to use it

Use the skill when authorized implementation is about to modify a Git repository, regardless of the command, skill or workflow used. It supports direct implementation requests and bounded handoffs from delivery workflows or implementation methods.

The skill is model-invoked; no particular implementation command or companion skill is required. It contributes only Git branch and pull-request preparation. Loading it does not authorize implementation or invoke another workflow.

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
5. returns that result, existing pull-request state and any blockers or unavailable information to its caller.

The caller may be the agent handling a direct request or a workflow or skill. Implementation, validation, documentation, changelog updates, review and commits remain with that caller. Preflight starts no implementation or publication stage; pull-request preparation is offered, not performed unless selected.

## Project prerequisite

Direct and bounded use consume established project guidance or a meaningful equivalent. Missing/conflicting common guidance allows safe inspection, not branch writes; return the specific gap and recommend explicit setup/reconciliation. Do not invoke Setup or manufacture policy. Protected work includes bytes, modes, symlink targets and index entries.

## Requirements

- Git
- GitHub CLI for pull-request detection and creation when using GitHub
- An agent runtime that supports model-invoked skills

## Validate package changes

Check frontmatter, rendered structure, isolated-package links and `git diff --check`. Walk direct implementation, a delivery-workflow handoff and an implementation-method handoff against the description and procedure: each should reach the same Git preparation and caller return without requiring a named command. Planning-only and investigation-only requests should not trigger branch preparation; missing implementation authority permits inspection only. Label these routing walkthroughs separately from executed agent trials. In disposable repositories, inspect direct and bounded entry with equivalent project guidance, missing/conflicting authority, explicit no-integration policy despite an incidental `develop`, continuation of related work and a finished-PR/new-branch route. Compare protected staged/unstaged/untracked bytes, modes, symlink targets and index entries before/after preparation; uncertain ownership must block conflicting operations. Record actual commands/results separately from these authored cases. Read-only inspection without guidance does not authorize branch preparation. These checks need no tracker writes, installation or model calls.

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
