---
name: prompt-mirroring
description: Mirror a user's free-form feature or workflow description, surface ambiguities and contradictions, resolve important questions, and produce a confirmed platform-agnostic skill. Use when the user wants their intent reflected back before a skill is written. Do not use when the user already provides a complete skill and only wants a direct edit or conversion.
---

# Prompt Mirroring

Help the user clarify a proposed skill before writing it. Optimize for shared understanding, not speed of generation.

## Workflow

1. Analyze the user's description and mirror it under these headings:
   - 목적
   - 사용자 / 사용 시점
   - 입력
   - 처리 흐름
   - 출력
   - 제약조건
   - 예외 / 실패 상황
   - 아직 결정되지 않은 사항
2. Connect related requirements instead of merely repeating the user's words. Label any inference as `추론:` and do not present it as confirmed.
3. Check for material ambiguity, contradiction, missing information, hidden assumptions, and unclear scope. In particular, distinguish analysis, execution, validation, recovery, and external-system responsibilities.
4. If a material matter remains unresolved, present the current understanding under `# 내가 이해한 내용`, then ask only the single most important question. Never label this draft `# 최종 요구사항`. Prefer this order:
   1. purpose or core behavior
   2. responsibility boundary
   3. inputs or data
   4. decision criteria
   5. failures and exceptions
   6. output format
   7. minor conveniences
5. Make the question concrete. Offer choices and a recommendation when useful, but never treat the recommendation as the user's decision.
6. After each answer, briefly state changes under `반영된 내용`, reassess the whole specification, and ask the next single material question. Re-mirror the full specification only when the conversation has become complex or drift is likely.
7. Stop questioning when the purpose, scope, inputs, core flow, decision criteria, output, important constraints, and major failure behavior are sufficiently clear. Do not prolong the conversation for details that have a clear convention, little impact, or are easy to change; record those as `기본 가정:` instead.
8. Only when no material question remains, present the final requirements using the structure below and ask the user to confirm them. Do not write the skill yet.
9. Write the skill only after the user explicitly confirms the presented requirements, including confirmations such as “좋아”, “확정”, “이대로 만들어줘”, or “Skill 만들어줘”. A confirmation from earlier context counts only when it clearly refers to the current final requirements.

## 미러링 형식

Use this format while any material question remains:

```markdown
# 내가 이해한 내용

## 목적
## 사용자 / 사용 시점
## 입력
## 처리 흐름
## 출력
## 제약조건
## 예외 / 실패 상황
## 아직 결정되지 않은 사항
```

Then ask exactly one question.

## 최종 요구사항 형식

```markdown
# 최종 요구사항

## 목적
## 사용자 / 사용 시점
## 입력
## 처리 흐름
## 판단 기준
## 출력
## 제약조건
## 예외 / 실패 처리
## 기본 가정
## Skill 범위 밖
```

End with a direct request to confirm or correct the requirements.

## 생성할 Skill 형식

Unless the user requests a platform-specific format, produce a platform-agnostic skill with only the sections that add useful guidance:

```markdown
# Skill: {이름}

## 목적
## 사용 시점
## 책임 범위
## 범위 밖
## 입력
## 작업 절차
## 판단 기준
## 예외 및 실패 처리
## 출력
## 제약조건
## 금지 사항
## 완료 조건
```

Write concrete, testable guidance instead of vague terms such as “appropriately,” “automatically,” or “as needed.” Preserve the user's chosen scope and omit empty, redundant, or speculative sections.

## Non-Negotiable Rules

- Never invent unspoken requirements.
- Keep confirmed requirements, inferences, default assumptions, and unresolved matters visibly distinct.
- Surface contradictions instead of silently choosing a side.
- Ask one material question at a time, most important first.
- Do not let minor details block progress.
- Clarify purpose and responsibility before implementation details.
- Revise prior understanding when the user's answers require it.
- Do not generate the final skill before explicit confirmation.
- Do not introduce platform-specific syntax or capabilities unless requested.
- Never use the `최종 요구사항` heading while a material question remains unresolved.

## First Response

When the user first describes the proposed skill, mirror the requirements under `내가 이해한 내용`, identify the most consequential gap, and ask exactly one question. If no material question remains, present `최종 요구사항` and request confirmation.
