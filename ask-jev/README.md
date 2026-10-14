# Ask Jev

Request an evidence-backed judgment from TypeSafe's hosted Jev model. The agent gathers relevant evidence, sends a bounded assessment, validates the response, and interprets the result.

## Usage

```text
/ask-jev Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-jev <question>`. Installing the skill does not create a custom `/ask-jev` alias. The skill supports explicit requests and bounded handoffs authorized by a maintainer-approved project model-use policy. Discovery alone grants no hosted-call permission.

Jev fits bounded semantic judgments: classification, policy checks, evidence support, and explicit rubrics. Factual lookups, arithmetic, empirical probabilities, and open-ended tasks are answered directly without a Jev call.

## Requirements and consent

Use an agent with evidence-reading, JSON-writing, secure HTTP, and temporary-file cleanup capabilities. API calls require an existing authorized TypeSafe credential source and are billable. The standard environment variable is `TYPESAFE_API_KEY`; configure it outside the conversation.

Explicit invocation authorizes a normal billable assessment at `https://api.typesafe.ai/v1/systemone` with minimal task-relevant evidence; it does not trigger another confirmation. Applicable project prohibitions and stricter limits still apply. Configuring a key alone does not authorize calls. The agent asks only for exceptional scope, such as sensitive/private disclosure not clearly covered by your request, a different recipient, unusually large batches, or additional experiments. You can request the exact payload. Credentials and unrelated private data stay out of the payload and logs.

For autonomous use, follow the policy linked from the target's `AGENTS.md` (normally `docs/agents/model-use.md`, or its authoritative equivalent). It must approve the exact skill, TypeSafe recipient/endpoint, model ID or moving alias, purpose, evidence disclosure, finite shared call/retry/correction/spending limits and fallback. The lead reserves allowance; Ask Jev rechecks before every attempted send. Missing, denied, conflicting or exhausted permission causes zero authenticated operations. Authorized calls need no recurring confirmation. Unknown cost blocks sending without a safe worst-case reservation; failed and unknown-charge attempts consume allowance across parent/worker handoffs and resume.

If Jev is unavailable, explicit requests retain offer-and-wait direct fallback unless already authorized; autonomous use takes only policy-permitted direct assessment. Jev never silently switches its model, provider or transport. Any named approved alternative is returned to the lead for separate discovery and authorization. Valid insufficient-data results remain Jev decisions. Results are advisory and do not authorize project changes.

All internal references ship with this package; no sibling skill layout, mandatory delivery companion or policy parser is required. Installing/updating this source does not approve a policy or change installed copies elsewhere.

## Relationship to TypeSafe's skill

Keep the [upstream `typesafe-ai` skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) for designing and implementing TypeSafe-powered applications. Ask Jev consults that skill and relevant live docs when needed to craft questions or interpret results, before or after inference. It works without an installed copy by reading the upstream source.

This skill adds evidence gathering, disclosure-scope checks, bounded calls, contract validation, freshness checks, and explicit attribution. Jev supplies judgments and probabilities; explanations come from the agent. Answers include the decision and interpretation, with relevant uncertainty and next steps. Routine usage, model-version, and validation details stay out of the answer unless requested or material to a limitation.

## Files and validation

- [SKILL.md](SKILL.md): assessment workflow and completion checks.
- [Authorization](references/authorization.md): policy/explicit authority, shared hosted limits and fallback.
- [Judgment design](references/judgment-design.md): primitives and contrasting criteria.
- [Hosted API procedure](references/hosted-api.md): contracts, credentials, transport, validation, and cleanup.
- [Validation scenarios](references/testing.md): offline checks and opt-in live scenarios.

No production HTTP client is bundled. Test-only procedure simulations use mocked transport and synthetic resolved permissions; they are not a policy format or proof of real-agent enforcement. From this package root, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Validate the actual chosen runtime's transport separately. Live inference, credential changes and retained records require applicable separate authority; this source repository has not opted into model calls.
