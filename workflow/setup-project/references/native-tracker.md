# Native tracker library

Read this complete library for GitHub issue publication, role/readiness checks or native graph work. Setup Project owns it; it is a library entry, not a setup invocation.

## Discovery and authority

Discover the actual `setup-project` package through runtime/project metadata and resolve `references/native-tracker.md` from that package root. Consumers may inspect this entry directly without reading `SKILL.md` or the label audit. Record its resolved source/revision or digest; recover truncated reads and resolve links from their containing file. Check semantic compatibility with the requested operations below. Missing, ambiguous or incompatible material blocks the dependent tracker route, not diagnosis or local drafting; no installation or silent prose fallback.

Read the target's tracker/title/label/completion policy and actual mappings. Existing authentication is not permission: the caller's selected stage and exact approved effects govern publication, role/readiness assignments and graph writes. Library access grants no setup, settings/label audit, vocabulary changes, scheduling or mutation authority. Preserve unrelated content, labels and edges. Other hosts/trackers need an inspected project-approved native procedure; do not treat this GitHub route or helper as universal.

## Spec/work-ticket roles, titles and readiness

When the target uses spec decomposition, map distinct roles for the specification and its bounded work tickets. Propose `implementation-step` for the latter on new GitHub setups; reuse an explicitly approved equivalent on existing trackers. This is a generic work-ticket role, not a per-initiative area label. It includes design and validation work as well as coding. Keep spec and work-ticket roles mutually exclusive, while preserving other compatible type classifications. A small standalone request need not acquire a speculative parent/child hierarchy.

Require spec creation and ticketing to apply and read back the respective mapped role. Determine the role from the issue's purpose and native relationships; do not copy the parent's spec/readiness/release labels or assume every sub-issue is an implementation step. Native parentage identifies which specification owns a step; native blockers establish execution dependencies, not a mandatory linear sequence. Delivery PRs do not become implementation-step issues merely because they implement one.

Establish the target's approved title conventions and identify workflow roles through actual metadata rather than guessing from title text. Include exact label metadata, assignments, affected automation and any historical title migration in the approval plan. Preserve unrelated labels and historical titles; do not impose prefix-free titles where the project's approved convention requires prefixes.

Evaluate spec readiness independently of publication. A spec may receive the mapped agent-ready label when its approved behavior and shared design decisions are actionable. On a parent spec this enables coordination of eligible children, not duplicate parent implementation. Actionable child tickets may be labeled ready while native blockers still prevent execution. Require readiness reassessment after accepted decisions and merges, using actual completion evidence and the target's mutation authority; do not invent an automated label service or infer authority from issue closure. Apply and read back approved assignment changes, preserving unrelated labels.


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

The optional [dependency helper](../scripts/dependencies.py) implements additive blocker reconciliation for **one github.com repository**, including reachable-cycle checks, deduplication, pagination, and forward/reverse read-back against resolved database IDs. It does not manage parentage, cross-repository graphs, labels, readiness decisions, or approvals. These stay with the procedure above. Unsupported graph scope fails closed; use an approved, inspected native procedure rather than changing the plan to fit the helper.

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
