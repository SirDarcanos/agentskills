# Tracker setup and native relationships

Read when configuring an issue tracker, reconciling labels, or documenting how later agents create and schedule work. The [documentation contract](documentation-contract.md) owns the output homes. This reference owns the setup label audit; shared role/readiness and graph procedures belong to the [native tracker library](native-tracker.md). GitHub security/branch settings belong to the `github-repo-setup` companion.

## Label audit and vocabulary

The roles below are a starting point, not a five-label limit. Account for the project's work types, ownership, priority, release automation, and existing useful categories. Do not generate an elaborate taxonomy without an actual use.

1. Inventory all current labels, including GitHub defaults and custom labels. Use `gh label list --repo OWNER/REPO --limit 1000 --json name,description,color`; if results hit the limit, use paginated REST rather than assuming the list is complete.
2. Inspect usage across **open and closed issues and pull requests**, issue forms, Actions/release configuration, and documented workflows. A paginated `GET repos/OWNER/REPO/issues?state=all&per_page=100` includes issues and PRs; preserve which is which. Inspect external/organization automation when relevant or mark its usage unknown. Zero assignments alone do not prove a label is unnecessary; GitHub-default status alone is not a reason to delete it.
3. Map roles by meaning, not spelling. Classify every existing label as **keep**, **edit/rename**, **consolidate**, **remove**, or **needs clarification**, with rationale and affected usage/automation. Keep custom and default labels that still serve the project.

### Present the labels step

Show the audit in clearly separated **Keep unchanged**, **Rename/edit**, **Add**, **Consolidate**, **Delete**, and **Needs clarification** groups; mark empty groups “none.” Account for every inventoried label exactly once and show exact names, descriptions/colors for creates or metadata edits, assignment migrations and automation effects. Give each deletion a reason and its historical assignment impact. Ask the user to confirm this exact disposition before including it in the cumulative approved plan. A blanket “preserve GitHub defaults” is not a disposition.

When retained, propose `good first issue` → `good-first-issue` and `help wanted` → `help-wanted` in **Rename/edit**, not **Keep unchanged**. Already-hyphenated labels need no rename. If both spellings exist, propose an explicit consolidation with assignment/consumer migration rather than an overwriting rename. Existing name-based consumers or organization requirements must be reconciled; unknown impact leaves the rename blocked, not silently authorized. If either label is unnecessary, propose its deletion with evidence instead of renaming it. Apply only the exact approved disposition.

For a new repository that does not yet exist, show expected defaults as provisional, not an observed inventory. After creation, read back actual labels before applying the audit; unexpected labels or metadata/usage differences require a focused labels-step confirmation before affected mutations. Repository creation approval does not approve unseen label deletions.

### Roles

For a new tracker, propose these workflow roles plus applicable type/priority/component/release roles:

| Role | Meaning |
| --- | --- |
| `spec` | A product specification issue, distinct from implementation tickets, discussion, and ordinary requests. |
| `implementation-step` | A bounded work ticket under a spec; includes design, implementation and validation work. |
| `needs-triage` | Scope, routing, or relevance still needs examination. |
| `needs-info` | A consequential answer or evidence is missing. |
| `ready-for-agent` | Actionable criteria, decisions, and known dependencies; start only when native blockers and completion evidence permit. |
| `ready-for-human` | The next action requires a human decision or capability. |
| `wontfix` | Explicitly declined work, with rationale. |

Use the literal `spec` label on new GitHub setups. Preserve an existing equivalent such as `type:spec` only when the mapping is explicit and approved; do not create duplicate synonymous labels. Generated tracker instructions must tell the spec-creation workflow to apply the mapped label **when creating a spec issue**, then read back its presence. A spec label does not imply readiness or replace native parent/blocker relationships. Apply it to existing confirmed spec issues only when that backfill is included in the plan, not by guessing from every issue title.

Read [changelog/versioning setup](releases.md) before choosing release-impact roles. For confirmed Semantic Versioning, include these roles (reuse approved equivalent names already consumed by automation):

| Role | Stable-release meaning |
| --- | --- |
| `patch` | Backward-compatible bug fix. |
| `minor` | Backward-compatible functionality. |
| `major` | Incompatible public API/behavior change. |

The project's versioning policy owns pre-1.0, prerelease, and package-specific exceptions. Document whether these labels apply to implementation issues, PRs, or release issues and how automation consumes them. Classify actual delivered impact rather than inferring it solely from `bug` or `enhancement`. For one release unit use one resolved impact label per classified item; if several apply, resolve the highest required bump under project policy before release. Independently versioned packages may need scoped mappings. A spec need not predict a bump before its implementation is understood. Non-release work may need none. Labels are classification, not permission to publish.

For non-SemVer or unresolved versioning, retain the existing scheme and explicitly agree on release/impact vocabulary; do not falsely assign SemVer behavior to calendar versions.

### Spec/work-ticket roles, titles and readiness

Read the [native tracker library](native-tracker.md#specwork-ticket-roles-titles-and-readiness) for the shared role, title and readiness contract before establishing mappings. The audit below owns approval and application of vocabulary/assignment changes; consumer publication uses the same library without loading this audit.

### Apply the approved audit

1. Re-read labels, affected assignments, and automation references against the plan; changed or unknown impact blocks destructive cleanup pending clarification. Preserve label metadata and affected issue/PR references in the approved operation record before destructive changes. Deleting a label removes its assignments, including historical ones; recreating its name does not restore that history.
2. Create verified missing labels. Example **after approval**:

```sh
gh label create 'spec' --repo OWNER/REPO --description 'Product specification and acceptance criteria' --color 5319E7
```

3. Use `gh label edit` for exact approved metadata changes/renames. Do not force-update as a substitute for inspection. For consolidation, create/verify the destination, add it to approved affected issues/PRs, update approved local automation/docs references, and read back assignments before removing the source. If an external consumer cannot be updated, defer the destructive action. An in-place rename must also account for name-based automation.
4. Remove only explicitly approved unused/retired labels, including GitHub defaults. Confirm affected open/closed assignments and automation dependencies are migrated or their loss is explicitly accepted. Preserve unrelated labels and assignments. Failed cleanup leaves a visible partial result; no blind deletion retry or automatic rollback.
5. Fetch labels and affected assignments again. Verify approved creates/edits/renames, expected deletions, preserved labels, spec backfills if any, and updated automation/docs. Reconcile body/status summaries with native relationships; labels do not replace the graph.
6. Record final mappings and readiness rules. Being labeled ready or closed is not evidence of verified implementation/integration. A clean rerun produces no new migration or changelog rewrite.

A local/non-GitHub tracker is valid: document its location, explicit spec/type/impact representation and dependency capabilities. GitHub unavailability is different from a deliberately chosen local route. An alternative to a requested unavailable native feature needs explicit agreement.

**Done:** the full label inventory has an approved disposition or explicit question; required spec and applicable release roles exist and are verified; approved cleanup is verified or individually blocked. No backlog or production issues were created merely as setup fixtures.

## Native GitHub graph

The [native tracker library](native-tracker.md) is the sole owner of the graph procedure, role/readiness contract and optional helper limits. Read it completely before graph work. This retained target supports existing callers; following it does not invoke setup or grant mutations. New consumers discover that library entry directly without loading this audit or the setup entry. Source changes do not update installed copies; an older package without the supported library must be reported as incompatible for that route, not silently migrated.
