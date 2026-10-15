# Architectural decision records

Read when an architectural choice needs a durable record or an existing decision is reconsidered. Apply the entry point's mode and authorization gates before writing.

Offer a record when **all three** apply: changing course has meaningful cost, the choice would surprise a future reader without context, and there was a real trade-off. A difficult-to-reverse provider choice or deliberate ownership boundary may qualify; an ordinary helper or speculative future abstraction usually does not. Deferral or no qualifying ADR is a legitimate outcome.

## Procedure

1. Read relevant existing ADRs and establish the decision, alternatives that genuinely mattered, reason, and decision authority. Mark an unapproved proposal as proposed; consequential product/cost/risk effects require the appropriate approval. Do not retrofit an invented rationale onto historical code.
2. Reuse an existing record for an unchanged decision or a factual clarification. For a new record, inspect the existing location and naming scheme, including context-specific records. Otherwise propose `docs/adr/0001-short-decision.md` and increment the highest number; recheck before writing to avoid concurrent numbering collisions. Create the directory only for the first actual record.
3. Write a short title and a concise paragraph covering context, decision, and rationale. Add consequences, alternatives, or status only when useful. Record accepted status explicitly if it could be mistaken for a proposal. Preserve any fields required by the project's existing convention.
4. When an accepted replacement changes a decision, preserve the old explanation, mark it superseded, and link both records. A proposed replacement links the current decision but leaves that decision in force until acceptance. A rejected or deferred proposal is not a supersession.
5. Make the relevant record discoverable from the existing domain/architecture index or an in-scope entry-point pointer; otherwise return the needed pointer to the caller. Do not require every agent to read every ADR for every change.
6. Verify status, rationale, links, and preserved history against the actual approval. On an interrupted supersession, inspect both records and reconcile only the remaining approved delta; never create another replacement merely because a prior write was partial.

**Done:** the decision and authority are clear, rationale survives, and relevant future work can find the record. A proposed choice has not silently displaced an accepted decision.
