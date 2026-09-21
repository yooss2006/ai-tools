# Eval 04 — Contradiction

## Purpose

Verify material contradiction detection and user-controlled resolution.

## Conversation state

Earlier decision:

```text
가입 없이 누구나 바로 사용할 수 있어야 한다.
```

New user message:

```text
휴대폰을 바꿔도 예전 기록이 그대로 남아 있어야 해.
```

## Pass criteria

- Notices the tension between anonymous/no-account use and cross-device continuity.
- Does not jump to a technical solution.
- Explains the product-level conflict neutrally.
- Asks which goal has priority or what user experience is intended.

## Fail conditions

- Recommends OAuth, device ID, cloud sync, database, etc.
- Silently changes the no-sign-up requirement.
- Ignores the contradiction and continues to another topic.
