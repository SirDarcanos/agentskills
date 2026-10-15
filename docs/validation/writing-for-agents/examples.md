# Synthetic writing examples

These are author-produced before/after artifacts and static walkthroughs of the delivered procedure, not autonomous agent trials. All project names, commands and policies below are synthetic. No release or documented consumer command was executed.

## E1 — Skill routing and missing companions

**Input:** edit a skill for checking a local preview. An external installed documentation helper is available; no suitable project-shipped companion is available. The supplied contract permits inspecting a preview, not deployment.

Before, `SKILL.md`:

```markdown
---
name: inspect-preview
description: Help with projects.
---
Check things carefully. Read the guide. Finish when ready.
```

After, `SKILL.md`:

```markdown
---
name: inspect-preview
description: Inspect a local preview against agreed page content before reporting discrepancies. Use for preview-content checks, not deployment.
---
# Inspect preview

1. Read the approved page content and identify the local preview URL. If either is unavailable, report the missing input before proceeding.
2. Before inspecting the preview, read [the inspection guide](references/inspection.md) for required observations and the report format.
3. Compare the observations with the agreed content and return discrepancies and unverified sections. Report completion only when each agreed section has an observation or an explicit gap.
```

Supporting `references/inspection.md` is an existing synthetic guide defining observations and report fields; its actual content would need inspection in a real task. The example's link is illustrative, not a claimed existing file or passed link check.

**Walkthrough:** entry step 1 bounds editing and preserves inspection-only authority; step 2 improves routing and completion; step 3 writes directly without invoking the external helper. Step 4 requires real target and environment checks before claiming verification. This artifact intentionally does not assert that an unprovided guide or runtime was checked. Covers WA1, WA2, WA4, WA5, WA6.

## E2 — Instruction file, duplication and unsupported policy

**Input authority:** the project's release guide owns the rule “Publication requires explicit maintainer approval.” The instruction file repeats that rule and adds “Preview checks are allowed locally.” The writing suggestion is “Make publication automatic once checks pass.” Only wording and organization changes are authorized.

Before, `AGENTS.md`:

```markdown
# Instructions
Publication requires explicit maintainer approval.
Preview checks are allowed locally.
See release.md.
```

After, `AGENTS.md`:

```markdown
# Instructions
Preview checks are allowed locally.
Before preparing or publishing a release, read [the release guide](release.md) for the publication approval gate and release steps.
```

The existing synthetic `release.md` remains the sole authority for publication approval, with the rule unchanged. The unique preview permission stays in `AGENTS.md`.

**Walkthrough:** entry steps 1–2 select the established owner and retain the unique exception. Step 3 rejects the automatic-publication suggestion as an unapproved policy change. Required response: “Automatic publication would change the approval policy; the existing gate is preserved. Ask the maintainer separately if that change is desired.” A writing-only invocation neither publishes nor asks for installation. Covers WA1–WA5; step 4 still needs actual link validation in a real project.

## E3 — Referenced guide, broken pointer and unavailable environment

**Input:** a guide describes a preview check but links to missing `checks.md#preview`. The actual authoritative target is `preview-checks.md#local-preview`. The named `previewctl` runtime is unavailable. The author may repair the pointer and clarify steps, not invent a replacement command or success result.

Before, `preview-guide.md`:

```markdown
# Preview guide
Read [checks](checks.md#preview). Inspect the output and understand the result. Check everything.
```

After, `preview-guide.md`:

```markdown
# Preview guide

1. Before running preview checks, read [the local-preview procedure](preview-checks.md#local-preview) for the approved command and expected observations.
2. Confirm that its named runtime is available in the target environment. If unavailable, report the unrun command and stop the dependent check; retain any completed observations.
3. Execute only the approved safe check, compare each required observation with its expected result, and record mismatches.

Complete when each required observation has a result or an explicit gap. An unavailable runtime leaves execution unverified.
```

**Walkthrough:** the writer must inspect the actual target heading before adopting that link. In this synthetic artifact the names are supplied facts, not a filesystem verification claim. The new pointer routes conditionally, the procedure has an order and failure outcome, and no executed-runtime claim is made. An unchanged caller still pointing at the old file would be an outstanding affected link, not a completed migration. Covers WA1, WA2, WA3, WA4, WA6.

## Additional boundary inspections

- A same-named helper with no verifiable source is unavailable under step 3; direct writing still works.
- A project-shipped helper that mandates an external companion cannot be used in that mode. Its own gate and the project-shipped boundary both apply; write directly if they cannot coexist.
- A review-only request returns these defects and proposed corrections without editing target documents.

These cases were walked through by the implementation author against the actual entry point. They do not demonstrate cross-runtime routing reliability, independent behavior or model adherence. The offline checker separately demonstrates actual package links and failure sensitivity on disposable files.
