# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Breaking changes

- Require existing project guidance for project-oriented writing, `ask-jev`, `ask-nimble` and `build-with-nimble`; non-project supplied-text writing and named assessments remain available without setup, and model permissions stay unchanged. ([#141](https://github.com/SirDarcanos/agentskills/issues/141))
- Require meaningful project guidance before `implementation-preflight` branch writes; safe inspection remains available, and explicit branch policy takes precedence over incidental integration-branch names. ([#136](https://github.com/SirDarcanos/agentskills/issues/136))

### Added

- Add `what-now` for explicitly requested, installed-skill recommendations that respect project rules and stop before workflow execution. ([#112](https://github.com/SirDarcanos/agentskills/issues/112), [#142](https://github.com/SirDarcanos/agentskills/issues/142))
- Add `writing-for-agents` for project-guided or standalone supplied-text instruction writing, preserving meaning and authority with project-shipped companions only. ([#111](https://github.com/SirDarcanos/agentskills/issues/111), [#141](https://github.com/SirDarcanos/agentskills/issues/141))
- Add `resolve-merge-conflicts` for project-agreement-aware merge/rebase resolution, protected unrelated work, relevant checks and decision pauses for unsafe continuation. ([#110](https://github.com/SirDarcanos/agentskills/issues/110), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add `handoff` for user-selected, purpose-specific session transfers with approved storage, receiving-task authority and preserved unknown history, ownership and budgets. ([#102](https://github.com/SirDarcanos/agentskills/issues/102), [#140](https://github.com/SirDarcanos/agentskills/issues/140))

- Add `work-on-spec` for project-guided rolling ticket coordination, native eligibility, serial integration and aggregate verification/review/recovery, ending before user-selected PR work or persistence. ([#68](https://github.com/SirDarcanos/agentskills/issues/68), [#127](https://github.com/SirDarcanos/agentskills/issues/127), [#130](https://github.com/SirDarcanos/agentskills/issues/130), [#140](https://github.com/SirDarcanos/agentskills/issues/140))
- Add standalone `pr` for user-selected, project-guided PR reporting/publication that reuses current delivery evidence, with concise summaries, visible blockers and impact accounting. ([#66](https://github.com/SirDarcanos/agentskills/issues/66), [#125](https://github.com/SirDarcanos/agentskills/issues/125), [#127](https://github.com/SirDarcanos/agentskills/issues/127), [#139](https://github.com/SirDarcanos/agentskills/issues/139))
- Add standalone `investigate-bug` for bounded diagnosis that can finish in conversation without a ticket, with explicit investigation gaps and user-selected ticket or fix continuations. ([#64](https://github.com/SirDarcanos/agentskills/issues/64), [#122](https://github.com/SirDarcanos/agentskills/issues/122), [#138](https://github.com/SirDarcanos/agentskills/issues/138))
- Add standalone `write-tickets` for project-guided decomposition and selected publication, exact native relationship authority and linked ticket summaries without duplicate wording approval. ([#63](https://github.com/SirDarcanos/agentskills/issues/63), [#117](https://github.com/SirDarcanos/agentskills/issues/117), [#137](https://github.com/SirDarcanos/agentskills/issues/137))
- Add standalone `write-spec` for project-guided agreed behavior, stable acceptance IDs and configured publication with concise linked returns, explicit draft overrides and separate readiness. ([#62](https://github.com/SirDarcanos/agentskills/issues/62), [#137](https://github.com/SirDarcanos/agentskills/issues/137))
- Add standalone `shape-work` for project-guided discovery ending with a confirmed plan, current analysis reuse and preserved concern dispositions, without mandatory artifacts or automatic stage transitions. ([#61](https://github.com/SirDarcanos/agentskills/issues/61), [#121](https://github.com/SirDarcanos/agentskills/issues/121), [#137](https://github.com/SirDarcanos/agentskills/issues/137))
- Add standalone `analyze` for project-agreement-aware readiness, current evidence reuse and lead-owned method/check recommendations, with conversation-only findings and conditionally loaded domain/delegation detail. ([#60](https://github.com/SirDarcanos/agentskills/issues/60), [#117](https://github.com/SirDarcanos/agentskills/issues/117), [#135](https://github.com/SirDarcanos/agentskills/issues/135), [#155](https://github.com/SirDarcanos/agentskills/issues/155))
- Add standalone `build-and-check` for project-guided implementation-first increments with immediate validation, coverage reuse and lightweight local evidence. ([#59](https://github.com/SirDarcanos/agentskills/issues/59), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add standalone `acceptance-first` for project-guided executable workflow examples, checked increments and criterion-level evidence. ([#58](https://github.com/SirDarcanos/agentskills/issues/58), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add standalone `characterize` for project-guided legacy protection with baseline provenance, sensitivity and explicit unknown/defect limits. ([#57](https://github.com/SirDarcanos/agentskills/issues/57), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add standalone `prototype` for project-guided bounded experiments, recommendations and authority-safe artifact disposition without claiming production readiness. ([#56](https://github.com/SirDarcanos/agentskills/issues/56), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add standalone `tdd` for project-guided behavioral red–green–refactor, independent oracles and reusable coverage. ([#55](https://github.com/SirDarcanos/agentskills/issues/55), [#136](https://github.com/SirDarcanos/agentskills/issues/136))
- Add independently usable `research` with cited, version-aware findings, project or non-project prerequisites, conversation-first results and optional authorized conditional delegation. ([#54](https://github.com/SirDarcanos/agentskills/issues/54), [#135](https://github.com/SirDarcanos/agentskills/issues/135))
- Add `work-on` for project-guided single-change delivery from plans, tickets or conversation diagnoses, with lead-selected methods, meaningful checks, independent review and bounded repair, ending before user-selected PR work or persistence. ([#14](https://github.com/SirDarcanos/agentskills/issues/14), [#67](https://github.com/SirDarcanos/agentskills/issues/67), [#118](https://github.com/SirDarcanos/agentskills/issues/118), [#127](https://github.com/SirDarcanos/agentskills/issues/127), [#139](https://github.com/SirDarcanos/agentskills/issues/139))
- Add `review-delivery` for project-guided independent Standards/Spec review, with delivery-inherited permission, dirty-scope freshness, conditional coordination and conversation-first original reports. ([#24](https://github.com/SirDarcanos/agentskills/issues/24), [#65](https://github.com/SirDarcanos/agentskills/issues/65), [#127](https://github.com/SirDarcanos/agentskills/issues/127), [#139](https://github.com/SirDarcanos/agentskills/issues/139))
- Add `ask-clef` and `ask-clef-flash` for evidence-backed local judgments through Ollama, by explicit standalone request or project-guided invocation under unchanged model permissions. ([#141](https://github.com/SirDarcanos/agentskills/issues/141))
- Add a shared 100-case decision-model benchmark with known labels, per-category reporting, and opt-in local/hosted comparison.
- Add `setup-project` for compact project-owned agreements, semantic no-op reconciliation, user-selected publication/persistence boundaries, stepwise approvals, conditional domain, assessment and GitHub setup, and a directly readable native tracker library. ([#8](https://github.com/SirDarcanos/agentskills/issues/8), [#134](https://github.com/SirDarcanos/agentskills/issues/134), [#156](https://github.com/SirDarcanos/agentskills/issues/156))
- Add `domain-modeling` for project-agreement-aware glossary/context-map maintenance, conversation-only planning and explicitly approved ADR changes with preserved history. ([#8](https://github.com/SirDarcanos/agentskills/issues/8), [#11](https://github.com/SirDarcanos/agentskills/issues/11), [#135](https://github.com/SirDarcanos/agentskills/issues/135))

### Changed

- Group skill packages under `workflow/`, `writing/`, and `models/`; manual copy/link paths now include the group, while skill names and CLI selection stay unchanged.
- Allow policy-authorized hosted `ask-jev` assessments alongside explicit requests, with shared disclosure, call and spending limits. ([#53](https://github.com/SirDarcanos/agentskills/issues/53))
- Allow policy-authorized `ask-nimble` assessments alongside explicit requests, with shared budgets and scoped lifecycle/fallback authority. ([#52](https://github.com/SirDarcanos/agentskills/issues/52))
- Move the three D&D skills to [SirDarcanos/dnd-agentskills](https://github.com/SirDarcanos/dnd-agentskills); install or update them from that repository. ([#49](https://github.com/SirDarcanos/agentskills/pull/49))
- Let `github-repo-setup` configure existing repositories and accept approved setup handoffs while preserving unrelated settings. ([#10](https://github.com/SirDarcanos/agentskills/issues/10))

### Fixed

- Preserve MIT notices when skills are copied independently and make `stay-positive`'s companion guidance portable outside sibling directories. ([#73](https://github.com/SirDarcanos/agentskills/issues/73))

## [1.6.0] - 2026-10-03

### Added

- Add `build-with-nimble` for application integrations, with composable decision design, local/self-hosted serving guidance, and validation checks.

## [1.5.0] - 2026-10-02

### Added

- Add command-only `ask-jev` for evidence-backed hosted judgments, with invocation-scoped disclosure and optional upstream TypeSafe guidance.

## [1.4.1] - 2026-10-01

### Added

- Add opt-in `ask-nimble` regression replay with synthetic fixtures and offline response-contract tests.

### Changed

- Improve `ask-nimble` with neutral evidence, comparison coverage and freshness checks, contrasting criteria, and up to four independent Choice, Noul, or Score judgments.

### Fixed

- Recognize Pi's expanded `ask-nimble` skill invocation without requiring the original slash command to remain visible.

## [1.4.0] - 2026-10-01

### Added

- Add command-only `ask-nimble` for evidence-backed local decisions, with direct-answer fallback and permission-based server management.

## [1.3.0] - 2026-09-10

### Added

- Add `implementation-preflight` to select or create the correct Git branch before an implementation workflow begins.

### Changed

- Expand `github-repo-setup` to configure direct-push, pull-request, development-branch, and bypass-exception workflows from explicit user choices.
- Make `github-repo-setup` explicitly user-invoked to prevent unintended remote and repository-wide changes.

## [1.2.0] - 2026-09-01

### Added

- Add `dnd-create-monster` and `dnd-speak-with-dead` for designing balanced monsters and rewriting Speak with Dead answers.
- Add `dnd-format-prose` for table-ready narration, boxed text, bestiary lore, and adventure lore.

## [1.1.0] - 2026-08-31

### Added

- Add `stay-positive` for constructive prose framing that preserves meaning, context, and necessary negativity.

### Changed

- Cross-referenced `stay-positive` in `slop-guard`.

## [1.0.0] - 2026-08-31

### Added

- Add a `github-repo-setup` skill with minimal project files, Dependabot, and secret-scanning safeguards.
- Add skills for creating and maintaining concise changelogs from repository evidence.
- Add `slop-guard` for auditing, editing, and drafting human-facing prose while preserving facts and voice.
- Add a README for each skill and a repository-level skill index.
