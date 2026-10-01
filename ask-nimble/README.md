# Ask Nimble

Ask a question in plain language. Your coding agent first checks whether Nimble fits the task. For bounded judgments, it gathers relevant evidence, sends a structured decision request to local Nimble, and interprets the result. Otherwise, it answers directly.

## Usage

Invoke explicitly:

```text
/ask-nimble Is the Bigger Bowl upgrade priced correctly in Feed the Chonk?
/ask-nimble Does this implementation satisfy the acceptance criteria?
```

In Pi, use `/skill:ask-nimble <question>`; `/ask-nimble` is the shorthand used by runtimes with name-based skill commands. Installing this skill does not create a custom Pi alias.

The skill is command-only, with `disable-model-invocation: true`. It also contains an explicit invocation gate for runtimes that do not enforce that frontmatter.

If the subject or meaning of “correct” is unclear, the agent asks for clarification. When evidence is missing, the allowed answers include `insufficient_data`.

## Which questions fit?

Nimble fits classification, routing, policy checks, evidence support, and judgments against an explicit rubric.

The agent answers factual questions, empirical probabilities, arithmetic, deterministic checks, and open-ended requests directly. For example, a newborn cat's chance of reaching 20 requires survival data, not Nimble's output probabilities. The agent explains the direct-answer choice and does not contact or start Ollama.

An explicit request to test Nimble against a known answer can still use it as a model test.

## Requirements

An agent with repository-reading, file-writing, and shell tools; local Ollama 0.35 or later with Nimble pulled; Python 3; and curl. See [the API reference](references/ollama-api.md) for the request procedure and validation.

The agent reuses an existing local Ollama server. If none is responding, it asks before starting `ollama serve` in the background; the desktop app is optional. After answering, it asks whether to stop a server it started or leave it running. Reused servers stay untouched.

If Ollama, Nimble, or the decision API is unavailable—or a call fails—the agent reports the blocker and offers to assess the question directly instead. It waits for your approval and labels an accepted fallback as an agent assessment, not a Nimble verdict.

Nimble sees only the evidence the agent sends. It does not independently read your repository or telemetry. The agent explains the decision; Nimble returns an outcome and probabilities, not an explanation.

Results are advisory. The command does not modify your project or authorize consequential actions.

## Files

- [SKILL.md](SKILL.md): the agent workflow.
- [references/ollama-api.md](references/ollama-api.md): local API requirements, request example, and response checks.
