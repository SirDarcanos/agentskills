# Resolve project decisions

Inspect before questioning. Keep an evidence note for each relevant decision: existing source, confirmed answer, proposal, unknown, or intentionally omitted. Reuse setup answers across specialists.

## Ordered confirmation rounds

Present one short, numbered step per turn. State the known facts, recommend the unresolved choices, and ask for confirmation or corrections for that step only. Wait for the user's answer before showing the next step. A step may need a focused follow-up; settle it before advancing. Reuse explicit prior answers rather than asking again. For reruns, skip satisfied steps and present only changed decisions using the same order.

| Step | Confirm in this round |
| --- | --- |
| 1. Target and Git | Exact local directory; local-only/new/existing remote route; host, owner/name and visibility when relevant; initialize/preserve Git, branch/PR flow, direct pushes, review/check requirements and bypasses. Explicitly include any initial commit and push. Distinguish bootstrap pushes from subsequent PR-only work. |
| 2. Files and permissions | Purpose, maintenance and collaboration gaps that affect the guidance; exact files/sections and authoritative mapping, content to preserve, ignore rules and optional domain records. Show the ordinary-workflow default below and the separate assessment/sensitive-action approval gates. Use the model-use reference to name installed assessment skills, explain their effects, ask about each one's permission mode and invite other allowances/prohibitions. Resolve the policy home and exact selected delta with limits, disclosure, lifecycle, fallback and approval provenance. If bounded permissions need more discussion, keep follow-ups in this step. |
| 3. History and repository safeguards | Versioning/changelog route, license, and requested GitHub features/security controls from the companion's plan. Show unavailable controls as blockers. Local-only projects omit remote settings. |
| 4. Labels and tracker | Follow the tracker reference's full audit and presentation contract: exact labels kept, renamed/edited, added, consolidated, deleted or awaiting clarification, with usage/automation effects and applicable spec/work/readiness/release roles. Omit for projects without labels; never summarize this as “preserve defaults.” |

If a later answer changes an earlier decision, reopen only that affected step and obtain confirmation of the delta. Keep accepted decisions in the cumulative plan. After applicable steps are settled, ask briefly whether to apply them; do not repeat them as a wall of text. Execution still waits for that final approval.

Explain recommendations through their consequences, not implementation jargon. Explore relevant constraints and failure modes without assuming every discovered concern needs a feature.

## Ordinary-workflow default

For new workflow guidance, include standing permission for ordinary skill execution within the user's requested scope: inspection, planning, implementation, safe local checks, bounded task delegation through the configured agent runtime, independent review, and lead-owned repair/recheck/re-review. Present this as **allowed by default** in step 2. Once the setup policy is approved, ordinary transitions and in-scope repairs need no additional permission prompt. Delegated implementers may write only their assigned scope; reviewers remain independent and read-only, return separately inspectable reports, and cannot repair their own findings or recursively delegate. The lead owns findings, integration and acceptance recommendations. Retain finite assignment runtime and repair bounds from the target's delivery contract or agree missing consequential bounds in this step. Leave routine worker concurrency to the delivery lead based on eligible work, ownership and actual resources; do not invent a numerical worker ceiling or fixed ticket-batch size by default. Record explicit user, organization, runtime or resource restrictions when they exist. On reruns, preserve existing consumer-project concurrency limits until their exact reconciliation is approved; updating a skill does not override the project's working agreement.

The lead inspects each finding, fixes valid in-scope defects and justified improvements, reruns affected checks, and renews affected review for significant repairs. Material unresolved findings block acceptance. Nonessential suggestions may be explicitly deferred with rationale; scope or product changes return to the user. A standalone review request remains review-only: permission for the repair loop does not turn a report-only invocation into delivery. The loop runs under a delivery or review-and-fix request.

Keep this workflow authority separate from optional assessment permission for Jev, Clef, Nimble and similar services. “No model assessments” means no auxiliary assessment calls, not a ban on ordinary agent work, reviewer agents or lead-owned repairs. Optional assessments, new sensitive disclosure, spending, installation, credentials, deployment, destructive actions, and repository/tracker mutations outside the exact approved plan retain their approval gates. Merge and release authority remain explicit. Invocation gates, agreed repair limits, existing restrictions and binding organization/runtime rules still apply; propose policy changes visibly rather than overwriting authority. Setup itself only establishes policy and performs approved setup effects; it does not launch delivery or reviewers. Missing runtime capability is a limitation, not permission to install it.

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
| Permissions | Exceptions to ordinary workflow authority and consequential action boundaries; none or exact auxiliary assessment permissions through the [model-use procedure](model-use.md), including disclosure, shared limits and service lifecycle. | Default ordinary skill work, bounded delegation and lead-owned repairs to allowed within requested scope; inspect existing authority, keep proposals distinct from permission and verify without exercising it. |

Ask about a GitHub owner, repository visibility/license, pushes, rules, and bypass actors only on the selected remote route and only if unresolved; let the GitHub companion own those concrete settings. A missing credential is a blocker, not an invitation to print secrets or provision accounts.

For new work, broad intentions may remain undecided. Produce useful confirmed context and identify the next necessary decision rather than inventing architecture. No professional-experience questionnaire is required: ask how the user wants to participate.

## Close the interview

Separate:
- required now;
- worth considering later;
- explicitly unnecessary;
- accepted limitations.

Finish when the applicable confirmation rounds are settled and the selected setup route is actionable, or consequential questions are explicitly blocking. Preserve deferred concerns without turning them into implied commitments. Confirm an important assumption before it becomes authoritative policy.
