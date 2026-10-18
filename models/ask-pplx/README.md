# Ask Pplx

Use Perplexity's local `pplx-decider` decision model, not its search or chat service. Ask a question in plain language. Your coding agent first checks whether Pplx fits the task. For bounded judgments, it gathers relevant evidence, sends a structured decision request to local Pplx, and interprets the result. Otherwise, it answers directly.

## Usage

Invoke explicitly:

```text
/ask-pplx Is the Bigger Bowl upgrade priced correctly in Feed the Chonk?
/ask-pplx Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-pplx <question>`; `/ask-pplx` is the shorthand used by runtimes with name-based skill commands. Installing this skill does not create a custom Pi alias.

Agents may also invoke this package for a bounded judgment under the target's approved model-use policy. Permission must name `ask-pplx`, its exact local model/endpoint, purpose, disclosure, shared limits, lifecycle and fallback. Within those bounds no repeated approval is needed. Absent, denied or exhausted autonomous permission produces no calls or server effects. Explicit requests remain supported within project restrictions. See [authorization](references/authorization.md).

If the subject or meaning of “correct” is unclear, the agent asks for clarification. It gathers neutral evidence, checks comparison coverage and freshness, and defaults to a Choice with `insufficient_data` for gaps. Up to four independent dimensions can be assessed together; their outcomes remain separate. Noul and Score are available when their meanings fit and the required evidence is present.

## Which questions fit?

Pplx fits classification, routing, policy checks, evidence support, and judgments against an explicit rubric.

The agent answers factual questions, empirical probabilities, arithmetic, deterministic checks, and open-ended requests directly. For example, a newborn cat's chance of reaching 20 requires survival data, not Pplx's output probabilities. The agent explains the direct-answer choice and does not contact or start Ollama.

An explicit request to test Pplx against a known answer can still use it as a model test.

This skill selects `pplx-decider` only. It can judge text, JSON, and relevant images. Other models, tags and hosted transports are not substitutes. See [model workings](references/model-workings.md) for how its readout works and how to interpret its probabilities.

## Project context

Project work requires the target's existing working agreement or meaningful equivalent; missing or conflicting guidance is reported for explicit reconciliation, not replaced by this skill. Named non-project assessments remain usable under their exact invocation and authorization gates. Setup and ordinary invocation grant no assessment permission; no delivery companion is required.

## Requirements

An agent with repository-reading, file-writing, and shell tools; a local Ollama build supporting `pplx-decider` on System One, with the model pulled; Python 3.10+; and curl. See [the API reference](references/ollama-api.md) for the request procedure and validation.

After authorization, the agent reuses an existing local Ollama server, leaving it untouched. Startup requires exact policy or invocation-specific authority. Owned servers follow the approved cleanup disposition, or a reported pending user choice; the desktop app is optional.

If Ollama, Pplx, or the decision API is unavailable—or a response fails validation—the agent reports the blocker. Autonomous use follows only the configured direct fallback; explicit use offers and waits unless already authorized. Direct results are labeled agent assessments, not Pplx verdicts. This package never silently substitutes a model or endpoint.

Pplx sees only the evidence the agent sends. It does not independently read your repository or telemetry. The agent explains the decision; Pplx returns an outcome and probabilities, not an explanation.

Results are advisory. The command does not modify your project or authorize consequential actions.

After installing or upgrading Ollama, download this skill's model:

```sh
ollama pull pplx-decider
```

The skill uses the decision API for structured response validation; Ollama also documents `ollama run --ask`, but chat/generation endpoints are not substitutes. The agent asks before performing installations, upgrades, downloads, or server startup.

## Testing

The skill includes synthetic regression fixtures and a Python standard-library replay tool. Offline tests use mocked responses; live inference and retained records require explicit opt-in. See [testing guidance](references/testing.md) for commands and full agent-workflow scenarios.

## Files

- [SKILL.md](SKILL.md): the agent workflow.
- [references/authorization.md](references/authorization.md): explicit/policy gates, shared limits, lifecycle authority and fallback.
- [references/judgment-design.md](references/judgment-design.md): primitives, contrasting criteria, and decomposition.
- [references/ollama-api.md](references/ollama-api.md): local API requirements, request example, and response checks.
- [references/model-workings.md](references/model-workings.md): model architecture, calibration caveats and task design implications.
- [references/testing.md](references/testing.md): offline/live validation and failure diagnosis.
- [scripts/replay.py](scripts/replay.py) and [tests/cases.json](tests/cases.json): opt-in regression replay and synthetic fixtures.
