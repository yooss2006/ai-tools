# Migration Guide Profile

## Purpose

Help an existing user/system move from a known source state to a target state safely, with explicit prerequisites, breaking changes, verification, and recovery options.

## Default structure

```markdown
# [Source]에서 [Target]으로 마이그레이션하기

## Scope and supported paths

## Before you start

## Breaking changes

## Migration steps

## Data / configuration changes  <!-- when relevant -->

## Verify the migration

## Rollback / recovery  <!-- when feasible -->

## Known issues

## References
```

## Primary / secondary types

- Primary: Problem solving
- Common secondary: Reference

## Guidance

- State exact source/target versions or states when migration depends on them.
- Put backups, prerequisites, maintenance windows, and irreversible steps before execution.
- Distinguish automated and manual steps.
- State what success looks like after each risky stage when practical.
- Include rollback only if it is real and tested/credible; do not promise reversible migration by default.

## Quality checks

- The reader can determine whether the guide applies to their current state.
- Breaking changes are discoverable before the migration steps.
- Verification is concrete.
- Irreversible operations are explicitly marked.
