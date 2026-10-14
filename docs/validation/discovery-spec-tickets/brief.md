# Discovery return: personal next-read selection

**Complete for the synthetic scope**, not a real product approval. Input/approval: [scripted owner turns 1–2](input.md#discovery-request-and-scripted-owner-turns). Two rounds used; no unresolved consequential intent remains after turn 2. If turn 2 is absent, ordering/undo/pin meaning and limitation remain unresolved and the result is blocked with a useful draft.

Goal: find next books in one's personal list. Required: pin/unpin own books, pinned group above ordinary books, saved relative order inside each group, undo restoring the ordinary saved position without losing entries, reader isolation and an unchanged empty list.

- Required now: the behavior above, with observable success at the reading page.
- Deferred: reminders until the list is larger; revisit at that point.
- Excluded: sharing, because this is personal next-read selection.
- Accepted limitation: no manual pin order, explicitly accepted only in scripted turn 2.

Confirmed meaning: pin is a personal next-read selection, not a reservation or reading status. Domain Modeling returned a plan-only proposed `CONTEXT.md` definition, with no target write: “Pin: a reader's reversible selection of an own-list book to appear in the next-read group. It does not reserve a book or change reading status.” Example: selecting an own book changes its group; counterexample: reserving a shared copy does not constitute a pin. No new context map or ADR is warranted for this bounded vocabulary question. Caller can later request an approved glossary update; ticketing cannot silently apply it.

Research return R1: the [baseline](../shape-work/reading_list.py) `visible_books` filters on `reader` and iterates in input order (lines 9–11); `reading_page` calls it (lines 14–15). At source SHA-256 `8bd75d96a037084637b56b5d10703d1ffbc3ac49771ee3e0d6d8eea57874cc71`, inspection supports preserved reader-filtered order. Inspection date: 2026-10-14; source publication date unknown. Observed: three baseline tests passed on Python 3.14.7. Interpretation: preserving this order is compatible with the proposed grouping; no implemented pin feature, storage durability, scale/performance or production privacy guarantee was demonstrated. R1 answers only the local-source question; no external research or worker was needed.

Authority: inspect, safe checks and retain this trial brief; no application writes/publication. Target source unchanged. Product home: this retained trial brief until the separately requested spec expresses it at `spec.md`. Companions resolved through the explicit repository-source catalog, not installed discovery. Research and Domain Modeling each stopped at their returns; no glossary/ADR applied. No execution ledger workers or assessments: zero launches/calls.

Standalone stop: no spec, ticket, feature or tracker effect is implied by this return. Next action under the separate caller request: inspect this brief and write its specification, reusing R1 and the confirmed decisions.
