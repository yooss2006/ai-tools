# Eval 03 — Existing Plan

## Purpose

Verify that the skill absorbs an existing plan and interviews only the gaps/conflicts.

## Supplied plan

```text
목표: 혼자 점심 메뉴를 10초 안에 결정한다.
사용자: 직장인 1인 사용자.
핵심 흐름: 앱 실행 -> 브랜드 선택 -> 메뉴 1개 추천.
가입: 없음.
수익화: 아직 미정.
```

## User prompt

```text
$planning-interviewer
이 기획에서 빠진 부분부터 인터뷰해줘.
```

## Pass criteria

- Does not ask again what the target user is or whether sign-up is required.
- Reconstructs known decisions implicitly or briefly.
- Selects one material gap, contradiction, or hypothesis.
- A question about what happens when the recommendation is unacceptable, scope/brand policy, or monetization may be reasonable depending on context.

## Fail conditions

- Starts from "어떤 서비스를 만들고 싶나요?"
- Repeats all known facts as questions.
- Generates a complete PRD without further interviewing.
