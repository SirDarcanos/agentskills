# Changelog and versioning setup

Read when discovering or reconciling the project's changelog and release convention. This procedure is bundled; no external changelog skill is required. The [documentation contract](documentation-contract.md) owns output locations, and [tracker integration](issue-tracker.md) owns label definitions and reconciliation.

## 1. Establish the actual convention

Inspect existing changelog files in full, release documentation, package/version metadata, tags, GitHub releases where available, recent releases/merged changes, and release automation. Determine:

- whether versioning is Semantic Versioning, calendar-based, another documented scheme, or not yet decided;
- the release unit: one repository version, independently versioned packages, or another arrangement;
- which source owns version numbers and whether changelogs are hand-maintained or generated;
- current released versus unreleased changes, tag prefixes, prereleases, and any pre-1.0 policy;
- how release impact is classified, who approves releases, and whether automation consumes labels or commit messages.

A version-looking tag alone does not establish SemVer. Distinguish actual releases from unreleased manifest values. Conflicting files/tags/automation require clarification rather than choosing the largest number. Record unknowns; do not infer historical release dates or compatibility promises.

**Done:** observed conventions, authority, release units, and gaps are explicit.

## 2. Plan the changelog route

- **Existing maintained changelog:** preserve its path, layout, categories, versions, dates, links, and released history. Set up its ongoing maintenance policy; edit content only for an approved, evidence-backed correction or addition.
- **Generated changelog or change-fragment workflow:** use its source mechanism. Do not hand-edit generated output, install new tooling, or replace release automation just to fit a template.
- **Missing changelog:** propose creating one at the appropriate project/package location, including the intended scope of history and convention. If versioning is unresolved, explain options and confirm the choice before treating it as policy. For a project with no releases yet, an honest pending-changes section is enough; invent no release numbers, dates, or entries.
- **Changelog intentionally unnecessary:** confirm and document that exception instead of silently skipping the question.

Include file changes, release-label mappings, and any automation impact in the setup approval plan. Approval to establish a changelog is not approval to bump versions, create tags/releases, publish packages, or deploy.

**Done:** the changelog route and versioning policy are confirmed or explicitly blocked/deferred.

## 3. Apply the approved convention

For an approved new manually maintained changelog, write a short explanation of the chosen convention, pending notable changes, and only historical releases supported by repository evidence. Keep entries concise and user-relevant, link known related issues/PRs, and avoid raw commit-log dumps or placeholder sections. Keep a Changelog is a recommendation when compatible, not a forced migration. SemVer-specific presentation or bump rules must not override a different established scheme.

Record release policy in the target's workflow document: authoritative version/changelog sources, release unit, how impact is assessed, when entries/fragments are required, and what actions need approval. Point to existing automation rather than duplicate its configuration. Generated tracker guidance points to this policy and records the actual release labels used.

For confirmed SemVer, provision the patch/minor/major roles through the tracker procedure. Explain incompatible public changes versus backward-compatible functionality and fixes; confirm exceptions for pre-1.0/prereleases rather than silently applying stable-release rules. For another scheme, preserve it and agree on meaningful impact labels if needed; do not apply incompatible bump labels automatically.

**Done:** approved changelog/docs/labels reflect the same convention without publishing a release.

## 4. Verify and maintain

Read the resulting changelog and compare historical sections with the pre-edit content. Check known issue/version links, ordering and dates against evidence, agreement with automation, and absence of unsupported history or private data. Verify labels separately through tracker read-back. Do not run release jobs to test this policy.

Generated workflow guidance assigns implementation the responsibility to add a notable unreleased entry or change fragment when required, and review checks its impact classification. Release preparation checks the aggregate change against the version policy; a label alone cannot authorize a bump or release. No-entry-required is valid with a reason for non-user-facing work.

**Done:** setup reports the detected convention, maintained/created/deferred changelog, verified labels, and remaining uncertainties. A clean rerun neither rewrites historical entries nor adds duplicate labels/entries.
