# Eval 08 — Plan Change

## Purpose

Verify impact analysis after a material decision changes.

## Conversation state

Previous decision:

```text
모든 사용자는 하루 한 번만 기록할 수 있다.
```

## User prompt

```text
유료 사용자는 추가 기록을 할 수 있게 바꾸자.
```

## Pass criteria

- Updates the current direction.
- Recognizes that free/paid policy is now differentiated.
- Identifies affected policy questions instead of restarting the whole interview.
- Asks one material follow-up, such as whether paid usage has a cap or how additional usage is defined.
- Keeps the old decision only as important history, not as current truth.

## Fail conditions

- Leaves both rules as simultaneously active without reconciliation.
- Re-asks unrelated user/problem questions.
- Decides all paid-plan details on its own.
