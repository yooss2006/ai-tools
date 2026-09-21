# Eval 06 — Scope Reduction

## Purpose

Verify that the skill challenges weak scope without deleting it unilaterally.

## Conversation state

Core goal:

```text
처음 방문한 사용자가 30초 안에 오늘 먹을 점심 메뉴를 하나 결정한다.
```

User addition:

```text
그리고 다른 사람 프로필을 팔로우하고 피드도 보고 댓글도 달 수 있으면 좋겠어.
```

## Pass criteria

- Tests how social features support the core goal.
- May recommend deferring them based on the current goal.
- Asks the user whether there is a reason they must be included now.
- Does not simply delete the features.

## Fail conditions

- Automatically adds the social system to MVP.
- Automatically removes it without asking.
- Discusses social feed implementation technology.
