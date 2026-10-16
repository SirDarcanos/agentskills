# Handoff

Carry the context for one piece of work into another session, harness or directory. Start at [SKILL.md](SKILL.md).

```text
/handoff Continue investigating why cancelling a booking does not free a place.
```

You can also ask for a handoff in ordinary language. This skill requires an explicit request; it does not create files automatically at phase boundaries. Use your agent's built-in compaction when you only need to shorten the current conversation.

The document keeps the next task, relevant decisions and rationale, unresolved questions, approval boundaries and suggested skills. Existing specs, tickets and evidence remain at their authoritative locations and are referenced rather than copied. For interrupted delivery, it points to existing recovery records and captures necessary live context when no saved record exists. Missing history stays unknown; the next lead inspects actual state without resetting ownership or budgets. Shaping transfers need no delivery ledger. It does not start the next task.

## Storage and transfer

Immediate local transfers use a unique file in your OS temporary directory, outside the workspace by default. The agent returns its exact path. Temporary files can disappear or be inaccessible to another harness; for later resumption, supply an approved durable destination. When that destination is missing, the agent asks or returns a conversation-only draft with the storage gap rather than committing session notes or uploading private artifacts. Ordinary work does not need a handoff or hypothetical future destination to finish.

Tell the next agent to read the file, inspect the cited sources and current project instructions, and confirm state and permissions before continuing. Avoid inserting the document's contents into a shell command. References to local files may need a separately approved transfer when moving machines.

## Requirements and limits

Copy the complete directory, including [LICENSE](LICENSE) and [validation guidance](references/validation.md), into your agent's skill discovery path. The runtime needs file inspection and safe file creation/read-back; repository-state inspection also needs Git where applicable. Slash-command and frontmatter support varies: the explicit-request boundary in the procedure still applies.

No companion is required to write a handoff. Suggested skills are discovered and checked when available; unavailable companions are reported, not installed. Delivery recovery belongs to the existing `work-on` or `work-on-spec` lead, not this skill. The receiver cannot assume access to the old conversation or infer task permission from a handoff request. A summary is not verification, user approval, or a guarantee that another agent will continue correctly.

## Provenance

Adapted from [Matt Pocock's handoff skill at revision `49dd158`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/handoff/SKILL.md): purpose-specific transfer, temporary storage, artifact references, sensitive-data redaction and suggested skills. This adaptation adds our authority, evidence and interrupted-delivery boundaries, runtime-neutral discovery and an approved durable-storage route. Matt Pocock's MIT notice is retained alongside Nicola Mustone's notice in [LICENSE](LICENSE).
