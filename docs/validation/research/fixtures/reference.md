# Synthetic Retry Client reference

Synthetic first-party documentation for offline research exercises only; not a real product or external API.

Revision: reference-2.0-a. Published: 2026-10-01. Applies to version 2.0.

## Retry behavior

The client allows three total attempts, including the initial request. Attempts after the first retry immediately; there is no documented delay guarantee.

## Runtime

The supported runtime is version 20. This requirement is independent of the retry setting.
