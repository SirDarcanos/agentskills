---
name: resolve-merge-conflicts
description: Resolve an in-progress Git merge or rebase conflict during already-authorized integration work, preserving compatible intent and unrelated changes. Pause for incompatible intent or unsafe continuation.
---

# Resolve merge conflicts

Use during authorized integration without requiring a separate invocation. Loading this skill grants no integration authority: inspect the original task and project policy for the operation, branches and permitted completion. A request only to inspect conflicts stays read-only. Do not start a new merge/rebase just because conflicts are mentioned.

## 1. Inspect the operation and protect existing work

Read project instructions and the integration goal. Inspect `git status`, branch/HEAD, recent history, staged and unstaged diffs, untracked files and `git ls-files -u`. Identify the merge heads or current rebase commit and target; detached HEAD can be normal during rebase. Use `git rev-parse --git-path` for operation metadata, including in linked worktrees. If no merge/rebase is active, report that state rather than guessing a different operation.

Record the starting HEAD, operation/target, conflict paths, intended resolution scope, and protected work's bytes, modes, symlink targets and index entries. Distinguish cleanly integrated staged changes belonging to this operation from unrelated staged work; use the caller's pre-operation evidence when available. Unknown ownership blocks conflicting writes and eventual completion, not safe inspection elsewhere. Preserve untracked files and unrelated history too. No automatic stash, reset, checkout of whole sides, clean or index manipulation to clear an obstacle.

**Complete when:** authority, operation and owned paths are known, and unrelated/uncertain work is identified and protected.

## 2. Resolve compatible intent

Read [Git mechanics](references/git-mechanics.md) before resolving; it covers stage meanings, non-text conflicts and safe staging/continuation. For each conflict inspect available base and side versions, surrounding code/callers/tests, commit messages and relevant task/PR decisions. During rebase, derive side identity from the current operation rather than interpreting “ours” as the user's original branch.

Resolve each compatible conflict so both intended effects survive; include necessary related edits only within approved scope. Inspect whole-file behavior, not just marker removal. Treat modify/delete, rename, binary, executable-bit, symlink and submodule conflicts according to their actual data and intended outcome. Missing content, incompatible product rules or uncertain meaning requires a decision, not a guessed winner or invented behavior.

Preserve completed resolutions and pause the affected integration with the conflicting intentions, paths/commits, exact decision needed and recommended next step. Do not stage a partial file as fully resolved. Stage only fully inspected resolution paths with explicit path arguments; verify the staged result and protected index/worktree against the baseline.

**Complete when:** each conflict is either intentionally resolved and narrowly staged, or preserved with a precise blocker. Unrelated work remains unchanged.

## 3. Check the result before continuing

Discover relevant checks from the target's instructions and configuration. Inspect the resolution diff and remaining unmerged entries; check for accidental markers in changed text and use `git diff --cached --check` for staged whitespace errors. Run available relevant tests, type checks and formatting checks in the named environment; avoid automatic whole-project reformatting. Include tests of both retained intentions when existing checks are insufficient.

Record commands, exit codes, observed outcomes and unavailable checks with reasons. Inspect check side effects and recompare protected work. Failed or materially unavailable checks block continuation: preserve the result and report the failing obligation rather than installing tools, weakening checks or silently committing. Repair only integration-caused defects within task authority; unrelated failures and consequential behavior decisions return to the caller.

**Complete when:** relevant checks have current results, preservation is confirmed and any unsafe continuation has a specific blocker.

## 4. Finish only the authorized integration

Before every commit/continuation, require no unmerged entries, fresh relevant checks and an inspected index containing only the integration's intended changes. A merge commit consumes the index: unrelated staged content blocks completion even when its bytes are preserved. Ask how that work should be handled; leave it staged until separately authorized. Do not hide it by unstaging/stashing or include it by accident. Unrelated unstaged edits also block when they contaminate required checks or risk continuation. Rebase continuation rejects unstaged tracked changes even outside the conflict paths; preserve those edits and request an authorized handling plan rather than trying to clear them.

If the original task and project policy authorize completion, finish the active merge with `git merge --continue` or continue the active rebase with `git rebase --continue`. Inspect hook/editor failures without bypassing hooks or signing policy. After each rebase stop, re-inspect the operation/current commit and repeat steps 1–3 for new conflicts, retaining the original protected-work baseline. Stop on unexpected state, empty-commit decisions or unsafe continuation; skipping a commit needs separate approval. Repeat only while making understood progress within the caller's execution bounds; a repeated failure returns a blocker rather than a retry loop.

After Git reports completion, confirm operation metadata is gone, intended branch/history and integrated content are correct, protected work is intact, and final-state relevant checks pass. When completion is not authorized, leave the inspected resolutions in place and report the pending command and required permission.

Abort, discard, skip, push and merge-to-main are separate actions requiring their own authorization. This skill neither grants nor substitutes for it; preserve partial work when pausing instead of automatically aborting.

**Complete when:** the authorized operation has finished and been checked, or the exact pending operation/decision is reported with resolutions preserved.

## Return

Report operation/branch/HEAD, resolutions and retained intentions, protected-work comparison, check commands/results/gaps, completed versus pending integration, and the exact decision or permission needed. Distinguish local completion from push, PR merge, deployment and release. For package validation rather than target integration, read [validation](references/validation.md).
