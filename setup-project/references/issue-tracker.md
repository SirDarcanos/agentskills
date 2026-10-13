# Tracker setup and native relationships

Read when configuring an issue tracker, reconciling labels, or documenting how later agents create and schedule work. The [documentation contract](documentation-contract.md) owns the output homes. This reference owns tracker procedures; GitHub security/branch settings belong to the `github-repo-setup` companion.

## Labels and local alternatives

1. Inspect the actual tracker and vocabulary. On GitHub, use `gh label list --repo OWNER/REPO --limit 1000 --json name,description,color`; if results hit the limit, use paginated REST rather than assuming the list is complete.
2. Map roles to existing labels/statuses by meaning, not spelling. Propose only missing roles the workflow needs. For a new tracker recommend:

| Role | Meaning |
| --- | --- |
| `needs-triage` | Scope, routing, or relevance still needs examination. |
| `needs-info` | A consequential answer or evidence is missing. |
| `ready-for-agent` | Actionable criteria, decisions, and known dependencies; start only when native blockers and completion evidence permit. |
| `ready-for-human` | The next action requires a human decision or capability. |
| `wontfix` | Explicitly declined work, with rationale. |

3. Put exact names, descriptions, and colors to create/change in the approval plan. Example **after approval**, for a verified missing label:

```sh
gh label create 'needs-triage' --repo OWNER/REPO --description 'Scope or routing needs examination' --color D4C5F9
```

Do not use force-update as a substitute for inspection. An approved metadata change uses `gh label edit` against the exact existing name. Never implicitly delete, rename, or repurpose a label. After mutation fetch labels again and compare names, descriptions, and colors to the plan; preserve unrelated metadata.

4. Record mappings and readiness rules. Being labeled ready or closed is not evidence of verified implementation/integration.
5. A local/non-GitHub tracker is valid: document its location, explicit dependency representation, and capability limits. GitHub unavailability is different from a deliberately chosen local route. An alternative to a requested unavailable native graph needs explicit agreement.

**Done:** approved labels/mappings are verified or individually blocked; no ticket backlog or production issues were created merely as setup fixtures.

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
