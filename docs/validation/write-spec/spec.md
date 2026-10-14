# Export the filtered reading list

## Agreement and rationale

Approved synthetic behavior from `agreement-1` in [the input](agreement.md). A reader exports visible reading-list entries for spreadsheet use. Existing read-only list behavior is retained. This spec is an expression of those decisions, with no new commitments or discovery session.

## Behavior and acceptance

| ID | Observable outcome |
| --- | --- |
| AC1 | A manual export produces UTF-8 CSV containing only loaded entries visible under the current filter, in their displayed order. |
| AC2 | The first row contains `title` and `author` headers; an empty filtered list produces this row with no data rows. |
| AC3 | Reading the exported CSV preserves each title and author, including commas, quotes and line breaks, through CSV quoting. |
| AC4 | Export leaves the existing read-only list unchanged. |

## Dispositions

- Required now: filtered manual export and field-content preservation (AC1–AC4).
- Deferred: choosing columns; revisit after spreadsheet feedback.
- Excluded: scheduling and background jobs; the agreed workflow is manual.
- Accepted limitation: only loaded entries export; fixture owner accepted pagination outside scope in `agreement-1`.

## Decisions, authority and readiness

Behavior and dispositions are approved in the synthetic input. No new proposal or assumption is required. Shared design for filtering remains unresolved; product approval is not technical readiness. Publication is permitted only to the local fixture with mapped specification role `product-agreement`, not `delivery-task`; `agent-actionable` is not authorized. No tickets, native graph changes or implementation follow. Existing authoritative matches are reused rather than duplicated.
