# ADR 0004: Keep skill packages independent of their source repository

**Status:** Accepted. The maintainer confirmed that skills must stand alone without requiring agents to consult this repository's commits, issues or pull requests, then explicitly requested that Domain Modeling document the recurring boundary failure in the repository. This records that existing distribution requirement and its validation consequence; it grants no installation, merge or release permission.

## Context

A skill's source repository, its independently copied package and the target project where it is used are different contexts. [The vocabulary](../../CONTEXT.md) distinguishes them. [ADR 0003](0003-session-oriented-project-agreement.md) places common operating guidance in the target project; that is not a dependency on this skill collection's operating documents or development history.

During the implementation-method simplification, a delivery-specific reading comparison against a source commit was copied into five shipped validation references. Copied-package link and fixture checks passed, but those checks did not exercise the written historical-comparison requirement. The maintainer identified the dependency and reported that this class of mistake had occurred more than once. The concrete failure here was treating development evidence as reusable procedure and checking file/script portability without checking instruction portability. This explains the observed failure; it does not establish the cause of every earlier occurrence.

## Decision

The installed or copied package is the distribution boundary for its instructions, shipped references, scripts and fixtures. Ordinary use and package maintenance validation must not require a checkout of this skill collection, its Git metadata, commit baselines, issues, pull requests, design records or delivery reports. Reusable behavior and check expectations belong in the package itself; source-specific history and measurements belong in repository development evidence outside the package.

The target project's applicable instructions and task evidence remain legitimate inputs. A Git or tracker skill may inspect that target's history or issues when its requested task calls for it. Compatible companions may be discovered through the runtime under their own contracts; independence does not mean every specialist must be bundled or every task works without its actual tools. Source attribution and optional installation/documentation links are allowed, but may not carry instructions or expectations needed to complete the package's procedure.

For example, a copied method can run its shipped fixture from its own directory. Requiring a commit from this collection to compare reading costs is a source-repository dependency, even when it appears only in a maintenance reference. Resolving the link or successfully running a different fixture does not validate that requirement.

## Consequences and validation

- Review all reachable instructions, including conditional references, README commands, fixtures and embedded prompts, for source-repository assumptions. Do not limit portability review to `SKILL.md` or file links.
- Validate a copied package without the source checkout, its Git metadata or access to this collection's tracker. Walk the written procedure as well as running its scripts; distinguish target-project/tool requirements from accidental source dependencies. Report unexercised branches rather than treating successful fixture execution as complete instruction validation.
- Keep reproducible source-history comparisons, issue acceptance mapping and per-delivery reports in repository evidence or the selected tracker destination. Do not turn those records into consumer prerequisites or remove preserved historical evidence as cleanup.
- Prefer shipping the reusable example or expectation over a pointer to development history. The cost is maintaining that useful material with the package; the alternative would make an independently installed skill depend on a separate evolving checkout or tracker.

This clarifies the existing independent-package contract without superseding ADR 0003, changing method semantics or authorizing a repository-wide migration. Source corrections do not update separately installed copies.
