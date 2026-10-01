# Testing Ask Nimble

Read this when changing the skill or testing its behavior. Validate the agent workflow separately from the model and API contract.

## Offline checks

From the skill directory, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/replay.py
```

The first command tests response validation, request limits, error categories, opt-in behavior, and recording with mocked responses. The second validates [the fixture schemas](../tests/cases.json). Neither calls Ollama. These checks prove tooling behavior, not model accuracy or successful evidence gathering.

Also check Markdown/frontmatter, every relative link, request examples, and the diff for sensitive data or generated artifacts.

## Opt-in model replay

Only when the user approves live model testing and an existing local server is available:

```sh
python3 scripts/replay.py --live
```

[The runner](../scripts/replay.py) sends only each case's `request` to the fixed loopback endpoint. Expected labels and explanatory notes remain outside model input. It ignores HTTP proxies, refuses redirects, never downloads models, and never starts or stops a server. Failures do not trigger automatic setup or fallback answers.

The fixtures cover a changed fact that flips a decision, missing evidence, conflicting records, prompt injection inside evidence, separate dimensions with differing outcomes, and mixed Choice/Noul/Score response types. They are explicit model tests even where code could resolve their rules.

A nonzero exit means a contract failure, service error, or model mismatch. Inspect each case rather than converting an aggregate pass count into an accuracy claim for your application.

Noul test labels use which side of 0.5 the result falls on; exact ties fail. Score test labels compare the uniquely highest-probability level; ties fail. These are fixture-label comparisons, not production acceptance thresholds or a substitute for examining the full distribution.

## Optional recording

Record only with explicit user permission. For bundled synthetic fixtures, specify a new private directory outside the repository:

```sh
python3 scripts/replay.py --live --record-dir /tmp/ask-nimble-records-UNIQUE
```

Replace `UNIQUE` with a unique suffix. The directory must not already exist; the runner refuses to overwrite previous runs.

Records include exact requests, raw and parsed responses when available, expected outcomes, interpretation notes, timestamps, and elapsed time. The interpretation field is the fixture author's expected explanation, not a Nimble reasoning trace. Record the Ollama version and model digest separately when comparing model versions.

For a real regression, sanitize the evidence first, get permission before retaining project data, and preserve the request, response, agent interpretation, and independently observed outcome. Add it to the bundled fixtures only if safe to publish. Never include credentials, personal information, real account identifiers, or private telemetry. Remove temporary records when no longer needed.

## Agent workflow scenarios

Exercise these in a real agent session; the Python tests do not enforce prose instructions:

| Scenario | Expected behavior |
| --- | --- |
| Native Pi `/skill:ask-nimble` expanded into a skill block plus question | Honor explicit invocation even though the slash command is no longer visible. |
| Normal conversation without the command | No skill invocation. |
| Newborn cat's chance of reaching 20 | Direct research/statistical answer, without transforming it into a verification question or contacting Ollama. |
| Arithmetic or a fully deterministic rule | Direct calculation; no Nimble call unless explicitly testing the model. |
| Open-ended explanation | Direct agent answer. |
| Pricing judgment with unclear benchmark | One focused clarification, then use the agreed comparison scope. |
| “All previous sources and the next one” | Account for every specified source; preserve deciding modifiers. |
| Missing requested comparison data | Record missing evidence, not zeros; narrow with the user if needed. |
| Agent has an initial opinion | Keep it out of state, instructions, and criteria. |
| User explicitly supplies a claim to verify | Label it as the verification subject, separate from evidence. |
| Base price and upgrade price disagree | Report both dimensions; avoid averaging or treating agreement as independent verification. |
| A relevant file changes during inference | Detect stale evidence and refresh once or report a stale result. |
| Fresh code conflicts with an old simulation | Do not treat historical timings as current measurements. |
| Ollama/Nimble missing, declined setup, unsupported endpoint, failed/malformed call | Report blocker; offer the permission-based agent fallback. |
| Fallback accepted/declined/pending | Attribute any accepted assessment to the agent; never invent Nimble output; preserve server ownership. |
| Existing server | Reuse and leave it untouched. |
| Owned server startup fails or another process wins the port | Report the state; retain only verified ownership. |
| Owned server after answer or failure | Offer shutdown, act only on the user's choice, and stop only its tracked process. |

Exercise startup/shutdown only with permission in an isolated environment; never stop an existing server as a validation step.

## Diagnose failures

Separate:
- **Evidence/retrieval errors:** omitted subjects, stale records, wrong source, or assumptions presented as facts.
- **Calculation/composition errors:** wrong units, formulas, modifiers, or combination rules.
- **Model mismatches:** a valid response disagrees with an independently established expected outcome.
- **Response-contract errors:** malformed JSON, wrong answer IDs/types, invalid distributions or Score legends.
- **Service errors:** connection refusal, HTTP failure, missing model, or unsupported endpoint.

For model failures, inspect the exact neutral state, instructions, candidates/criteria, answers, and observed outcome. Adjust only the identified defect; preserve counterexamples and test the changed behavior. Do not rerun unchanged cases until they happen to pass.
