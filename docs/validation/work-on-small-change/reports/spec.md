# Spec review — #29 synthetic small change

## Agreement and snapshot

- **Source revision:** `e171a9b5f18495d5f388a1daeaa0dcdfba08527e`, as identified by the packet; Git revision metadata was not independently resolved.
- **Non-Git scope pointer:** `docs/validation/work-on-small-change/scope.md`, supported by `scope.json`.
- **Agreement:** fixed `fixture/baseline/REQUEST.md:3–24`, acceptance IDs F1–F4. Its delivered copy is unchanged.
- **Included changes:** `file_types.py`, `test_file_types.py`, README behavior text.
- **Protected exclusions:** `unrelated-note.txt` and `note-link`. Their contents were not read, and the link was not followed; only supplied metadata was inspected.

Paths below are relative to `docs/validation/work-on-small-change/` unless otherwise specified.

## Independence and authority

This is the **Spec-only, task-2 reviewer context**, separate from the implementation author. I did not inspect the Standards report or rely on another reviewer’s conclusions.

The user authorized bounded read-only inspection with a ten-minute timeout. Outer `AGENTS.md`, `docs/agents/project.md`, and `docs/agents/workflow.md` govern authority and evidence reporting. No edits, shell execution, scripts, network requests, delegation, optional assessments, acceptance, merge, release, or tracker operations were performed.

## Per-criterion coverage

| Criterion | Delivered behavior and assertions | Recorded evidence | Disposition and gaps |
|---|---|---|---|
| **F1 — extension case** (`fixture/baseline/REQUEST.md:12`) | `fixture/delivered/file_types.py:4–5` compares the lowercased final three characters with `.md`, producing a Boolean. `test_file_types.py:7–13` checks lowercase and all three non-lowercase ASCII combinations. | `evidence/red.json:78–79` records three direct assertion failures for `notes.MD`, `notes.mD`, and `notes.Md`. Green and integrated records report those assertions passing. | **Covered.** Red demonstrates sensitivity to the intended missing behavior, not a dependency/tool failure. |
| **F2 — final suffix; no trimming** (`REQUEST.md:13`) | Slicing only the final three characters preserves suffix-only classification and does not trim. Unchanged assertions at delivered `test_file_types.py:19–25` reject empty names, extensionless names, `.txt`, `.markdown`, `.md.bak`, and trailing whitespace. | Baseline, red, green, and integrated `output` fields record both negative-test methods passing. | **Covered.** Short strings are safe under slicing. Mixed-case negative examples are not separately asserted, but the inspected expression preserves the same final-position and whitespace boundaries. No material gap identified. |
| **F3 — unchanged names, order, duplicates** (`REQUEST.md:14`) | Sole caller `fixture/delivered/file_types.py:8–9` is unchanged: it filters without transforming returned names. Tests at `test_file_types.py:15–17,27–29` assert exact lists for mixed-case and original lowercase inputs, including order and duplicates. | Red records `['plain.md']` instead of the expected mixed-case list; original caller test still passes. Green/integrated record both caller tests passing. | **Covered.** Exact-list assertions would detect lowercased output, dropped duplicates, sorting, or lost original lowercase matches. |
| **F4 — bounded changes; protected work** (`REQUEST.md:15`) | Full `delivered.diff` changes exactly the three authorized files. Agreement, instructions, and caller remain unchanged. Both directory inventories contain the same seven entries. | `scope.json` baseline/delivered manifests differ only for the three owned files. All four records have equal before/after manifests. Protected note hash/mode and symlink target/mode match throughout. | **Covered by supplied manifest evidence.** Protected contents remain excluded. Current on-disk hashes/modes were not independently recomputed by this reviewer. |

### Failure paths and regression sensitivity

Static inspection confirms a pure string classifier with no filesystem access, persistent state, credentials, disclosure, or destructive product operations (`file_types.py:1–9`). Those product failure categories are inapplicable to this fixture; preservation of unrelated artifacts remains explicitly covered by F4.

The red run isolates the delivered test additions against baseline implementation and README hashes. Its four failures are the three mixed-case subtests plus the caller assertion. Existing negative, whitespace, lowercase, and original caller checks remain passing. This is meaningful regression sensitivity for F1/F3, not universal mutation coverage.

No API expansion, additional extensions, CLI, configuration, filesystem inspection, dependency, or abstraction was introduced. These exclusions agree with `fixture/baseline/REQUEST.md:17–24`.

## Checks and evidence classification

**Recorded lead execution, not reviewer execution:** all four JSON records specify `python3 -B -m unittest -v`, `<fixture>` working directory, and Python `3.14.7` (`:76–80`).

| Record | Result | Inspected state |
|---|---|---|
| `evidence/baseline.json` | Exit 0; four tests pass | Baseline implementation and assertions |
| `evidence/red.json` | Exit 1; six methods, four assertion failures | Baseline implementation with delivered assertions |
| `evidence/green.json` | Exit 0; six tests pass | Delivered manifest |
| `evidence/integrated.json` | Exit 0; six tests pass | Same delivered manifest |

**Static reviewer inspection:** actual sources, assertions, complete patch, record fields, manifest relationships, capture semantics, and replay/freshness logic.

`capture.py` preserves the test subprocess’s exit/output separately from capture success. `verify.py` checks manifest relationships and provides an explicitly labeled scripted replay; it does not execute Work On agents.

Green and integrated records are byte-identical, including their pinned hashes. This is consistent with deterministic capture of identical results, but does not independently establish two distinct execution events. The second-run provenance is the lead’s account; neither record represents independent reviewer execution.

**Not run:** unittest, capture, replay, freshness verification, cross-runtime checks, or live/production checks. No such execution is claimed here.

## Documentation

The README change at `fixture/delivered/README.md:3` accurately describes the extension-case fix. Lines 4–6 retain the promises of unchanged names, order, duplicates, string inputs, and no filesystem/content inspection. The documented check command remains unchanged.

Fixture `AGENTS.md:16–17` explicitly requires README maintenance and establishes no changelog/version policy. `plan.md`, “Documentation owner,” justifies no outer changelog entry because this delivery retains synthetic evidence rather than changing a shipped skill’s public behavior. No documentation contradiction was found.

## Inspected files

Read completely:

- Repository `AGENTS.md`, `docs/agents/project.md`, `docs/agents/workflow.md`.
- `review-delivery/SKILL.md`, `references/scope.md`, `references/report.md`.
- `work-on/references/contracts.md`, `work-on/references/verification.md`.
- Packet `scope.md`, `scope.json`, `plan.md`, full `delivered.diff`, `capture.py`, `verify.py`.
- Both baseline and delivered copies of `AGENTS.md`, `REQUEST.md`, `README.md`, `file_types.py`, and `test_file_types.py`.
- All four evidence JSON records.

Inspected baseline/delivered directory membership twice. No additional directory-scoped `AGENTS.md` was discovered under `docs` beyond the fixture copies.

## Freshness and limitations

The packet names the lead as freeze owner. Inspected source changes, assertions, manifests, and raw outcomes are internally consistent; no stale or inaccessible material input was observed.

However, supplied fingerprints are not independent recomputation. This reviewer did not verify current file modes, protected hashes, all supporting-input hashes, or the post-review freshness comparison. Directory membership was unchanged between this reviewer’s two observations. The final fingerprint/path-discovery gate remains with the lead after both reports return.

This result covers the synthetic F1–F4 fixture—not the full #29 workflow trial, other workflow branches, production suitability, or the other review axis.

## Review

- **Correct:** F1–F4 have inspected behavior and relevant recorded evidence; caller and documentation promises are preserved; the change stays within authorized scope.
- **Fixed:** None; read-only review.
- **Findings:** No issues found.
- **Merge verdict:** **OK with notes** for the inspected Spec axis only, subject to freshness confirmation. This is not acceptance or merge authorization.

**Outcome:** Spec content/evidence inspection completed; final freshness confirmation remains outstanding.

**Next action:** The lead should complete the existing scoped freshness/path-discovery comparison after both reviewers return—for example, the default read-only `python3 -B docs/validation/work-on-small-change/verify.py` check—and record its outcome. Any material drift requires repinning and renewal of affected checks/review before these results are consumed.