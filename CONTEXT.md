# Agent Skills vocabulary

**Skill package:** An independently installable unit of agent instructions, with a `SKILL.md` entry point and any shipped references, scripts, or assets. This is the source/distribution unit, not the project an agent will modify when using it.

**Entry point:** The `SKILL.md` that declares a skill's invocation conditions and working instructions. Supporting material is reached through its conditional pointers; an entry point is not the full instruction set by itself.

**Companion skill:** A separately maintained skill that owns a specialist responsibility needed by another workflow. The caller discovers a compatible companion and follows its contract; sharing an installation directory is not part of that contract.

**Handoff:** A bounded transfer of scope, evidence, confirmed decisions, authority, and expected results to a specialist procedure. A plan-only handoff permits inspection and recommendations without writes; an approved handoff permits the exact authorized operations. A handoff does not inherently launch another agent.

**Target project:** The repository or directory where a skill is being applied. Its operating documents and domain records belong to that project, not to the skill package that generated or maintains them.

**Installed skill:** The copy or link exposed through an agent runtime's discovery mechanism. A separately installed copy needs its own update; a symlink reflects changes to its linked directory. A repository merge alone does not refresh separate installed copies.
