---
name: create-changelog
description: Create a concise CHANGELOG.md using Semantic Versioning and a Keep a Changelog structure. Use when a software project has no changelog.
---

# Create a changelog

Create a human-readable `CHANGELOG.md` from evidence in the repository. Follow [the example changelog](references/example-changelog.md).

## Workflow

### 1. Establish the history

Inspect the project documentation, package metadata, tags, releases, commit history, merged pull requests, and issue references available locally. Determine:

- the public API or user-facing behavior;
- the latest released version and date;
- which changes are unreleased;
- which earlier releases have enough evidence to document accurately;
- the repository URL needed for version and issue links.

Ask the user when the intended history range, release version, or public impact cannot be established. Record only supported facts; leave undocumented history out rather than reconstructing it from guesses.

This step is complete when every planned release and entry has a repository source.

### 2. Select notable changes

Include changes relevant to users, operators, integrators, or security reviewers. Exclude routine refactors, formatting, test-only work, dependency churn without user impact, and raw commit-log noise.

Assign each entry to one of these non-empty sections, in this order:

1. `Breaking changes`
2. `Added`
3. `Changed`
4. `Deprecated`
5. `Removed`
6. `Fixed`
7. `Security`

Write one short sentence per bullet. State the observable change directly. Include only the context needed to understand its impact.

When an entry has a related issue, append a Markdown link to that issue, such as `([#123](https://github.com/OWNER/REPO/issues/123))`. Resolve bare issue numbers from the repository remote. A related pull-request link may follow the issue link, or appear alone when no issue exists. Add only links supported by repository evidence.

This step is complete when every notable sourced change appears once, under the correct heading, and every known related issue is linked.

### 3. Apply versions

Use Semantic Versioning for release numbers:

- major for incompatible public API changes;
- minor for backward-compatible functionality;
- patch for backward-compatible bug fixes.

Treat version selection separately from changelog presentation. If the public API impact is ambiguous, ask before choosing the release number.

Use `## [Unreleased]` for pending work. Put released versions below it in newest-first order as `## [X.Y.Z] - YYYY-MM-DD`. Use ISO 8601 dates. Add version comparison links when the repository URL and tags make them reliable.

This step is complete when every release number matches its documented impact and every released section has a date.

### 4. Write `CHANGELOG.md`

Create the file at the repository root. Preserve the preamble and layout shown in the example. Omit empty category headings. Include a release summary only when a breaking release needs a short migration note.

This step is complete when the Markdown renders clearly and the file contains no placeholders.

### 5. Verify

Check all of the following:

- versions are valid Semantic Versions and appear newest first;
- dates use `YYYY-MM-DD`;
- entries are concise, user-relevant, and not duplicated;
- breaking changes are prominent;
- every known related issue is linked to the correct issue URL;
- version comparison links resolve to the intended tags when included;
- no unsupported claims, local paths, credentials, or generated commit dumps remain.

Report the releases covered, evidence gaps left undocumented, and any version decision that still requires confirmation.
