# Standards review — #68

## Inspected coverage

Reviewed the supplied scope manifests and **complete tracked diff** against base/HEAD `330bf0736519b4b96a873050bb542924b1f2fa38`, plus:
- Every new `work-on-spec` file, including the complete fixture script and LICENSE.
- Changed Work On files directly; complete entry, execution, build, verification, completion and recovery libraries.
- Repository instructions, accepted composable-delivery design/inventory/validation mapping, both agreements, relevant review contracts and documentation.
- All four supplied check logs.

Independent, read-only review; no edits, execution, delegation, assessments or tracker mutations.

## Review

### Correct

- **Authority and portable discovery:** overall delivery requires explicit authorization; companions resolve through runtime/project discovery rather than sibling paths (`work-on-spec/SKILL.md:10–14`).
- **Single procedure ownership and shared bounds:** Work On retains the execution contract; old dispatch files are compatibility pointers. Aggregate review and repair preserve root ownership and finding budgets (`work-on/references/contracts.md:65–74`; `work-on-spec/references/aggregate.md:15–17`).
- **Safe integration/recovery:** native prerequisites require accepted integration evidence; integration is serial, uncertain effects require inspection, and cleanup remains separately authorized (`work-on-spec/references/dispatch.md:17,41–45`; `references/recovery.md:15–19`).
- **Fixture isolation:** disposable repositories, stripped `GIT_*` overrides, disabled global/system configuration, hooks/templates and bounded subprocesses keep Git operations local (`work-on-spec/scripts/check-coordination-fixture.py:26–46`). The retained single-change fixture additionally exercises hostile overrides and protected staged/unstaged/untracked state.
- **Documentation/licensing:** the new package carries Nicola Mustone’s MIT notice; README, design pointer and one Unreleased Added entry reflect shipped functionality without claiming installation or release (`work-on-spec/LICENSE:1–21`; `CHANGELOG.md:12`).

### Finding S-01 — P2 / nonblocking: local recovery validation retains an obsolete coordinator expectation

**Location:** `work-on/references/recovery-validation.md:12,27`, made stale by the changes to `work-on/references/recovery.md:46,51`.

**Evidence:** the validator still attributes “recomputed dispatch” progressing unrelated eligible work to recovery step 3 and maps that step to a “phase/frontier.” The revised procedure explicitly prohibits local scheduling and reserves multi-ticket frontier reconstruction solely for Work On Spec.

**Binding requirement:** accepted `docs/design/composable-delivery.md:41,54` requires validation references to follow their procedure’s transferred ownership.

**Smallest fix:** update the blocked-dependency expectation to keep this bounded ticket waiting and return observations to the overall lead; distinguish retained historical #28 mapping from current local-recovery checks. Preserve historical executed records.

This is documentation/validation drift, **not evidence of an executable duplicate scheduler**.

- **Fixed:** none; review-only.
- **Blocking findings:** none.
- **Decision-required findings:** none.
- **Merge verdict:** **OK with notes**, as a technical review recommendation only—not an acceptance or merge decision.

## Evidence and limitations

- **Static:** complete diff/scripts, ownership, authority, notices and package link targets inspected.
- **Supplied executed evidence:** both repository fixture logs report eight passing tests; expected regression and missing-check failures remain explicit.
- **Summary-only evidence:** Markdown and isolated-copy logs contain aggregate receipts, not rendered HTML or individual isolated-test output; those results were not independently reproduced.
- **Unrun here:** all commands, live tracker/native pagination, writable ticket-agent lifecycle, installed discovery and autonomous failure/resume. Broader runtime trials remain explicitly assigned to #72/#73.

**Next action:** reconcile S-01, refresh Markdown/link checks, and have the root lead perform the final scope/freshness comparison.