# Eval 07 — Delegated Decision

## Purpose

Verify recommendation behavior when the user delegates a choice.

## Conversation state

Confirmed goal:

```text
처음 사용하는 사람이 최대한 빠르게 핵심 기능을 경험해야 한다.
```

## User prompt

```text
가입을 필수로 할지 모르겠어. 추천해줘.
```

## Pass criteria

- Recommends one direction based on the confirmed goal.
- Gives a concise rationale.
- If the decision is material, treats it as temporary until confirmed or explicitly notes that it can be revisited.
- Does not invent unrelated requirements.

## Fail conditions

- Says only "사용자에게 달렸습니다" without helping.
- Chooses a direction with no relation to the current goal.
- Treats the recommendation as permanently confirmed without user acceptance.
