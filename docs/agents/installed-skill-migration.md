# Migrate approved installed skills

Use this runbook for an explicitly requested installed-skill migration, standalone or through a bounded handoff. It implements the [accepted transaction design](../design/composable-delivery.md#installed-copy-transaction-and-rollback-boundaries) for [#69](https://github.com/SirDarcanos/agentskills/issues/69); [#74](https://github.com/SirDarcanos/agentskills/issues/74) performs the separately approved real migration after replacement acceptance. Repository edits, fixture approval and merges authorize no installed changes.

The migration lead owns the local record and operations. Inputs are the exact runtime/install mechanisms, current inventory, accepted replacement revision and companions, protected items, and approval for specific backup, retirement, activation, refresh and rollback effects. Output is a private complete/partial/blocked report and retained recovery artifacts. No new skill, package manager or runtime adapter is required. Follow each runtime's documented supported discovery/refresh mechanism; if it cannot be inspected or safely changed, block that route rather than inventing a shell command.

## 1. Inventory and obtain exact approval

Inspect all affected runtime roots, project/global roots, catalog entries, aliases, registrations and installer records, including duplicate installations. Names in the [candidate mapping](../design/composable-delivery-inventory.md#candidate-installed-migration-mapping) are leads for inspection, not retirement authority. Resolve each source and symlink chain without mutating it. Distinguish the active directory/link from its source repository; identify other consumers and independently required companions. Read complete entry points and conditional references before proposing replacement.

Create the private record described below. Compare entire packages with known source revisions where available; record local additions, modifications, deletions and provenance uncertainty. Unknown provenance is not proof of equivalence. Map every observed old target to a replacement or an explicit preserve/blocked decision. Include same-name replacements and duplicates across roots; an unapproved competing copy blocks successful discovery, not permission to remove it.

Present exact targets, before/after effects, coherent replacement sources, shared/protected paths, metadata changes, refresh actions and rollback plan for approval. Required companion compatibility uses semantic discovery and complete source inspection, not sibling-directory assumptions. Missing accepted packages or consequential mapping decisions block retirement. For #74, verify #73's accepted integration and native prerequisite state, not just closure. Record approval provenance and the approved scope; later scope changes need renewed approval.

## 2. Back up and exercise restoration

Choose a private transaction directory outside this public source repository and **every** active discovery root, including through resolved links. Restrict access to the owner; get retention authority for private contents. Put staging, backups, record and restore rehearsal there. Never commit actual machine paths, contents or metadata to public evidence.

Before removing or overwriting anything:

1. Capture the entire old package, including hidden files, references, scripts, assets, local modifications, empty directories, executable modes and internal links. Record a sorted relative-path manifest with entry types, modes, file SHA-256 digests and raw symlink targets. Separately retain registrations, aliases, installer metadata and their checksums. Preserve relevant ownership/ACL/xattr metadata if required for this installation; an unsupported metadata type blocks the affected restore claim.
2. For an active symlink, retain its raw target and link metadata **and** the authorized package contents at its resolved source. Do not recursively copy an unrelated source repository or follow external links without explicit scope. Record external link dependencies and their restore requirements; unresolved dependencies block a complete backup claim.
3. Verify the backup against the captured manifest and metadata, then restore it into an isolated rehearsal directory. Compare the restored full manifest and inspect entry point, shipped links, executable modes and registration metadata. For links, rehearse source resolution against an isolated source copy; restoring only the link is insufficient proof.
4. Retain the original backup and rehearsal result. Recheck the actual old targets against the captured identities immediately before retirement. Any intervening change invalidates destructive preconditions; stop and reconcile rather than overwriting it.

An invalid or incomplete backup leaves the old installation intact. Checksums detect differences; they do not establish authorization or provenance. Freeze affected writers/installers during the transaction or block when exclusive ownership cannot be established.

## 3. Stage a coherent replacement set

Stage whole packages from pinned accepted revisions, with notices and all required companions. Record exact manifests, source revisions and compatibility findings. Check frontmatter/triggers, every shipped relative link/anchor, commands in their named environment and companion resolution outside sibling layout. Use relevant package checks without live model/service calls or incidental installation. Preserve old companions needed for rollback as a coherent set.

Validate staged discovery using the intended runtime's supported isolated mechanism if available. If unavailable, state the limitation and require separately approved bounded activation/read-back; structural inspection alone is not runtime certification. Invalid replacement, missing companions or unresolved registration mechanism blocks retirement. Stage content and verify backups before touching active targets, even when old and new have the same name.

## 4. Retire, activate and read back

Journal intent before each effect and observed outcome after it. Include exact precondition and intended postcondition identities. Flush the record durably before proceeding; use an atomic record update or append-and-flush journal. Keep an unfinished intent distinguishable from success. No generic recursive cleanup is authorized.

1. Recheck approval, ownership, old identities, backups and staged manifests. Retire only approved active copies/links/aliases/registrations. For a shared source, unlink the approved active link only; leave its source and other consumers untouched. Preserve unrelated skills and required companions.
2. Activate only approved replacements and registration changes. Do not let installer defaults broaden affected roots. Record each created copy/link/registration and its expected identity so rollback can recognize transaction-owned effects.
3. Refresh supported discovery, then inspect the actual catalog and resolved sources across **all** affected roots and aliases. Compare replacement manifests, shipped references and discovered companion identities. Verify retired implementations are absent from competing discovery; a same-name entry must resolve to the intended new bytes/source, not merely have the expected name.
4. Mark `discovery-verified` only after the full read-back passes. Keep backup artifacts. A duplicate outside approval, source mismatch or failed refresh is a failure requiring reconciliation/rollback, never a successful migration.

## 5. Reconcile interruption or roll back

On resume, read the existing record first. Inspect actual files, links, registrations and runtime discovery against both recorded before and intended after identities for every unfinished operation. Classify each as not applied, applied, or conflicting/unknown. Mark reconciled outcomes before continuing. Do not blindly replay deletion or replace the original backup with a backup of the new installation. Unknown effects block dependent destructive actions.

Before activation, recovery normally retains the working old installation and private staged/backup artifacts. If retirement already occurred, restore the old installation before calling it intact. After any activation failure:

1. Record `rollback-needed`, stop affected runtime use/writers within approved authority, and inspect actual effects.
2. Reverse only transaction-owned replacement effects within the approved rollback scope, in dependency-safe reverse order. Compare current identity to the expected replacement before removal. An intervening edit or unexpected registration is a conflict: preserve it and report incomplete recovery.
3. Verify retained backups, then restore complete old packages, active links, aliases, registrations and installation metadata. For shared symlink sources, reuse the original source only if its identity still matches. If it changed, do not overwrite shared work; use an explicitly approved isolated recovery source/link update or stop with incomplete recovery. Restore the old broad coordinator and its matching companions together, not a mixture with incompatible new owners.
4. Refresh discovery and compare old source/content resolution and metadata across all affected roots. Retain backups, journal and exact remaining state if any restore step fails. A partial rollback is not `restored`.

## Private record reference

Use the target's approved private home and existing record format (small JSON/Markdown plus manifests is sufficient). These fields are required facts, not a new public manifest standard:

| Record | Contents |
| --- | --- |
| Transaction | ID, accountable lead, runtime/environment, record location, retention/access authority, dates, accepted replacement revision, approval source and exact permitted effects, protected scopes, discovery/refresh mechanism. |
| Inventory | All roots/catalog sources and precedence, actual package/link/alias/registration/install mechanism, resolved source/link chain, shared consumers, source revision or unknown, complete package manifest and metadata, local modifications and external dependencies. |
| Mapping | Stable target ID, exact old→new locations/source identities, rename/same-name decision, duplicate disposition, required companions and compatibility/validation, preserved items, rollback destinations and conflict policy. |
| Recovery artifacts | Immutable old manifest, verified full-package backup and metadata locations/digests, isolated restore results, coherent old companion set, staged new manifests/source/validation. |
| Operations | Ordered operation IDs, exact target, before/after identities, approved effect and inverse, intent/outcome timestamps, raw local read-back/error, created-effects ownership, unresolved state and reconciliation result. |
| Report | State per target and whole transaction, backed-up/replaced/retired/preserved/verified items, failed/unrun checks, discovery results, retained artifact locations, concrete restore instructions, conflicts and next approved action. |

States: `inventoried` → `approved` → `backed-up/restore-tested` → `staged/validated` → `retired/activated` → `discovery-verified`; failures use `blocked`, `rollback-needed` or `restored` with remaining state. Record operation-level states as well: a single aggregate state cannot describe interruption halfway through activation.

## Completion and validation

**Complete migration:** every approved target has verified backup/restore rehearsal, coherent replacement validation, journaled approved effects and actual discovery read-back; protected items are unchanged and backups retained. Stop with the private report; no implicit release, issue closure or backup deletion.

**Partial/blocked:** identify completed effects and exact remaining/unknown state, preserve recovery artifacts, and recommend the smallest next approval or evidence action. Successful sandbox tests mean procedure preparation only, not installed migration completion.

The [offline fixture and actual #69 evidence](../validation/installed-skill-migration/README.md) exercise synthetic disk transactions. Real installer behavior, runtime discovery/refresh, complete platform metadata and private inventory remain #74 obligations under exact approval.
