---
name: update-changelog
description: Maintain an existing software changelog with concise, user-relevant entries. Use when recording unreleased changes, preparing a Semantic Versioning release, adding a missing historical release, or correcting an entry.
---

# Update a changelog

Update the project's existing changelog from repository evidence. Preserve its established format unless the user explicitly requests migration. When the project already follows Keep a Changelog, use [the example changelog](references/example-changelog.md) as the target structure.

## Workflow

### 1. Read the existing convention

Read the complete changelog before editing it. Identify:

- filename and markup format;
- release heading, date, and ordering conventions;
- category names and order;
- `Unreleased` workflow;
- version comparison and issue-link style;
- the latest documented release or change.

Use the existing convention as authoritative. If the file is malformed or mixes conventions, describe the conflict and ask before restructuring it.

This step is complete when the insertion point and formatting rules are unambiguous.

### 2. Establish the update scope

Inspect the user request and relevant repository evidence: commits, diffs, tags, releases, merged pull requests, and issue references. Compare it with existing entries to avoid duplicates.

Determine whether the update should:

- add pending entries under `Unreleased`;
- create a dated release from pending entries;
- add a missing historical release; or
- correct an existing entry.

Ask when the target version, date, change range, or public impact cannot be established. Record only supported facts.

This step is complete when every proposed entry has a source and a single destination in the changelog.

### 3. Draft concise entries

Record only changes relevant to users, operators, integrators, or security reviewers. Match the changelog's existing categories. For a Keep a Changelog file, use non-empty sections in this order:

1. `Breaking changes`
2. `Added`
3. `Changed`
4. `Deprecated`
5. `Removed`
6. `Fixed`
7. `Security`

Write one short sentence per bullet. State the observable change directly and include only context needed to understand its impact. If multiple changes relate to the same user-facing change, combine them into a single entry.

When an entry has a related issue, link to that issue using the file's established syntax. If no syntax exists, append `([#123](https://github.com/OWNER/REPO/issues/123))`. Resolve bare issue numbers from the repository remote. A related pull-request link may follow the issue link, or appear alone when no issue exists. A known issue link remains present when a pull-request link is also included. Add only links supported by repository evidence.

This step is complete when every new entry is concise, correctly categorized, unique, and linked to every known related issue.

### 4. Apply the release update

For pending work, add entries under `Unreleased` without changing released sections.

For a release:

1. Determine the version from the requested release or confirm it against Semantic Versioning: major for incompatible public API changes, minor for backward-compatible functionality, and patch for backward-compatible bug fixes.
2. Move the relevant pending entries into `## [X.Y.Z] - YYYY-MM-DD` or the file's equivalent format.
3. Leave unrelated pending entries under `Unreleased`.
4. Keep releases newest first.
5. Update comparison links when the changelog uses them.
6. Remove category headings left empty by the move.

Ask before selecting a version when public API impact is ambiguous. Preserve older release wording unless the user requests a correction.

This step is complete when the requested changes appear in exactly one release section and all unrelated content remains intact.

### 5. Verify

Check all of the following:

- the existing changelog convention is preserved;
- versions and dates are valid and ordered correctly;
- new entries are short, user-relevant, and not duplicated;
- breaking changes are prominent;
- every known related issue is linked to the correct issue URL;
- comparison links and issue links resolve correctly when included;
- no unrelated release content changed;
- no unsupported claims, local paths, or credentials were introduced.

Report the section updated, entries added or moved, and any evidence gap that prevented an entry or link.
