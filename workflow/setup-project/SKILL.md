---
name: setup-project
description: On an explicit setup request, establish or reconcile project context, agent instructions, approved model-use policy, and GitHub configuration.
disable-model-invocation: true
---

# Set up a project

Run on an explicit setup request, including a runtime-expanded invocation. Learn the project's needs; do not assume a team size, engineering role, scale, or architecture. This command configures the working agreement, not the application.

Use normal file and shell tools. No particular agent SDK, literal Skill tool, subagents, or model service is required. Operating-document authoring ships here; domain work requires the maintained `domain-modeling` companion, and GitHub creation/configuration requires `github-repo-setup`. Locate applicable companions through runtime skill discovery and read them completely. Missing or incompatible companions block their affected routes; ask before installing or replacing anything. Never silently substitute a different procedure.

## Read-only procedure library

A delivery caller may discover this package and read [tracker integration](references/issue-tracker.md), especially its native-graph procedure, without invoking `/setup-project` or executing the setup steps below. Record the resolved source/revision and check semantic compatibility: native hierarchy/blockers, identity/pagination, conflict checks, additive writes and both-direction read-back. Target-project policy and exact caller approval govern operations; library access grants no setup, label/settings audit or mutation authority. The optional helper supports only its documented one-repository additive blocker scope; parentage, labels and unsupported cases stay with the procedure. Missing capability blocks the affected route rather than causing installation or silent prose fallback.

## 1. Inspect before asking or changing

Read applicable instructions and inspect Git status, remotes, existing entry points, operating/domain docs, ADRs, tracker conventions, changelog/version sources, release automation, and discoverable build/check commands. Follow document pointers. Inspect relevant organization requirements through authorized access; unavailable information remains unknown.

Read the [documentation contract](references/documentation-contract.md). Map every required responsibility to an existing authoritative file or proposed new file. A valid existing layout wins over the default layout. Inspect both AGENTS and CLAUDE files, symlinks, nested instructions, and any context map before choosing where to write.

Select **local-only**, **new GitHub repository**, or **existing GitHub repository**. A remote already present selects configuration, not another repository creation. Inspect permissions/settings read-only when the GitHub route is requested; local-only setup needs no GitHub login. Do not initialize Git, install tools, change labels, or write project documents during discovery.

Read [model-use agreement](references/model-use.md) to inventory installed assessment skills, ask explicitly about permission for the discovered names, invite other allowances/prohibitions, and propose exact permissions without exercising them. Setup requires no model/service calls, startup, credentials, downloads or installations.

For an existing or interrupted setup, read [reconciliation](references/reconciliation.md) before proposing edits.

**Done:** existing authorities, route, current work, known facts, gaps, and capability limits are identified without mutations.

## 2. Agree setup one step at a time

Read [discovery](references/discovery.md) and follow its ordered confirmation rounds in the user's preferred language. Present only the current round, ask for its missing decisions and confirmation, then wait for the reply before advancing. Reuse confirmed decisions and show only necessary deltas on reruns. Resolve contradictions rather than silently picking the most convenient instruction. Organization requirements are not overridden by user preferences.

Prepare companion plan-only results as needed for the relevant round: use the [domain handoff](references/domain-records.md) for domain deltas and `github-repo-setup` for GitHub settings, without executing either plan. Read [changelog/versioning setup](references/releases.md) before the history round and [tracker integration](references/issue-tracker.md) before the labels round. Establish versioning/changelog policy before recommending release labels. Existing relationships change only when explicitly included; setup does not create a backlog by default.

Separate confirmed decisions, proposed recommendations, unknowns, and intentionally deferred concerns. A product director need not choose test seams or internal abstractions. A technical collaborator can choose technical co-design. Neither preference sets the project's security requirements.

**Done:** applicable rounds are confirmed with exact proposed effects, or execution is paused on a blocking decision. Optional unknowns and deferred concerns remain explicit.

## 3. Confirm execution of the agreed steps

Maintain one cumulative plan from the confirmed rounds, including exact effects, exclusions, preserved content, approvals and blockers. Keep detail with its round rather than presenting the full plan again. Finish with a short readiness summary and ask whether to apply the agreed steps. This final confirmation authorizes execution of those effects only; earlier round confirmations do not trigger mutations.

Ask for approval before any setup mutation. Approval covers only the listed actions, including commits or pushes only if explicitly agreed in the Git round. New settings, deployment, billing, disclosure, credential changes and global installations retain their own approval gates. A plan with mandatory blocked operations cannot be called complete; the user may separately approve useful independent local progress.

**Done:** execution of the cumulative concrete scope is approved, or execution is paused.

## 4. Apply through bounded handoffs

Recheck affected state against the plan. If it changed materially, reconcile and obtain approval for changed scope.

1. Author operating docs and entry-point pointers using the documentation contract; apply only the approved model-policy delta through the model-use reference, without exercising permission. Preserve unrelated content; do not regenerate whole existing files from a template.
2. For approved domain work, execute the handoff through `domain-modeling`; use the same mapping and confirmed decisions supplied during planning. Inspect its results and integrate approved pointers without moving operating context into the glossary.
3. For approved GitHub work, hand the companion the target, inspected state, approved operations/exclusions, organization constraints, and known capability limits. It returns actual changes, read-back evidence, and blockers; it must not repeat resolved questions or expand scope.
4. Apply the approved changelog route using the release reference without bumping versions, tagging, or publishing. Record release authority and maintenance expectations.
5. Apply the approved full label audit using the tracker reference, including spec and applicable release roles, approved migrations/cleanup, and native relationship guidance. Preserve unapproved vocabulary, assignments, and relationships.
6. Maintain a short per-operation outcome record in the conversation or approved task artifact. Follow the reconciliation reference on partial failure; do not undo completed work automatically.

Do not place credentials or private personal profiles in repository docs. Record actionable collaboration preferences and permission boundaries, not capability ratings of named people.

**Done:** approved operations have outcomes; failed/deferred operations remain visible and unrelated work is preserved.

## 5. Verify and report

- Inspect diffs and compare actual results to the approved plan.
- Follow every generated entry-point link. Confirm documents have useful content, one authoritative policy home, and read/update conditions. Check the domain companion's actual results against its approved scope; missing required domain work leaves setup partial/blocked.
- Verify remote settings through the companion and labels/relationships through tracker read-back, including preserved labels, approved removals/migrations, and spec assignments when in scope. Command success alone is insufficient.
- Verify the changelog and versioning guidance agree with observed release sources/automation; preserve released history and report any unresolved convention.
- Verify documented non-mutating commands when the environment permits. Ask before installation or any command with deployment, migration, cost, or destructive effects. Unexecuted checks remain unverified.
- Read back model policy and pointers against approval using the model-use reference; preserve existing permission/provenance and shared budgets. Policy publication does not prove assessment-package enforcement.
- Check that a rerun would inspect existing state and propose no substantive changes unless facts or decisions changed.
- Record documentation impact; distinguish static checks from agent walkthroughs and live verification.

Report **completed**, **intentionally omitted**, **deferred**, and **blocked** work, with evidence and the smallest next action. Never hide failed mandatory GitHub protections behind successful local documents.

**Done:** all approved required operations are verified, or the result is explicitly partial/blocked. Use [validation](references/validation.md) when maintaining or testing this skill; setup invocation does not authorize live test repositories or model calls.
