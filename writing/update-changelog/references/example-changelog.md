# Example changelog

Use this structure when the existing changelog follows Keep a Changelog. Preserve another established format unless migration is explicitly requested. Include only category headings that have entries.

```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add CSV export. ([#142](https://github.com/OWNER/REPO/issues/142), [PR #145](https://github.com/OWNER/REPO/pull/145))

### Fixed

- Prevent duplicate records during import. ([#147](https://github.com/OWNER/REPO/issues/147))

## [2.0.0] - 2025-03-08

### Breaking changes

- Replace `legacyMode` with `compatibilityMode`. ([#120](https://github.com/OWNER/REPO/issues/120))

### Added

- Add configurable retry limits.

### Security

- Reject unsigned webhook payloads. ([#131](https://github.com/OWNER/REPO/issues/131))

## [1.1.1] - 2025-02-14

### Fixed

- Preserve Unicode characters in exported filenames. ([#118](https://github.com/OWNER/REPO/issues/118))

[unreleased]: https://github.com/OWNER/REPO/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/OWNER/REPO/compare/v1.1.1...v2.0.0
[1.1.1]: https://github.com/OWNER/REPO/releases/tag/v1.1.1
```
