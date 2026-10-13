# Domain records

Use this procedure when setup encounters established product terms, existing domain docs, or a consequential architectural decision. This is maintained setup guidance, not a dependency on a globally installed skill. The [documentation contract](documentation-contract.md) owns document locations and update responsibilities.

## Glossary

1. Read existing definitions, context maps, relevant specs, and code using the terms. Distinguish intended vocabulary from implementation names; code alone cannot establish a historical product decision.
2. Reuse confirmed terms. Ask about a consequential ambiguity in product language. A new project with no confirmed terms needs no empty glossary.
3. Record each term's meaning, important relationships, and ambiguity it resolves. Prefer the existing term when it accurately expresses the concept; avoid a catalog of every class and function.
4. Preserve multiple bounded contexts and their context map. Do not flatten different meanings into a global definition merely to fit CONTEXT.md.
5. Update only affected definitions and their references. Recheck terminology against the approved decision and identify any implementation mismatch separately.

**Done:** relevant confirmed meanings are discoverable, conflicts are resolved or explicit, and operating preferences remain outside the glossary.

## Architectural decisions

Offer a record when **all three** apply: changing course has meaningful cost, the choice would surprise a future reader without context, and there was a real trade-off. A difficult-to-reverse provider choice or deliberate ownership boundary may qualify; an ordinary helper or speculative future abstraction usually does not.

1. Establish the decision, alternatives that genuinely mattered, reason, and decision authority. Mark an unapproved proposal as proposed; consequential product/cost/risk effects require the appropriate approval.
2. For a new record, inspect the existing naming scheme. Otherwise use `docs/adr/0001-short-decision.md` and increment the highest number; recheck before writing to avoid concurrent numbering collisions. Create the directory only for the first actual record.
3. Write a short title and a concise paragraph covering context, decision, and rationale. Add consequences, alternatives, or status only when useful. Record accepted status explicitly if it could be mistaken for a proposal.
4. If replacing a decision, preserve the old explanation, mark it superseded, and link both records. Do not retrofit an invented rationale onto historical code.
5. Make the relevant record discoverable from the existing domain/architecture index or entry-point pointer. Do not require every agent to read every ADR for every change.

**Done:** the decision and authority are clear, its rationale survives, and relevant future work can find it. Deferral or no qualifying ADR is a legitimate outcome, not missing paperwork.

This reference is original repository guidance implementing the agreed setup contract. It does not copy an externally installed domain-modeling package or require its license/runtime assumptions.
