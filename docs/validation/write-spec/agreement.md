# Synthetic agreed input

Fixture owner approved this behavior and limitations at revision `agreement-1`; this is not a real product commitment.

Write a specification for exporting the reading list. A reader exports only the currently visible filtered entries as UTF-8 CSV, in displayed order, with `title` and `author` headers. An empty filter exports the header row. CSV quoting must preserve commas, quotes and line breaks in fields. The existing read-only list is unchanged. The purpose is to use a filtered list in a spreadsheet.

Required now: filtered export and preserved field content. Deferred: choosing columns, reconsidered after spreadsheet feedback. Excluded: export scheduling and background jobs because this is a manual action. Accepted limitation: fixture owner accepts that only loaded entries are exported; pagination is out of this change.

The authoritative home is the existing tracker spec if one matches; otherwise the fixture spec body. Specification approval is given, but shared design (where filtering occurs) remains unresolved; no readiness grant. Fixture-only publication authority: create one specification and apply mapped `product-agreement`, preserving unrelated labels. No work-ticket creation, graph changes or implementation. Fixture title convention requires `Proposal: <subject>`; work-ticket role is `delivery-task`, ready role `agent-actionable`.
