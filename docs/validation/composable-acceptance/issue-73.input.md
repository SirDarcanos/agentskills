## Outcome

Finish package discovery and delivery acceptance coverage.

Part of #48. Acceptance references: AC1, AC6, AC9, AC10, AC12, AC13, AC14, AC15, AC16.

## Scope and acceptance

- [ ] Validate isolated installation/discovery and links for all delivered skills; verify optional companions do not silently become mandatory and missing required routes fail clearly.
- [ ] Reconcile README/install guidance, public names, authoritative runtime ownership, design/ADR pointers, operating policy and changelog with the integrated implementation.
- [ ] Consolidate acceptance evidence across package checks and the three integrated trials, explicitly retaining limitations and unresolved findings.
- [ ] Verify replacement packages and migration procedure are ready for the separately approved installed-copy operation; AC16 remains pending until that real operation is verified.

## Verification

- [ ] Run package/link/frontmatter/discovery checks and inspect the integrated diff for duplicate procedure owners, private paths, secrets, source/licensing omissions and false capability claims.
- [ ] Map all AC1–AC16 to actual evidence or explicit remaining migration/approval blockers; no blanket completion while material gaps remain.

## Boundaries

- Actual global installation/removal
- Automatic release
- Rewriting historical #14 evidence

## Prerequisites

Blocked by #69, #70, #71, #72. Native edges, not this summary, govern eligibility.

## Delivery and documentation

- Consume the accepted #50 design and the current #48 agreement; prerequisite issue closure alone does not establish accepted integration.
- Each package owns its procedure once, supports standalone and bounded handoff use, and declares invocation, authority, dependencies, completion and blocked outcomes.
- Read full entry points before changes. Preserve unrelated work, attribution and license notices. Companion discovery must work outside a sibling-directory layout.
- Perform applicable frontmatter, relative-link, isolated-package, and executable checks; inspect the integrated diff and record actual results separately from authored scenarios.
- Update owned documentation and changelog where public behavior changes, or record a justified no-change decision. Keep this ticket open until accepted and merged under project policy; operational migration uses its explicit completion criteria instead of pretending local installation is a code merge.
