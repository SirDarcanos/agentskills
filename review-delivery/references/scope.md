# Delivered scope

This is the authoritative snapshot contract consumed by delivery callers. Keep a compact Markdown record at the target's approved evidence location; machine fingerprints are supporting artifacts, not a mandatory state service. Retain no secret contents or unrelated private logs.

## 1. Discover and bound

Inspect the target's branch/worktree, actual status and supplied scope. For Git, resolve the requested comparison semantics explicitly: a fixed commit uses that commit; a branch-relative review normally uses the resolved merge-base with the named target. Record the original selector, rule and full resulting base ID; do not silently switch two-dot/three-dot semantics. Resolve delivered HEAD to a full ID. If no meaningful base can be established, block comparison rather than invent it.

Inventory committed differences from base to HEAD, index changes from HEAD, working-tree changes from index and relevant untracked files. Use NUL-delimited Git output when processing filenames. For example, `git status --porcelain=v1 -z --untracked-files=all`, `git diff --name-status -z <base> HEAD`, `git diff --cached --name-status -z` and `git diff --name-status -z` identify candidates; inspect authorized actual patches/files separately. Account for both old and new paths of renames, deletions, mode changes and symlinks. Scope may include relevant unchanged callers, tests, configuration and supporting evidence. Check directory-scoped authority for those paths.

Record every candidate as included, excluded with rationale/protection, or uncertain. Investigate uncertain ownership without changing it; a material exclusion or unreadable input blocks complete review. Ignored/generated files are not automatically authorized: include only when relevant and approved. Submodule state needs its own resolved commit/dirty manifest and content access; a gitlink alone cannot prove its dirty contents. Avoid stash, reset, clean, checkout, staging or index mutation during review.

**Complete when:** the file manifest accounts for each relevant candidate and supporting input; unavailable material content is a blocker, not a clean finding.

## 2. Record and expose the state

Minimum snapshot fields:

| Field | Content |
| --- | --- |
| Identity | Target/worktree, branch, original base selector and comparison rule, resolved base and HEAD IDs; non-Git marks these inapplicable |
| Agreement/authority | Spec/brief and acceptance IDs, standards/policy sources with revision or content digest, approved operations and disclosure/retention location |
| Scope manifest | Included exact paths and role (change/support), rename source/destination, deletion/absence, protected/excluded paths with rationale, unavailable inputs |
| Fingerprints | Separate base→HEAD, HEAD→index and index→working-tree patch fingerprints; scoped index entries/status; final content and modes for files, link target for symlinks, absent markers for deletions; include all authorized untracked files and supporting inputs |
| Access/freeze | Actual diffs and final files plus relevant context available to reviewers; immutable snapshot identity or named scoped-write freeze and owner; before/after comparisons |

Separate deltas prevent a staged change later undone in the working tree from disappearing. Inspect the final integrated behavior as well as layer differences. Use full patches with binary/mode metadata and deterministic options; include content fingerprints even for untracked/binary files. SHA-256 is sufficient for identifying observed bytes; neither hashing nor status proves semantic correctness.

For non-Git work, retain authorized before/after manifests of exact paths, content/mode or symlink-target fingerprints and absent/new markers, with actual source access. If a historical baseline is unavailable, disclose that limitation and block any material comparison claim; current-state inspection remains possible. Apply the same agreement/freeze/freshness rules.

### Optional Git helper

With Python 3.9+ and Git available, `scripts/snapshot.py` captures explicitly named repository-relative **file paths**, never discovers scope or launches reviewers. Resolve the base before use. Run from the target repository, resolving the script from this installed package:

```text
python3 -B <package>/scripts/snapshot.py pin --base <resolved-base> -- <file> <other-file> > <approved-evidence>/scope.json
python3 -B <package>/scripts/snapshot.py check <approved-evidence>/scope.json
```

Store the artifact outside included scope. Output contains paths, IDs and hashes, not file contents. Exit 0 means listed paths match; exit 1 means stale; exit 2 means invalid/unavailable capture. It fingerprints supporting files only if explicitly included. It rejects directories, submodules, unresolved index entries, path escapes and symlinked parents; handle these manually under this contract or report the affected blocker. Leaf symlink targets are fingerprinted without following them.

The helper is read-only toward the repository. Its check does **not** detect a new relevant path outside the pinned list, an external agreement edit, or concurrent transient writes reverted before capture. Repeat discovery and compare those inputs separately. Do not claim full freshness from helper exit 0 alone. Copying or running the helper is optional; an equivalent inspected manifest satisfies the contract.

## 3. Detect drift

Freeze scoped writes before initial capture and keep the freeze through both reports and final comparison. Verify immutable snapshots actually contain all included dirty files and supporting inputs; a commit-only archive cannot represent a dirty delivery. Compare state before each reviewer reads and after both finish, and again when consuming retained evidence. If a freeze cannot be guaranteed, use an authorized immutable snapshot; otherwise report unreliable freshness as a blocker.

Repeat candidate discovery with the same approved ownership boundary, comparison rule and exclusions. Compare path membership, base/HEAD, index/staged/unstaged fingerprints, final contents/modes/link targets, agreement, standards and check-input fingerprints. Newly relevant files, renamed/deleted paths, changed policy or check evidence can invalidate coverage even if the old manifest's files still match. Changes outside scope remain protected; reassess relevance without incorporating them silently.

Report exactly which inputs changed and which axes/checks they affect. Keep old evidence labeled stale for its old snapshot; repin and renew affected review. If a new HEAD only commits identical content, retain content evidence solely after explicit full-manifest/delta equivalence is recorded; rerun branch/commit/integration-sensitive checks. A new SHA is not automatically equivalent.
