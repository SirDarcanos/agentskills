# Ask Jev

Request an evidence-backed judgment from TypeSafe's hosted Jev model. The agent gathers relevant evidence, gets approval before sending it remotely, validates the response, and explains the result.

## Usage

```text
/ask-jev Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-jev <question>`. Installing the skill does not create a custom `/ask-jev` alias. The skill is command-only and includes an invocation gate for runtimes that do not enforce its frontmatter.

Jev fits bounded semantic judgments: classification, policy checks, evidence support, and explicit rubrics. Factual lookups, arithmetic, empirical probabilities, and open-ended tasks are answered directly without a Jev call.

## Requirements and consent

Use an agent with evidence-reading, JSON-writing, secure HTTP, and temporary-file cleanup capabilities. API calls require an existing authorized TypeSafe credential source and are billable. The standard environment variable is `TYPESAFE_API_KEY`; configure it outside the conversation.

Invoking the command does not automatically approve remote disclosure. Before calling, the agent explains the destination, sanitized evidence scope, chosen model, billing, and bounded call budget. You can inspect the payload or decline. Credentials and unrelated private data stay out of the payload and logs.

If Jev is unavailable, the agent asks before assessing the question itself. It never silently substitutes Nimble or another model. Results remain advisory and do not authorize project changes.

## Relationship to TypeSafe's skill

Keep the [upstream `typesafe-ai` skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) for designing and implementing TypeSafe-powered applications. Ask Jev consults that skill and relevant live docs when needed to craft questions or interpret results, before or after inference. It works without an installed copy by reading the upstream source.

This skill adds an operational assessment workflow: evidence gathering, remote-disclosure approval, bounded calls, contract validation, freshness checks, and explicit attribution. Jev supplies judgments and probabilities; explanations come from the agent. The report identifies the returned model version and available token usage.

## Files and validation

- [SKILL.md](SKILL.md): command workflow and completion checks.
- [Judgment design](references/judgment-design.md): primitives and contrasting criteria.
- [Hosted API procedure](references/hosted-api.md): contracts, credentials, transport, validation, and cleanup.
- [Validation scenarios](references/testing.md): offline checks and opt-in live scenarios.

No HTTP client or model tests are bundled. Validate the actual chosen runtime's transport separately. Live inference and retained records require explicit approval.
