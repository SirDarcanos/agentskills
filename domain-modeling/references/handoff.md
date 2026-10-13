# Domain handoff contract

Read when another workflow invokes domain modeling. A caller may follow this skill directly in the same agent; delegation is optional and requires its own authorization. The caller locates and reads the complete SKILL.md and relevant references through runtime discovery, not a fixed installation path.

## Inputs

The caller supplies, or identifies as unknown:

- Target project/directory and the bounded terms, relationships, contexts, or decisions to examine.
- Inspected evidence and authoritative document mapping, including relevant specs/code, glossary/context map, ADRs, and documentation maintenance policy.
- Confirmed decisions and their source/authority, unresolved questions, proposals, and intentional deferrals.
- **Plan-only** or **approved** mode; for approved mode, exact permitted files/sections and operations, approval evidence, and exclusions.
- Constraints, collaboration preference, known capability limits, and any concurrent or unfinished work to preserve.

Missing approval defaults to plan-only. Missing material evidence remains unknown, not permission to invent it. Verify supplied facts for freshness without repeating resolved interviews. Return consequential gaps to the caller, which owns the larger approval conversation.

## Ownership

Domain modeling owns vocabulary, domain relationships/context maps, and selective ADR creation/supersession. The caller owns its broader scope, product commitments, operating profile, permissions, entry-point integration, and acceptance of results. The project's existing documentation policy owns document locations and maintenance assignments; this skill supplies domain procedures, not a competing operating contract.

## Return contract

Return a compact record containing:

- Target, scope, and mode.
- Evidence inspected and confirmed decisions reused; unresolved or newly changed decisions.
- In plan-only mode: exact proposed file/section deltas, preserved content, required approvals, and blockers. No writes occurred.
- In approved mode: actual outcomes per authorized operation, affected paths, verification evidence, and any partial/failed writes.
- Records intentionally omitted and why; remaining conflicts, code/document mismatches, and unverified/deferred items.
- Required read/update pointers for caller-owned entry points and the smallest next action.

The caller checks these outputs against its plan and inspects the resulting documents. It must not infer full completion from an unsupported success summary. Domain work requiring new authority returns to the caller before execution.
