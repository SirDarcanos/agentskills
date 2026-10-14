# Resolve project decisions

Inspect before questioning. Keep an evidence note for each relevant decision: existing source, confirmed answer, proposal, unknown, or intentionally omitted. Reuse setup answers across specialists.

Ask a few related questions per round. Explain recommendations through their consequences, not implementation jargon. Explore relevant constraints and failure modes thoroughly without assuming every discovered concern needs a feature.

## Question branches

| Missing context | Ask about | Keep with the agent |
| --- | --- | --- |
| Purpose/stage | Who uses it, for what, prototype versus maintained service, what failure would mean. | Discover current stack and commands from files. |
| Maintenance | Who builds, reviews, operates; realistic maintenance time and budget. | Internal file/module decomposition. |
| Collaboration | Product-level decisions, technical collaboration, or another arrangement; which decisions need approval. | Routine engineering choices within that authority. |
| Risk | Sensitive data, access separation, irreversible actions, losing work, recovery expectations. | Translate the answers into appropriate verification and constraints. |
| Operations | Hosting/integration constraints, expected usage supported by evidence, organization requirements. | Avoid speculative scaling infrastructure. |
| Delivery | How changes reach production/default branch; actual reviewers and required checks. | Offer a simple branch flow unless requirements need more; do not invent reviewers or checks. |
| Releases and labels | Resolve conflicting/unknown versioning, whether a missing changelog should be created, and which audited labels serve the workflow. | Inspect changelog/history, version sources, automation, and open/closed issue/PR label usage before asking. |
| Permissions | Delegation and deployment boundaries; none or exact model permissions through the [model-use procedure](model-use.md), including disclosure, shared limits and service lifecycle. | Inspect existing authority first; keep proposals distinct from permission and verify without exercising it. |

Ask about a GitHub owner, repository visibility/license, pushes, rules, and bypass actors only on the selected remote route and only if unresolved; let the GitHub companion own those concrete settings. A missing credential is a blocker, not an invitation to print secrets or provision accounts.

For new work, broad intentions may remain undecided. Produce useful confirmed context and identify the next necessary decision rather than inventing architecture. No professional-experience questionnaire is required: ask how the user wants to participate.

## Close the interview

Separate:
- required now;
- worth considering later;
- explicitly unnecessary;
- accepted limitations.

Finish when the selected setup route is actionable and consequential questions are answered or explicitly blocking. Preserve deferred concerns without turning them into implied commitments. Confirm an important assumption before it becomes authoritative policy.
