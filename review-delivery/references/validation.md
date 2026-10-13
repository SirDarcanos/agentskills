# Review Delivery validation

Read when changing or validating this package. There is no shared repository test command. The helper tests are offline and use temporary synthetic Git repositories; they never launch reviewers, call model services, install anything or mutate a live tracker.

## Reproducible checks

From the repository root:

```bash
python3 -B review-delivery/scripts/test_snapshot.py
git diff --check
```

Read all changed Markdown and frontmatter, resolve every relative link/anchor from its containing file, and inspect rendered headings, tables and code blocks. Copy only `review-delivery/` to a temporary location and run its helper tests there: no sibling package or workstation path should be needed. Inspect the full diff (including untracked files) for private data, generated files, local paths, vendored material and unauthorized legacy-skill changes.

### Executable fixture scope

The test fixture establishes a base commit, a delivered commit, staged and unstaged changes on the same file, a dirty formatter, a new untracked duplicate, deletion/rename paths, a leaf symlink, supporting input with an unusual filename, and unrelated staged/unstaged/untracked sentinels.

Synthetic agreement **F1:** heading normalization preserves case and words while trimming outer whitespace. Synthetic standard **S1:** the formatter owns heading normalization; consumers reuse it instead of duplicating the rule. Known findings: `formatter.py:2` uppercases text only in uncommitted work (F1 violation); untracked `duplicate.py:1–2` owns a second normalization implementation (S1 violation). Neither appears in the base→HEAD patch.

Tests assert complete explicit-path capture, distinct committed/staged/unstaged fingerprints, missing and rename endpoint states, known defective behavior and duplicate source presence, CLI stale detection after editing the untracked file, index-only drift, content-identical-commit drift, mode/link/deletion/support-input drift and unchanged protected bytes/index/history. Invalid bases, malformed artifacts, path escapes, directories and symlinked parents fail closed. A new file outside the pinned list deliberately leaves helper output unchanged; rediscovery identifies it and a repinned inventory differs. This regression guards against claiming the helper is a complete scope discoverer.

These assertions demonstrate scope coverage, defect observability and helper drift detection. They are **not evidence that an independent agent found the defects**.

## Reviewer trial protocol (requires separate permission)

1. Create the fixture above with explicit inspection-only delegation/disclosure authority. Pin all relevant files and supporting agreement/standard, freeze writes and retain actual diffs/files. Keep sentinels excluded and protected. Name reviewer identities, independent contexts, finite bounds and available slots.
2. Execute Standards and Spec reviewers separately using the actual skill and report contract; give neither the expected findings nor the other's conclusions. Check whether Standards reports the duplicate and Spec reports case corruption with locations/rationale/materiality. Retain actual execution pointers and findings, not an authored expected report.
3. Modify the untracked file after review. Repeat discovery/fingerprints and require stale evidence, not approval for the new state. Repin before renewed review.
4. In a no-delegation/unavailable-runtime variant, require an explicit independent-review acceptance blocker. Lead inspection is not relabeled independent. Do not launch a worker to demonstrate lack of permission.

This protocol is an **authored scenario, unexecuted** until authorized execution is recorded. Non-Git manifests, submodule/manual capture, worker timeout and resumed retained evidence also require honest branch-specific trial evidence, not extrapolation from helper tests.

## #24 execution record

Executed locally with Python 3.14.7 and Git 2.54.0 (Apple Git-157), from baseline `c3d4dcb698b2ae4ebd4d0affd1dbaea7da89b5cc` on `feat/review-delivery`, with the new package still uncommitted:

| Check | Actual result |
| --- | --- |
| `python3 -B review-delivery/scripts/test_snapshot.py` | Exit 0; all 11 fixture checks passed, including dirty-only scope, submodule/unmerged-index rejection and malformed artifacts. |
| Same command against a temporary isolated copy of only this package | Exit 0; all 11 checks passed without repository siblings. |
| Python relative-link/anchor and frontmatter assertions across the new package and changed repository docs | Exit 0; 41 relative links/anchors resolved; name/description and model-discoverable frontmatter checked. |
| `git diff --check` | Exit 0 for tracked edits; full staged diff is checked again before commit. |
| Direct author inspection | Procedure, scope/report tables and code blocks inspected against #24 and the accepted contract; this is self-review, not independent review. No Markdown renderer was available, so HTML rendering was not executed. |

Independent Standards/Spec reviewer execution is **not run**: this session's implementation authority does not grant delegation. Consequently actual reviewer finding detection and runtime blocker/stale-report behavior remain an acceptance evidence gap; the fixture/helper checks do not replace them. No installation, global legacy command replacement, optional assessment, model vote, repair loop or integrated workflow trial is included.

## Documentation impact

This package owns the delivered snapshot and separate axis report contracts. The repository overview, accepted design implementation pointer and changelog identify the new companion. `work-on` already discovers a semantically compatible companion and consumes this snapshot contract; its completion/repair integration remains #26, so no lead procedure change is needed. Domain meanings, ADR decisions, project operating authority, tracker relationships, installed copies and legacy skills are unchanged. Compatible new functionality has minor release impact; no release is authorized.
