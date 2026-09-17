# Document Types

Use this reference to decide how a technical document should serve the reader. The four types are not rigid genres; they are reader-goal patterns. Choose one primary type and add a secondary type only when it improves the reader experience.

## Selection table

| Type | Reader's immediate goal | Typical forms |
|---|---|---|
| Learning | Learn a new tool, workflow, or concept by progressing through a successful path | Getting started, tutorial |
| Problem solving | Complete a concrete task or fix a concrete problem | How-to, troubleshooting |
| Reference | Look up exact, complete, structured information | API reference, configuration reference, error catalog |
| Explanation | Understand background, mechanisms, tradeoffs, or domain concepts | Concept guide, design explanation, domain overview |

## Combining types

- **Primary type** determines the main reading experience and overall flow.
- **Secondary type** adds supporting sections without taking over the document.
- Do not combine types merely to be comprehensive.
- If distinct reader goals each need substantial treatment, consider separate documents with cross-links instead.

## TYPE-LEARN — Learning document

**Reader goal:** reach a clear learning outcome by following a safe, progressive path.

### Core requirements

- `MUST` state what the reader will be able to do or understand.
- `SHOULD` state prerequisites and required environment before the first irreversible or confusing step.
- `SHOULD` organize the path from simple to more complex steps.
- `MUST` ensure essential code/commands are executable when execution is part of the learning goal.
- `SHOULD` make the expected successful result observable.
- `HEURISTIC` move common failure modes to a short FAQ/troubleshooting section so the main path remains focused on success.

### Getting started vs tutorial

- **Getting started:** teaches the overall flow and the minimum concepts needed to begin.
- **Tutorial:** has a concrete target/result and teaches through a complete sequence of actions.

### Minimal structure

```markdown
# [Title]

[Overview: outcome and value]

## Goal

## Prerequisites

## Step 1. ...

## Step 2. ...

## Verify the result

## Troubleshooting / FAQ  <!-- optional -->
```

## TYPE-PROBLEM — Problem-solving document

**Reader goal:** complete a task or resolve an observed failure quickly and correctly.

### Core requirements

- `MUST` define the problem, desired task, or observable symptom clearly.
- `SHOULD` separate cause from symptom when troubleshooting.
- `MUST` provide an actionable procedure, code, command, or configuration when one exists.
- `SHOULD` explain why the fix works when that explanation prevents misuse or recurrence.
- `SHOULD` state relevant environment/version differences.
- `SHOULD` provide a way to verify that the task or fix succeeded.

### How-to vs troubleshooting

- **How-to:** starts from a desired task and guides the reader to completion.
- **Troubleshooting:** starts from a failure/symptom and guides diagnosis and recovery.

### How-to structure

```markdown
# [Task-oriented title]

[What this enables and when to use it]

## Prerequisites  <!-- optional -->

## Steps

## Verify the result

## Environment-specific notes  <!-- optional -->
```

### Troubleshooting structure

```markdown
# [Specific symptom/error] 해결하기

## Problem

## Likely cause

## Resolution

## Verify the fix

## Environment-specific notes  <!-- optional -->
```

## TYPE-REFERENCE — Reference document

**Reader goal:** find exact information quickly without reading the document from start to finish.

### Core requirements

- `MUST` prioritize factual accuracy.
- `MUST` use a stable, repeated structure for comparable elements.
- `SHOULD` cover required fields, parameters, return values, defaults, constraints, and edge behavior when relevant.
- `SHOULD` make scanning and direct navigation easy.
- `SHOULD` include a practical example when it clarifies usage.
- `MUST` avoid implying completeness when known information is missing.

### Minimal structure

```markdown
# [Element / API / option]

## Overview

## Signature / syntax

## Parameters / options

## Return value / output

## Examples

## Constraints / notes
```

Use tables when parameterized information is easier to scan that way.

## TYPE-EXPLAIN — Explanation document

**Reader goal:** understand why something exists, how it works, what tradeoffs it has, or how a domain is structured.

### Core requirements

- `SHOULD` explain the background or problem that makes the topic relevant.
- `MUST` define concepts needed to understand the explanation.
- `SHOULD` explain mechanisms and relationships, not only outcomes.
- `SHOULD` compare alternatives/tradeoffs when they matter to understanding.
- `SHOULD` use diagrams when relationships or flows are otherwise hard to understand.
- `SHOULD` connect the concept to real usage or consequences.

### Minimal structure

```markdown
# [Concept]

[Overview: what this explains and why it matters]

## Background

## Core concept

## How it works

## Tradeoffs / alternatives  <!-- when relevant -->

## Application / examples
```

## Type-selection checks

Before finalizing the type, ask:

1. What is the reader trying to accomplish **right now**?
2. Do they need a successful learning path, a concrete task/fix, lookup data, or deeper understanding?
3. Would mixing another goal substantially lengthen the document?
4. If yes, should that goal become a linked document instead of a secondary type?
