# ADR 0001: Keep delivery procedures together and review independently reusable

**Status:** Superseded by [ADR 0002](0002-composable-delivery-ownership.md) through the maintainer's acceptance and merge authorization for [PR #75](https://github.com/SirDarcanos/agentskills/pull/75), under #48/#50.

**Decision history:** Originally proposed with [#18](https://github.com/SirDarcanos/agentskills/issues/18) under the [#14 product agreement](https://github.com/SirDarcanos/agentskills/issues/14), then accepted through [PR #32](https://github.com/SirDarcanos/agentskills/pull/32). The explanation below preserves that earlier decision's rationale and pre-merge wording as history. Supersession changes future ownership, not prior execution evidence; it authorizes no installed migration.

## Context and decision

Delivery needs one lead accountable for phase selection, integration, repair and evidence, while independent review also has a useful standalone invocation. The installed commands split those responsibilities across incompatible invocation, branch, testing and review-scope assumptions; wrapping them would make those assumptions part of the new workflow. The [inventory](../design/delivery-workflow-inventory.md) records that evidence.

Recommend one explicitly invoked `work-on` package with package-local procedures for discovery through completion, and a discoverable `review-delivery` companion for independent Standards/Spec review. Reuse existing domain-modeling and Git-preflight companions, and the maintained tracker procedure on applicable routes. Leave existing command names and installed copies untouched. The [design contract](../design/delivery-workflow.md) owns the concrete handoffs, destination map and capability requirements.

## Alternatives and consequences

- **Wrap the installed commands:** fewer new instructions initially, but inherits command-only invocation gates, mandatory integration/TDD behavior and committed-only review. Repairing those assumptions via caller overrides would leave conflicting authorities and unsafe compatibility guesses.
- **Create a separate package for every phase:** makes all phases independently invocable, but adds installation, discovery and contract maintenance without a current need for ten public entry points. Keep those responsibilities internally distinct instead.
- **Ship everything in one package:** minimizes companion requirements, but makes independently useful review depend on the delivery entry point or duplicates its procedure for standalone use. A separate review package earns its installation boundary through that independent use.
- **Replace or alias `code-review`:** retains a familiar name but risks shadowing a separately installed command. A new name makes opt-in behavior and missing-companion failures explicit.

The proposed boundary costs one new required review companion at acceptance and conditional existing companions for their routes. It avoids global migration and a general orchestration service. Later extraction of another phase is possible, but must be justified by actual independent use and preserve the handoff contract.

## Record scope

Applied the repository's domain-modeling decision-record procedure directly within the authorized #18 design task; no delegated agent was required. This choice meets its record threshold: changing package ownership after consumers install it has meaningful compatibility cost; retaining internal phase responsibilities while exporting review needs explanation; the installation/maintenance trade-off is real. No domain definitions changed, so `CONTEXT.md` is intentionally unchanged. No earlier ADR exists to supersede.

Acceptance of this proposal must be explicit in the #18 PR/decision evidence before downstream implementation. A later incompatible change should supersede this record with reciprocal links while preserving this rationale.
