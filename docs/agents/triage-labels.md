# Label vocabulary

These mappings describe the approved GitHub labels for `SirDarcanos/agentskills`. Read the live inventory before changing it. The [workflow](workflow.md) owns mutation authority and release policy; [tracker guidance](issue-tracker.md) owns relationships and completion semantics.

## Types and contribution signals

| Label | Use |
| --- | --- |
| `bug` | Existing behavior fails its intended contract. |
| `documentation` | Documentation or instruction wording changes; not a substitute for assessing skill behavior. |
| `enhancement` | New or improved functionality. |
| `spec` | Product specification with intended behavior and acceptance criteria. Apply when creating a spec issue and read back the assignment. |
| `good first issue` | A genuinely bounded, newcomer-appropriate contribution. |
| `help wanted` | A contribution would be useful; does not imply a team or assigned reviewer. |

## Triage and next action

| Role / label | Meaning |
| --- | --- |
| `needs-triage` | Scope, relevance, or routing still needs assessment. |
| `needs-info` | Further information is required before work can proceed. This replaces the former `question` label. |
| `ready-for-agent` | Actionable criteria and decisions are available; inspect native blockers and completion evidence before starting. |
| `ready-for-human` | The next action requires a human decision or capability. |
| `wontfix` | Work has been explicitly declined, with a recorded reason. |

Use the next-action labels deliberately and remove stale ones when the state changes within the approved task. A published spec is not automatically ready for implementation. Duplicate or invalid requests can be explained and linked in the issue discussion without dedicated labels; do not recreate retired labels on a rerun.

## Release impact

Apply to PRs when delivered public impact is established. One resolved impact label per release-relevant PR; none is valid for work with no release impact. These labels currently have no automation consumers and never authorize publication.

| Label | Meaning under the repository's SemVer policy |
| --- | --- |
| `patch` | Backward-compatible fix. |
| `minor` | Backward-compatible functionality. |
| `major` | Incompatible public behavior or interface change. |

## Approved initial reconciliation

The setup audit covered all open and closed issues/PRs, repository configuration, and local automation. The maintainer confirmed that no external tools rely on the old labels.

- Keep `bug`, `documentation`, `enhancement`, `good first issue`, `help wanted`, and `wontfix` with their existing metadata.
- Rename unused `question` to `needs-info`, preserving its metadata and meaning.
- Remove unused `accessibility`, `invalid`, and `duplicate`; no historical assignments require migration.
- Add `spec`, `needs-triage`, `ready-for-agent`, `ready-for-human`, `patch`, `minor`, and `major`.
- Add `spec` to confirmed specification #8 while preserving its existing `enhancement` assignment. Preserve all other historical assignments and native relationships.

These are reconciliation decisions, not commands to repeat. Later vocabulary changes require an inspected, approved delta, including automation and historical-assignment effects. Read back label metadata and affected assignments after each change; retain partial outcomes rather than claiming global success after a failure.
