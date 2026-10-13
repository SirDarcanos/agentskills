# Independent-review trial results for #24

**Outcome: the bounded dirty-work, drift and unavailable-capability trial executed successfully.** Both independent reviewers found the deliberately planted defects and blocked the synthetic delivery. A successful trial is not an approval of that defective fixture or evidence for every runtime/branch.

This is a separately authorized retry of the [failed startup attempt](trial-attempt.md), after the maintainer updated the local extensions/Pi installation. The shipped review procedure remained at merged revision `95c42ef05baff60e1747f6d6ab2aac742e5565fe`; none of its entry/scope/report bytes changed for the retry. `pi-subagents` now reported 0.78.0; the host manifest reported Pi 1.2.0. The same exported launcher guard, `resolveHostPeerAliases(hostRoot)`, changed from missing Chord aliases to an empty missing list. The user performed the update; the lead did not install or patch the runtime.

## Execution and independence

Workflow `bac6165d-0ad6-488c-9f32-138ea419e2c0` completed with two successful reviewer executions:

| Axis | Identity / report |
| --- | --- |
| Standards | `192fc621-7d8f-44ff-90b4-e4099824d124`; [full portable report](reports/standards.md) |
| Spec | `45e3469d-66e0-4760-a842-a051b809e20f`; [full portable report](reports/spec.md) |

Both were builtin `reviewer` contexts, requested/resolved **fresh**, distinct from the implementation/fixture author and each other's conclusions. The recorded route was `openai-codex/gpt-6.1-sol:high` for both; this identifies execution, not a required model or model-voting rule. Tools allowed inspection and supervisor contact, not shell, writes, network or recursive delegation. Each had a 15-minute bound and 70-call tool limit; at most two active workers. Both returned before their deadlines. The lead executed checks and integrated evidence; reviewers independently inspected actual source and raw evidence rather than approving a requested verdict.

Inputs were the identical authorized procedure, synthetic brief/standards, fixed-base/dirty manifests, separate committed/staged/unstaged patches, actual included files and lead execution observations. Neither saw the validation/test expectations, parent conversation, protected contents or the other report. Each independently sent its initial report through a supervisor checkpoint before the controlled mutation. Final output preserved each initial report; assertions compared it with the original checkpoint text and passed (only outer whitespace ignored).

Original artifact SHA-256 values:

- Standards: `14723009e8f46a44c87c72e8ec031f5ef010c57b4c9cafdd9b230ee0e58f66c7`.
- Spec: `e4e88f0f2d1a73dd72ed223c18751aea9faa854765ef02c444e7a2a0bf4cdce5`.

Runtime-managed originals and execution receipts retain those IDs under local retention policy. Linked public copies replace only temporary filesystem paths for portability; their headers disclose that transformation. No private session logs, credentials or workstation paths are published.

## Scope and phase boundary

The retained fixture still matched its original pin before retry. Comparison rule: fixed base `cef787b6707038b7806a4eacbca3a6ca691e5441` to HEAD `b7682d1c55d12e35e8e742a0765ded20ca3a9d24`, branch `main` in the synthetic repository, plus dirty layers. The original ten paths and procedure digests are recorded in the failed-attempt record; `AGENTS.md` and `brief.md` are supporting inputs. Original content-manifest digest: `9307635b977d2030862fad9a258cc41ab892a8c3d0cec40c3ae802a6869969e8`.

1. Freeze the original included files/support. Both reviewers inspect the initial state and submit separate immutable reports; scoped capture still matches before mutation.
2. Supply missing non-following symlink evidence: lead `Path.lstat()` and `os.readlink()` show `note-link` targets already included `duplicate.py`, mode 493, with target digest matching the initial snapshot. Neither reviewer follows a link into protected content. Both retain the original gap finding and address it in a separately labeled supplement.
3. Only after both initial checkpoints, release the old freeze for controlled source drift: change `duplicate.py` from `strip()` to `rstrip()` and add untracked `consumer.py` importing/calling that duplicate. These are new deliberate fixture defects, not repairs.
4. Repin the eleven-file scope, repeat candidate discovery and freeze current files/support. The original-list helper check exits **1** (changed file fingerprint). Separate root discovery finds the newly relevant caller, which the original path list cannot detect. HEAD, index and all three tracked patch fingerprints remain unchanged because the affected files are untracked.
5. Give both reviewers identical new manifests, transition observations, link metadata and separate unavailable-capability handoff; preserve the other axis's conclusions. They independently assess impact and next gates without claiming complete renewed review.
6. After both reports, recapture current sources and supporting evidence/procedure digests. Assert unchanged protected bytes, scoped protected status, complete index/history and current scope; no worker writes or repairs occurred.

Current content-manifest digest: `5cae48c20ccda313111c48455d35811ecb8327bd65308591bdaddf711665c2ba`. The changed duplicate has digest `11b87c87d6addb066818136d4da8a52218f1270ac63e674cf414670addbe6031`; new consumer digest `0e4f24616965e407a5df43986aaaae8f75e319440cb474535ac3e69c637fd3dd`. Agreements, protected work and original tracked state remain unchanged.

## Observed outcomes

| Trial requirement | Actual result |
| --- | --- |
| Inspect dirty scope, including relevant untracked work | Both inspect committed/staged/unstaged layers and actual untracked `duplicate.py`, account for deletion/new-name paths and supporting inputs; they do not equate HEAD with dirty delivery. |
| Independently detect known findings | Standards STD-01 and Spec SP-1 identify the unstaged `upper().strip()` case regression at `formatter.py:2`. Standards STD-02 and Spec SP-2 identify duplicate ownership at untracked `duplicate.py:1–2`, citing S1/F2. Both distinguish binding violations, static reasoning, lead execution and unavailable checks. |
| Materiality/actionable reporting | Both provide locations, requirement references, user-visible/ownership consequences, bounded correction recommendations, evidence and limits. Neither turns an unsupported architecture preference into a rule. |
| Missing material source metadata | Both initially report the unavailable symlink-target evidence as an access gap rather than follow the link blindly or claim complete coverage. Both address the supplied non-following evidence as an initial-state supplement, not a rewritten report. |
| Detect post-pin drift | Both explicitly mark affected initial coverage stale and identify the added caller; unchanged HEAD/patches do not establish equivalence. They retain isolated unchanged formatter evidence but require renewed duplicate/consumer/link-destination and cross-axis coverage. Both additionally observe the new leading-whitespace defect statically (STD-03 / SP-4). |
| Missing independent-review capability | Both apply the shipped gate to a separate handoff grounded in the actual earlier startup failure: unavailable independent review blocks acceptance; direct inspection stays lead self-review, and their current successful contexts do not substitute for that separate handoff. This is executed reviewer assessment of supplied prior-failure evidence, not a newly induced runtime outage. |
| Preservation and final freshness | Lead assertions pass for protected content/status, complete index/history, exact current scoped capture, procedure/supporting-input digests and unchanged initial checkpoint text. Neither reviewer mutates the target. |

Final package checks also passed: `python3 -B review-delivery/scripts/test_snapshot.py` exited 0 (11 checks); 19 package-relative links/anchors resolved; public report copies matched the originals except the declared path substitutions and contained no workstation paths; an isolated copy of only this package generated a fresh matching fixture without exposing test expectations. `git diff --cached --check` passed before commit. Direct author inspection is separate from the executed fixture reviewers; HTML rendering and independent review of this evidence-only follow-up are not executed.

Lead operations actually executed include the exported Node compatibility guard, Python fixture/manifest comparison, `snapshot.py check <initial-artifact>`, `git status --porcelain=v1 -z --untracked-files=all`, `git ls-files --stage -z`, `git rev-list HEAD`, non-following link metadata, SHA-256 comparisons and initial-report/checkpoint equality assertions. Environment: Python 3.14.7 / Git 2.54.0 (Apple Git-157). The initial public-interface observation was separately lead-executed using `git show <base>:formatter.py`, Python `exec` for that synthetic baseline, and `runpy.run_path` for delivered `heading('  Hello world  ')`: baseline `Hello world`, delivered `HELLO WORLD`. Reviewers did not execute code.

## Limits, disposition and next action

The trial meets #24's specific dirty/untracked finding-detection, stale-scope and unavailable-capability exercises. Deliberate fixture findings remain unresolved **by design**; no acceptance of the fixture, repair loop, merge or release is claimed. Phase two is impact triage, not a complete renewed two-axis review of repaired code. Non-Git manifests, manual submodule capture, timeout/recovery, successful repair/acceptance and broader runtime certification remain unrun branches; #29/#30 own integrated trials.

Both reviewers correctly note that the initial heading observation packet lacked the exact command/interpreter version, and the Spec report notes external support fingerprints were not individually present in that packet. Later metadata identifies the environment, while the lead's final assertions cover support digests; those are distinct evidence, not retroactive edits to initial reports. Static source inspection independently establishes the known defects. Future trial packets should include exact commands/environment and support-artifact hashes upfront; the shipped contracts already require these, so no new runtime rule is introduced.

Only validation support/evidence changes in this follow-up. No extra changelog entry or release-impact label is warranted; existing review behavior, domain/ADR records, lead completion/repair integration, native graph and installed skills remain unchanged. Keep #24 open until the maintainer accepts and merges this follow-up evidence under project policy; prior approval to merge #39 does not authorize #40.
