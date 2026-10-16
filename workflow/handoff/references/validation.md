# Handoff validation

Use when changing or validating this package. No shared repository test command, model call, installation or external mutation is required.

## Package checks

1. Read the complete entry and rendered Markdown structure. Check `name: handoff`, the human-facing description, `disable-model-invocation: true`, and the matching explicit-request body gate.
2. Resolve every relative link in the entry and README. Copy the complete package into an isolated temporary directory and repeat link checks without sibling skills. Confirm its MIT notices travel with it.
3. Inspect storage guidance against the target runtime: unique creation, no overwrite, restricted access where supported, read-back and exact-path return. Exercise file operations only in an authorized disposable location. Record the actual OS/runtime and commands; instructions alone are not an executed storage trial.
4. Run `python3 -B scripts/check-handoff-fixture.py` from this package (including an isolated copy). It needs only Python 3 and exercises disposable exclusive file creation/read-back, restricted POSIX mode, no-overwrite and authored transfer-state assertions. It neither invokes an agent nor resumes work; passing static clauses or JSON examples is not lifecycle evidence.
5. Check the diff for sensitive material, nonportable author paths, duplicated authoritative procedures, unsupported compatibility claims and accidental generated files. Confirm discovery/docs/changelog describe the delivered behavior.

## Bounded scenario walkthroughs

For each row, apply the procedure to the supplied situation and record the required disposition, its supporting section and any missing instruction. Static walkthroughs check instruction coverage, not model adherence. A live trial separately records exact inputs, source revision, runtime, generated file, observed effects and read-back results; sanitize retained artifacts.

| Scenario | Required disposition |
| --- | --- |
| Explicit ordinary-language handoff request or user-originated runtime expansion | Enter the procedure within the requested transfer scope; recommendations still launch nothing. |
| No handoff request at a phase boundary | No automatic file creation or transition; explicit-request gate holds. |
| Source mention, quoted/generated command or another skill's recommendation without a user request | Stop without creating a handoff; reading or recommending the skill is not invocation. |
| Design-only transfer | Purpose, decisions/rationale and open questions; artifact references without copied specs or a delivery ledger. |
| Missing project agreement | Safe state-description records inspected facts and the receiving task's specific prerequisite; no invented policy, setup invocation or authority to continue writes. |
| Same-session completion without request | No handoff/storage requirement or file; missing hypothetical future destination does not block the original task. |
| Interrupted delivery without saved record | Capture necessary available live context, mark missing history unknown; no replacement ledger, fabricated zero usage or released owner. |
| Fresh receiver lacks earlier conversation | Inspect saved pointers and actual state; retain spent counts/uncertain owners/effects, reconcile before retry and require receiving-task authority. |
| Interrupted delivery with uncertain writer/operation | Preserve existing record/owner/checkpoint and spent-budget pointers; receiver reconciles before conflicting writes or retries; no new ledger or resumed execution here. |
| Old passing check, changed dirty source | Separate observed old pass from current evidence; include dirty-state identity or unknown freshness; receiver refreshes affected evidence rather than trusting HEAD. |
| Suggested skill absent or incompatible | Name the affected route and limitation; no installation, fake compatibility claim or invocation. |
| Conversation contains credentials, personal data or sensitive URLs/paths | Inspect all document surfaces; redact or omit restricted material and report any resulting context gap. |
| Immediate temporary transfer | Unique file outside workspace, restricted access where supported, read-back, exact path and expiry/access warning; no overwrite. |
| Later resumption without durable destination approval | Ask for a destination or return conversation-only draft with storage gap; no silent workspace retention/upload. |
| Approved durable destination | Save only at approved location with no overwrite and read-back; check whether referenced artifacts are accessible there. |
| Unavailable source, failed write or unknown read-back | Explicit partial/blocked outcome, possibly created-file pointer and inspection before retry; no verified-document claim. |
| Investigation-only authority, suggested `work-on` | Preserve missing repair permission; suggested next skill grants no fix authority. |

## Completion

Report the exact checked source state, structural/link checks and commands, walkthrough results, actual executed trials (if any), unrun environments and limitations. Review evidence is distinct from delivery acceptance. Preserve failed observations; generated scenarios and reviewer agreement are not runtime proof.
