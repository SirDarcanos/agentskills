# Synthetic receipt delivery agreement — revision 1

Local-only trial for #72 / #48 AC2, AC3, AC4, AC10, AC11, AC13, AC15.
Approved by the maintainer in the parent session. This is a disposable local
tracker, not production GitHub issues or a substitute for live API validation.
Graph.json stores roles, parent membership and both dependency directions.

- A: render(name) returns "Receipt: " + name. Own render.py only.
- B: normalize(name) trims strings; blank or non-string input raises ValueError.
  Own normalize.py. First attempt deliberately returns partial after trim only
  and an observed rejection-test failure; no further repair in that assignment.
- D: add keyword-only upper=False to normalize; upper=True uppercases the
  trimmed name, preserving B's rejection/default behavior. Own normalize.py.
  No native prerequisite, but serialized behind B's exclusive interface owner.
- C: make_receipt(name) composes normalize(name, upper=True) and render.
  Own pipeline.py; blocked by accepted integration of B and D.

Tests are supplied acceptance examples; workers may not weaken/edit them.
No new product design/analysis is needed: inspect the supplied technical record
and deciding files and reuse current facts. Refresh only changed inputs.

Policy: root alone integrates scoped patches and commits in this disposable
repository. Local implementation is not acceptance. Required prerequisite
acceptance = inspected integration, relevant passing checks, both independent
review axes and root disposition. No PR/remote/merge requirement inside this
fixture. Repository delivery still targets a real PR on main with no merge.
Root owns shared interface decisions, execution ledger, worker launches and
final integration checkpoint. At most two active non-lead assignments (including
read-only gates/review), no recursive delegation, finite runtime per assignment.
B checkpoint B-reject: maximum two correction cycles; partial cycle one spends
one, resumed cycle two uses the remaining one. No reset on resume or owner switch.
Optional assessment allowance is zero; no calls/reservations/services/substitution.

Protected: staged+unstaged protected.txt, protected-link symlink, untracked
private-note.txt. Preserve bytes, index entries, modes and link target. Workers
must not stage/commit or touch files outside their single module. Temporary
outputs go outside worktrees. No cleanup or installed-source writes.
