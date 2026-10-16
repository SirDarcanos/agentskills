# Direct native tracker library delivery evidence

Source-development evidence for #156 under #132 (WF-11, retaining WF-06/WF-14); not a copied-skill prerequisite. Setup Project remains the package owner. No installed copies, tracker roles/edges, permissions or stage selection change.

## Agreement and scope

- Consumers discover the actual Setup Project package root and read `references/native-tracker.md` directly. Its discovery/authority contract needs neither setup entry nor label audit; missing/incompatible libraries block the dependent route without installation.
- The library owns the existing role/title/readiness text and unchanged native graph algorithm/recipes/helper limits. Readiness is not scheduling eligibility. #145's behavior correction is not reimplemented here.
- Setup retains its approved audit. `references/issue-tracker.md#native-github-graph` remains a forwarding target. Older installed versions without the new library are explicitly incompatible with the new route, not silently updated.
- Write Tickets, Write Spec publication, Work On and Work On Spec incoming runtime callers use the direct entry. Repository tracker guidance and package READMEs point to the same owner.

## Reproducible reading surface

Run from this source checkout:

```sh
python3 -B docs/validation/session-delivery/measure_reading.py --base 45e5a24
python3 -B docs/validation/native-tracker/check.py
```

Count full files once per context with Python whitespace splitting, not tokens or timing. Baseline `45e5a24` uses its actual guidance. Candidate uses current guidance and actual mandatory references, not proposed sketches. Established local cause, no material source/technical/domain gap, no new record, no optional delegation or helper execution, and familiar native operations select no extra branch references. README/license/maintenance checks are not runtime instructions. No public writes are performed for this measurement.

Equivalent endpoint is investigation followed by the selected ticket stage (baseline necessarily prepares tickets). Baseline total: **10,678** words. Candidate total: **8,980**, **1,698 fewer (15.9%)**. The earlier issue observation of 11,305 is historical, not substituted for the acceptance baseline.

| Candidate required input | Words |
| --- | ---: |
| AGENTS.md | 549 |
| docs/agents/project.md | 361 |
| docs/agents/workflow.md | 1,623 |
| docs/agents/issue-tracker.md | 501 |
| docs/agents/triage-labels.md | 803 |
| workflow/investigate-bug/SKILL.md | 1,713 |
| workflow/investigate-bug/references/ticket-stage.md | 433 |
| workflow/write-tickets/SKILL.md | 2,024 |
| workflow/setup-project/references/native-tracker.md | 973 |

The candidate selected ticket path preserves publication/read-back and draft overrides. Diagnosis-only is a distinct endpoint: **4,246** words, no tracker stage/access. Its savings are not claimed as equivalent ticket-endpoint savings. Missing tracker capability blocks selected ticket work, not supported diagnosis or local drafting. Static counts do not establish agent adherence.

## Validation and limits

Relevant commands (safe offline fixtures only):

```sh
python3 -B -m unittest discover -s workflow/setup-project/tests -p 'test_*.py'
python3 -B docs/validation/native-tracker/check.py
python3 -B docs/validation/write-tickets/check.py
python3 -B -m unittest discover -s docs/validation/write-tickets -p 'test_*.py'
python3 -B docs/validation/write-spec/check.py
python3 -B docs/validation/investigate-bug/check.py
python3 -B -m unittest discover -s docs/validation/investigate-bug -p 'test_*.py'
python3 -B -m unittest discover -s docs/validation/bug-to-fix -p 'test_*.py'
git diff --check
```

The direct-library check inspects all six runtime incoming routes, repository tracker links, and source/isolated copies of the five affected packages: frontmatter, anchors/links, Python syntax, notices and no source Git metadata. Setup's 27 checks cover helper reconciliation and direct/legacy library placement. Existing tracker fixtures retain authorization, role/readiness, pagination, ID, cycle/conflict and partial-write assertions unchanged.

Instruction portability inspection: the library resolves from runtime/project metadata, uses target-project authority/authentication, and links only to a shipped helper or public API documentation. No collection Git revision, issue or development record is a runtime prerequisite. The source comparison above deliberately stays outside shipped packages.

Raw execution logs and independent axis reports are retained by the delivery session. Static package checks and scripted synthetic persistence are not independent agent workflow trials or live GitHub certification. Live mutations, live-host failure paths, automatic installation/migration and independent end-to-end publication trials are unrun; none is authorized as a test here. The optional helper implementation is unchanged.

Documentation impact: update the existing Unreleased Setup Project Added entry; update package library/forwarder documentation, actual callers, tracker guidance and this evidence. No new domain meaning or ADR; no version bump, PR publication, issue closure, merge or release is selected by this request.
