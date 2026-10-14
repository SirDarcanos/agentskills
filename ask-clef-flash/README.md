# Ask Clef Flash

Ask a question in plain language. Your coding agent first checks whether Clef Flash fits the task. For bounded judgments, it gathers relevant evidence, sends a structured decision request to local Clef Flash, and interprets the result. Otherwise, it answers directly.

## Usage

Invoke explicitly:

```text
/ask-clef-flash Is the Bigger Bowl upgrade priced correctly in Feed the Chonk?
/ask-clef-flash Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-clef-flash <question>`; `/ask-clef-flash` is the shorthand used by runtimes with name-based skill commands. Installing this skill does not create a custom Pi alias.

Agents may also invoke this package for a bounded judgment under the target's approved model-use policy. Permission must name `ask-clef-flash`, its exact local model/endpoint, purpose, disclosure, shared limits, lifecycle and fallback. Within those bounds no repeated approval is needed. Absent, denied or exhausted autonomous permission produces no calls or server effects. Explicit requests remain supported within project restrictions. See [authorization](references/authorization.md).

If the subject or meaning of “correct” is unclear, the agent asks for clarification. It gathers neutral evidence, checks comparison coverage and freshness, and defaults to a Choice with `insufficient_data` for gaps. Up to four independent dimensions can be assessed together; their outcomes remain separate. Noul and Score are available when their meanings fit and the required evidence is present.

## Which questions fit?

Clef Flash fits classification, routing, policy checks, evidence support, and judgments against an explicit rubric.

The agent answers factual questions, empirical probabilities, arithmetic, deterministic checks, and open-ended requests directly. For example, a newborn cat's chance of reaching 20 requires survival data, not Clef Flash's output probabilities. The agent explains the direct-answer choice and does not contact or start Ollama.

An explicit request to test Clef Flash against a known answer can still use it as a model test.

This skill selects `clef-flash` only. It can judge text, JSON, and relevant images; use the separate `ask-clef` command to choose the other variant. Neither skill sends evidence to Cloudflare.

## Requirements

An agent with repository-reading, file-writing, and shell tools; local Ollama 0.35.1 or later with `clef-flash` pulled; Python 3; and curl. See [the API reference](references/ollama-api.md) for the request procedure and validation.

After authorization, the agent reuses an existing local Ollama server, leaving it untouched. Startup requires exact policy or invocation-specific authority. Owned servers follow the approved cleanup disposition, or a reported pending user choice; the desktop app is optional.

If Ollama, Clef Flash, or the decision API is unavailable—or a response fails validation—the agent reports the blocker. Autonomous use follows only the configured direct fallback; explicit use offers and waits unless already authorized. Direct results are labeled agent assessments, not Clef Flash verdicts. This package never silently substitutes a model or endpoint.

Clef Flash sees only the evidence the agent sends. It does not independently read your repository or telemetry. The agent explains the decision; Clef Flash returns an outcome and probabilities, not an explanation.

Results are advisory. The command does not modify your project or authorize consequential actions.

After installing or upgrading Ollama, download this skill's model:

```sh
ollama pull clef-flash
```

Requests use the decision API, not `ollama run` or a chat endpoint. The agent asks before performing installations, upgrades, downloads, or server startup.

## Testing

The skill includes synthetic regression fixtures and a Python standard-library replay tool. Offline tests use mocked responses; live inference and retained records require explicit opt-in. See [testing guidance](references/testing.md) for commands and full agent-workflow scenarios.

## Files

- [SKILL.md](SKILL.md): the agent workflow.
- [references/authorization.md](references/authorization.md): explicit/policy gates, shared limits, lifecycle authority and fallback.
- [references/judgment-design.md](references/judgment-design.md): primitives, contrasting criteria, and decomposition.
- [references/ollama-api.md](references/ollama-api.md): local API requirements, request example, and response checks.
- [references/testing.md](references/testing.md): offline/live validation and failure diagnosis.
- [scripts/replay.py](scripts/replay.py) and [tests/cases.json](tests/cases.json): opt-in regression replay and synthetic fixtures.
