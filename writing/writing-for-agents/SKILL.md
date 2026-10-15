---
name: writing-for-agents
description: Write or revise agent-facing skills, instruction files such as AGENTS.md or CLAUDE.md, and guides reached through their references. Use when authoring or reviewing instructions that agents consume; preserve established meaning and authority while making actions, routing and completion checkable.
---

# Writing for agents

Make instructions usable at the point where an agent needs them.

## Invocation

Load this skill when creating, editing, or reviewing skills, agent instruction files, or referenced agent-facing documentation, including plain guides outside a skill package. No explicit invocation is required. Apply it within the existing task's authority; reviewing alone does not authorize edits.

## 1. Establish the writing boundary

Read the complete affected document, applicable project instructions and the authoritative sources for its facts, terms and permissions. Identify the intended reader, task, requested mode, owned files and what must remain unchanged. Inspect incoming pointers and relevant callers so a local edit does not silently change when another workflow runs.

Preserve established actors, actions, scope, requirement strength, exceptions, uncertainty and approval gates. A writing request is not authority to add policy, change product meaning, execute the documented workflow or update installed copies. If sources conflict or a consequential commitment is missing, keep the affected meaning unchanged and report the exact decision needed; continue independent safe writing.

**Complete when:** the purpose, sources, allowed edits and protected meaning are identified, with consequential gaps separated from routine wording choices.

## 2. Organize around decisions and actions

Read [structure guidance](references/structure.md) when choosing pointers, splitting detail, or changing a skill's routing/frontmatter.

1. Put shared instructions in one authoritative home. Replace duplicates with pointers to that home without dropping unique exceptions or context. Respect existing ownership; if moving a rule needs approval, propose the move instead of creating a second authority.
2. Keep actions needed on every path in the main procedure. Put branch-specific or lengthy detail behind references whose wording states what the target contains and when to read it.
3. Write procedures as ordered actions. State inputs or preconditions where needed, observable completion criteria, and what happens on failure or unavailable evidence. Reference-only material can remain definitions or rules rather than a fabricated sequence.
4. Keep each definition beside its rules and caveats. Remove repetition and irrelevant exposition while preserving rationale needed for a decision.

**Complete when:** each procedure has an order and a checkable end, each required branch has a clear pointer, and each shared instruction has one identified owner.

## 3. Draft or revise within authority

Use concrete actors and verbs; name the artifact, decision or observation that proves completion. Prefer supported positive directions while keeping explicit safety boundaries. Replace vague commands such as “understand the system” with the evidence the next action requires. Verify discoverable commands, file layout and configuration rather than copying stale facts into prose.

Write directly by default. Optional companions may be invoked only when they are relevant, discoverable, compatible and demonstrably shipped by `SirDarcanos/agentskills`; this restriction travels with a copied package. Establish provenance from the project source/package metadata or a verified source revision, not the installed skill's name or proximity. Read the full candidate entry and applicable references before invoking it, and retain its own invocation, companion and permission gates. Any further companion invocation must satisfy this same project-shipped boundary. A relevant project-shipped prose editor can help with human-facing wording; it cannot decide agent workflow semantics or grant new authority.

An external installed documentation skill is not a fallback. When provenance is unknown, no suitable companion exists, or a helper cannot operate within this boundary, handle the writing directly and report any remaining specialist gap. Do not install helpers or expand task effects.

**Complete when:** the draft matches the requested mode, preserves the source commitments and facts, and uses only permitted companions or direct writing.

## 4. Validate the affected paths

Follow [validation](references/validation.md) before returning any written or reviewed result. Check the actual affected files and incoming pointers, not only the intended diff. In a review, report defects without silently rewriting them. In an edit, correct authorized writing defects and recheck affected paths; permission or meaning changes return to their owner.

**Complete when:** affected links and anchors, applicable frontmatter/routing, rendered structure and named-environment instructions have inspected results or explicit verification gaps. The return identifies changed files or findings, preserved meaning, checks performed, unrun checks and the smallest next action. Authored examples and static checks remain distinct from executed agent behavior.
