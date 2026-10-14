## Outcome and status

Provide independently usable skills that a technical lead agent can compose to deliver work. The maintainer describes the desired outcome; the lead chooses the engineering approach, performs or delegates the work, verifies it, and explains the consequences in plain language.

This specification records the maintainer's agreed follow-up to #14. It replaces the earlier decision to keep discovery, specification, ticketing, and implementation methods inside `work-on`. The safeguards and useful implementation from #14 should be retained, not rebuilt without reason.

This request authorizes creation of this specification. It does not begin implementation, create its child tickets, change installed skills, grant model-call permission to this repository, or authorize merges or releases. Detailed contracts, migration, and the proposed implementation graph must be presented before implementation begins. Publication alone does not establish implementation readiness.

## Why this change is needed

The delivered `work-on` contains separately readable references, but those references cannot be invoked, installed, or maintained as independent skills. It also combines single-change implementation with multi-ticket coordination. The maintainer wants reusable specialists and a technical lead who selects them without requiring the maintainer to act as the engineer.

Bug investigation should end with an actionable ticket rather than quietly fixing the bug. PRs should explain what merging changes, including test and CI impact, without requiring the reader to understand code diagrams. Optional classification models should be available to agents under an explicit project policy rather than requiring a manual slash command for every consultation.

## Skill ownership

Each listed specialist is independently invocable. It accepts ordinary user input as well as a bounded handoff from another skill, has its own completion criteria, and can stop without starting the entire delivery workflow. Independently usable does not mean dependency-free: required companions and unavailable-companion behavior must be documented and discoverable.

| Skill | Owns | Typical collaboration |
| --- | --- | --- |
| `setup-project` | Project context, working conventions, and the approved model-use policy | Uses `domain-modeling`; retains existing approved GitHub/setup companion boundaries. |
| `shape-work` | Project-manager-oriented discovery: goals, users, scope, priorities, constraints, trade-offs, and success criteria | Uses `analyze`, `research`, and `domain-modeling` as needed. Replaces the grilling responsibility. |
| `write-spec` | Agreed behavior, rationale, exclusions, accepted limitations, and verifiable acceptance criteria | Consumes discovery and analysis without reopening settled decisions. Does not automatically create tickets or build. |
| `write-tickets` | Cohesive decomposition, dependencies, and actual ticket creation after approval | Consumes a spec or a bounded ready investigation; uses native tracker relationships when applicable. The name does not limit it to drafting. |
| `research` | Bounded investigation against authoritative sources | Returns cited findings, relevant versions/dates, uncertainty, options, and recommendations when requested. May run directly or use an authorized background agent. |
| `analyze` | Codebase-informed technical readiness and a recommended method/check strategy | Inspects existing behavior, interfaces, reuse, dependencies, risks, and available evidence; uses other specialists where needed. |
| `domain-modeling` | Shared terms, relationships, context maps, and qualifying architectural decisions | Remains available throughout setup, discovery, analysis, investigation, and delivery. Reading definitions alone does not require a modeling run. |
| `investigate-bug` | Confirming a reported defect, establishing its cause, and producing an implementation-ready ticket | Uses `analyze`/`research` as needed and `write-tickets` to publish or reconcile the ticket. Does not ship the fix. |
| `work-on` | Delivery of one bounded change, including verification, review, repair, and reporting | Our replacement for `implement`; uses the selected method and `review-delivery`. |
| `work-on-spec` | Delivery across a spec's tickets: scheduling, ownership, integration, overall verification, and recovery | Our replacement for `implement-spec`; assigns bounded work to subagents using `work-on`. |
| `review-delivery` | Independent Standards and Spec review of the actual delivered scope | Remains our code-review skill. Do not introduce a competing maintained `code-review` implementation. |
| `pr` | Preparing and opening/updating a PR within project authority, with a plain-language decision report | Reuses current implementation, verification, and review evidence; opening a PR does not authorize merging it. |
| Existing `ask-*` assessment skills | Bounded advisory judgments using their named models | Become model-invocable under approved project policy, while retaining explicit user invocation. No additional mandatory classification wrapper. |

Canonical names are `shape-work`, `write-spec`, `write-tickets`, `investigate-bug`, `work-on`, `work-on-spec`, `review-delivery`, and `tdd`. Do not reintroduce `create-tickets`, `to-spec`, `to-tickets`, `implement`, or `implement-spec` as duplicate procedure owners. Replaced installed skills must be backed up and removed from active discovery through the scoped migration below; a repository merge alone does not perform that migration.

## Technical lead and handoffs

A technical lead is always present when `work-on` or `work-on-spec` runs. This is an accountable role, not a requirement to spawn a separate agent process for a small change.

- With `work-on`, the calling agent owns the change and may implement directly or delegate within runtime/project authority.
- With `work-on-spec`, the calling agent owns the overall delivery. Ticket agents using `work-on` own local decisions within their assignments; shared interfaces, cross-ticket trade-offs, scheduling, and integration remain with the overall lead.
- `analyze` recommends; the lead decides. The maintainer is asked about product commitments, meaningful cost/risk changes, permissions, and unresolved consequential trade-offs, not routine test seams or method choices.
- Calling a skill does not inherently spawn another agent. Delegation needs clear ownership, permitted effects, a bounded lifetime, and inspectable results. The runtime plan must prevent uncontrolled recursive delegation and count workers across the whole run.

Every handoff identifies scope, agreement/acceptance references, protected work, relevant sources and revisions, confirmed decisions, unresolved gaps, authority, and expected results. Returns identify actual outcomes, evidence, changed artifacts, uncertainty, blockers, and the next action.

The receiver checks whether supplied evidence still applies. It fills material gaps rather than repeating discovery, investigation, or analysis. Changed deciding code or contradictory evidence warrants targeted reassessment; an unchanged handoff does not trigger an automatic re-analysis loop.

Each procedure has one authoritative owner. Coordinators discover and consume specialist contracts rather than carrying a second copy. Companion updates must have documented compatibility expectations and must not require editing duplicate procedures in each caller.

## Development methods available in the first delivery

The first delivery must include multiple usable methods, not only TDD with alternatives deferred. The technical lead selects the smallest useful method or sequence from analysis and project requirements.

| Method capability | Initial package name | Required behavior |
| --- | --- | --- |
| Test-first implementation | `tdd` | Red → green → refactor in small behavioral increments. Establish a meaningful failure, implement, and refactor while relevant checks remain green. Refactoring is part of the loop. |
| Prototype-first exploration | `prototype` | Answer a bounded design, UX, or feasibility question through an experiment. Return findings and artifact disposition; a successful prototype is not automatically production-ready implementation. |
| Characterization-first change | `characterize` | Capture relevant existing behavior before changing poorly understood code. Distinguish intended behavior from known defects rather than locking bugs into acceptance criteria. |
| Acceptance-first delivery | `acceptance-first` | Establish observable, executable acceptance examples for a workflow, then implement and verify against them. |
| Small implementation-first increments | `build-and-check` | Implement a bounded increment and immediately run appropriate tests or validation before proceeding. This is not permission to postpone verification until the end. |

`tdd` is the agreed package and invocation name for test-driven development; red–green–refactor is its core procedure, not a separate skill name. Our version includes refactoring in the loop rather than postponing it until review. The other method names are initial recommendations to resolve in the design; their capabilities are in scope now. Inspect existing prototype and testing skills before adaptation and preserve required attribution.

Methods may compose, for example `prototype` followed by `tdd`, or `characterize` followed by `tdd`. The lead explains a consequential method change but does not ask the maintainer to choose a routine technique. Documentation/configuration changes receive appropriate validation rather than forced unit tests. Test counts and coverage percentages are not delivery targets.

## Entry behavior

These are supported paths, not a mandatory pipeline:

- Unresolved idea: `shape-work` → `write-spec` → `write-tickets` when decomposition is useful → `work-on-spec`.
- Clear single change or actionable ticket: `work-on` → selected method → verification and `review-delivery` → `pr` within delivery authority.
- Existing specification with tickets: `work-on-spec` consumes the existing agreement and graph; it does not rediscover the product or rewrite completed analysis.
- Bug observation: `investigate-bug` → actionable ticket. An explicit request to investigate and fix permits a subsequent `work-on` handoff. A request only to investigate stops at the ticket.
- A request to `work-on` to fix a bug without sufficient diagnostic evidence may route to `investigate-bug` first. Once the ticket is ready, delivery consumes it rather than invoking investigation again.
- Partial work: inspect actual state and resume the unmet responsibility while preserving unrelated work, active ownership, and repair history.

`shape-work` explores relevant product branches in manageable rounds. It distinguishes required work, deferred concerns, exclusions, and accepted limitations. It delegates technical fact-finding to the appropriate procedure and translates consequential choices into user, scope, cost, risk, or delivery terms.

## Bug ticket contract

A successful `investigate-bug` result contains enough evidence for `work-on` to start without repeating analysis:

- Confirmed expected and actual behavior, impact, and relevant environment.
- Reproduction steps or a runnable reproduction check, observed results, and any intermittent behavior.
- Established cause, supporting evidence, affected code, and investigated revisions.
- Recommended fix scope, constraints, exclusions, dependencies, and material risks.
- Verifiable acceptance criteria, a regression-check strategy, and recommended implementation method.
- Relevant context/source references and any remaining non-blocking uncertainty.

Check for a matching issue and reconcile it within approved scope instead of creating duplicates. A standalone bug does not need an artificial parent spec or ticket hierarchy.

Diagnostic probes and reproduction harnesses may be created within authorized scope. Preserve useful reproduction evidence and explicitly account for temporary instrumentation; do not leave an unapproved product fix behind. Diagnostic failure is a legitimate outcome: if the bug cannot be confirmed or its cause cannot be established sufficiently, record attempted checks and the blocker, and identify any resulting ticket as investigation work rather than implementation-ready. Do not investigate indefinitely or manufacture certainty to satisfy the ticket contract.

## Project-controlled classification models

Update the existing `ask-jev`, `ask-clef`, `ask-clef-flash`, and `ask-nimble` packages for model invocation. Each model/variant remains separately identifiable and authorized; permission for one does not automatically authorize another. Update frontmatter, in-body gates, references, and validation together.

### Policy home

`setup-project` establishes or reconciles a maintainer-approved policy at `docs/agents/model-use.md`, linked from `AGENTS.md`. If the target already has an authoritative equivalent elsewhere, preserve it and link to it rather than creating conflicting instructions.

The policy records:

- Whether agents may use classification models at all, including an explicit none option.
- Exact permitted skills, models/services, and local or hosted endpoints; availability and authorization are separate facts.
- Permitted purposes and any required escalation conditions.
- Data/disclosure boundaries, including private project evidence and local versus remote processing.
- Call, retry, and spending limits with a defined scope, including how delegated callers share the budget.
- Permission for local service startup and lifecycle responsibilities.
- Allowed fallback behavior and whether model substitution is permitted.
- Decision rationale and approval provenance sufficient for a lead to recognize the applicable agreement.

The technical lead and assessment skill check the applicable policy before an autonomous call. Within its approved bounds, the lead may consult a useful available model without repeatedly asking the maintainer. Missing, ambiguous, conflicting, or exceeded permission blocks the automatic call, not ordinary delivery; the lead continues with normal engineering judgment where sufficient and reports a material evidence gap when it is not.

Explicit user invocation remains supported under its bounded assessment authorization and applicable project restrictions. No silent service/model substitution is allowed. Policy changes require maintainer approval; agents cannot expand permission because a model recommends it.

Setup records the agreement. It does not automatically install/download models, change credentials, start services, or make paid assessment calls. This specification does not itself opt this repository into any calls.

### Judgment limits

Use classifiers only for bounded questions with defined criteria and adequate, current evidence, such as method routing, ticket readiness, or support for an acceptance claim. Preserve insufficient-data outcomes. Compute deterministic facts directly. Returned classifications remain advisory, with the lead accountable for the interpretation and decision.

Models are optional. Do not call every available model, treat agreement as independent verification, replace executed checks/review with a model verdict, or repeatedly ask until receiving the desired answer. Research and code inspection remain the source of facts.

## PR reporting

`pr` presents the same substantive evidence in language a non-technical maintainer can use to decide whether to merge. Lead with user and maintainer consequences; technical diagrams, file trees, raw logs, and implementation details belong in supporting links or an optional expanded section when useful.

The report answers:

1. What changes, for whom, and what stays the same?
2. Why is the change needed, and which issue/agreement does it address?
3. What behavior was checked, what passed or failed, and what remains unverified?
4. How many tests were added, removed, or updated, and what protection changed? Explain meaningful removals. State the counting basis, distinguish moves/renames from actual loss, and disclose unavailable counts rather than guessing.
5. How did CI change? Describe jobs/checks added or removed and measured duration changes, if available. Identify the comparison baseline, sample/context, and distinguish elapsed waiting time from compute usage when relevant. Local test duration alone is not a CI measurement; one noisy run is not proof of a lasting speedup. Say when timing impact was not measured or CI does not exist.
6. What happens after merging? Inspect the actual deployment/release workflow; explain automatic actions, configuration, migrations, required follow-up, affected existing data, and any delayed effects. Do not assume merging deploys.
7. What risks and limitations remain, and can reverting restore the previous behavior? Identify lasting effects and unresolved decisions.

Reuse existing delivery and independent-review evidence, tied to the state being proposed. Reporting may gather missing impact facts but must not silently run costly benchmarks or mutate CI to fill a table. Unknown impact remains explicit. Avoid duplicate sections and omit genuinely inapplicable ceremony without hiding uncertainty.

## Safeguards retained from #14

Preserve context/authority checks, Git preflight, protected unrelated work, native tracker relationships, bounded ownership and repair, revision-aware evidence, integrated verification, independent Standards/Spec review, documentation/changelog duties, and honest completion states.

Independent review includes relevant committed, staged, unstaged, and untracked work. Lead self-review or classifier agreement cannot substitute for reviewer independence. Repairs refresh affected checks and significant-change review. Ticket closure, PR readiness, merge, deployment, and release remain separate states governed by target-project policy.

Reuse existing concurrency and repair bounds unless the revised design explicitly justifies and obtains approval for a change. Extraction must not erase those bounds or reset budgets across parent/child handoffs or resumed work. Preserve the target's tracker label mappings and native parent/blocker rules; publication and role labels do not prove readiness.

## Backup and retirement of replaced installed skills

Delivery includes a dedicated migration ticket to back up and remove installed skills that the new maintained skills replace. This requirement covers renamed replacements and same-name replacements such as `tdd`, `pr`, or `research` when an older installed copy is being replaced. Updating this specification does not execute that migration.

1. Inventory the actual installed copies, aliases, runtime discovery roots, registrations, installation mechanism, symlinks, and local modifications. Produce an explicit old-to-new mapping with exact local targets for approval. Candidate mappings include `implement` → `work-on`, `implement-spec` → `work-on-spec`, `code-review` → `review-delivery`, grilling variants → `shape-work`, `to-spec` → `write-spec`, `to-tickets` → `write-tickets`, and diagnosis variants → `investigate-bug`; names alone do not establish that a particular installed package is safe to retire. Include older setup or same-name packages only when the inventory confirms the replacement.
2. Before removing or overwriting an approved target, make and verify a restorable backup of its complete shipped package and local modifications, not only `SKILL.md`. Record content checksums, source/version where known, original locations, link metadata, and relevant registration/installation metadata. For symlinked packages, preserve both the link information and the in-scope package contents needed to restore the old behavior. Keep backups outside all active discovery roots and outside the public repository; keep machine-specific paths and private content in the local migration record.
3. Stage and validate the replacement and its required companions before retiring the old installation. Verify backup integrity and exercise restoration in an isolated location before destructive changes. If the backup or replacement is incomplete, stop without removing the working old installation.
4. Within the approved migration scope, remove the old active copies, links, aliases, or discovery registrations and activate the replacement. Respect the installation mechanism and shared ownership: removing a runtime symlink must not delete its source repository or a target used elsewhere. Do not remove unrelated skills or independently required companions. Retain the verified backup rather than deleting it during cleanup.
5. Refresh the affected runtime's discovery where supported and verify that the intended replacement resolves, its shipped references/companions are available, and the retired skill no longer appears as a competing active implementation. A replacement with the same name must resolve to the intended new source. If activation fails, restore the backed-up installation within the approved rollback scope, preserve unrelated changes, and report any incomplete recovery.
6. Report what was backed up, replaced, removed from active discovery, preserved, and verified, with local backup/restore instructions. Interrupted migrations must retain enough state to resume safely without deleting or backing up the wrong copy.

Removal means retiring the old active installation, not erasing historical source, attribution, or the recovery backup. The migration ticket must include rollback, same-name replacement, symlink/shared-source, duplicate-discovery, and partial-failure checks. Exact paths and effects require migration approval; no blanket global cleanup is authorized.

## Acceptance criteria

The detailed requirements above are part of these criteria; the IDs support later ticket traceability.

| ID | Checkable outcome |
| --- | --- |
| AC1 — Independent packages | Every specialist and method has a standalone entry point, clear triggers, inputs, outputs, completion/blocking conditions, and portable companion discovery. A standalone invocation stops at its own boundary. Procedure ownership is not duplicated inside coordinators. |
| AC2 — Two delivery scopes | `work-on` delivers one bounded change; `work-on-spec` coordinates multiple tickets using `work-on` agents. Both always have an accountable technical lead, without requiring a separate lead process for direct work. |
| AC3 — Lead decisions | The lead selects methods, checks, and direct/delegated execution within authority. Routine technical decisions do not require maintainer selection. Cross-ticket decisions and integration have one accountable owner. |
| AC4 — Reusable evidence | Current complete analysis/investigation is consumed without repeat calls. A material change triggers only relevant reassessment. Executed scenarios show both reuse and invalidation. |
| AC5 — Discovery and artifacts | `shape-work`, `write-spec`, and `write-tickets` implement their distinct boundaries in plain language. Ticket writing includes actual approved creation and verified native relationships, not just a proposed list. |
| AC6 — Methods now | All five method capabilities ship in the first delivery, are usable independently and by `work-on`, and have executed examples. TDD uses red–green–refactor, including green refactoring; prototype/characterization outcomes and production-readiness limits remain explicit. |
| AC7 — Bug to workable ticket | A confirmed bug yields the complete ticket contract without shipping a fix. A subsequent authorized `work-on` uses the evidence directly. Duplicate, unconfirmed, unresolved-cause, and stale-evidence routes remain honest and bounded. |
| AC8 — Research and domain reuse | Research returns source-backed findings and may execute directly or through authorized background delegation. Domain modeling remains shared across callers. Both reuse prior evidence and preserve their authority boundaries. |
| AC9 — Model-use agreement | Setup proposes, obtains approval for, writes/reconciles, and links the model-use policy, including none, provider-specific permissions, limits, fallback, service lifecycle, rationale, and existing-policy reuse. A rerun does not silently broaden permission. |
| AC10 — Model invocation | All maintained `ask-*` assessment entry points support policy-authorized model invocation and explicit user invocation consistently across frontmatter, procedure, references, and checks. Authorized calls need no repeated approval; missing/denied/exceeded authority causes no automatic call. |
| AC11 — Advisory and optional models | No model is mandatory for ordinary delivery. Unauthorized disclosure, unapproved substitution, implicit installation, uncontrolled retry, and parent/child budget resets are prevented. Classifier output never replaces deterministic facts, checks, or independent review. |
| AC12 — Decision-ready PR | PRs explain behavior, purpose, evidence, test additions/removals/updates, CI impact, post-merge actions, risks, and reversibility in plain language. Measurements and unknowns are distinguishable and traceable to the delivered state. |
| AC13 — Delivery integrity | Native graph checks, safe preflight, bounded workers/repairs, dirty-work review, integrated verification, recovery, and separate completion states continue to work after extraction. A multi-ticket failure/resume scenario demonstrates preservation of ownership and evidence. |
| AC14 — Migration and documentation | Revised design and a superseding ADR explain the new ownership while preserving #14 history. Installation/discovery and companion requirements, public listings, relevant operating policies, examples, validation coverage, and changelog reflect delivered behavior. Installed-copy replacement follows the approved backup and retirement contract in AC16. |
| AC15 — Validation evidence | Record package checks and executed standalone/composed workflow trials separately from paper scenarios. Cover the failure and authorization cases below. No live model call, paid service, or public mutation fixture is implied by a test plan. Unrun material checks remain visible. |
| AC16 — Back up and retire replacements | A dedicated migration ticket inventories and maps the replaced installations, obtains approval for exact targets, verifies complete restorable backups outside active discovery, validates replacements, and removes old active copies/registrations without deleting unrelated or shared source. Evidence demonstrates correct discovery after activation, retained backups, safe rollback, same-name replacement, symlink handling, and interrupted-migration recovery. |

## Required validation coverage

Use safe fixtures and available tools, with explicit authority for any delegated runs or external mutations. At minimum cover:

- Standalone specialist use and isolated package/link/discovery checks, including missing or incompatible companions.
- A small direct change and a spec with multiple `work-on` assignments, integration, failure, and resume.
- All five method capabilities and at least one useful method sequence; no method questionnaire sent to the maintainer.
- Bug investigation stopping at a ticket, investigation-and-fix consuming the same evidence, a duplicate issue, unresolved diagnosis, and changed code invalidating only affected evidence.
- Model policy absent, explicitly disabled, local-only, bounded hosted permission, denied sensitive disclosure, exhausted shared budget, unavailable model, and disallowed fallback. Use mock transports to verify zero forbidden calls and valid response handling; clearly distinguish this from real inference.
- Existing model policy preservation and a setup rerun with no permission expansion or incidental model/service operations.
- Independent review of dirty work, repairs with stale evidence, and a PR reporting both measured and unavailable impact information.
- Test deletion/rename accounting, CI absent or unmeasured, and post-merge behavior that does not include deployment.
- Migration fixtures covering full-package backup/restore, local modifications, same-name replacement, symlinks with shared source, duplicate runtime discovery, invalid backup/replacement blocking removal, activation failure/rollback, and interrupted recovery. Actual installed-skill migration is separately approved and read back; fixture success alone is not evidence that installed copies changed.

Retain reproducible evidence with the actual environment, commands/agent actions, revisions, outcomes, limitations, and acceptance mapping. Static inspection and authored scenarios alone do not establish composed workflow behavior. Live inference requires its own applicable authorization and is not a prerequisite for ordinary offline validation.

## Design and delivery follow-up

The next deliverable is a bounded design and proposed implementation breakdown, not immediate implementation of this entire spec. It must:

1. Map existing `work-on` procedures and installed-source observations to the new owners; identify reusable material and license/attribution requirements.
2. Settle exact method names, minimal handoff/evidence formats, companion compatibility, and where single-change versus cross-ticket verification, repair, and recovery live.
3. Define runtime delegation ownership so `work-on-spec` and its `work-on` agents remain within one bounded execution plan.
4. Reconcile model permission enforcement and fallback semantics across setup, lead workflows, and each `ask-*` package without conflicting gates or duplicate policy homes.
5. Define migration for the narrowed `work-on` entry point and create a dedicated backup-and-retirement work item in the proposed ticket plan. It must implement the installed-skill migration contract above, including exact-target approval, replacement readiness, rollback, and clear unavailable-route behavior.
6. Propose cohesive child tickets with acceptance references and native parent/blocker relationships for approval; do not create a speculative graph as part of this spec-publication task.

The product direction is agreed. Method package names other than `tdd` and the concrete contracts/migration are design work, not permission to omit the agreed capabilities. Do not mark downstream implementation ready before the applicable design decisions and blockers are resolved.

## Exclusions

- A mandatory end-to-end phase sequence, model panel, TDD-only policy, or test-count quota.
- A new orchestration service, generic runtime adapter framework, model gateway, or independent package-versioning system.
- Unscoped or unapproved global skill replacement/removal; the approved-target backup-and-retirement migration described above is in scope. Model installation, credential changes, repository settings changes, paid calls, deployment, merging, and release are not authorized by this specification.
- Changing product commitments or weakening acceptance because a classifier or implementer recommends it.
- Rewriting the historical #14 issue, its completed child tickets, or prior validation evidence to imply these new boundaries were already delivered.

## Documentation impact and provenance

This issue is the authoritative specification; avoid a second independently maintained local copy. The publication task changes no runtime skill, glossary, ADR, repository policy, or installed copy, so it needs no release changelog entry. Implementation must update the affected authoritative documents under AC14 and follow the repository's domain-modeling procedure when superseding the ownership ADR.

Background: #14 and #18; the [previous delivery design](https://github.com/SirDarcanos/agentskills/blob/86b30ef48f2b18fdc65dc977ac36847077467392/docs/design/delivery-workflow.md), [ownership ADR](https://github.com/SirDarcanos/agentskills/blob/86b30ef48f2b18fdc65dc977ac36847077467392/docs/adr/0001-delivery-workflow-ownership.md), and [inventory/provenance](https://github.com/SirDarcanos/agentskills/blob/86b30ef48f2b18fdc65dc977ac36847077467392/docs/design/delivery-workflow-inventory.md). Those records explain the prior design; this follow-up specifies the requested change, not retrospective evidence of implementation.

## Approved implementation ticket plan

The maintainer approved this 25-ticket decomposition and its native parent/blocker graph. This publication records that approval; it does not start implementation or authorize installed-skill changes, model calls, merges, or releases.

All rows are native sub-issues of this specification. Native dependencies remain authoritative; the table is a reader summary. Each ticket has scope, acceptance references, verification, exclusions, and documentation requirements.

| Plan | Ticket | Blocked by |
| --- | --- | --- |
| T1 | #50 — Define the composable skill contracts and migration design | None |
| T2 | #51 — Add approved model-use policy to project setup | #50 |
| T3 | #52 — Allow policy-authorized calls to local assessment skills | #51 |
| T4 | #53 — Allow policy-authorized calls to hosted Jev | #51 |
| T5 | #54 — Add independently usable evidence-backed research | #50 |
| T6 | #55 — Add TDD with a complete red–green–refactor loop | #50 |
| T7 | #56 — Add a bounded prototype-first method | #50 |
| T8 | #57 — Add a characterization-first method | #50 |
| T9 | #58 — Add an acceptance-first delivery method | #50 |
| T10 | #59 — Add an incremental build-and-check method | #50 |
| T11 | #60 — Extract technical analysis and method selection | #54 |
| T12 | #61 — Extract project-oriented work shaping | #60 |
| T13 | #62 — Extract specification writing as an independent skill | #50 |
| T14 | #63 — Extract ticket writing with native dependencies | #50 |
| T15 | #64 — Turn bug investigation into an implementation-ready ticket | #60, #63 |
| T16 | #65 — Adapt independent review to specialist handoffs | #50 |
| T17 | #66 — Add plain-language PR reports with measured impact | #65 |
| T18 | #67 — Refocus work-on on technical-led single-change delivery | #52, #53, #55, #56, #57, #58, #59, #64, #66 |
| T19 | #68 — Add technical-led delivery across specification tickets | #67 |
| T20 | #69 — Prepare and test safe installed-skill migration | #50 |
| T21 | #70 — Exercise discovery through specification and ticket creation | #61, #62, #63 |
| T22 | #71 — Exercise bug-to-fix and direct delivery handoffs | #67 |
| T23 | #72 — Exercise multi-ticket delivery with failure and recovery | #68 |
| T24 | #73 — Finish package discovery and delivery acceptance coverage | #69, #70, #71, #72 |
| T25 | #74 — Back up and retire the replaced installed skills | #73 |

Only #50 is initially labeled `ready-for-agent`. All children carry `enhancement` and `implementation-step`; the parent retains its existing labels. Reassess downstream readiness after accepted design decisions and prerequisite integration, not just issue closure.

#74 performs the real installed-skill migration only after separate approval of exact targets, backups, removal/activation effects, and rollback. #69 prepares and tests the safe procedure first.
