# Ask Jev

Request an evidence-backed judgment from TypeSafe's hosted Jev model. The agent gathers relevant evidence, sends a bounded assessment, validates the response, and interprets the result.

## Usage

```text
/ask-jev Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-jev <question>`. Installing the skill does not create a custom `/ask-jev` alias. The skill is command-only and includes an invocation gate for runtimes that do not enforce its frontmatter.

Jev fits bounded semantic judgments: classification, policy checks, evidence support, and explicit rubrics. Factual lookups, arithmetic, empirical probabilities, and open-ended tasks are answered directly without a Jev call.

## Requirements and consent

Use an agent with evidence-reading, JSON-writing, secure HTTP, and temporary-file cleanup capabilities. API calls require an existing authorized TypeSafe credential source and are billable. The standard environment variable is `TYPESAFE_API_KEY`; configure it outside the conversation.

Explicit invocation authorizes a normal billable assessment at `https://api.typesafe.ai/v1/systemone` with minimal task-relevant evidence; it does not trigger another confirmation. Configuring a key alone does not authorize calls. The agent asks only for exceptional scope, such as sensitive/private disclosure not clearly covered by your request, a different recipient, unusually large batches, or additional experiments. You can request the exact payload. Credentials and unrelated private data stay out of the payload and logs.

If Jev is unavailable, the agent asks before assessing the question itself. It never silently substitutes Nimble or another model. Results remain advisory and do not authorize project changes.

## Relationship to TypeSafe's skill

Keep the [upstream `typesafe-ai` skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) for designing and implementing TypeSafe-powered applications. Ask Jev consults that skill and relevant live docs when needed to craft questions or interpret results, before or after inference. It works without an installed copy by reading the upstream source.

This skill adds evidence gathering, disclosure-scope checks, bounded calls, contract validation, freshness checks, and explicit attribution. Jev supplies judgments and probabilities; explanations come from the agent. Answers include the decision and interpretation, with relevant uncertainty and next steps. Routine usage, model-version, and validation details stay out of the answer unless requested or material to a limitation.

## Files and validation

- [SKILL.md](SKILL.md): command workflow and completion checks.
- [Judgment design](references/judgment-design.md): primitives and contrasting criteria.
- [Hosted API procedure](references/hosted-api.md): contracts, credentials, transport, validation, and cleanup.
- [Validation scenarios](references/testing.md): offline checks and opt-in live scenarios.

No HTTP client or model tests are bundled. Validate the actual chosen runtime's transport separately. An explicitly invoked model test covers its normal billable assessment. Additional live experiments and retained records require separate approval.
