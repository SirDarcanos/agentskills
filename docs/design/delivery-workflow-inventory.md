# Delivery skill inventory and provenance

Evidence for [#18](https://github.com/SirDarcanos/agentskills/issues/18). Read when assessing legacy compatibility, importing source material, or checking the assumptions behind the [design contract](delivery-workflow.md). These are observations of the inspected installation, not claims that upstream still has identical behavior.

## Observation boundary

The repository baseline was `84ec29844bea7225baf3ab47884347d1b6e5b46b` (the merged operating agreement). Inspected the complete installed `SKILL.md` files below, relevant local package contents, installation source metadata, repository-owned companions, and the #14/#18 issue bodies. The legacy delivery entry points were inspected, not executed. No installed skill files were changed and nothing was installed. No workflow agents or model assessments were launched.

The installation metadata identifies the first eight entries as `mattpocock/skills`, with paths under `skills/engineering/` except `grilling` under `skills/productivity/`. It records folder hashes, not a reliable source commit for every installed byte. Installed files can be locally modified; the content digests below identify what was actually read. Package-local `agents/openai.yaml` files exist but are not evidence of cross-runtime support. No package-local license was found in those inspected eight directories.

| Installed entry point | Observed behavior | Design disposition |
| --- | --- | --- |
| `implement` | Command-only; recommends TDD where possible, pre-agreed seams, repeated typechecks/tests, review before committing to the current branch | Preserve direct building and local checks as responsibilities; new build procedure adds preflight and contextual verification. Do not invoke this command internally. |
| `implement-spec` | Model-invocable; requires a single integration branch, concurrent worktree implementers, literal Skill-tool TDD per implementer, a merger agent and final cleanup | Preserve graph/frontier and context-pointer concepts; use project branch policy, bounded ownership and safe failure handling instead of inheriting this execution policy. |
| `code-review` | Model-invocable; two parallel Standards/Spec agents inspect `git diff <base>...HEAD`; rejects an empty committed diff; asks for a base if absent; skips Spec if unavailable | Retain the two perspectives, not the committed-only scope or fixed tool assumptions. `review-delivery` must cover actual dirty work and require a brief/spec for delivery acceptance. |
| `grilling` | Model-invocable; asks the entire available question frontier, treats decisions as the user's, delegates fact-finding and stops only when all branches are visited | New product-agreement procedure asks manageable rounds, owns routine engineering and allows explicit deferral while preserving relevant discovery breadth. |
| `to-spec` | Command-only; requires user confirmation of test seams, extensive user stories, a setup-command fallback and automatic `ready-for-agent` labeling | New spec procedure captures product behavior and exclusions, uses target context, applies the mapped `spec` label and evaluates readiness separately. |
| `to-tickets` | Command-only; session-sized vertical slices, approval of breakdown, dependency links, automatic readiness; native features when available but prose fallback otherwise; prohibits parent edits | Preserve bounded cohesive work and approval. New ticketing obeys the target's exact parent/blocker policy, reconciles native edges and requires agreement for alternatives. |
| `tdd` | Model-invocable; behavior/public-interface tests, red-before-green, one slice at a time; requires user-confirmed seams and postpones refactoring to review | Preserve behavior-focused testing as a method. New build procedure permits relevant green refactoring and lead-owned technical choices; this installed skill is not an automatic companion. |
| `codebase-design` | Model-invocable reference; deep modules, small interfaces, leverage/locality and explicit vocabulary; linked optional design exploration | Use #14's existing requirements for useful interfaces and locality. Do not impose this external glossary over a target's domain vocabulary or invoke its optional exploration automatically. |
| `implementation-preflight` | Repository-owned; checks work/branches/PR state, preserves work, prefers explicit branch conventions and prepares a short-lived branch | Reuse as a semantic companion before Git implementation; target policy wins over incidental branch names. Installed entry point matched the repository copy at inspection. |
| `domain-modeling` | Repository-owned; separate bounded plan-only/approved handoffs, confirmed/proposed distinctions, selective ADRs and preserved history | Reuse when meanings/models or qualifying records change. Installed entry point matched the repository copy at inspection. |

No installed `work-on`, `review-delivery`, `analyze`, `dispatch`, or `verify` directory was found in the inspected skill root. Discovery on another machine may differ. This inspection does not authorize replacing a colliding installation.

### Installed entry-point fingerprints

SHA-256 of each observed `SKILL.md`; these identify source observations, not runtime certification or upstream commit IDs.

```text
implement                 6d3fd9e83b8f36e5213854779db49b256a457a7ebb4a503e53fa7dcff696adc3
implement-spec            ff50f779d9dfd35d3edf30987a637d9aeb1fa453299cf3552be1aea55b3329db
code-review               47f4e52c21694def9c7c11cbfbf891ca35eac7a93e395797515be3c8a409ae50
grilling                  10ff989e7498b23b5acb49d5048f11dcd906757d2f79c5cdf8a00001381296f2
to-spec                   43ad9cf318e5e7d3d1fa360253a37021796dc87a0c2e595ad262661a10f85088
to-tickets                5c9fba69845c2519b9b35b9af42ae5142c21f8ca15ac2123dc2722002c8058ae
tdd                       cb01f66bebfaa25fa1f88e6b7e769cd9fd9f35b1120b8563749820738814c927
codebase-design           2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2
implementation-preflight  ccb940cb60819792947274f1d848636c6461d47ae3856bae80fcd83d1df39d15
domain-modeling           aae04989a6039707b20ca44c65b2fb9ebc0a7b35f408fc46f4ded5446ca21986
```

## License decision

Read the upstream [MIT license at commit 49dd158](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE), retrieved through the GitHub contents API with that exact ref. Its copyright is **2026 Matt Pocock**; the license file blob is `f1dd2c09108dde1a5f56097cee8461b3ea834499`. This is evidence for that revision's license, not proof of the installed copies' original revision. The receiving repository's [license](../../LICENSE) is MIT, copyright 2026 Nicola Mustone (maintainer name corrected after this inventory; the upstream observation above is unchanged).

The selected approach is newly authored procedures from the approved #14 behavior, not importing external skill bodies, templates, examples, smell catalogs or configuration. This design records factual observations and attribution; no external implementation is vendored by #18. Existing notices remain untouched. No new third-party license file is necessary for this no-import change.

If a later implementer proposes copying or adapting upstream material, inspect the exact source revision and applicable notices first. MIT permits compatible reuse but requires retaining the copyright and permission notice in copies/substantial portions. Carry the complete applicable license/attribution inside each independently distributed package containing that material; a link to this design or the repository's differently attributed root license is insufficient. If exact provenance or permission remains unresolved, continue with original implementation rather than assuming the install lock establishes permission. Reassess any third-party material embedded in the proposed source independently.

## Remaining limits

The installed instruction inventory and license lookup were inspected directly. There was no executed agent workflow trial, independent review, or assertion that the installed material matches current upstream files byte-for-byte. Do not turn these observations into install/update instructions; #31 owns future installation guidance and its actual validation evidence.
