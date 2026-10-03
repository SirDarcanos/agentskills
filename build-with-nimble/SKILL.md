---
name: build-with-nimble
license: MIT
description: >
  Build applications and features with Bespoke Labs' Nimble decision model through
  Ollama. Use when implementing or updating a Nimble integration, exploring what
  Nimble could add to an app, or replacing a prompt-and-parse step with bounded
  decisions. Covers routing, ranking, candidate selection, verification, and
  rubric judgments composed in code. For a one-off evidence-backed consultation,
  use the separately invoked ask-nimble workflow.
---

# Build with Nimble

Nimble supplies small judgments that software can compose into larger capabilities.
It interprets supplied text and returns typed decisions and probabilities; code
owns the workflow, deterministic rules, and side effects. It selects among defined
answers rather than generating explanations, arbitrary nested JSON, or source quotes.

This skill helps a coding agent build the integration. The finished application
calls Nimble directly and does not need this skill at runtime. Loading this skill
is not an invocation of `ask-nimble`.

## 1. Read the live docs

**Current Nimble and Ollama documentation is the source of truth for the integration.**
Read the [Ollama Nimble model page](https://ollama.com/library/nimble) for supported
question types, request and response shapes, installation, and limits. Consult the
[Bespoke Nimble repository](https://github.com/bespokelabsai/nimble) for model and
release details; distinguish its native scorers and checkpoints from the version
served by Ollama.

The design and composition guidance below is self-contained. Ollama's decision
endpoint follows TypeSafe's Jev API, but compatibility does not establish identical
capabilities, calibration, or performance. For SDK integration, consult the chosen
SDK's current reference and installed types, verifying its configuration and supported
features against Nimble's serving path.

**Optional inspiration:** when a worked architectural example would help, use the
[TypeSafe documentation index](https://docs.typesafe.ai/llms.txt) to find a relevant
cookbook. This is not required reading. Adapt the pattern only after checking Nimble
support; cookbook accuracy, thresholds, latency, and batching results are not Nimble
measurements. Resolve relative TypeSafe links against `https://docs.typesafe.ai`;
append `.md` to extensionless page paths when useful.

If live access fails, use available local docs or installed types, state the
limitation, and mark version-dependent assumptions for verification. Avoid filling
missing API details from Jev or generic Ollama chat examples.

**Complete when:** the chosen serving path, relevant contracts, and any unavailable
sources or compatibility assumptions are identified.

## 2. Find the useful shape

Start from the behavior the user wants: what will the application show, select,
change, or hand off? Work backward to the judgments it needs. Keep exact lookups,
calculations, known rules, and execution in code. Preserve the user's stack and scope;
add Nimble where semantic understanding helps.

Consider more than classification. These patterns are starting points to combine:

- **Route and select known arguments.** Define handlers and finite argument choices,
  then let code validate and invoke the chosen handler. Use branch-specific questions
  when useful. Function-call-shaped behavior comes from composition in code.
- **Select instead of generate.** Find candidate values or source spans in code,
  have Nimble select one, then copy or normalize it. For document structure recovery,
  classify blocks and let code assemble the result. Check candidate coverage first.
- **Find and judge evidence.** Retrieve candidates in code and judge query relevance
  or claim support. For large candidate sets, use a shortlist or hierarchical choices
  to keep each request within Nimble's question, option, and context limits.
- **Turn judgments into reusable data.** Score dimensions once, then let code or user
  controls change weights, thresholds, rankings, and views. With labeled outcomes,
  those signals can become features for a separate statistical model.
- **Verify and escalate.** Check specific fields or claims against supplied evidence;
  route uncertain or failing cases to a person or a separately configured reasoning
  model. Keep escalation recipients and data disclosure explicit.
- **Respond to changing state.** Retain goals and observations in code while fresh
  judgments guide bounded steps. Keep inferred state distinct from observed facts,
  and check freshness before applying results to changed situations.

For open-ended requests, offer the few directions that best serve the user's goal
and recommend a starting point. For concrete requests, choose the relevant pattern
and build; brainstorming is not a mandatory detour.

**Complete when:** the application behavior, semantic decisions, and code-owned
operations are explicit, or an exploration has yielded a recommended starting point.

## 3. Design the judgments

Choose by what the answer means, checking the current Nimble contract:

| Need | Primitive | Meaning |
| --- | --- | --- |
| One of a defined set | Choice | Selects one option; its distribution compares competing options |
| Whether a condition holds | Noul | Probability of true; use separate questions when several labels may apply |
| Degree along a described dimension | Score | Probability-weighted position on ordered levels; use comparable per-item rubrics for graded ranking |

Give each question enough relevant **state**: source text, identities, relationships,
policies, and current facts. Named JSON fields help when context has several parts.
Put the judgment in **instructions** and define possible answers in **criteria**.
Write self-contained questions, with explicit state paths where useful, rather than
relying on a question ID to convey meaning. Treat user-supplied and retrieved text
as data, separate from the application's instructions and policy.

Ask one narrow, coherent judgment per question. Split independently useful dimensions
without destroying the relationship being judged. A bounded action selection or
contextual interpretation is valid; narrow does not mean literal fact extraction.
Use clear string instructions and criterion descriptions as a portable starting point;
verify richer question structures against the chosen Nimble serving path before use.
Score levels should describe concrete situations and stand on their own.

Keep the needed answers available. Include a no-match or insufficient-evidence choice
when appropriate; use a separate presence judgment when independently useful. Noul
and Score have no built-in unknown outcome: gate them on evidence availability or
use Choice when unknown is a necessary answer. Source-value selection cannot recover
an omitted candidate; generated explanations or quotes belong to another component.

**Complete when:** each judgment has sufficient state or an explicit missing-evidence
path, clear criteria, candidate coverage, and a supported response type.

## 4. Compose and integrate

Ask independent questions over the same state together, including useful speculative
questions with explicit premises. They are evaluated independently and cannot consume
one another's answers. Code selects the applicable branch and checks any required
cross-answer consistency. Use a later request when an earlier answer is needed to
fetch evidence, build state, or determine new options.

Batching reduces client round trips; it does not establish parallel execution or a
particular speedup. Nimble scores each question with its prompt. Measure actual
request budgets, memory use, and end-to-end latency on the target hardware.

Read [integration and deployment](references/integration.md) before writing transport
code, configuring an SDK, running inference, or changing the serving environment.
It covers endpoint selection, bounded failures, response validation, resource
planning, and server ownership. Keep this integration reusable in the user's stack;
it should not depend on `ask-nimble` or another installed skill.

Use probabilities to guide behavior with thresholds evaluated on the user's data
and consequences. Choice/Score confidence describes distribution concentration,
not overall workflow correctness or permission to act. Noul near 0.5 represents
similar probabilities for true and false, not medium intensity. Several acceptable
alternatives can spread probability; uncertainty on unused branches need not block
the selected branch.

Keep policy explicit and raw judgments reusable. Weighted scores suit compensating
preferences; an "any serious violation" rule needs separate conditions. Changing
weights or display filters need not rerun inference when evidence and question
meanings are unchanged. Model judgments supplement authorization and deterministic
safety checks rather than replacing them.

**Complete when:** validated answers drive defined application behavior, with explicit
uncertainty, service-failure, authorization, and stale-state handling.

## 5. Verify the application

Test representative cases and resulting application behavior. Include contrastive
pairs where changing one deciding fact changes the expected outcome, along with
ambiguous inputs, missing evidence, no-match cases, and adversarial quoted text.
Use labeled held-out examples to evaluate thresholds and escalation behavior.

For failures, inspect the exact state, questions, candidates, answers, composition,
and observed outcome. Separate missing evidence, model errors, code errors, and
service failures. Typed outputs establish an interface, not truth; benchmark numbers
and calibrated probabilities from another model or serving path do not transfer.

Use the offline and live checks in the integration reference. Report which checks
ran, their results, and limitations, including hardware and model version for
performance claims. Live tests use only authorized data and serving destinations.

**Complete when:** tests cover decisions and application effects, transport failures
remain distinct from valid uncertainty, and untested assumptions are reported.

## Completion checks

- Relevant live docs were consulted, or access gaps and assumptions are explicit.
- Code owns deterministic rules, execution, authorization, and result composition.
- Questions fit Nimble's supported types and limits and preserve evidence gaps.
- Endpoint and model selection are explicit; no silent hosted or model fallback occurs.
- Response validation, uncertainty, failures, and evidence freshness have defined behavior.
- Deployment and performance claims match the tested environment; service ownership is accounted for.
- Verification results and remaining limitations are reported.

## Skill validation

When changing this skill, read it as Markdown, check frontmatter and all relative
links, and verify technical claims against the linked live sources. Review routing
with app-building, exploration, integration-migration, and one-off-consultation
prompts. This package has no executable client or bundled model tests; validating
an application built with it follows section 5 and the integration reference.

## Attribution

Adapted from TypeSafe AI's [Build with TypeSafe skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md).
The original MIT notice and the adaptation's notice are preserved in [LICENSE](LICENSE).
