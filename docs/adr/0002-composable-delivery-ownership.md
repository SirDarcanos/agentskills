# ADR 0002: Compose independent specialists under two delivery leads

**Status:** Proposed for maintainer acceptance through [#50](https://github.com/SirDarcanos/agentskills/issues/50), under the confirmed [#48 product direction](https://github.com/SirDarcanos/agentskills/issues/48). Proposed successor to [ADR 0001](0001-delivery-workflow-ownership.md), whose design was accepted through [PR #32](https://github.com/SirDarcanos/agentskills/pull/32). Detailed contracts remain pending #50 acceptance; no runtime or installed migration is authorized by this record.

## Context and decision

#14 delivered broad `work-on` ownership with independently reusable review. #48 now establishes actual independent use of discovery, artifacts, analysis, investigation and methods, and separates one-change delivery from multi-ticket coordination. Keeping these procedures internal would prevent their independent installation/invocation; copying them into new packages would create conflicting owners.

Recommend independent `shape-work`, `write-spec`, `write-tickets`, `research`, `analyze`, `investigate-bug`, five method packages and `pr`, retaining existing domain, setup, preflight, review and named assessment owners. Narrow `work-on` to one bounded change and add `work-on-spec` for the spec's ticket agents, scheduling, serial integration and cross-ticket evidence. Each delivery scope has one accountable technical lead, which can be the caller rather than a separate process. Specialists own their procedures once; leads consume contracts and current evidence, own verification/repair at their scope, and share one bounded worker/repair/model ledger. The [design](../design/composable-delivery.md) owns concrete proposed contracts, stages and unavailable-route behavior.

## Alternatives and consequences

- **Retain internal references only:** preserves installation simplicity but no longer meets the confirmed independent-use product requirement.
- **Duplicate procedures in exported skills and coordinators:** avoids companion lookup initially but makes authorization, evidence and repair rules drift. Export ownership once; old routes use thin compatibility pointers until cutover.
- **Mandatory phase pipeline or orchestration/model gateway:** could enforce a common shape mechanically, but adds infrastructure and forces unnecessary phases/models. Ordinary requests and compact evidence suffice; runtime capability/authority limits remain explicit.
- **Immediate replacement of installed skills:** shortens transition but risks losing modifications, shared symlink sources and recovery. Stage coherent replacements and verified full-package restore before separately approved retirement.

Independent packages cost additional discovery and compatibility checks. Two scopes cost explicit integrated evidence beyond child passes. Preserve the prior two-worker and two-cycle repair ceilings, dirty-work review, native graph checks and completion distinctions. No classifier is mandatory; setup records project permission and named assessment owners enforce it without becoming another policy home.

## Supersession and preservation

Acceptance of this record replaces ADR 0001's two-package/internal-procedure boundary and unchanged-installed-command recommendation for the approved migration scope. It does not retroactively change #14's design, source provenance, executed trials or authorization. Until explicit acceptance and merge, this is a proposed replacement, not an accepted supersession. On acceptance, mark this ADR accepted with the decision evidence and mark ADR 0001 superseded by this record, preserving both rationales and reciprocal links.

Applied the repository's domain-modeling procedure directly within #50's authorized design scope. Package ownership has enduring installation/compatibility cost and a real independence-versus-maintenance trade-off, so an ADR qualifies. No glossary meaning changes are proposed. Installed retirement still needs #74's exact-target approval; model permission remains separately ungranted.
