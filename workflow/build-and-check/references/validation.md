# Build and Check validation

Read when changing or validating this package. Authored scenarios below are expected behavior, not executed agent trials.

## Package and executable checks

1. Read the complete entry and rendered Markdown. Verify `name: build-and-check`, matching-request/handoff triggers, ordinary model invocation, immediate checks and checkable completion/blocking conditions.
2. Resolve relative links from their containing files. Copy the complete package to an isolated directory without sibling skills, verify internal links and run the fixture there.
3. With Python 3.9+ and no third-party dependencies, run:

   ```sh
   python3 workflow/build-and-check/scripts/check-fixture.py
   ```

   The script writes only temporary synthetic files, runs six child Python checks with five-second timeouts, and removes its own temporary directory. It uses no network, model, Git/tracker mutation or installed-copy changes.
4. Inspect four unittest results and raw observations: code refactoring with existing coverage; documentation then configuration checked separately; a whitespace-regression assertion blocks the synthetic dependent artifact, followed by repair and green recheck; unavailable consumer stays blocked/unverified. The last case is a deterministic reporting oracle, not an executed missing-tool workflow. The failure gate is scripted, not proof that an agent stops. Existing harness and unrelated bytes remain unchanged; zero new target tests are needed for the demonstrated code increment.
5. Review the integrated diff for credentials/private data, generated files, local paths, protected work and notices. Record actual commands, environment and source identities outside the copied package, separately from expected scenarios.

## Authored cases

For the project-guidance migration, inspect direct and bounded entry with the same compatible existing agreement (no filename/template or Setup-origin requirement). Check missing/conflicting common guidance yields a specific prerequisite without setup or writes; conditional gaps affect only their capability. Exercise an unavailable material check and a recorded correction with prior spent lineage, including an old universal-contract-only companion. Record actual reads/actions/outcomes separately from these expectations. Ordinary same-session work returns evidence in conversation, without a new lead ledger or durable report.

Compare representative mandatory reading with baseline `45e5a24`: count complete required files once per context, include project guidance and any selected preflight/coordination/repair loads, and distinguish static closure counts from runtime adherence. Copy only this package for link/fixture checks; do not load maintenance validation during ordinary method execution.

| Case | Expected outcome |
| --- | --- |
| Standalone or Work On handoff | Inspect scope/current evidence, perform bounded increments inline, check immediately and return local evidence without PR/acceptance. |
| Sufficient existing coverage | Explain risk coverage and reuse checks; no test quota or manufactured red. |
| Non-code change | Check affected facts/links/frontmatter or configuration's parser/consumer before continuing. |
| Material check fails or cannot run | Stop dependent progress, classify cause, preserve partial work and report actual failure/gap; only current adequate recheck permits resumption. |
| Later edit invalidates evidence | Rerun dependent checks, retain unaffected evidence and original-state history. |
| Binding test-first policy | Follow it or request approved revision; this method cannot waive it. |
| Missing/ambiguous companion outside sibling layout | Block dependent Git/domain/delegation/correction route without install or legacy fallback. |
| Plan-only or unknown authority | Return bounded plan/blocker; no unapproved writes, runs or service effects. |
| Recorded finding/resume | Inspect only documented conditional coordination/repair libraries; preserve root ownership/bounds and existing checkpoint/lineage/spent cycles. An old universal-contract-only package blocks that route without resetting state; ordinary development remains independent. |
| Competing work/temporary artifacts | Preserve protected bytes/modes/links; clean only authorized unchanged owned scratch. |

## Limits

Static checks and deterministic fixtures do not certify agent adherence, composed routing, installed discovery, live tools/services, independent review or cross-runtime compatibility. Those require separate authorized trials. Local passes are not integrated acceptance, merge, deployment or release.
