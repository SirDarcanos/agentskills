---
name: implementation-preflight
description: Prepare the correct Git branch and pull-request target before implementation begins. Use when an agent is about to implement a change in a Git repository, including work started through /implement, and it must decide whether to continue the current branch or create a short-lived branch.
---

# Implementation preflight

Complete this Git and pull-request preflight before modifying files. This skill complements the active implementation workflow; it does not replace, invoke, or restate `/implement` or another implementation skill.

## Workflow

### 1. Inspect the repository

Determine:

- the working tree, including staged, unstaged, and untracked changes;
- the current branch and its upstream;
- the remote default branch;
- local and remote branches;
- repository documentation that names an integration branch;
- commits and diff between the current branch and its likely base;
- the current branch's open, closed, or merged pull request when `gh` is available.

Fetch remote refs when `origin` exists and fetching is safe. Treat an existing `develop` or `development` branch as the integration branch. Prefer an explicit repository convention when it names a different integration branch. Ask when multiple candidates remain ambiguous.

If the directory is not a Git repository, report that no branch preflight applies and let the active implementation workflow continue.

This step is complete when the current work, branch purpose, default branch, integration branch if any, and pull-request state are known or explicitly unavailable.

### 2. Select the route

When an integration branch exists, use it as the base for new work and as the intended pull-request target. Otherwise, use the default branch. Follow an existing development branch; never introduce one through this skill.

Continue the current branch only when all of these are true:

- it is neither the default branch nor the integration branch;
- its name, commits, diff, or pull request matches the requested work;
- it has no closed or merged pull request;
- any open pull request targets the selected integration or default branch;
- the request belongs in the same reviewable change.

Create a new short-lived branch when any of these are true:

- the current branch is the default or integration branch;
- its pull request was closed or merged;
- the request is a distinct feature, fix, refactor, documentation change, or other independently reviewable unit;
- continuing would mix unrelated work or unintentionally stack changes.

Ask before proceeding when the branch purpose is ambiguous, working-tree changes appear unrelated, an open pull request targets a different base, or selecting the correct route would require a stash, reset, rebase, force push, discard, or transfer of work. Never perform those operations implicitly.

Clearly related uncommitted changes on the default or integration branch may move onto a new branch with `git switch -c`; this preserves the working tree. Ask first when their relationship to the request is uncertain.

This step is complete when exactly one route is selected: continue the current branch, branch from the integration branch, or branch from the default branch.

### 3. Prepare the working branch

When creating a branch:

1. Use the latest safe local view of the selected remote base. Fast-forward a clean local base when possible; do not create a merge commit solely to begin work.
2. Choose a concise type-and-subject name such as `feat/add-search`, `fix/token-refresh`, `docs/setup-guide`, or `refactor/config-loader`.
3. Avoid local and remote branch-name collisions.
4. Preserve related working-tree changes.

When continuing a branch, preserve its name, history, upstream, and working tree. Do not rebase, merge the base, force-push, or rename it merely as preflight.

Before implementation starts, state:

- whether the branch was created or continued;
- the working branch;
- its base branch;
- the intended pull-request target;
- any existing pull request;
- any limitation caused by a missing remote or unavailable GitHub CLI.

This step is complete when `HEAD` is on a suitable working branch and implementation can commit without targeting the default or integration branch directly.

### 4. Yield to implementation

Let the active implementation skill or instructions perform the work, validation, review, and commits. Do not duplicate or alter that workflow.

After implementation finishes, report the resulting branch and existing pull request, if any. Offer to open a pull request or update the existing one against the target selected during preflight. Perform no additional validation, documentation, or changelog work through this skill.
