# Label vocabulary

These mappings describe the approved GitHub labels for `SirDarcanos/agentskills`. Read the live inventory before changing it. The [workflow](workflow.md) owns mutation authority and release policy; [tracker guidance](issue-tracker.md) owns relationships and completion semantics.

## Types

| Label | Use |
| --- | --- |
| `bug` | Existing behavior fails its intended contract. |
| `documentation` | Documentation or instruction wording changes; not a substitute for assessing skill behavior. |
| `enhancement` | New or improved functionality. |
| `spec` | Product specification with intended behavior and acceptance criteria. Apply when creating a spec issue and read back the assignment. |

## Areas and titles

| Label | Use | Color | Description |
| --- | --- | --- | --- |
| `delivery-workflow` | Project-aware delivery workflow work, including its spec and implementation tickets. | `0052CC` | Project-aware delivery workflow skills and supporting work. |

Area, type, readiness, and native relationships are separate dimensions. Apply the approved area label when classifying related work; it neither makes an issue a spec nor establishes parentage. A child may inherit `delivery-workflow` when its actual scope belongs to that area. Copy only explicitly mapped area labels, not the parent's entire label set: `spec`, readiness and release-impact labels require their own assessment.

Use descriptive, sentence-case issue titles without type or area prefixes such as `Spec:` or `Delivery workflow:`. Identify type/area through labels and relationships rather than parsing titles. Existing unrelated historical titles remain unchanged unless a migration is approved. Pull-request titles continue to follow the project's existing commit/PR conventions.

## Triage and next action

| Role / label | Meaning |
| --- | --- |
| `needs-triage` | Scope, relevance, or routing still needs assessment. |
| `needs-info` | Further information is required before work can proceed. This replaces the former `question` label. |
| `ready-for-agent` | Actionable criteria and decisions are available; inspect native blockers and completion evidence before starting. |
| `ready-for-human` | The next action requires a human decision or capability. |
| `wontfix` | Work has been explicitly declined, with a recorded reason. |

Use the next-action labels deliberately and remove stale ones when the state changes within the approved task. A published spec is not automatically ready for implementation. Apply `ready-for-agent` to a spec once its approved agreement and shared design decisions are actionable; on a parent spec it means the lead can coordinate eligible child work, not implement the parent a second time. An actionable ticket may carry this label while native blockers still prevent execution. After accepted decisions and merges, reassess affected parent/child readiness within authorized tracker changes and read back label assignments; issue closure alone does not establish readiness. Duplicate or invalid requests can be explained and linked in the issue discussion without dedicated labels; do not recreate retired labels on a rerun.

## Release impact

Apply to PRs when delivered public impact is established. One resolved impact label per release-relevant PR; none is valid for work with no release impact. These labels currently have no automation consumers and never authorize publication.

| Label | Meaning under the repository's SemVer policy |
| --- | --- |
| `patch` | Backward-compatible fix. |
| `minor` | Backward-compatible functionality. |
| `major` | Incompatible public behavior or interface change. |

## Approved initial reconciliation

The setup audit covered all open and closed issues/PRs, repository configuration, and local automation. The maintainer confirmed that no external tools rely on the old labels.

- Keep `bug`, `documentation`, `enhancement`, and `wontfix` with their existing metadata.
- Rename unused `question` to `needs-info`, preserving its metadata and meaning.
- Remove unused `accessibility`, `invalid`, `duplicate`, `good first issue`, and `help wanted`; no historical assignments require migration. The maintainer does not use contribution-recruitment labels for this repository.
- Add `spec`, `needs-triage`, `ready-for-agent`, `ready-for-human`, `patch`, `minor`, and `major`.
- Add `spec` to confirmed specification #8 while preserving its existing `enhancement` assignment. Preserve all other historical assignments and native relationships.

The later approved delivery-workflow reconciliation adds `delivery-workflow` to #14 and #18–#31, removes their type/area title prefixes, and marks the now-actionable #14 ready. Other assignments and native relationships are preserved; this is not a blanket historical rename or backfill.

These are reconciliation decisions, not commands to repeat. Later vocabulary changes require an inspected, approved delta, including automation and historical-assignment effects. Read back label metadata and affected assignments after each change; retain partial outcomes rather than claiming global success after a failure.
