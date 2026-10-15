# Integrated-verification validation

Use when changing or validating [integrated verification](verification.md). Follow [entry validation](validation.md#reproducible-static-checks) for complete Markdown/frontmatter inspection, relative links/anchors, isolated package copying and diff hygiene. These are instructions, not an executable verifier or a general test harness.

## Authored cases

Walk the cases through the actual procedure and record step references and deviations. Expected outcomes are **not executed agent evidence**.

| Case | Starting facts | Expected behavior |
| --- | --- | --- |
| Unsupported done | Implementer claims completion; only an unrelated arithmetic suite passes | Steps 1–2 inspect actual delivery and coverage; step 4 rejects unsupported acceptance, naming missing criterion evidence. |
| Baseline versus regression | Same assertions/environment: legacy failure in both states; privacy test passes baseline and fails integrated state | Step 3 retains the baseline defect and identifies the privacy regression by observed cause; no blanket green or automatic baseline waiver. |
| Unknown baseline | Relevant check fails, but no comparable baseline is accessible | Step 3 records failed/unknown origin; baseline and regression claims remain unsupported. |
| Material unavailable check | Required recovery driver or execution permission absent | Steps 2–4 block affected acceptance immediately and recommend obtaining evidence or requesting an explicit agreement change; no installation or automatic retries. |
| Existing sufficient coverage | Assertions already exercise the affected public interface and meaningful denial path | Step 2 reuses coverage with rationale; no test quota or redundant new suite. |
| Authored only / weak sensitivity | Written recovery scenario never ran; a proposed regression check fails only on import | Step 3 labels not-run and uncertain sensitivity separately; neither is an observed behavior pass. |
| Dirty integrated state | Relevant staged, unstaged and untracked changes/supporting inputs exist | Steps 1 and 3 pin all relevant layers through the maintained scope contract, freeze writes and check final membership/fingerprints; HEAD alone is insufficient. |
| Drift / identical commit | Supporting input changes during checks, or identical final bytes are later committed | Step 3 marks affected evidence stale and repins/reruns; identical-content retention requires recorded equivalence and state-sensitive reruns. |
| Risk categories | Delivery changes access, persistence, destructive effects or domain invariants | Step 2 maps relevant failure paths to actual assertions or explicit gaps; safe synthetic coverage discloses its limits. |
| Verification versus acceptance | Relevant checks pass; independent review or completion procedure unavailable | Step 4 returns verification evidence and the later gate blocker, rather than claiming acceptance, repairing automatically or closing the ticket. |

## Executed-fixture protocol

A bounded direct exercise may use a disposable Git project with Python public-interface tests: one pre-existing failure, a privacy regression introduced into the integrated revision, a passing unrelated check, an unsupported implementer return and a deliberately absent material recovery driver. Pin agreement, base/HEAD, actual diffs and supporting inputs. Run comparable baseline and integrated checks, inspect failure causes, assess each criterion against the procedure and compare state before/after. Then change a supporting input to demonstrate invalidation.

Retain execution evidence at the target's approved evidence location **outside this installable package**. Include reproduction source/commands, observed results, snapshot identifiers, criterion dispositions, missing evidence, documentation impact and limitations. A script exit code tests only its fixture assertions; evidence sufficiency is the lead's inspected decision. Clearly separate that direct walkthrough from autonomous skill execution, independent review and integrated trials. No agent/model launch, live tracker mutation or sensitive fixture is needed for this check.
