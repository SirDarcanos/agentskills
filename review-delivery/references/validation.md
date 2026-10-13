# Review Delivery validation

Read when changing or validating this package. These are reusable checks and trial scenarios, not retained execution reports. Record actual results in the target's approved task/PR evidence location, outside the installed skill.

## Local checks

Python 3.9+ and Git are required for the optional helper tests. From this package directory:

```bash
python3 -B scripts/test_snapshot.py
```

In a Git source checkout, also run `git diff --check`. Read changed Markdown/frontmatter, inspect rendered headings/tables/code blocks, and resolve relative links/anchors from their containing files. Verify that the description routes delivery reviews and bounded handoffs. Copy only this package to a temporary directory and run its tests there; no sibling package or workstation path should be needed. Inspect the full diff, including untracked files, for private data, generated artifacts, nonportable paths and unintended legacy-skill changes.

### Executable fixture scope

The offline tests use temporary synthetic Git repositories. They cover committed/staged/unstaged changes, included untracked files, deletion/rename endpoints, file modes, leaf symlinks, supporting inputs and protected unrelated work. They exercise index-only/content-identical-commit drift, invalid capture inputs and unchanged protected bytes/index/history.

The fixture's dirty formatter changes case; an untracked module duplicates normalization ownership. Tests demonstrate defect observability and helper drift detection, not independent reviewer finding detection. A new file outside the explicit path list intentionally leaves the helper capture unchanged: separate discovery must identify it before repinning.

## Behavioral trial (requires separate permission)

1. Use `python3 -B scripts/trial_fixture.py` to create a retained synthetic target and initial evidence. The generator launches no agents; the caller owns retention/cleanup. Read the generated brief/standards, pin all relevant source/support inputs, and keep unrelated sentinels protected.
2. Confirm inspection-only delegation authority, independent contexts, finite bounds and available slots. Freeze included files/support and provide actual diffs/files, safe non-following symlink metadata, exact check commands/environment and supporting-artifact fingerprints. Keep test expectations and each axis's conclusions out of the other reviewer's context.
3. Execute Standards and Spec separately using this skill and its report contract. Check whether they detect the dirty case regression and untracked duplicate ownership with locations, rationale and materiality. Retain actual reports, not authored expected findings.
4. After initial reports, change an included untracked file and add a relevant caller. Repeat discovery/fingerprints and require affected evidence to be marked stale; repin before renewed review. An unchanged HEAD or tracked patch cannot identify untracked state.
5. Exercise a no-permission/unavailable-runtime handoff without launching an unauthorized worker. Require an independent-review acceptance blocker; lead self-review cannot substitute. Keep simulated handoffs distinct from actual runtime failures.

Report executed/static/not-run/failed/stale results and limits. Non-Git, manual submodule capture, timeout/recovery and renewed-review branches need their own evidence; passing the local checks is not certification of those behaviors. Retain run-specific reports and revision history outside this package.
