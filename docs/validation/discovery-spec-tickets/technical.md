# Analyze return and lead decision

**Complete bounded fixture readiness**, not production readiness or implementation permission. Agreement: [spec P1–P3](spec.md). Direct handoff from the caller: inspect only the unchanged reading-list baseline, R1 source support, planned state/presentation boundary and baseline assertions; return a method/check/decomposition recommendation. Protect source bytes; no feature edits or probes.

## Inspected findings and deciding inputs

R1 is current at SHA-256 `8bd75d96a037084637b56b5d10703d1ffbc3ac49771ee3e0d6d8eea57874cc71`; the caller and tests are in the same [source](../shape-work/reading_list.py). `visible_books` owns reader filtering/order; `reading_page` consumes it. Records have reader/title only, no stable book ID or pin state. The three baseline tests cover input order, privacy and empty lists, not pinning. Python 3.14.7; baseline passed. The fixture has no storage/API/UI implementation: durability across sessions and production authorization cannot be inferred. They are outside this in-memory trial, not silently claimed supported.

Smallest adequate recommendation: keep pin/unpin selection and grouped presentation with one owner. For an implementation of this synthetic interface, add stable fixture book identities and per-reader selection state, preserve the current reader filter, and present stable pinned/ordinary groups. Removing a selection restores normal position; do not physically move or duplicate source entries. Reject an attempt to select another reader's book without revealing its content or modifying either selection set. This is a planned design within P3, not observed feature behavior. No new framework, repository setup or model service is needed.

| Risk / acceptance | Coverage and needed check |
| --- | --- |
| P1 group/order, multiple selections | Existing input-order assertion protects the baseline; new pin/group examples required. |
| P2 undo/loss/empty | Existing empty check reused; new round-trip and duplicate-selection examples required. |
| P3 access/isolation | Existing other-reader visibility check reused; new cross-reader pin attempt and unchanged-other-state checks required. |

No pin acceptance checks have run. Lead chooses TDD for the cohesive state/presentation change: clear behavioral increments with a callable seam, sensitive order/undo/privacy checks. Catalog candidate `tdd/SKILL.md` was read completely: bounded standalone/handoff inputs, meaningful red, green, green refactor and local-evidence stop are compatible. No method is executed by this shaping trial. No technical-method questionnaire was sent to the fixture owner.

## Domain and documentation disposition

Reuse the confirmed pin meaning and Domain Modeling's plan-only return from [brief](brief.md). No enduring architectural choice or new bounded context warrants an ADR/context map. No target glossary write is authorized; leave the plan unapplied rather than treating the caller's approval of behavior as document-write authority. Repository CONTEXT/ADRs and public skill behavior are unchanged.

## Decomposition and freshness

PIN owns all coupled pin/unpin/filter/presentation state and checks. VERIFY is a genuinely separate bounded acceptance-validation deliverable consuming PIN's integrated behavior, not a split by file count. No parallel writer or worker assignment is implied. Spec remains the parent, not another implementation unit. Exact titles/bodies/roles/graph are proposed in `tickets.json` and approved only for the disposable tracker by the input fixture.

At Write Spec/Write Tickets handoff, re-read the brief/spec and compare source identity. Current agreement and R1 require no new discovery, Research or full Analyze run. The stale variant later changes only a disposable caller copy; its output-shape finding/check is invalidated while reader-filter service support, pin intent and P1–P3 remain current. That variant blocks relying on old caller compatibility, not the unchanged main trial.

Standalone stop: return this recommendation. Caller inspects support and selects TDD for future PIN work, but this trial ends at ticket graph read-back. No implementation, review acceptance, scheduling or production readiness is claimed.
