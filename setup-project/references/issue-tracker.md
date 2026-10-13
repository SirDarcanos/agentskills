# Tracker setup and native relationships

Read when configuring an issue tracker, reconciling labels, or documenting how later agents create and schedule work. The [documentation contract](documentation-contract.md) owns the output homes. This reference owns tracker procedures; GitHub security/branch settings belong to the `github-repo-setup` companion.

## Label audit and vocabulary

The roles below are a starting point, not a five-label limit. Account for the project's work types, ownership, priority, release automation, and existing useful categories. Do not generate an elaborate taxonomy without an actual use.

1. Inventory all current labels, including GitHub defaults and custom labels. Use `gh label list --repo OWNER/REPO --limit 1000 --json name,description,color`; if results hit the limit, use paginated REST rather than assuming the list is complete.
2. Inspect usage across **open and closed issues and pull requests**, issue forms, Actions/release configuration, and documented workflows. A paginated `GET repos/OWNER/REPO/issues?state=all&per_page=100` includes issues and PRs; preserve which is which. Inspect external/organization automation when relevant or mark its usage unknown. Zero assignments alone do not prove a label is unnecessary; GitHub-default status alone is not a reason to delete it.
3. Map roles by meaning, not spelling. Classify every existing label as **keep**, **edit/rename**, **consolidate**, **remove**, or **needs clarification**, with rationale and affected usage/automation. Show exact names, descriptions, colors, renames, assignment migrations, and deletions in the approval plan. Keep custom and default labels that still serve the project.

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

When the target uses spec decomposition, map distinct roles for the specification and its bounded work tickets. Propose `implementation-step` for the latter on new GitHub setups; reuse an explicitly approved equivalent on existing trackers. This is a generic work-ticket role, not a per-initiative area label. It includes design and validation work as well as coding. Keep spec and work-ticket roles mutually exclusive, while preserving other compatible type classifications. A small standalone request need not acquire a speculative parent/child hierarchy.

Require spec creation and ticketing to apply and read back the respective mapped role. Determine the role from the issue's purpose and native relationships; do not copy the parent's spec/readiness/release labels or assume every sub-issue is an implementation step. Native parentage identifies which specification owns a step; native blockers establish execution dependencies, not a mandatory linear sequence. Delivery PRs do not become implementation-step issues merely because they implement one.

Establish the target's approved title conventions and identify workflow roles through actual metadata rather than guessing from title text. Include exact label metadata, assignments, affected automation and any historical title migration in the approval plan. Preserve unrelated labels and historical titles; do not impose prefix-free titles where the project's approved convention requires prefixes.

Evaluate spec readiness independently of publication. A spec may receive the mapped agent-ready label when its approved behavior and shared design decisions are actionable. On a parent spec this enables coordination of eligible children, not duplicate parent implementation. Actionable child tickets may be labeled ready while native blockers still prevent execution. Require readiness reassessment after accepted decisions and merges, using actual completion evidence and the target's mutation authority; do not invent an automated label service or infer authority from issue closure. Apply and read back approved assignment changes, preserving unrelated labels.

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

Hierarchy and blockers are distinct:
- Parent/spec membership uses **sub-issues**.
- Scheduling dependencies use **blocked-by/blocking**.

Prose, checklists, labels, and issue mentions are supplementary; they do not create either relationship. Generated tracker instructions must require actual native writes and read-back, not just a “Blocked by” paragraph.

Use the GitHub CLI's existing authorized authentication. Read the live [dependency API](https://docs.github.com/en/rest/issues/issue-dependencies) and [sub-issue API](https://docs.github.com/en/rest/issues/sub-issues) before using an unfamiliar operation. Resolve issue database IDs with `GET repos/OWNER/REPO/issues/NUMBER`; a database ID is not the issue number or GraphQL node ID.

After inspection and approval, the relevant operations are:

```sh
# Dependent issue NUMBER is blocked by issue with database ID BLOCKER_ID.
gh api --method POST repos/OWNER/REPO/issues/NUMBER/dependencies/blocked_by -F issue_id=BLOCKER_ID

# Child with database ID CHILD_ID belongs to parent issue PARENT_NUMBER.
gh api --method POST repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues -F sub_issue_id=CHILD_ID

# Read back, including all pages. Inspect actual identifiers, not just exit status.
gh api --paginate repos/OWNER/REPO/issues/NUMBER/dependencies/blocked_by
gh api --paginate repos/OWNER/REPO/issues/BLOCKER_NUMBER/dependencies/blocking
gh api --paginate repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues
gh api repos/OWNER/REPO/issues/CHILD_NUMBER/parent
```

These are placeholder recipes, not commands to execute unchanged.

### Reconciliation algorithm

1. Resolve target issues and current parent/blocker edges, including pagination. Preserve cross-repository identities; equal issue numbers in different repositories are not equal issues.
2. Compare planned and observed edges. Skip existing intended edges; preserve unrelated ones. Conflicting existing parentage needs approval, not `replace_parent=true` by default.
3. Check self-links, conflicting proposed parents, and cycles in the combined existing-plus-planned graph. For a blocker edge A → B, follow B's transitive blockers before linking. For hierarchy, follow the prospective parent's ancestors; it cannot be the child or its descendant. Do not mix the two graphs.
4. Write only approved missing edges. Parent absence must be established through available issue metadata/API semantics; an ambiguous 404 can be a permission/capability failure, not proof of absence. Let server-side conflict checks remain enabled.
5. Re-fetch both relationship directions and ensure the intended IDs are present. A partial response, wrong direction, or missing edge is a verification failure. Stop dependent scheduling and report it; inspect actual state before retrying.
6. If the API or permissions cannot support the required relationship, report a blocker and seek an explicit alternative. No silent text-only fallback or false readiness.

The optional [dependency helper](../scripts/dependencies.py) implements additive blocker reconciliation for **one github.com repository**, including reachable-cycle checks, deduplication, pagination, and forward/reverse read-back. It does not manage parentage, cross-repository graphs, labels, readiness decisions, or approvals. These stay with the procedure above. Unsupported graph scope fails closed; use an approved, inspected native procedure rather than changing the plan to fit the helper.

Plan format:

```json
{"repository":"OWNER/REPO","dependencies":[{"blocked":10,"by":9},{"blocked":11,"by":9}]}
```

With an existing authenticated GitHub CLI, first inspect the read-only proposed additions:

```sh
python3 /PATH/TO/SKILL/scripts/dependencies.py /PATH/TO/plan.json
```

Only after approval of those exact edges:

```sh
python3 /PATH/TO/SKILL/scripts/dependencies.py /PATH/TO/plan.json --apply
```

The helper re-inspects before applying, refuses cycles/unknown scope, and reports verified writes or partial progress. It never deletes edges or retries failed writes. The agent must still compare fresh evidence to the approved plan, check parent membership, and verify task completion before dispatch.
