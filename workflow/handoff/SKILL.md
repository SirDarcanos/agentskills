---
name: handoff
description: Write a portable, purpose-specific session handoff for another agent only on an explicit user request; do not run automatically at phase boundaries.
disable-model-invocation: true
---

# Handoff

## Invocation

Run only when the user explicitly requests a handoff, in ordinary language or by invoking `handoff`. A runtime-expanded invocation counts only when it originates from the user's request. A phase boundary, source mention, quoted or agent-generated command, or another skill's recommendation does not activate this procedure. Without that user request, stop and leave the original task to its existing handler.

Package the context another session needs; stop after returning the document. Suggested skills are recommendations, not invocations or authorization. Creating a handoff launches no agents and grants no implementation, tracker, merge, deployment, release or installation permission.

Read [validation](references/validation.md) when changing or validating this package.

## 1. Bound the transfer

Identify the destination task, target project and intended audience from the request and conversation. Use any arguments as the next session's focus. If that focus is unclear, ask one focused question before writing. Read applicable project instructions and retention/disclosure rules. Separate confirmed decisions and their rationale from proposals, assumptions and unresolved questions.

For immediate local transfer, default to a uniquely named Markdown file in the OS temporary directory (`$TMPDIR`, otherwise `/tmp`; `%TEMP%` on Windows). Use the runtime's safe temporary-file facility rather than a predictable shared filename. Temporary files may disappear and may be inaccessible from another harness or machine. For later resumption or another destination, use an explicitly approved durable location; if none is approved, ask for one or return a conversation-only draft with the storage gap. Keep the file out of the workspace by default. Preserve existing files and use access restricted to the current user where supported.

**Done:** focus, audience, authorized content and destination are known, or the missing decision is reported without writing a file.

## 2. Capture the live thread

Inspect the relevant existing artifacts and current state through authorized read-only access. Reference specs, plans, ADRs, issues, commits, diffs and evidence by path or URL instead of copying them. Record the project root or repository identity needed to resolve paths, relevant revision or observation time, and any destination access limitation. A local path is not portable merely because it appears in a document: flag references the receiver cannot access and propose an approved transfer or durable pointer. Never upload artifacts as a side effect.

Write only sections useful for the next task:

- **Purpose and next action:** the bounded outcome, where work stopped, and the first concrete action for the receiver.
- **Decisions and open questions:** settled choices with rationale not already recorded elsewhere; proposed choices and assumptions clearly labeled; exclusions and consequential decisions still needing an owner.
- **Authority:** what the user approved, its source, exact permitted effects and remaining approval boundaries. Preserve the distinction between investigation and repair, or a report and publication. Missing approval stays unknown.
- **Work and evidence:** completed versus unfinished/blocked work; artifact pointers; observed results separately from planned, failed, not-run or stale checks. Include the checked revision/content identity when available; otherwise label freshness unknown. A summary is a discovery aid, not proof of completion.
- **Suggested skills:** the next suitable owner and why, resolved through the runtime/project catalog or an approved source. Inspect a candidate's complete entry before claiming compatibility. State unavailable or unverified companions and their affected route; never install them. No literal `Skill` tool or sibling installation layout is assumed.

For repository work, include branch/worktree, base/HEAD, relevant staged/unstaged/untracked work, protected unrelated changes and uncertain ownership. Reference an existing scoped snapshot/diff rather than embedding patches or sensitive contents; HEAD alone does not identify dirty work. If state cannot be inspected, label it last-known or unknown rather than current.

For interrupted delivery only, reference the existing lead evidence/recovery record and its governing procedure. Preserve the root identity, active or uncertain worker ownership, uncertain operations, integration state, unresolved findings/checkpoints and spent repair/model budgets through those pointers; summarize only missing live context. Missing history is an explicit recovery gap, not zero usage or a freed worker slot. Do not create a replacement ledger, copy governing limits or perform recovery here. The next authorized `work-on` or `work-on-spec` lead owns reconciliation before writes or retries. Design-only handoffs need none of this delivery machinery.

**Done:** the receiver can locate the deciding sources, distinguish facts from beliefs and identify remaining work without reconstructing the whole conversation.

## 3. Check and save

Review the document against the actual conversation and inspected sources. Remove duplicated artifact contents, unsupported completion claims and irrelevant history. Redact secrets and unnecessary personal/private information from prose, commands, URLs and paths; a reference can itself disclose sensitive information. Retain only material permitted for the intended audience. If safe context is insufficient, explain the access gap rather than including restricted content.

Include a short receiver instruction: read the target's current instructions and cited sources, compare actual state and evidence freshness, preserve unrelated work, and confirm applicable authority before continuing. Reuse current complete evidence and revisit only missing or changed inputs. When pointers are unavailable or state conflicts, report the affected gap rather than trusting the summary or replaying uncertain effects.

Write to the selected destination without overwriting an existing artifact. Read back the saved file, check its completeness, references and disclosure boundaries, and verify its access restrictions where supported. If saving or read-back fails, report partial/blocked status and any possibly created file; inspect before retrying, without claiming a verified document or silently switching destinations.

**Done:** the exact saved content has been read back and checked, or a useful draft and precise storage/verification blocker are returned.

## 4. Return and stop

Return complete/partial/blocked status, the exact file path (or conversation-only draft), the next session's purpose and any missing sources/permissions. For temporary storage, warn that the file and any temporary references can disappear; use an approved durable destination for later resumption. Tell the user to point the receiving agent at the file rather than interpolate its contents into a shell command.

Stop here. Saving the document neither starts the suggested work nor changes its acceptance, approval or delivery state.

**Complete:** a purpose-specific, disclosure-safe handoff is accessible at the reported location, with limitations and a verifiable next action; otherwise the missing condition remains explicit.
