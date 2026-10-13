# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add Work On's explicit context-aware entry and routing for requests, existing agreements, and partial work; later delivery phases remain unavailable. ([#19](https://github.com/SirDarcanos/agentskills/issues/19))
- Add separate command-only Ask Clef and Ask Clef Flash skills for evidence-backed local text and image judgments through Ollama.
- Add a shared 100-case decision-model benchmark with known labels, per-category reporting, and opt-in local/hosted comparison.
- Add Setup Project for project-aware docs, changelog/versioning setup, audited spec/release labels, and verified native issue dependencies. ([#8](https://github.com/SirDarcanos/agentskills/issues/8))
- Add Domain Modeling as a reusable companion for Setup Project and other workflows, with plan-only and approved glossary, context-map, and ADR handoffs. ([#8](https://github.com/SirDarcanos/agentskills/issues/8), [#11](https://github.com/SirDarcanos/agentskills/issues/11))

### Changed

- Clarify Setup Project's distinct spec/implementation-step roles, project-specific issue titles, and independently assessed readiness. ([#14](https://github.com/SirDarcanos/agentskills/issues/14))
- Let GitHub Repository Setup configure existing repositories and accept approved setup handoffs while preserving unrelated settings. ([#10](https://github.com/SirDarcanos/agentskills/issues/10))

## [1.6.0] - 2026-10-03

### Added

- Add Build with Nimble for application integrations, with composable decision design, local/self-hosted serving guidance, and validation checks.

## [1.5.0] - 2026-10-02

### Added

- Add command-only Ask Jev for evidence-backed hosted judgments, with invocation-scoped disclosure and optional upstream TypeSafe guidance.

## [1.4.1] - 2026-10-01

### Added

- Add opt-in Ask Nimble regression replay with synthetic fixtures and offline response-contract tests.

### Changed

- Improve Ask Nimble with neutral evidence, comparison coverage and freshness checks, contrasting criteria, and up to four independent Choice, Noul, or Score judgments.

### Fixed

- Recognize Pi's expanded Ask Nimble skill invocation without requiring the original slash command to remain visible.

## [1.4.0] - 2026-10-01

### Added

- Add command-only Ask Nimble for evidence-backed local decisions, with direct-answer fallback and permission-based server management.

## [1.3.0] - 2026-09-10

### Added

- Add Implementation Preflight to select or create the correct Git branch before an implementation workflow begins.

### Changed

- Expand GitHub repository setup to configure direct-push, pull-request, development-branch, and bypass-exception workflows from explicit user choices.
- Make GitHub repository setup explicitly user-invoked to prevent unintended remote and repository-wide changes.

## [1.2.0] - 2026-09-01

### Added

- Add D&D skills for designing balanced monsters and rewriting Speak with Dead answers.
- Add D&D Format Prose for table-ready narration, boxed text, bestiary lore, and adventure lore.

## [1.1.0] - 2026-08-31

### Added

- Add Stay Positive for constructive prose framing that preserves meaning, context, and necessary negativity.

### Changed

- Cross-referenced Stay Positive in Slop Guard.

## [1.0.0] - 2026-08-31

### Added

- Add a GitHub repository setup skill with minimal project files, Dependabot, and secret-scanning safeguards.
- Add skills for creating and maintaining concise changelogs from repository evidence.
- Add Slop Guard for auditing, editing, and drafting human-facing prose while preserving facts and voice.
- Add a README for each skill and a repository-level skill index.
