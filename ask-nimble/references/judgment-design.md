# Judgment design

Read this before writing Ask Nimble questions. Keep deterministic calculations and exact lookups in code; use Nimble for the remaining semantic judgment.

## Choose the primitive

| Meaning | Type | Use and limitation |
| --- | --- | --- |
| One of competing outcomes | `choice` | Default. Include `insufficient_data` when evidence may be missing, and `no_match` when no substantive category fits. These are different conditions. |
| Whether one condition holds | `noul` | Probability of true. Use only when required evidence is available and an explicit unknown outcome is unnecessary. For multiple labels that may coexist, use independent questions rather than a mutually exclusive Choice. |
| Degree along an ordered rubric | `score` | Describe 2–26 concrete levels, lowest first. Use only when evidence supports the dimension; otherwise use Choice with an unknown outcome. |

For pricing direction, prefer Choice: too cheap, reasonable, too expensive, or insufficient data. A single Score would blur a middle “reasonable” outcome and missing evidence.

Noul's `noul` value is the model's probability of true, not the intensity of a condition. A value near 0.5 is not “medium severity.” Score returns a probability-weighted position across the supplied levels, not necessarily one discrete level. Neither primitive estimates a real-world event's frequency without empirical data.

Use Ollama's documented field names and response contracts from [the local API reference](ollama-api.md). Jev's hosted SDK features, limits, and structured instruction formats are not automatically Nimble features. Keep instructions and descriptions as strings unless local support is separately verified.

## Define contrasts, not desired answers

Each question must name its subject, scope, and benchmark. Reference nested state paths explicitly, such as `comparison.sources`. Put the full meaning in instructions rather than relying on a question ID.

For Choice, make substantive outcomes mutually exclusive. Describe:
- what evidence qualifies for this outcome;
- what belongs to an adjacent outcome instead;
- missing-data or no-match handling.

Start with concise descriptions. Add boundary examples when categories are easy to confuse; mark them as illustrative, and keep them out of the observed facts. Do not slip an agent-preferred verdict into instructions, examples, or criteria. A contrastive example should clarify a rule, not resemble the current subject so closely that it gives away the desired answer.

### Relative-pricing example

With the user's agreed benchmark of preceding sources and the immediately following source:

- **Too expensive:** a conspicuously poor cost/output relationship compared with that progression; a larger absolute price alone is not enough.
- **Reasonable:** broadly follows the tier-to-tier progression without a conspicuous favorable or unfavorable outlier.
- **Too cheap:** a conspicuously favorable cost/output relationship compared with that progression; ordinary tier variation alone is not enough.
- **Insufficient data:** missing or contradictory comparison facts prevent this scoped assessment.

Contrast examples: a price jump without a corresponding output improvement may indicate too expensive; proportionate growth can remain reasonable; unusually large output without comparable cost growth may indicate too cheap. These are qualitative examples, not numerical thresholds or a game-specific policy.

Compare marginal gain and actual cost when the user asks about a saved game's next purchase. Base-cost/base-rate comparisons answer catalog progression only. Include upgrades, discounts, ownership scaling, and synergies when they affect the requested scope. Missing a deciding modifier means missing evidence, not a neutral modifier.

## Decompose only independently useful dimensions

Default to one question. Use at most four over the same state when each dimension contributes to the requested answer and can be judged without another answer.

Example: base-source price consistency and upgrade-price consistency can be separate questions for a source's overall pricing assessment. A campaign-pacing question requires current simulation or playtest evidence; catalog ratios alone cannot answer it.

All questions in one request share evidence but are scored independently and cannot consume one another's outputs. Write any conditional premise explicitly. Ask a second request only when the first answer determines new evidence or options; keep the total assessment bounded rather than building an autonomous decision loop.

## Interpret without manufacturing agreement

Report dimensions separately. Two model judgments over the same evidence are not independent verification. If they disagree, explain which scope each addresses; do not hide disagreement with a majority vote.

Combine scores only under an explicit user-approved rule with comparable rubrics. Weights express preferences; they cannot cancel a hard policy violation. If no composition rule exists, preserve the separate outcomes.

Use uncertainty to choose the next useful verification, not to authorize action. A spread distribution may reflect ambiguous criteria, missing evidence, or several acceptable options. Low confidence does not itself diagnose which one. Investigate the actual state and question; never rerun merely to increase confidence.

## Sources

- [TypeSafe agent skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md): state/question separation, primitive selection, composition, and verification.
- [TypeSafe State](https://docs.typesafe.ai/concepts/state.md) and [Choice](https://docs.typesafe.ai/primitives/choice.md): context structure and contrasting options.
- [Ollama Nimble](https://ollama.com/library/nimble): authoritative local contracts and limitations.
