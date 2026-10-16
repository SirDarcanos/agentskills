# Reconcile existing or partial setup

Run this before editing an existing project or resuming interrupted setup. The current files, remote configuration, and confirmed decisions are the evidence; an earlier success message is not.

## Procedure

1. Map current documents/settings to the [documentation contract](documentation-contract.md). Inspect existing Matt-style `docs/agents/domain.md`, `issue-tracker.md`, and `triage-labels.md` when present. Retain useful mappings and authority; do not install a competing setup framework.
2. Apply the documentation contract's semantic compatibility check against actual responsibilities and effects, not filenames, hashes or template wording. Classify each proposed operation as **already satisfied**, **missing**, **changed decision**, **conflict**, or **unverifiable**, citing the actual source and affected action. A compatible alternative layout is already satisfied; missing common guidance blocks dependent project work, while absent tracker/model/domain detail blocks only that capability.
3. Preserve custom sections, tracker vocabulary, entry-point arrangements, remotes, branches, and organization rules. Inspect symlinks before writing. Treat an existing file as authored material, not proof that it is generated or safe to replace.
4. Present only the necessary delta. Explain changed assumptions and effects. New settings, changed authority, destructive operations, and resolution of conflicting instructions require fresh approval. Unchanged approved operations need no duplicate interview, provided their authorization still applies. A skill upgrade is not approval: preserve explicit restrictions on delegation, assessments, PRs and persistence until their exact delta is approved. Equivalent guidance needs neither regeneration nor a ceremonial setup run.
5. Re-read each affected item immediately before applying its approved delta. If another actor changed it, stop that operation and reconcile instead of overwriting.
6. Apply additive/targeted changes. Keep a short outcome record with observed evidence, not a permanent orchestration database. On failure stop dependent actions and report the exact failed operation; separately approved independent local work may continue.
7. Verify local diffs and remote read-back. Re-run inspection to ensure the new plan has no remaining substantive delta except explicit deferred/blocked items.

**Done:** each approved operation is verified or individually blocked/deferred; the report does not combine partial success into global readiness.

## Failure and rerun rules

- Failed writes can have succeeded remotely. Read back before retrying; use idempotent operations. Never resend blindly after a timeout.
- Audit labels actively rather than preserving GitHub defaults by habit. Use the [tracker procedure](issue-tracker.md) for usage/automation analysis and approved cleanup; unrelated or unapproved labels/edges remain intact. Removing, renaming, reparenting, or deleting requires a specific approved plan.
- For model-policy deltas, follow the [model-use procedure](model-use.md): preserve an authoritative equivalent, rationale and approval provenance; resolve missing/conflicting material facts before permission expands. A pointer repair grants no calls; rerun/resume grants no budget reset or service operations.
- For domain deltas, use the `domain-modeling` companion through the domain handoff. Pass current evidence, prior approvals that still apply, and remaining operations; an unavailable/incompatible companion blocks that route without restarting completed operating-document work.
- Unknown remote state is not “absent.” Permission/API failures are blockers, not evidence that a repository, label, protection, or relationship should be created.
- If local docs describe desired remote controls that could not be enforced, label them pending/blocked. Do not publish them as active enforcement.
- If rollback would discard user work or reverse an already-used remote change, ask; do not automatically undo successful work after a later failure.
- A clean rerun does not regenerate prose, update timestamps for their own sake, repeat settled questions, create another ruleset, duplicate release labels, or rewrite changelog history. A missing old label after an approved migration is already reconciled, not a reason to recreate it.
- A changed project profile does not silently remove protections. Reconcile the consequence and applicable organization policy.
- No domain terms/decisions or remote tracker means no empty glossary, ADR directory or tracker files. Assessment denial is compatible; absence grants no automatic calls. Preserve actual native capability/role facts when tracker work is in scope.
- Confirm glossary maintenance stays in current authorized work, while ADR creation/supersession requires explicit agreement/permission and preserved history. Do not silently revise an accepted record as wording cleanup.
- Keep the documentation contract's transition bridge explicit. Retain live Work On library targets and unique safeguards; mark old diagnosis/PR endpoints not yet migrated. When legacy requirements conflict with the project's selected stages, report that route's incompatibility without automatic ticket/PR publication or installed-copy changes.
- If AGENTS and CLAUDE disagree, identify the conflict and ask for authority unless an applicable higher-level rule resolves it. A pointer or symlink relationship is preserved; nested guidance remains scoped.
