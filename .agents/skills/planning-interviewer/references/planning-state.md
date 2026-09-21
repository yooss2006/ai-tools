# Planning State

This file defines the canonical conceptual state maintained during a planning session.

It is not a database schema and must not be discussed as an implementation model.

## 1. Context

Track only what is relevant:

- planning subject;
- current objective;
- planning maturity;
- requested interview depth;
- supplied source material;
- whether external validation has already been authorized;
- whether code inspection has explicitly been authorized for behavior discovery.

## 2. Problem

Possible fields:

- problem statement;
- situation in which it occurs;
- frequency or importance when known;
- current workaround or alternative;
- limitation of the current alternative;
- consequence of leaving the problem unsolved.

Do not force all fields for an early exploratory session.

## 3. Users

Possible fields:

- primary user;
- secondary user;
- payer if different from user;
- operator/admin if relevant;
- usage context;
- user goal;
- relevant differences between user groups.

Avoid fictional demographic detail that does not change the plan.

## 4. Value

Track:

- desired outcome;
- core value proposition;
- reason the user would choose this over the current alternative;
- value assumptions still unverified.

## 5. Experience

Track product behavior at planning level:

- entry condition;
- main journey;
- core action;
- completion condition;
- exit/cancel path;
- empty state;
- error/failure state;
- restricted state;
- feedback the user must receive;
- context differences such as mobile/desktop only when they change the experience.

Do not specify visual styling or implementation.

## 6. Scope

Track:

- must-have capability;
- supporting capability;
- deferred capability;
- explicitly excluded capability;
- capability under evaluation;
- reason for important scope decisions.

## 7. Policies

Track when relevant:

- eligibility;
- permissions;
- limits;
- state transitions;
- retention or expiration policy at product level;
- retries and recovery behavior;
- cancellation/refund/rollback behavior at product level;
- moderation or safety policy;
- exception handling;
- differences by user type or plan.

Do not decide technical enforcement mechanisms.

## 8. Operations

Track:

- who operates the service;
- manual work required;
- review/approval work;
- support burden;
- exceptional manual handling;
- operational constraints that affect product policy.

## 9. Business

Track only when relevant:

- payer;
- charging model;
- value exchanged;
- major cost drivers at business level;
- willingness-to-pay assumptions;
- business constraints;
- monetization decisions and hypotheses.

Do not turn this into financial modeling unless the user asks.

## 10. Success

Track:

- what success means;
- observable user behavior that would indicate success;
- failure signals;
- decision criteria for continuing, changing, or stopping the plan when relevant.

Metrics are useful only when they support a real decision.

## 11. Evidence state

Every important claim should conceptually belong to one of these states.

### FACT — 사실

Information supported by the user, supplied material, or an explicitly verified external source.

A fact is not necessarily a product decision.

### DECIDED — 확정

A planning decision explicitly accepted by the user.

### HYPOTHESIS — 가설

An unverified belief, prediction, or causal expectation.

A hypothesis must not be written as a confirmed requirement.

### OPEN — 미정

An unresolved item that may require a decision or evidence.

Not every possible unknown belongs here. Track only meaningful unknowns.

### DROPPED — 폐기

A direction that was discussed and intentionally excluded or deferred out of the current plan.

Record the reason when it matters for future reconsideration.

## 12. Temporary decisions

When the user delegates judgment on a material decision, the skill may record a temporary direction.

A temporary decision:

- has a clear recommendation rationale;
- is usable for continuing the interview;
- is not equivalent to `DECIDED` until the user confirms it;
- should be surfaced before finalization if it remains temporary.

## 13. Decision history

The latest planning state is the source of truth.

Preserve history only for decisions that materially changed:

- target user;
- core problem;
- core value;
- major policy;
- monetization;
- major scope addition/removal;
- a contested decision likely to be revisited.

Do not log wording changes or minor detail edits.

Suggested entry:

```text
Changed: <old direction> -> <new direction>
Reason: <why, if known>
Affected: <policies/flows/scope/hypotheses impacted>
```

## 14. Open questions

Maintain a small ordered set of unresolved high-value questions.

The first item should be the best candidate for the next interview question, unless a new contradiction or user request takes priority.

## 15. Development handoff items

Track planning issues that later require a development/design decision without suggesting a technical solution.

Good:

- 실시간성 요구 수준에 맞는 구현 방식 결정 필요
- 대량 사용 시 처리 제약 검토 필요

Bad:

- WebSocket 사용
- PostgreSQL 사용
- Redis 캐시 추가

## 16. State update rules

After each meaningful answer:

1. identify whether it adds a fact, decision, hypothesis, open item, dropped direction, or temporary decision;
2. check whether an existing item changed;
3. identify affected parts of the plan;
4. resolve any material contradiction before building further decisions on it;
5. select the next highest-value uncertainty.
