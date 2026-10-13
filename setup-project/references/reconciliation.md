# Reconcile existing or partial setup

Run this before editing an existing project or resuming interrupted setup. The current files, remote configuration, and confirmed decisions are the evidence; an earlier success message is not.

## Procedure

1. Map current documents/settings to the [documentation contract](documentation-contract.md). Inspect existing Matt-style `docs/agents/domain.md`, `issue-tracker.md`, and `triage-labels.md` when present. Retain useful mappings and authority; do not install a competing setup framework.
2. Compare desired approved state with observed state. Classify each proposed operation as **already satisfied**, **missing**, **changed decision**, **conflict**, or **unverifiable**.
3. Preserve custom sections, tracker vocabulary, entry-point arrangements, remotes, branches, and organization rules. Inspect symlinks before writing. Treat an existing file as authored material, not proof that it is generated or safe to replace.
4. Present only the necessary delta. Explain changed assumptions and effects. New settings, changed authority, destructive operations, and resolution of conflicting instructions require fresh approval. Unchanged approved operations need no duplicate interview, provided their authorization still applies.
5. Re-read each affected item immediately before applying its approved delta. If another actor changed it, stop that operation and reconcile instead of overwriting.
6. Apply additive/targeted changes. Keep a short outcome record with observed evidence, not a permanent orchestration database. On failure stop dependent actions and report the exact failed operation; separately approved independent local work may continue.
7. Verify local diffs and remote read-back. Re-run inspection to ensure the new plan has no remaining substantive delta except explicit deferred/blocked items.

**Done:** each approved operation is verified or individually blocked/deferred; the report does not combine partial success into global readiness.

## Failure and rerun rules

- Failed writes can have succeeded remotely. Read back before retrying; use idempotent operations. Never resend blindly after a timeout.
- Preserve unrelated labels/edges. Removing, renaming, reparenting, or deleting requires a specific approved plan. Default to additive reconciliation.
- Unknown remote state is not “absent.” Permission/API failures are blockers, not evidence that a repository, label, protection, or relationship should be created.
- If local docs describe desired remote controls that could not be enforced, label them pending/blocked. Do not publish them as active enforcement.
- If rollback would discard user work or reverse an already-used remote change, ask; do not automatically undo successful work after a later failure.
- A clean rerun does not regenerate prose, update timestamps for their own sake, repeat settled questions, or create another ruleset.
- A changed project profile does not silently remove protections. Reconcile the consequence and applicable organization policy.
- If AGENTS and CLAUDE disagree, identify the conflict and ask for authority unless an applicable higher-level rule resolves it. A pointer or symlink relationship is preserved; nested guidance remains scoped.
