# State Strategies

The interview is state-based, not a fixed linear questionnaire.

Use these states internally. Do not require the user to select or learn the state names.

## State 1 — Exploration

### Enter when

- the user has no concrete idea;
- the user has only a broad interest area;
- the stated solution is clear but the problem is unknown;
- an existing plan loses its problem/goal foundation during review.

### Goal

Find a real problem, opportunity, or desired outcome worth planning around.

### Question strategy

Explore:

- recent recurring friction;
- workarounds;
- wasted time/money/attention;
- tasks repeatedly postponed or abandoned;
- situations where people combine multiple tools awkwardly;
- solutions users already pay for but dislike;
- problems observed in a group the user understands well.

Do not generate a catalog of app ideas unless the user explicitly changes the task to ideation.

### Exit when

There is a sufficiently concrete problem/opportunity and a plausible user/context to investigate.

---

## State 2 — Validation

### Enter when

- a problem candidate exists;
- a solution idea exists and needs grounding;
- a core assumption is uncertain;
- the plan depends on a claim that has not been tested.

### Goal

Determine whether the problem, user, desired outcome, and proposed direction are coherently connected.

### Question strategy

Probe:

- who experiences the problem;
- when it happens;
- how often or how seriously it matters;
- what they do now;
- why the current alternative is insufficient;
- what outcome they actually want;
- why the proposed solution may improve that outcome;
- what must be true for the plan to work.

Avoid asking the user to prove the entire market before planning can continue. The required evidence depth depends on the stage.

### Exit when

The core problem-user-value relationship is strong enough for the requested planning depth, or the user decides to proceed with explicitly labeled hypotheses.

---

## State 3 — Elaboration

### Enter when

Problem, user, and intended value are clear enough to define behavior.

### Goal

Turn intent into implementation-independent product/service behavior.

### Question strategy

Choose only relevant dimensions:

- main user journey;
- entry/completion/exit conditions;
- necessary capabilities;
- priorities;
- policies and limits;
- permissions;
- state changes;
- exception/failure/recovery behavior;
- operational handling;
- monetization/business constraints;
- success criteria.

Do not exhaust every category if it does not change the plan.

### Exit when

The main experience and material policies are coherent enough to review.

---

## State 4 — Review

### Enter when

- the plan is already detailed;
- the user supplies an existing planning document;
- scope has grown;
- the user asks for gap checking;
- a major decision has changed.

### Goal

Find contradictions, unnecessary scope, unsupported assumptions, missing policies, and broken decision dependencies.

### Review dimensions

- Does each major capability support a user problem or core value?
- Are confirmed policies mutually consistent?
- Are edge cases missing where failure would materially affect the user or operations?
- Did a changed decision invalidate an older flow/policy?
- Are hypotheses written as if they were facts?
- Is the plan solving multiple unrelated goals?
- Is there a decision that can be deferred safely?

### Exit when

Material issues are resolved or explicitly left open.

---

## State 5 — External Validation

### Enter only when

- the user already authorized external validation; or
- the skill explains the useful validation target and the user approves.

### Goal

Use external evidence to test important assumptions or reveal alternatives, not to replace user decisions.

Use `external-validation.md`.

### Exit when

The requested evidence is gathered and converted into planning implications/questions.

---

## State 6 — Synthesis

### Enter when

- the user asks to summarize/finalize;
- sufficiency is high and the user chooses to finalize;
- a handoff is requested.

### Goal

Represent the current plan faithfully without inventing missing content.

Use `output-guide.md`.

### Exit when

The requested planning artifact or handoff is complete.

---

## Moving backward is allowed

States are not a one-way funnel.

Examples:

- During elaboration, a feature exposes uncertainty about the underlying problem → return to validation.
- During review, the target user changes → revisit user/problem/value before repairing scope.
- External evidence challenges a core assumption → return to validation and ask the user to decide.

The interview should follow the plan's uncertainty, not a predetermined sequence.
