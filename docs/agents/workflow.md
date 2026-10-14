# Repository workflow

## Authority

The maintainer approves implementation scope and consequential changes. Agents make routine engineering decisions within that scope, investigate discoverable facts, and bring recommendations rather than internal design questionnaires.

| Action | Authority |
| --- | --- |
| Read repository evidence; make scoped file edits; run safe local checks | Within the approved task and applicable instructions. |
| Create a short-lived branch, commit scoped changes, push that branch, and open/update its PR | Allowed after implementation scope is approved. |
| Merge a PR; create release tags; publish a release | Explicit maintainer approval for that action. A previous merge approval does not authorize later merges. |
| Install or replace tools/skills/models; change credentials; deploy; spend money; perform external assessments or sensitive disclosure | Explicit approval for the specific action and scope. |
| Change repository settings, permissions, labels, or native issue relationships; perform destructive operations | Include the exact changes in an approved task or plan. |
| Delegate work or invoke an optional assessment | Respect runtime authorization and the invoked skill's consent requirements; no standing delegation permission is granted here. |

For model assessments, consult the policy linked from AGENTS.md when one has been separately approved. An approved policy may authorize exact bounded autonomous consultations only when the assessment package and runtime support that gate; explicit named assessment requests remain subject to project restrictions and package bounds. The lead checks policy fit and reserves shared allowance, and the assessment owner rechecks immediately before sending. Policy establishment through setup performs no calls or service actions. This repository has no separately approved model-use policy: model calls remain disabled until such approval; this task does not opt it in.

Unknown permission remains ungranted. A configured credential, available tool, or documentation preference does not authorize its use. Explicit-invocation-only skills keep their own invocation gates.

## Branches and pull requests

Use short-lived branches from current `main`; there is no integration branch. Inspect the working tree and existing PR first. Start a new branch after the previous branch's PR has merged or closed, and preserve unrelated work.

The agreed `main` ruleset, `main-pull-request-workflow`, requires PRs and prevents branch deletion and force pushes. It has no bypass actors, required approving reviews, or required status checks. This supports a single maintainer without requiring self-approval or a second reviewer. Inspect the [live rules](https://github.com/SirDarcanos/agentskills/settings/rules) before changing protections; documented policy does not establish enforcement by itself.

Follow the PR scope and reporting requirements in [AGENTS.md](../../AGENTS.md). Push the reviewed changes to the feature branch and make the PR available for the maintainer to inspect. Stop before merging unless that specific merge is approved. Approval for repository-local changes does not update globally installed copies of skills.

## Verification and completion

Follow the per-skill validation requirements in [AGENTS.md](../../AGENTS.md) and the changed skill's own validation/testing reference. The repository has no shared build or test command and currently no GitHub Actions workflows. Discover relevant commands from the affected package rather than inventing a universal suite.

Choose checks for the meaningful failure modes of the change. Extend existing coverage when sufficient; avoid test quotas, mandatory model voting, or blanket test-first requirements. Preserve checks that protect authorization, disclosure, destructive behavior, persistence, or public contracts.

For documentation-only changes, inspect the actual policy and Markdown, resolve relative links, preserve symlinks and history, and check the diff for private data and nonportable paths. Code or script changes also need relevant executable checks. Run read-only remote verification when settings or tracker state change; do not attempt a destructive operation just to test a protection.

Review the actual integrated diff against scope and repository instructions before reporting completion. Independent review can be used when authorized and useful; it is not a mandatory second-maintainer sign-off. Distinguish direct review, independent review, offline tests, agent walkthroughs, and live checks. Authored scenarios are not executed evidence. Report unresolved findings and unrun checks rather than presenting partial work as verified.

## Changelog and releases

[CHANGELOG.md](../../CHANGELOG.md) is the manually maintained, repository-wide release history, using Keep a Changelog and Semantic Versioning. Individual skill packages are installable independently but currently have no separate version sources. Git tags and [GitHub releases](https://github.com/SirDarcanos/agentskills/releases) identify published releases; an `Unreleased` entry is not a publication.

For a notable change to a skill's public behavior, installation contract, or supporting tool, add a concise `Unreleased` entry with known related issue/PR links. Internal maintenance or operating-document changes may need no entry; record the reason in completion evidence. Preserve released sections. This repository has no changelog generator or release automation to invoke.

Classify delivered PR impact using the [release labels](triage-labels.md). A backward-compatible fix is patch, compatible new functionality is minor, and an incompatible public interface or behavior change is major. Routine documentation-only work may have no impact label. Resolve one label to the highest required impact when a PR has multiple release-relevant changes; classify from behavior, not the commit prefix alone.

Release preparation assesses all changes since the last published version and requires explicit approval for the target version, tag, and publication. Do not automatically release after a merge or create retrospective tags for changelog headings. Establish any new prerelease or independently versioned-package policy before using it.

## Documentation ownership

Update the authoritative home when an approved change alters its facts; keep proposals distinct from accepted decisions.

| Change | Owner and authoritative home |
| --- | --- |
| Domain meaning or relationship | Discovering/changing phase: follow [domain-modeling](../../domain-modeling/SKILL.md) to maintain [CONTEXT.md](../../CONTEXT.md). Reuse confirmed decisions and the current document mapping. |
| Qualifying enduring architectural decision | Analysis/implementation: use the same specialist to create or supersede a relevant ADR, preserving rationale and links. Default home is `docs/adr/`, created only for an actual record. |
| Purpose, maintenance context, or operating constraint | Lead/maintainer: reconcile [project context](project.md) with appropriate approval. |
| Authority, verification, delivery, or release convention | Lead/change owner: update this document and reconcile any affected configuration through an approved plan. |
| Model-use permission | Lead/setup: maintain the separately approved policy home linked from AGENTS.md, preserving shared budgets, disclosure, lifecycle, fallback and provenance; no default opt-in. |
| Tracker capabilities, relationships, or completion rules | Ticketing/change owner: maintain [tracker guidance](issue-tracker.md) and read back approved native changes. |
| Label vocabulary or application rule | Tracker/change owner: maintain [label guidance](triage-labels.md), actual labels, and affected assignments together. |
| Product commitments | Delivery lead: update the authoritative spec with maintainer approval; setup does not invent a backlog. |
| Notable public change | Implementer: maintain the changelog under the release policy above. |

Read domain definitions when relevant; changing them or an ADR uses the specialist's scoped plan-only/approved workflow. This repository ships that procedure, so follow its local entry point rather than a conflicting older installed copy. Keep operating preferences out of the glossary.

Before completion, list affected documents and updates or justify no documentation change. Resolve code/document conflicts through evidence and decision authority; neither code nor an old summary silently overrides an accepted decision. A clean rerun inspects and proposes only changed facts, not cosmetic regeneration.
