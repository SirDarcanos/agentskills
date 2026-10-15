# Approved setup handoff

Use this only when a requested setup workflow supplies an explicit handoff. Discovery by another agent is not authorization to mutate.

## Inputs

The caller supplies:
- target directory and owner/repository identity;
- create-new or configure-existing route;
- inspected state and organization constraints, with evidence/unknowns;
- exact proposed or approved files, settings, branch/ref rules, actor IDs and bypass modes;
- exclusions, push/commit choices, capability limits, and approval status.

For a **plan-only** handoff inspect and return the proposed delta and blockers; do not execute. For an **approved** handoff reuse the exact decisions after checking freshness. Do not repeat the interview, assume missing permission, or apply an extra setting “by default.” Missing consequential choices return to the caller before execution.

## Ownership

This skill owns repository creation/configuration and its security baseline. The caller owns the larger approval plan, operating/domain docs, tracker labels, and issue-relationship guidance. It may execute the specialist procedure directly when the runtime has no skill invocation tool. It need not launch another agent.

Read SKILL.md in full and follow its existing/new route and verification rules. An absent permission or unsupported required control is reported to the caller, not worked around with a weaker baseline. Do not invoke other setup frameworks.

## Output

Return:
- verified target and route;
- actual local/remote changes, preserving unrelated state;
- settings deliberately retained or omitted;
- read-back evidence per approved operation;
- blocked/deferred/unverified actions and exact constraints;
- any fresh decision requiring approval.

A successful command with no read-back is not verified. A failed write may have applied; inspect before retry. Never claim full readiness if a required protection remains blocked.
