# Judgment design

Use Jev for semantic judgment over supplied evidence; keep exact calculations, rules, and lookups in code.

## Choose by meaning

| Primitive | Meaning | Use in this command |
| --- | --- | --- |
| Choice | One of competing outcomes and their distribution | Default; include `insufficient_data` for evidence gaps and `no_match` when no substantive outcome fits. |
| Noul | Probability that one condition holds | Use when the required evidence is available and an explicit unknown outcome is unnecessary. Multiple labels can use independent Nouls. |
| Score | Probability-weighted position on ordered rubric levels | Use concrete, standalone levels describing one dimension. Missing evidence needs Choice with an unknown outcome instead. |

Noul near 0.5 means similar probability for yes and no, not medium intensity. Score can fall between levels; it is not necessarily a discrete classification. Choice/Score confidence measures distribution concentration, not workflow correctness. None of these values estimates a real-world event's frequency without empirical data.

Consult the current primitive pages from the [documentation index](https://docs.typesafe.ai/llms.txt) when structured instructions, boundary cases, or returned values need clarification. Hosted formats and limits come from the [API procedure](hosted-api.md), not Nimble's local contracts.

## Write contrasting criteria

Each question names the subject, scope, benchmark, and relevant state paths. Its ID is only for code and is not supplied to the model. Instructions state the judgment; criteria define possible answers. Structured instructions or descriptions can clarify contrasts, definitions, and illustrative examples without embedding a preferred verdict.

For Choice, make substantive outcomes mutually exclusive. Describe what qualifies, what belongs to an adjacent outcome, and what evidence gap prevents a judgment. Distinguish missing evidence from a fully evidenced no-match case. For selection tasks, verify candidate coverage: Jev cannot select an omitted value.

For an implementation review, suitable outcomes might be:

- **Meets:** supplied behavior and evidence satisfy every criterion in the agreed scope.
- **Does not meet:** at least one criterion has a supported violation.
- **Insufficient data:** no violation is established, but deciding behavior or evidence is missing or contradictory.

These are illustrative; use the actual project's acceptance policy. Whether missing evidence itself counts as failure depends on that policy and must be explicit.

## Keep decomposition bounded

Default to one question, with at most four independently useful dimensions. Each must be answerable from the shared state without reading another answer. Explicit speculative premises are acceptable; consume only applicable branches and ignore uncertainty in unused ones.

Preserve separate dimensions unless the user agrees to a composition rule. Weighted preferences cannot cancel a hard-policy violation. Low confidence may reflect missing evidence, vague criteria, or several acceptable alternatives; inspect the actual state and questions rather than treating it as an automatic diagnosis.

For deeper design guidance, use the upstream skill under the conditions in step 2 of `SKILL.md`. For production thresholds, evaluate labeled domain examples; cookbook thresholds are examples, not universal acceptance rules.
