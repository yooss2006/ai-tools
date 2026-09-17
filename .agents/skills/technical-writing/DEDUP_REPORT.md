# Deduplication Report

이 문서는 `technical-writing.dev`에서 추출한 22개 페이지를 Skill용 Canonical Reference로 재구성하면서 어떤 내용을 유지·병합·제거했는지 기록한다.

## 목표

원본은 사람이 순서대로 학습하기 좋은 구조지만, Skill 런타임에서는 같은 원칙이 튜토리얼, 요약 페이지, AI 프롬프트, 상세 페이지에 반복된다. 이 초안에서는 다음 기준을 적용했다.

1. 하나의 규칙은 하나의 Canonical Reference에서만 정의한다.
2. 요약 페이지는 상세 규칙의 Source of Truth가 되지 않는다.
3. 교육용 반복·실습·GPT 설정 절차는 런타임 Reference에서 제거한다.
4. 대표 Before/After는 규칙 파일에 짧게 남기고, 완성 예제는 `references/examples/`로 분리한다.
5. 원문에 없는 실무 문서 프로필·검증·다중 문서 운영 규칙은 Extension으로 분리한다.

## 원본 페이지 매핑

| # | 원본 페이지 | 처리 | 최종 위치 |
|---:|---|---|---|
| 1 | 시작하기 | 핵심 3단계 철학만 워크플로우에 반영. 사이트 안내/License 설명은 runtime에서 제외 | `SKILL.md`, `README.md`, `NOTICE.md` |
| 2 | 기본 문서 작성하기 | 긴 개선 전/후와 반복 개선 포인트 제거. 예제 역할만 유지 | `references/examples/*` |
| 3 | 문서 구조 만들기 | 다중 페이지 구조, 역할 분리, 크로스링크 개념 유지 | `information-architecture.md`, `documentation-system.md` |
| 4 | AI와 함께 쓰기 | GPT UI 설정 절차 및 중복 프롬프트 제거. 단계적 실행 개념을 progressive loading으로 재설계 | `SKILL.md` |
| 5 | 문서 유형 정하기 | 4유형 분류, 결합 원칙, 최소 템플릿을 Canonical화 | `document-types.md` |
| 6 | 학습을 위한 문서 | 목표/사전조건/단계/실행 예제 규칙을 병합 | `document-types.md` |
| 7 | 문제 해결을 위한 문서 | How-to/트러블슈팅 차이와 해결 중심 규칙을 병합 | `document-types.md` |
| 8 | 참조를 위한 문서 | 정확성/완전성/일관 구조/탐색성 규칙을 병합 | `document-types.md` |
| 9 | 깊은 이해를 위한 문서 | 배경/원리/시각화/응용 규칙을 병합 | `document-types.md` |
| 10 | 정보 구조 만들기 | 11~16의 요약이므로 독립 규칙 본문 제거 | `information-architecture.md`의 인덱스 역할로 흡수 |
| 11 | 한 페이지에서는 하나만 다루기 | Canonical 규칙화 | `IA-ONE` |
| 12 | 가치를 먼저 제공하기 | Canonical 규칙화 | `IA-VALUE` |
| 13 | 효과적인 제목 쓰기 | Canonical 규칙화. 30자 기준은 절대 규칙이 아닌 heuristic으로 약화 | `IA-HEADING` |
| 14 | 개요 빠트리지 않기 | Canonical 규칙화 | `IA-OVERVIEW` |
| 15 | 예측 가능하게 하기 | 구조 일관성/순서 규칙은 IA로, 용어 일관성은 Writing으로 분리 | `IA-PREDICT`, `IA-SEQUENCE`, `WR-TERMS` |
| 16 | 자세히 설명하기 | 필요한 배경/동작 조건을 Canonical화 | `IA-CONTEXT` |
| 17 | 문장 다듬기 | 18~22의 요약이므로 독립 규칙 본문 제거 | `writing-principles.md`, `language/ko.md` |
| 18 | 문장의 주체를 분명하게 하기 | 주체/능동 표현으로 정규화 | `WR-SUBJECT`, `WR-ACTIVE` |
| 19 | 필요한 정보만 남기기 | 한 문장 한 생각/메타 담화 최소화 | `WR-ONE-THOUGHT`, `WR-META` |
| 20 | 구체적으로 쓰기 | 동사/구체성/수치/참조 맥락 규칙으로 분해 | `WR-VERB`, `WR-CONCRETE`, `WR-MEASURE`, `WR-REFER` |
| 21 | 자연스러운 한국어 표현 쓰기 | 언어 독립 규칙과 분리하여 한국어 전용 Canonical로 이동 | `language/ko.md` |
| 22 | 일관되게 쓰기 | 용어/약어는 공통 규칙, 한국어 외래어 표기는 한국어 규칙으로 분리 | `WR-TERMS`, `WR-ABBREV`, `KO-TECH-TERM` |

## 주요 중복 제거 결정

### 1. AI 프롬프트의 체크리스트를 Canonical 규칙으로 사용하지 않음

원본의 AI 프롬프트는 Step별 핵심 원칙을 다시 요약한다. Skill에서는 이 요약문을 유지하지 않고 실제 상세 원칙 Reference를 필요 시 로드한다.

### 2. 소개 페이지의 원칙 목록을 제거

`정보 구조 만들기`와 `문장 다듬기`의 소개 페이지는 하위 상세 페이지와 중복된다. 런타임에서는 하위 규칙을 Canonical Source로 사용한다.

### 3. 용어 일관성을 한 곳으로 이동

원본에서는 정보 구조의 “예측 가능성”과 문장 단계의 “일관되게 쓰기” 양쪽에서 용어 일관성을 다룬다.

최종 구조에서는:

- 구조 예측 가능성: `IA-PREDICT`
- 용어 일관성: `WR-TERMS`

로 나눠 중복 정의를 제거했다.

### 4. 한국어 전용 규칙을 분리

`동사를 우선한다`, `명확하게 쓴다` 같은 언어 독립 원칙과 `수행/진행` 명사화, 번역체, 외래어 표기처럼 한국어에 특화된 규칙을 분리했다.

### 5. 숫자 기준을 기계적 규칙으로 만들지 않음

원본의 `H4 이상`, `제목 30자 이내` 같은 기준은 Skill에서 자동 실패 조건으로 사용하지 않는다. 문서 분리/축약 필요성을 판단하는 `HEURISTIC`으로 둔다.

### 6. 예제를 두 층으로 분리

- 규칙 Reference: 짧은 Before/After
- `references/examples/`: 완성형 패턴 하나

긴 교육용 예제와 동일 교훈을 반복하는 실습 문제는 제거했다.

## Skill 확장 영역

다음은 원본 22개 페이지에서 직접 추출한 별도 장이 아니라, 인터뷰에서 결정한 확장 기능이다.

- Practical profiles: README, ADR, RFC, Architecture, Incident/Postmortem, Migration, Onboarding
- MUST / SHOULD / HEURISTIC
- Structure approval gate
- Selective verification
- Repository inspection policy
- Semantic duplication detection
- Source of Truth 관리
- Cross-document conflict resolution
- Metadata preservation policy
- Behavioral evals with concrete fixtures
- Cross-cutting semantic-preservation guardrail for review/rewrite/polish

상세한 출처와 경계는 `references/meta/provenance.md`에서 관리한다.

## 정규화 결과

원본의 22개 페이지는 Skill 런타임 관점에서 다음 8개 지식 영역으로 정규화된다.

```text
문서 유형       -> references/core/document-types.md
정보 구조       -> references/core/information-architecture.md
공통 문장 규칙  -> references/core/writing-principles.md
한국어 규칙     -> references/language/ko.md
다중 문서 관리  -> references/extensions/documentation-system.md
사실 검증       -> references/extensions/verification.md
실무 문서 형식  -> references/profiles/*
대표 패턴       -> references/examples/*
실행/라우팅     -> SKILL.md
```

## 다음 검토 포인트

- Rule strength(MUST/SHOULD/HEURISTIC)가 과하거나 약한 부분이 없는지
- ADR/RFC/Architecture 프로필의 기본 섹션이 실제 사용 습관에 맞는지
- Migration/Onboarding을 v1에 계속 포함할지
- 공개 저장소의 최종 LICENSE 선택
- `evals/fixtures/` 기반 판정 기준을 실제 Skill runner에서 자동화할 방법
