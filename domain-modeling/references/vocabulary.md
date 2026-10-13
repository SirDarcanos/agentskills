# Vocabulary and context maps

Use when establishing or changing domain meanings. Apply the entry point's mode and authorization gates before writing.

## 1. Locate and test meanings

Read existing definitions, context maps, relevant specs, and code using the terms. Distinguish intended vocabulary from implementation names; code alone cannot establish a historical product decision. Preserve accepted definitions until a change is confirmed by the appropriate authority.

Identify overloaded terms and consequential contradictions. Propose a precise meaning with a concrete example and a counterexample; test relationships with relevant edge cases such as shared ownership, partial completion, or a concept crossing contexts. These are questions to resolve, not new requirements. Prefer an existing term when it still expresses the concept accurately.

Separate intended behavior from observed implementation. If they differ, report which evidence disagrees and whether the meaning is unresolved, the documentation is stale, or a code change may be needed. Resolve within the project's decision authority; escalate what lies outside it.

**Done:** each affected term and relationship is either confirmed in its context or explicitly unresolved, with consequential ambiguity exposed.

## 2. Choose the existing home or a minimal new one

Reuse the project's authoritative glossary and context map. For a new single-context project with confirmed terms and no existing home, propose `CONTEXT.md`. With no confirmed terms, omit the file.

Preserve multiple bounded contexts and their map. A term may legitimately mean different things in different contexts; do not flatten those meanings into a global definition. When confirmed distinct contexts need a new map, propose `CONTEXT-MAP.md` linking their actual glossary locations and describing their responsibilities and relationships. Confirm boundaries from domain evidence, not folder count or hypothetical scale. Keep existing layouts and avoid creating empty per-context glossaries.

**Done:** each confirmed meaning has one authoritative scoped home, and any new file has useful content rather than a placeholder.

## 3. Record the approved delta

1. Record each term's concise meaning, important domain relationships, and the ambiguity it resolves. Include aliases or distinctions only where they help avoid a real misunderstanding; preserve the existing format.
2. Keep the glossary focused on product/domain concepts. Operating preferences, implementation plans, and a catalog of every class/function belong elsewhere.
3. For a context map, identify each context's responsibility, link its existing definitions, and describe confirmed cross-context ownership or exchange. Keep architectural rationale in relevant ADRs rather than copying it into the map.
4. Update only affected definitions, map entries, and in-scope references. Return other affected consumers as follow-up findings, including code names that now disagree.
5. Recheck the result against the confirmed meaning and scenario answers. A future reader should be able to tell which concept is meant and where its definition applies.

**Done:** approved meanings and relationships are discoverable, unrelated definitions remain intact, and unresolved questions remain visible outside the confirmed glossary.
