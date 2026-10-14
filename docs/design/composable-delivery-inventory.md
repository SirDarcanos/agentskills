# Composable delivery inventory and provenance

Read with [#50's design](composable-delivery.md) when extracting a procedure or assessing candidate source material. This is read-only evidence, not permission to import, install or retire anything.

## Observation boundary

Repository input revision: `06ff29cbd32442cb59511ff34982fb48dcde7ae8` (current `origin/main` at preflight). Read #48/#50, project/workflow/tracker/label authorities, CONTEXT, the complete `work-on`, `review-delivery`, `setup-project`, `domain-modeling` and four `ask-*` entry points, Work On's contracts/product/readiness/ticketing/build/verification/completion/dispatch/recovery procedures, ADR 0001 and all three #14 design documents. The [destination map](composable-delivery.md#current-procedure-destination-map) assigns these capabilities to future owners.

The repository's `research/` contains a feasibility note, not a `SKILL.md`; #54 must add the independent package without dropping that note. New method/specialist names in the design are planned destinations, not claims that they are shipped. Existing assessment entries remain explicit-invocation-only; changing this design cannot enable autonomous calls.

The [prior inventory](delivery-workflow-inventory.md) records observed legacy implement/spec/review/grilling/spec/ticket/TDD behavior, digests, installed provenance uncertainty and a pinned MIT license inspection. Reuse it as historical evidence, not as a current installed-root inventory. #69/#74 must inspect actual roots and local modifications anew.

For #50, additionally read the complete installed entry points for `tdd`, `prototype`, `research`, `pr` and `diagnosing-bugs`. These were candidate observations only, not execution or comprehensive package/import review. Machine-specific locations and content are not copied into public design evidence.

| Candidate | Useful observed capability | Contract mismatch / proposed disposition |
| --- | --- | --- |
| Installed `tdd` | Behavioral tests, red-before-green, vertical slices | Requires user-confirmed seams and excludes refactoring from loop; author a compatible red–green–refactor owner, not a wrapper inheriting those rules |
| Installed `prototype` | Logic/state versus UI question routing, runnable throwaway artifact and learning capture | Prescribes artifacts/retention and folding decisions into code; adapt only if justified and licensed, retaining bounded experiment/authority and no automatic production promotion |
| Installed `research` | Primary-source claims and cited Markdown findings | Requires background agent and repository write; new owner allows direct execution and approved output home, respecting delegation/write authority |
| Installed `pr` | Before/after evidence, reversibility and risk; credits Dex Horthy / Humanlayer show-me | Diagram-first and glossary-path assumptions differ from #48's plain-language report; preserve credit if adapting, do not copy template without license review |
| Installed `diagnosing-bugs` | Specific reproduction loop, minimization, falsifiable hypotheses, instrumentation and regression sensitivity | Includes fix/cleanup phases and expansive loop suggestions; `investigate-bug` stops at ticket and bounds experiments/disclosure instead |
| Prior installed delivery/grilling/spec/ticket/review entries | Useful phase/graph/axis ideas catalogued under #14 | Existing invocation, mandatory integration/TDD and committed-only review assumptions are incompatible; no hidden legacy fallback |
| `codebase-design` (prior inventory) | Interface/locality vocabulary | No new mandatory vocabulary dependency; target domain definitions remain authoritative |
| Repository-owned packages and validation records | Implemented scope, preservation, snapshot, bounded repair/recovery and portability rules | Reuse maintained material and notices; leave old executed records at their original paths and label new scenarios separately |

## Candidate external sources and license gates

No external body/template/example/configuration is imported in #50. Default recommendation is original instructions derived from #48 plus reuse of repository-owned procedures. A named installed source or metadata credit alone does not prove licensing or byte provenance.

| Candidate source | Evidence available / unresolved | Requirement before later reuse |
| --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills), legacy entries and likely related methods | Prior inventory identifies installed engineering/productivity entries and MIT at pinned `49dd158d1076134a641b33efb035946536778336`, copyright 2026 Matt Pocock. No reliable source revision for all installed bytes; prototype/research/diagnosis source origin not independently verified here | Verify exact selected file/revision and applicable license/notices, including supporting files. Carry full applicable MIT copyright/permission notice inside every independently copied package containing substantial reused material |
| [Humanlayer show-me](https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md) | Installed `pr` credit names show-me, Dex Horthy and Humanlayer; applicable exact-revision license not checked in #50 | Inspect source revision and licensing before adapting prose/template/examples; preserve existing credit and required notices. If unresolved, write original report instructions |
| [TypeSafe skills](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) and service docs | Existing `ask-jev` links integration guidance; #50 does not fetch/import it or certify current service behavior | #53 follows named API guidance under its validation scope. Reading public guidance is not permission to vendor bodies or disclose project evidence; copying needs exact license review |
| Characterization / acceptance-first / build-and-check | No external package selected or license established | Author original procedures against #48 and existing local build/verification material; if a new import is proposed, add exact provenance/license evidence first |

Root repository MIT is not a substitute for another author's notice. Preserve current per-package LICENSE files and attribution; independently distributable adapted packages must carry applicable notices for their shipped material. Unresolved permissions block import, not original implementation. Candidate selection does not imply upstream still matches inspected copies or certify a runtime.

## Candidate installed migration mapping

These are candidates only; names alone never authorize retirement. #69/#74 inventory exact local packages, aliases, registrations, all discovery roots, installation mechanism, source/shared-link ownership and modifications before approving targets.

| Old observed/name family | Intended replacement if actual inventory confirms equivalence |
| --- | --- |
| `implement` | `work-on` |
| `implement-spec` | `work-on-spec` |
| `code-review` | `review-delivery` (no competing maintained code-review) |
| grilling variants | `shape-work` |
| `to-spec` | `write-spec` |
| `to-tickets` | `write-tickets` |
| diagnosis variants | `investigate-bug` |
| Older same-name `tdd`, `prototype`, `research`, `pr`, broad `work-on` | Corresponding approved new owner, full-package backup before overwrite |
| Older setup/assessment/domain/preflight or other same-name copies | Include only if confirmed replaced and exact scope approved; independently needed companions stay active |

Backups and machine-specific migration records stay private, outside this public repository and every active discovery root. Preserve historical source, attribution, local modifications and verified recovery copies. [Migration boundaries](composable-delivery.md#installed-copy-transaction-and-rollback-boundaries) own transaction/rollback design; this table is not a removal script.
