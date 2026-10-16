---
name: domain-modeling
description: Establish or revise domain terms, relationships, context maps, and architectural decision records during discovery, design, or implementation. Use for terminology conflicts, glossary changes, ADR creation or supersession, or a domain handoff from another skill; reading existing definitions alone does not require this workflow.
---

# Domain modeling

Own the project's domain vocabulary and decision records, whether invoked directly or by another workflow. Keep operating context, collaboration preferences, and permissions in their existing project/workflow documents. Modeling does not authorize application changes or a broader architecture redesign.

Use normal file-reading and editing tools; no specific SDK, literal Skill tool, subagent, or model service is required. Loading this skill grants no mutation permission.

## 1. Establish scope and authority

Check applicable project instructions and the actual agreement once per context, reusing already-read guidance and following relevant context/authority pointers and directory/runtime restrictions. Compare decision/effect authority, safety, verification, documentation and continuation guidance with this work. Equivalent existing layouts need no Setup provenance or template. Identify specific absent, conflicting or unverifiable guidance and recommend explicit setup/reconciliation without invoking it or rewriting policy. Missing common guidance blocks dependent project modeling; missing optional tracker/model detail blocks only that capability. Do not create empty domain records to satisfy prerequisites.

For a caller handoff, read [the handoff contract](references/handoff.md) before proceeding. For direct use, establish the same inputs from the request and project instructions: target, affected subject, evidence, document homes, decision authority, exclusions, and **plan-only** or **approved** mode. Confirmed glossary/context-map maintenance can use the current task and project agreement's existing authorization; do not demand repeated approval of that unchanged delta. ADR creation or change requires explicit user agreement and permission, including proposed drafts. If mutation authority is unclear, use plan-only and ask only for the missing authorization.

Read applicable instructions, the project's documentation ownership policy, existing glossary/context map, relevant ADRs and specs, and code using the affected concepts. Inspect current work and symlinks before choosing edit targets. Reuse valid document homes and confirmed decisions; a caller's mapping takes precedence over default paths unless it conflicts with existing authority, in which case return the conflict.

**Done:** the bounded subject, authoritative sources, current state, mode, and allowed writes are known; missing evidence or authority is explicit.

## 2. Resolve the model

When terms, relationships, or context boundaries need work, read [vocabulary and context maps](references/vocabulary.md). When an architectural choice needs recording or reconsideration, read [decision records](references/decisions.md). Apply only the relevant branch; neither a glossary nor an ADR is mandatory output.

Compare prior findings with deciding sources, confirmed meanings, affected code and relevant dirty state; reuse current evidence, refresh only changed or contradicted claims and preserve unaffected findings. A new phase alone does not require re-analysis. Reuse prior answers. Inspect discoverable facts and ask focused questions only about unresolved meanings or consequential choices. Explain choices through product behavior and operational effects, adapting to the documented collaboration preference. Keep confirmed decisions, proposals, contradictions, and deferred concerns distinct.

**Done:** every affected meaning or decision has supporting evidence and a disposition: confirmed, proposed, deferred, or blocked. No unresolved proposal has become an accepted fact.

## 3. Plan or apply the delta

Identify exact files/sections, proposed content changes, affected references, and preserved material. In plan-only mode, return this delta and the required decisions without writing files, including draft artifacts. The caller can incorporate it into a larger approval plan.

In approved mode, verify that each delta fits the supplied authorization and re-read affected state before writing. Changed facts or scope go back to the caller or decision-maker. Record confirmed decisions promptly within that scope; do not re-interview or request approval again for an unchanged authorized edit.

Apply targeted updates using the relevant branch procedure. Preserve authored content and historical rationale. Keep credentials, private personal profiles, and unnecessary sensitive source details out of shared records. Keep unresolved glossary meanings out of the confirmed glossary; proposed ADRs may be written only when that draft is in scope. Code/document mismatches are findings, not permission to rename code or change behavior.

If a write fails or is interrupted, inspect actual files before retrying, stop dependent writes, and report partial results. Preserve successful and unrelated work rather than rolling it back automatically.

**Done:** either a mutation-free plan has been returned, or each approved delta has an actual outcome with remaining work explicit.

## 4. Verify and return

Read affected documents and compare them with the confirmed decisions, sources, and approved scope. Check terminology within each context, preserved context boundaries and history, and every changed link. Confirm that relevant future work can discover the records without loading every ADR. Return pointer changes to the caller when the caller owns the entry point; do not expand the write scope to add them yourself.

Reinspect for a rerun: unchanged evidence should yield no substantive delta, duplicate record, or cosmetic rewrite. Return changes or proposed changes, evidence, preserved/omitted records, conflicts and code mismatches, unverified items, and the next required decision. Justify no documentation change when appropriate. The discovering/changing phase remains accountable for maintaining the affected records and reporting documentation impact. Authorized authoritative record maintenance is part of this work, not optional handoff storage. Plans and complete findings may remain in conversation; persist a separate report only to a user-selected destination. Offer useful next steps without invoking application work or another stage.

**Done:** each scoped item is verified, intentionally omitted, deferred, or blocked. A plan is not an applied change; link checks are not proof of semantic correctness. When maintaining this package, use [validation](references/validation.md).
