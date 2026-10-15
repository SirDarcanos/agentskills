# Issue tracker

Use [GitHub Issues](https://github.com/SirDarcanos/agentskills/issues) for this repository. The repository identity is `SirDarcanos/agentskills`; access it through the authenticated `gh` CLI. Verify access read-only before a mutation, and follow [workflow authority](workflow.md) for approval.

Specs record approved product behavior and acceptance criteria. Implementation tickets are cohesive work units under a spec when decomposition is useful. A small request does not require a speculative ticket hierarchy. Follow the [label and title policy](triage-labels.md) for descriptive issue titles, mutually exclusive spec/work-ticket roles, and independently assessed readiness. Apply and read back the mapped labels; a label neither approves scope nor proves readiness.

## Native relationships

Use GitHub's native sub-issues for parent/spec membership and native blocked-by/blocking relationships for execution dependencies. They are separate graphs. Issue-body links and checklists may summarize them but do not replace persisted relationships.

Before creating or changing edges:

1. Inspect both relationship directions, follow pagination, and resolve repository identities and issue database IDs. An issue number is not a database ID.
2. Compare the observed graph with the approved plan. Preserve unrelated edges and existing parentage; changes to ownership or removal require specific approval.
3. Reject self-links, reversed blockers, cycles, and conflicting parents. Check transitive blockers and parent ancestry, not just the immediate edge.
4. Add only missing approved relationships.
5. Read back both directions and compare actual IDs with the intended graph. After a timeout or partial failure, inspect before retrying; report unknown or failed operations.

The [maintained native-relationship procedure](../../workflow/setup-project/references/issue-tracker.md#native-github-graph) owns request details and links to the official APIs. Read it before performing graph work; its optional helper handles additive blockers in one repository, not parentage or approvals. Use normal skill/file discovery when working outside this repository rather than copying workstation paths.

This repository's native parent and blocker endpoints were successfully inspected during setup. Future permission/API failures are blockers, not evidence that a relationship is absent. Obtain explicit agreement on an alternative if a required native feature is unavailable; never silently substitute prose.

## Readiness and completion

An agent-ready ticket has actionable acceptance criteria, resolved consequential decisions, and known dependencies. Start only when its native blockers and their completion evidence permit. Closed issues or readiness labels alone are insufficient. Schedule eligible implementation tickets under the parent agreement; a ready parent spec is a coordination entry point, not an additional implementation unit. Reconcile readiness after accepted decisions and merges using the label policy and actual completion evidence, within the approved tracker scope.

The delivery owner reports implemented, verified, unverified, deferred, and blocked work separately. Keep implementation tickets open until their work is accepted and merged under the agreed workflow. Where appropriate, add closing references to the PR and verify issue state after an approved merge. Declined work closes with an explanation and the relevant label, not a claim of implementation.

The label guide owns spec labeling and the approved historical backfill. Issue #14 is the delivery-workflow spec; #18 defines its design contract. Publishing that plan does not implement the workflow or authorize downstream execution before its design decisions and native blockers are resolved.
