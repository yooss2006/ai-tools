# Incident / Postmortem Profile

## Purpose

Create a durable, blameless learning record of an incident: impact, sequence, contributing factors, response effectiveness, and corrective actions.

## Default structure

```markdown
# [Incident title]

## Summary

## Impact

## Detection

## Timeline

## Contributing factors / root causes

## Response and recovery

## What went well

## What did not go well

## Corrective and preventive actions

## Lessons learned
```

## Primary / secondary types

- Primary: Explanation
- Common secondary: Problem solving

## Guidance

- Describe system/process conditions, not personal blame.
- Separate observed facts from causal interpretation.
- Include impact in terms meaningful to users/business/operations when known.
- Timeline timestamps should use one timezone and format.
- Action items should have an owner/status/tracking link when the team's system supports them.
- Avoid reducing a complex incident to one convenient “root cause” when multiple contributing factors mattered.

## Quality checks

- The document explains how the incident became possible, not only who touched the system last.
- Corrective actions are tied to contributing factors.
- Unverified causal claims are labeled as unresolved rather than asserted.
