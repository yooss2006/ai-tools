# ADR Profile

## Purpose

Record an architecturally significant decision and enough context for a future reader to understand why the decision was made and what consequences it creates.

## Use when

- a decision is architecturally significant, costly to reverse, risky, or likely to be questioned later;
- the team needs a durable record of the chosen option and rationale.

## Do not use when

- the document is still proposing a broad change that has not been decided; prefer an RFC/technical proposal;
- the decision is trivial or fully explained by a local code comment.

## Default structure

Nygard-style minimum:

```markdown
# [Decision title]

## Status

## Context

## Decision

## Consequences
```

Recommended extension when tradeoff history matters:

```markdown
## Considered options

### Option A
- Benefits
- Costs / risks

### Option B
- Benefits
- Costs / risks
```

## Primary / secondary types

- Primary: Explanation
- Common secondary: Reference

## Writing guidance

- Context should describe the forces/constraints that made a decision necessary, not retell the whole project history.
- Decision should be specific enough that implementation/review can determine whether the system follows it.
- Consequences should include meaningful costs and limitations, not only benefits.
- Alternatives are useful when future readers are likely to ask “why not X?”.
- Status should make supersession/rejection visible when the team uses ADR lifecycle states.

## Quality checks

- The decision can be summarized in one or two sentences.
- The rejected/alternative options are represented fairly when included.
- Tradeoffs are explicit.
- Consequences describe operational/maintenance impact where relevant.
- The ADR does not become a full implementation specification when an RFC/design doc should own that detail.
