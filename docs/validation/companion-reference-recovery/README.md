# Companion reference recovery — #118

## Agreement and scope

Issue #118, REF1–REF5: recover incomplete required reads, resolve documented references at the discovered package location, inspect ENOENT before declaring a capability unavailable, retain read-only recovery authority and existing compatibility/permission gates. No aliases, installations, setup invocation, graph-procedure changes, private session logs or global skill updates.

Source baseline: `d851e66a80375c51fd9b5dd43b254a2de34642a9` (`origin/main` at entry). Branch: `fix/recover-companion-references`, PR target `main`. Entry working tree/index were clean; the prior branch's PR was merged. GitHub's paginated blocked-by/blocking responses were empty; the parent endpoint explicitly reported “No parent issue found.” No tracker relationships were changed.

One lead implemented directly using Build and Check: first the shared contract and immediate diff/clause inspection, then caller pointers and immediate diff inspection, then validation/changelog pointers. The shared contract owns recovery; callers point to it. Setup Project remains a read-only library for delivery callers, not a new dependency on Work On for ordinary setup.

## Executed static checks

- `git diff --check`: passed after each increment.
- A Python standard-library check inspected Markdown links and heading anchors in all three complete packages, then copied each package into a separate temporary parent and repeated with no sibling companions: Work On 86 links, Work On Spec 19, Setup Project 36; all resolved in both layouts.
- Entry frontmatter inspected in each copied package: opening delimiter and package name checked mechanically; descriptions and existing invocation gates inspected directly. No metadata behavior changed. No runtime frontmatter parser or rendered preview was exercised; headings, tables, fences and link syntax were inspected as Markdown source.
- Incoming references inspected with `rg` across Work On Spec, Work On's capability contract and Setup Project's entry. No graph algorithm was copied, filename alias added or sibling installation path introduced.

## Executed direct synthetic procedure walkthrough

A lead-operated Python heredoc used `tempfile.TemporaryDirectory`, `shutil.copytree`, actual file reads/directory listings and SHA-256/content-mode manifests. It deleted only its owned temporary tree on exit. The actions below were deliberately selected by the lead, not autonomously selected by another agent. Assertions check fixture observations, not model adherence.

| Case / acceptance | Actual observation |
| --- | --- |
| Combined output omits pointer — REF1 | A synthetic partial view of the current contract stopped before Required capabilities and contained no tracker filename. A focused complete read recovered the actual `references/issue-tracker.md` pointer before using it. This models incomplete visibility, not a test of a runtime truncation implementation. |
| Different filename — REF2 | The copied Setup Project entry's `tracker integration` Markdown link resolved to `references/issue-tracker.md`, not the initial assumption `tracker.md`. Its actual reference listing contained the documented filename. |
| ENOENT then recovery — REF3 | Reading the copied package's guessed `references/tracker.md` raised actual `FileNotFoundError`. Complete entry and layout inspection located the documented reference; its content included Native GitHub graph. The library's authority and semantic requirements were inspected before continued use. |
| Genuinely missing material — REF3–REF5 | A second disposable copy deliberately omitted the documented reference during fixture setup. Entry read, actual missing-target error and directory listing established the required material was absent. The walkthrough recorded only the dependent graph route as blocked; it created no replacement, alias or stub and invoked no setup/install/graph operation. |
| Independent installation — REF2, REF5 | Setup Project was discovered in its separate temporary parent; the entry-relative tracker read succeeded without Work On or any sibling at that location. Existing compatibility and permission requirements remained in the inspected material. |
| Read-only recovery — REF4 | Content/mode manifests before and after recovery matched, including the already-incomplete copy. Deliberate fixture construction/removal is separate from recovery actions. |

All heredoc assertions passed (exit 0). To repeat: copy the three packages under separate temporary parents, check their internal links/anchors, expose only the contract prefix before Required capabilities, reread the complete contract, try the wrong tracker path, then inspect the full copied entry/link/layout and read its target. In a second copy omit that target before capturing the baseline; repeat pointer/layout/error inspection and compare manifests without creating a replacement.

## Evidence boundaries and documentation disposition

These checks establish source/link integrity and the observed direct procedure paths. Autonomous agent adherence, runtime retained-output behavior, live tracker mutations and optional model calls were not tested. Existing offline workflow fixtures are separate regression evidence, not proof of these agent decisions; exact command results and independent review reports belong in the delivery PR.

Updated homes: Work On's shared capability contract and validation cases, Work On Spec's contract-consumption/validation pointers, Setup Project's library-entry/validation pointers, and the existing Unreleased Work On Added entry. No domain meaning, ADR, accepted delivery design, native graph requirement, runtime/tool assumption, label vocabulary or installation contract changes. Package/root overviews remain accurate; no index change is needed because no skill or public entry point was added. Compatible bug-fix impact: patch; no release is authorized. Issues remain open until accepted and merged.
