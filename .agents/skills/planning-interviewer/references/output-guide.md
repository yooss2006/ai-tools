# Output Guide

This file is the canonical source for planning summaries, final planning documents, and handoffs.

## 1. General output rule

Represent the current planning state faithfully.

Do not fill empty sections with invented content to make the document look complete.

Remove sections that are irrelevant to the project.

## 2. Checkpoint summary

Use at meaningful transitions only.

Suggested compact structure:

```markdown
### 현재까지 확정된 핵심
- ...

### 남아 있는 핵심 미정
- ...

### 중요한 가설
- ...
```

Omit empty groups.

## 3. Final planning document

Adapt depth to the project.

Recommended section pool:

```markdown
# 기획 요약

## 해결하려는 문제

## 대상 사용자

## 핵심 가치

## 사용자 경험

## 주요 기능과 범위

## 정책 및 제약

## 예외 및 실패 상황

## 운영

## 비즈니스

## 성공 기준

## 확정된 사항

## 임시 결정

## 가설 및 검증 필요 사항

## 미정 사항

## 제외/보류한 범위

## 중요한 의사결정 이력

## 개발/디자인 단계에서 결정할 사항
```

Do not include every heading automatically.

## 4. Requirements language

Write behavioral and policy requirements clearly enough for later work without deciding implementation.

Prefer statements such as:

- 사용자는 결제 실패 후 다시 시도할 수 있다.
- 무료 사용자는 하루 한 번 기록할 수 있다.
- 운영자는 신고된 콘텐츠를 검토한 뒤 숨김 또는 유지 결정을 할 수 있다.

Avoid implementation directives such as framework, API, database, or architecture choices.

## 5. Separate certainty levels

When present, keep these distinct:

- `확정`: user-confirmed decisions;
- `임시 결정`: delegated recommendation still awaiting confirmation;
- `가설`: beliefs that require validation;
- `미정`: decisions still open;
- `제외/보류`: intentionally not in current scope.

Do not collapse them into one requirement list.

## 6. Planning handoff

Create a handoff only when the user asks for one.

Suggested `planning-handoff.md`:

```markdown
# Planning Handoff

## 현재 목표

## 현재 기획 단계

## 확정

## 사실

## 임시 결정

## 가설

## 미정

## 제외/폐기

## 중요한 결정 이력

## 현재 가장 중요한 질문

## 다음 인터뷰에서 확인할 사항
```

The handoff is optimized for resuming the interview, not for presenting a polished PRD.

## 7. Resume from handoff

When a handoff is supplied:

1. restore the state;
2. identify whether anything conflicts with the user's new message;
3. do not ask the user to repeat established context;
4. ask the highest-value unresolved question.

## 8. Development handoff

When the user wants to move from planning to development, summarize:

- required product behavior;
- state/policy rules;
- permissions;
- success/failure behavior;
- unresolved product decisions;
- items that the later technical phase must decide.

Do not recommend the technical solution unless the planning skill has ended and the user explicitly starts a separate technical-design task.
