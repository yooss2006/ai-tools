# Eval 10 — Resume Handoff

## Purpose

Verify that a new conversation can resume from a planning handoff without restarting.

## Supplied handoff

```markdown
# Planning Handoff

## 현재 목표
혼자 점심 메뉴를 빠르게 결정한다.

## 확정
- 대상: 직장인 1인 사용자
- 가입 없음
- 앱 진입 후 한 번의 추천으로 종료 가능

## 가설
- 사용자는 메뉴 탐색보다 결정 자체에 더 큰 피로를 느낀다.

## 미정
- 추천 결과가 마음에 들지 않을 때의 행동

## 현재 가장 중요한 질문
추천 결과를 거절한 사용자가 즉시 다시 추천받을 수 있어야 하는가?
```

## User prompt

```text
$planning-interviewer
이어서 하자.
```

## Pass criteria

- Restores the handoff as current planning context.
- Does not ask for target user, goal, or sign-up again.
- Continues from the most important unresolved question or explains why another unresolved item now has higher priority.
- Keeps the hypothesis separate from confirmed decisions.

## Fail conditions

- Starts with "어떤 서비스를 만들고 싶나요?"
- Treats the hypothesis as confirmed.
- Generates a new plan unrelated to the handoff.
