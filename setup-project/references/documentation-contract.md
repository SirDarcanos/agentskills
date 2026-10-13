# Project documentation contract

This is the single authoring contract for setup's output. Other setup references own procedures, not competing document schemas. The `domain-modeling` companion owns domain/ADR procedures and receives the document mapping defined here through the domain handoff. Adapt to meaningful existing documents; these paths are defaults, not a migration requirement.

## Homes and content

| Default home | Authoritative content |
| --- | --- |
| `AGENTS.md` | Concise entry point: applicable rules and conditional read pointers. |
| `docs/agents/project.md` | Purpose/stage, users and evidenced scale, maintenance/operating ownership, resources/constraints, credible risks, collaboration preference. |
| `docs/agents/workflow.md` | Decision authority, delivery/review/verification expectations, versioning/changelog policy and sources, permitted actions, documentation upkeep. |
| `docs/agents/issue-tracker.md` | Actual tracker location/access, capabilities, native parent/dependency operations, limitations, completion semantics. |
| `docs/agents/triage-labels.md` | Spec/work-ticket roles, other applicable type/readiness/release roles mapped to actual labels/statuses; approved title conventions, role-assignment/readiness rules, and audit decisions. The tracker reference owns the authoring procedure. Omit if no label/status system is used. |
| Existing changelog path, otherwise approved `CHANGELOG.md` or package equivalent | Evidence-backed notable change history in the project's convention; use source fragments/configuration instead for generated changelogs. |
| `CONTEXT.md` or existing context map | Confirmed domain terms and relationships, not the operating profile. |
| `docs/adr/` | Selective enduring decisions and rationale; created only when needed. |

Create core project/workflow guidance with confirmed content. Leave optional fields unknown or omitted with reasons where they matter; avoid empty template sections. An early project can have no glossary or ADR. A tracker can be a local task file: document its actual location and explicit relationship representation instead of pretending it has GitHub features.

On a new project create AGENTS.md. On an existing project preserve its entry-point arrangement: use an existing CLAUDE-only authority if valid; inspect whether dual files are symlinked, generated, or independent. Preserve runtime-required compatibility entry points as pointers where supported. Ask before reconciling contradictory authorities; do not rewrite nested or organization rules from a root template.

## Operating context, not stereotypes

Keep these dimensions separate:
- Product stage and expected usage, with evidence rather than invented traffic targets.
- Who maintains, reviews, operates, and makes consequential decisions.
- Resources, hosting/integration constraints, and maintenance burden.
- Sensitive data, failure consequences, recovery needs, and binding organization requirements.
- How to collaborate: product-level explanations, technical co-design, or a specified arrangement.

For example, a public-safe preference is: “Agents own routine engineering decisions. Explain consequential choices in product terms and escalate scope, cost, security, or operating commitments.” Do not write that a named maintainer is inexperienced.

Use enough rigor for actual risks and requirements, not a team-size preset. Explore concerns without automatically implementing them. Record required-now, deferred, unnecessary, and accepted-limitations decisions when relevant.

## Authority and verification

Workflow guidance must distinguish routine agent decisions from actions requiring approval. Cover delegation, external assessments/disclosure, spending, pushes/PRs, deployment, destructive operations, and credential changes only as relevant. Unknown permission is ungranted. Project preferences do not override runtime restrictions or explicit-invocation requirements of another skill.

Record delivery policy from the agreed workflow and observed configuration. Distinguish desired policy from enforced controls. Point to executable configuration for commands rather than duplicating every package script. Record important non-obvious gotchas and environment limitations.

Choose verification by meaningful failure risk and existing coverage. A new test should protect a distinct failure; existing coverage can suffice. Preserve required checks and security/privacy/recovery contracts. Do not invent test quotas, blanket “all testable code needs new tests,” or coverage targets. If existing mandatory policy conflicts, flag it and propose a change for approval rather than silently ignoring it.

## Read pointers

Generate pointers to the project's actual files with explicit conditions. For example, adapted to the selected layout:

```markdown
Before planning or implementing, read [project context](docs/agents/project.md) and [workflow](docs/agents/workflow.md). For work using domain terms, read the linked glossary/context map and relevant ADRs. Before creating or scheduling issues, read the tracker and label guidance. Before classifying release impact or updating the changelog, read the workflow's release policy and linked sources. Update the authoritative documentation when work changes its facts or decisions; include documentation impact in completion evidence.
```

Only link files that exist after setup. Include actual domain/tracker links when applicable. When domain records are present, add a conditional instruction to discover and read `domain-modeling` for changes to meanings, relationships, or decision records, following its handoff contract and the project's approval boundaries. Reading existing definitions alone needs no specialist invocation. If the companion is unavailable or incompatible, report affected modeling work blocked rather than treating another same-named package as equivalent. Do not copy this package reference path into the target as a runtime dependency; the generated project docs must stand on their own.

## Documentation ownership and freshness

Put this maintenance contract in the target's workflow document; the entry point links to it.

| Change | Owner and required action |
| --- | --- |
| Domain term/relationship | Discovering phase, through `domain-modeling`: update the glossary/context map once confirmed and authorized. |
| Operating constraint or authority | Lead/setup: reconcile the project or workflow document with appropriate approval. |
| Delivery/check procedure | Implementation: update authoritative workflow guidance and verify safe commands. |
| Qualifying architectural decision | Analysis/implementation, through `domain-modeling`: create or supersede an ADR under the project's authority. |
| Product scope/behavior | Delivery lead: update the spec with the product decision-maker's approval. |
| Spec creation and ticket classification | Spec/ticket owner: follow approved title and distinct spec/work-ticket role mappings, evaluate readiness independently, and read back assignments; classify release impact under the agreed policy, not by guesswork. |
| Ticket dependencies/status | Ticketing/dispatch: update native relationships and actual evidence/status together. |
| Notable user-facing change | Implementation: update the agreed changelog or change fragment when required; review checks the entry and impact classification. |
| Release convention or label automation changes | Lead/release owner: reconcile policy, mappings, automation, and affected assignments through an approved plan; setup does not authorize publishing. |

A fact's owner updates its home when the decision is confirmed, not after it has been copied elsewhere. Proposals remain labeled as proposals. Before completion, report affected documents and their updates, or justify “no documentation change required.” Review compares docs with the actual change; link checks alone prove no semantic accuracy.

When code and docs conflict, determine whether code is wrong, docs are stale, or a decision is unresolved. Resolve within authority or escalate. Do not silently let code override an accepted decision. Revisit relevant context when project facts change, not through a mandatory recurring paperwork schedule.
