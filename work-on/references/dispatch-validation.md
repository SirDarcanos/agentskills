# Dispatch validation compatibility pointer

Current scheduling, integration and overall recovery validation belongs to discovered `work-on-spec` and its shipped validation references. Resolve that package independently of sibling paths and read its full entry before applying its checks.

Validate the [dispatch pointer](dispatch.md) as a pointer only: no old scheduler may run when the coordinator is missing/incompatible. Work On's [single-change checks](single-change-validation.md) must still pass, with local evidence/repair/recovery and shared limits preserved. Historical repository #14 dispatch/multi-ticket trial records remain unchanged, not proof of the new coordinator's runtime behavior.
