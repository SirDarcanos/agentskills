# Handoff validation evidence

Agreement: [#102](https://github.com/SirDarcanos/agentskills/issues/102), AC1–AC8. Comparison base: `a146427065c43e6b385bc799b50e78a14d444c60`. Scope: `workflow/handoff/`, root README and changelog, and this evidence note. No delivery ownership, domain meaning or ADR changes are made.

## Checks performed

- Python 3 structural assertions checked the entry's name, explicit-invocation flag, four ordered steps and key boundaries.
- A disposable full-package copy passed local Markdown link resolution and retained both MIT copyright notices, without sibling packages.
- Local links and fenced-block balance were checked across the entry, package README, validation guidance, root README and changelog. `git diff --check` passed.
- A local Python storage-primitive trial on macOS created a unique temporary Markdown file, verified current-user-only POSIX permissions and exact read-back, demonstrated exclusive-create refusal to overwrite it, and removed only its own disposable directory. This checks available host primitives, not an agent's adherence to the skill or Windows behavior.
- Direct inspection checked the Markdown structure, frontmatter, prose, artifact-reference strategy, authority boundaries, source attribution and absence of author-local paths or private data. No Markdown rendering engine or browser trial was run.

## Static walkthroughs

These are executed **instruction walkthroughs**, not live agent trials or generated production handoffs. Each case was traced against the entry; the listed disposition is supported by the cited step. They do not establish reliable model behavior.

| Case | Source and observed instruction disposition | Acceptance |
| --- | --- | --- |
| Phase boundary without a request | Entry gate requires explicit request; step 4 stops after document return. | AC1 |
| Design-only transfer with an existing spec | Step 2 references the spec, retains missing rationale/questions and omits delivery machinery. | AC2 |
| Investigation-only approval | Authority section preserves the investigation/repair distinction; recommendations confer no effects. | AC3 |
| Dirty source changed after a passing check | Step 2 records checked identity and staged/unstaged/untracked state or unknown freshness; step 3 directs current-state comparison. | AC4 |
| Interrupted delivery, uncertain writer and push | Step 2 points to original root/recovery records and spent budgets; missing history stays unknown; reconciliation belongs to the receiver's authorized lead. | AC5 |
| Next skill absent | Step 2 requires discovery/entry inspection before compatibility claims, reports unavailable routes and grants no installation or invocation. | AC6 |
| Sensitive credential or private URL in context | Step 3 checks prose, commands, URLs and paths; restricted material is omitted with any resulting gap reported. | AC7 |
| Immediate local transfer | Steps 1, 3 and 4 require unique restricted-access temporary storage, no overwrite, read-back, exact path and expiry/access warning. | AC7 |
| Later transfer without approved destination | Step 1 asks or returns a conversation-only draft; no silent workspace write or upload. | AC7 |
| Approved durable destination, local-only reference | Steps 1–3 permit approved storage and require checking reference accessibility, flagging transfer gaps without upload. | AC7 |
| Failed read-back or unavailable source | Steps 2–4 preserve partial/blocked status, identify possibly created files and require inspection before retry. | AC4, AC7 |
| Independent installation | Full-package copy/link/license checks above; README and changelog expose the new skill with upstream provenance. | AC8 |

## Limits and documentation disposition

No live receiving-agent continuation, cross-machine transfer, Windows storage, denied-filesystem trial, model assessment or installation command was run. Static inspection and host primitive checks do not prove runtime invocation support, secret detection, reliable permission enforcement by an agent, or recovery correctness in a consumer project. Independent review is recorded separately in the delivery/PR evidence rather than treated as an executed skill trial.

Updated authoritative public homes: the new package, root README and `CHANGELOG.md` under Unreleased. Existing delivery/recovery contracts and repository policies remain unchanged: this skill references their owners rather than moving or duplicating their procedures. New backward-compatible functionality is a minor release impact; no release is published.
