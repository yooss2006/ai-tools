# RFC / Technical Proposal Profile

## Purpose

Propose a substantial technical change before it is fully decided, make the problem and design inspectable, and enable review of tradeoffs, risks, alternatives, and unresolved questions.

## Use when

- a change affects multiple modules/teams or a public contract;
- implementation is costly enough that design review should happen first;
- alternatives and drawbacks need explicit discussion;
- important questions remain open.

## Default structure

```markdown
# [Proposal title]

## Summary

## Motivation / problem

## Goals
## Non-goals  <!-- recommended when scope is easy to expand -->

## Proposed design

## User / developer experience  <!-- when relevant -->

## Detailed design

## Drawbacks and risks

## Alternatives

## Rollout / migration  <!-- when relevant -->

## Observability / operations  <!-- when relevant -->

## Security / privacy  <!-- when relevant -->

## Unresolved questions
```

## Primary / secondary types

- Primary: Explanation
- Common secondary: Problem solving or Reference

## Writing guidance

- Motivation should establish the real problem before the proposed solution.
- Keep goals and non-goals explicit when scope could drift.
- Detailed design should be concrete enough for informed implementation review.
- Include drawbacks; an RFC is not advocacy copy.
- Alternatives should include meaningful options and the cost of doing nothing when relevant.
- Leave unresolved questions visible instead of hiding them with speculative answers.

## Quality checks

- A reviewer can evaluate the proposal without reconstructing missing context.
- The proposal explains impacts on existing behavior/contracts.
- Tradeoffs and alternatives are not token sections.
- Rollout/migration is included when the change can break existing users or data.
- The RFC is not written as if the decision were already final unless its status says so.
