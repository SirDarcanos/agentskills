# Git mechanics

Read before resolving a conflict. Commands below are inspection patterns, not permission to modify the target. Quote actual paths and use `--` where supported; prefer NUL-delimited output when processing filenames programmatically.

## Identify content and sides

1. Use `git status`, `git diff --name-only --diff-filter=U` and `git ls-files -u` to enumerate conflicts. `git diff`, `git diff --cached` and `git diff --cc` expose different worktree/index views; inspect each relevant view.
2. Inspect operation metadata via `git rev-parse --git-path MERGE_HEAD`, `git rev-parse --git-path rebase-merge` and `git rev-parse --git-path rebase-apply`. Read the files/directories that exist, not a hard-coded `.git/` path. `git show REBASE_HEAD` identifies the patch at a stopped rebase; `git rebase --show-current-patch` provides its diff. For merges inspect `HEAD`, the merge head(s) and their common ancestry.
3. `git show ':1:path'`, `git show ':2:path'`, `git show ':3:path'` inspect base, stage 2 and stage 3 when present. A missing stage is normal for some add/delete conflicts. Use actual paths from the index. During an ordinary merge stage 2 is current HEAD and stage 3 the incoming side. During rebase stage 2 is the rebased-so-far upstream side and stage 3 the commit being replayed. Inspect the replayed commit and its parent to recover its intended change.
4. Read source history and approved decisions for semantic intent. Conflict markers and stage numbers alone do not settle which product rule should win. Where PR/tracker access is unavailable, use sufficient local evidence or report the missing deciding source.

## Resolve and stage deliberately

- Text: edit the desired combined content, inspect the full result and its diff. Marker searches can find accidental leftovers but cannot prove semantic resolution.
- Modify/delete or rename: determine the intended final paths and content first. Preserve needed edits at their agreed location. Stage only those exact paths, including an intentional deletion with `git add -u -- 'old-path'` after inspecting that deletion. Removal of worktree content needs authority for that resolution; an ambiguous deletion pauses.
- Binary, symlink, mode or submodule: inspect object IDs, index modes, link targets or submodule commits using suitable tools. Seek a decision when the intended result cannot be established; text-marker editing does not resolve these cases.
- Use `git add -- 'resolved-path'` for a fully resolved file. It stages the entire file, so unrelated edits inside that file require an approved hunk-level plan or a pause. Never use `git add .`, `git add -A`, `git commit -a` or blanket ours/theirs selection as a shortcut.
- After staging inspect `git diff --cached`, `git diff`, `git ls-files -u` and protected-path index entries. Cleanly auto-merged changes are part of the operation only when evidence establishes their provenance; they must still be inspected before completion.

## Continuation is a new gate

`git merge --continue` completes the existing merge using staged changes. `git rebase --continue` may apply several commits and stop again; inspect its output and operation state even when it returns nonzero. A new conflict stop is not permission to skip or restart the rebase. A command failure can leave partial effects, so inspect before deciding what to do next.

An empty replayed commit, signing/editor error, hook failure, unexpected HEAD movement or ambiguous operation state requires a precise report. Preserve commit-message conventions, hooks and signing requirements. Do not set bypass flags or change configuration merely to make continuation succeed.

After completion, inspect `git status`, relevant history/parents and content and rerun final-state checks. A clean worktree is not required when deliberately protected unrelated changes remain; compare them to the original baseline instead.
