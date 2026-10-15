# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add `ask-nico` for explicitly requested, installed-skill recommendations that respect project rules and stop before workflow execution. ([#112](https://github.com/SirDarcanos/agentskills/issues/112))
- Add `writing-for-agents` for actionable skills, instruction files and referenced guides, preserving established meaning and authority with project-shipped companions only. ([#111](https://github.com/SirDarcanos/agentskills/issues/111))
- Add `resolve-merge-conflicts` for authorized merge/rebase resolution, protected unrelated work, relevant checks and decision pauses for unsafe continuation. ([#110](https://github.com/SirDarcanos/agentskills/issues/110))
- Add `handoff` for explicitly requested, portable session transfers with evidence pointers, approval boundaries and approved durable storage for later resumption. ([#102](https://github.com/SirDarcanos/agentskills/issues/102))

- Add `work-on-spec` for bounded ticket-agent scheduling, native dependency eligibility, serial integration and aggregate verification/review/recovery under `work-on`'s shared execution ledger. ([#68](https://github.com/SirDarcanos/agentskills/issues/68))
- Add standalone `pr` for plain-language decision reports, test and measured CI impact, and authorized opening/updating, with `work-on` using its discovered companion. ([#66](https://github.com/SirDarcanos/agentskills/issues/66))
- Add standalone `investigate-bug` for bounded diagnosis through exact ticket proposals, approval and verified publication/reconciliation, with explicit investigation-only outcomes and a separate-request Work On recommendation for actionable tickets. ([#64](https://github.com/SirDarcanos/agentskills/issues/64), [#122](https://github.com/SirDarcanos/agentskills/issues/122))
- Add standalone `write-tickets` for cohesive decomposition and ready bug publication with approved native dependencies, caller-owned prerequisite analysis and concise approval tied to complete drafts, with `work-on` using its discovered companion. ([#63](https://github.com/SirDarcanos/agentskills/issues/63), [#117](https://github.com/SirDarcanos/agentskills/issues/117))
- Add standalone `write-spec` for agreed behavior, stable acceptance IDs and authorized publication with separate readiness, with `work-on` using its discovered companion. ([#62](https://github.com/SirDarcanos/agentskills/issues/62))
- Add standalone `shape-work` with focused discovery, agreement-critical analysis before confirmation, direct companion continuation, settled-decision reuse and preserved concern dispositions, with `work-on` using its discovered companion. ([#61](https://github.com/SirDarcanos/agentskills/issues/61), [#121](https://github.com/SirDarcanos/agentskills/issues/121))
- Add standalone `analyze` for codebase-informed readiness, evidence reuse and method/check recommendations returned to the accountable caller, with `work-on` using its discovered companion. ([#60](https://github.com/SirDarcanos/agentskills/issues/60), [#117](https://github.com/SirDarcanos/agentskills/issues/117))
- Add standalone `build-and-check` for small implementation-first increments with immediate relevant validation and reusable coverage, also available through `work-on`. ([#59](https://github.com/SirDarcanos/agentskills/issues/59))
- Add standalone `acceptance-first` for executable workflow examples, checked implementation increments and criterion-level evidence, also available through `work-on`. ([#58](https://github.com/SirDarcanos/agentskills/issues/58))
- Add standalone `characterize` for legacy behavior protection with baseline provenance, sensitivity and explicit unknown/defect limits, also available through `work-on`. ([#57](https://github.com/SirDarcanos/agentskills/issues/57))
- Add standalone `prototype` for bounded experiments, recommendations and authority-safe artifact disposition, also available through `work-on` without claiming production readiness. ([#56](https://github.com/SirDarcanos/agentskills/issues/56))
- Add standalone `tdd` with behavioral red–green–refactor and reusable coverage, also available through `work-on`'s test-first route. ([#55](https://github.com/SirDarcanos/agentskills/issues/55))
- Add independently usable `research` with cited, version-aware findings, evidence reuse and optional authorized background delegation. ([#54](https://github.com/SirDarcanos/agentskills/issues/54))
- Add `work-on` for technical-led single-change delivery, complete-read recovery and inspected companion references, composed methods, verification, independent review, bounded repair/recovery and PR handoff; whole-spec scheduling requires `work-on-spec`. ([#14](https://github.com/SirDarcanos/agentskills/issues/14), [#67](https://github.com/SirDarcanos/agentskills/issues/67), [#118](https://github.com/SirDarcanos/agentskills/issues/118))
- Add `review-delivery` for independent Standards/Spec review of standalone and bounded handoffs, with dirty-scope freshness and shared execution limits. ([#24](https://github.com/SirDarcanos/agentskills/issues/24), [#65](https://github.com/SirDarcanos/agentskills/issues/65))
- Add `ask-clef` and `ask-clef-flash` for evidence-backed local judgments through Ollama, by explicit request or approved project policy.
- Add a shared 100-case decision-model benchmark with known labels, per-category reporting, and opt-in local/hosted comparison.
- Add `setup-project` with stepwise confirmations, default ordinary-workflow and lead-owned review/repair permission, explicit installed-assessment choices, label dispositions and retained-label normalization alongside project documentation, model-use policy and GitHub setup. ([#8](https://github.com/SirDarcanos/agentskills/issues/8))
- Add `domain-modeling` as a reusable companion for `setup-project` and other workflows, with plan-only and approved glossary, context-map, and ADR handoffs. ([#8](https://github.com/SirDarcanos/agentskills/issues/8), [#11](https://github.com/SirDarcanos/agentskills/issues/11))

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
