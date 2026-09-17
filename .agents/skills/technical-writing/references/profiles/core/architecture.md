# Architecture Document Profile

## Purpose

Explain the system's important structural boundaries, runtime interactions, deployment context, architectural decisions, quality concerns, and risks at the level needed by its stakeholders.

## Use when

- engineers need a shared system model;
- onboarding/review/operations depend on understanding boundaries and interactions;
- architecture knowledge is currently scattered across code and tribal knowledge.

## Default structure

Use only the sections that add value; do not force a heavyweight template onto a small system.

```markdown
# [System] Architecture

## Goals and scope

## Constraints

## Context and external dependencies

## Solution strategy / architecture overview

## Building blocks / modules

## Runtime views

## Deployment view

## Cross-cutting concerns  <!-- auth, data, observability, etc. -->

## Architectural decisions  <!-- links to ADRs when possible -->

## Quality requirements

## Risks and technical debt

## Glossary  <!-- when domain terminology needs it -->
```

## Primary / secondary types

- Primary: Explanation
- Common secondary: Reference

## Diagram guidance

Prefer diagrams for:

- system context;
- container/module relationships;
- critical runtime sequences;
- deployment topology;
- data/control flow.

A diagram must have accompanying prose that explains what the reader should notice.

## Quality checks

- Scope and system boundary are explicit.
- The document distinguishes static structure from runtime behavior.
- Critical external dependencies are visible.
- Important architecture decisions link to their decision records when available.
- Risks/technical debt are not omitted merely because they are uncomfortable.
- The document reflects the actual system or clearly labels future-state architecture.
