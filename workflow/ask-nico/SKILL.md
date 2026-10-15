---
name: ask-nico
description: Recommend an installed skill or workflow for your situation, without starting it. Only runs when you explicitly invoke ask-nico.
disable-model-invocation: true
---

# Ask Nico

An explicit-invocation workflow advisor, not a simulation of the maintainer.

## 1. Confirm the request

Proceed only when the user specifically invokes `ask-nico`, by name, slash command or the runtime's explicit skill expansion. A generic workflow question, source mention, quoted command, another skill's handoff or an agent's decision to load this file does not activate it. Without that user invocation, stop this procedure and leave the original request to its existing handler.

Identify the user's goal, current progress and whether they want discovery, diagnosis, writing, review or delivery advice. Ask only for consequential intent that the request and available context cannot settle.

**Complete when:** explicit user invocation is established and the question to advise on is clear, or this procedure has stopped without routing the request.

## 2. Inspect context and installed candidates

Read applicable project instructions and their relevant authority/workflow pointers. Reuse current context; inspect only what affects the recommendation. Distinguish project restrictions, existing approvals and missing permissions from personal preferences. The name “Nico” supplies no evidence of the maintainer's wishes.

Discover relevant candidates through the runtime's installed catalog or configured discovery locations. Catalog descriptions are leads, not proof. Before saying what a candidate does, recommending it or suggesting a step can be skipped, read its complete `SKILL.md` and any conditional references needed to establish that claim. Record its resolved source/path and revision or content digest when available. Inspect required companion availability when it affects whether the proposed route is usable; reading instructions is not invoking them.

Candidates may include external installed skills. A repository source directory alone does not establish installation. Do not assume a fixed installation tree, exhaustive catalog, capability from a name, or compatibility between same-named copies. If the entry cannot be read, report it as unverified rather than endorsing it. If competing copies or overlapping routes remain ambiguous, explain the distinction or ask the smallest necessary question.

**Complete when:** substantive candidate claims have inspected sources, project constraints are identified, and discovery limits, missing options and unresolved ambiguities are explicit.

## 3. Recommend the smallest suitable route

Prefer one suitable next skill; offer a short sequence only when the user's situation needs it. Explain why it fits the goal and current progress, what input the user would supply, and where it stops. Reuse settled work rather than prescribing every phase from scratch.

Apply project rules before recommending a route as usable. Name any unmet approval, missing companion or incompatible restriction and its effect. When no suitable installed option is established, say so; suggest a bounded manual next step or clarification without assuming installation permission. A recommendation may identify a skill needing separate user invocation or approval, but must preserve that gate.

Keep all activity advisory and read-only. Do not invoke candidates or companions, delegate work, call assessment services, install or update anything, modify files or tracker state, or begin a recommended workflow. Even “recommend and then run it” ends here with the recommendation; execution needs a separate request handled outside this advisor.

**Complete when:** the recommendation is supported by inspected entries, respects project authority and names unresolved prerequisites, with no workflow started.

## 4. Return control to the user

Return a concise answer containing:

- The recommended next skill or route, or “no verified suitable installed option.”
- Why it fits, with the inspected source identity and any material discovery limit.
- The input and separate invocation/approval needed next; an example command is text for the user, not an action to execute.
- Missing or ambiguous options and the specific decision needed, if any.

State that nothing was invoked or changed. Describe recommendations as evidence-backed workflow advice, never as the maintainer's personal judgment or preference.

**Complete when:** the user can choose the next action and the advisor has stopped.

For package changes or validation, read [validation](references/validation.md) for metadata, portability and recommendation-only cases.
