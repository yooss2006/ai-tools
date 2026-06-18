# Technical Writing Skill

기술 문서 작성, 리뷰, 구조화, 문장 개선을 돕는 Codex 스킬입니다. Viva Republica, Inc.의 테크니컬 라이팅 가이드 자료를 기반으로, AI가 필요한 지식을 단계적으로 불러올 수 있도록 재구성했습니다.

## 목적

이 스킬은 기술 문서를 작성하거나 개선할 때 다음 세 가지 관점으로 문서를 점검합니다.

1. 문서 유형이 독자의 목적에 맞는가?
2. 정보가 독자 입장에서 예측 가능하게 구조화되어 있는가?
3. 문장이 명확하고 구체적이며 일관적인가?

`SKILL.md`는 컨텍스트 사용량을 줄이기 위해 최소한의 라우팅 정보만 담습니다. 실제 가이드, 체크리스트, 예시는 `references/`에서 필요한 시점에만 읽도록 분리했습니다.

## 파일 구조

```text
technical-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── workflow.md
    ├── document-types.md
    ├── information-architecture.md
    ├── sentence-editing.md
    ├── prompts.md
    └── examples.md
```

## Reference 구성

- `workflow.md`: 전체 문서 작성, 리뷰, 재작성, 품질 개선 작업의 기본 흐름입니다.
- `document-types.md`: 학습 중심 문서, 문제 해결 문서, 참조 문서, 설명 문서의 선택 기준과 템플릿입니다.
- `information-architecture.md`: 한 페이지 한 목표, 개요, 제목, 정보 순서, 크로스링크 등 구조 설계 원칙입니다.
- `sentence-editing.md`: 한국어 문장 다듬기, 간결화, 구체화, 자연스러운 표현, 용어 일관성 원칙입니다.
- `prompts.md`: 문서 유형 판단, 정보 구조 개선, 문장 개선에 쓸 수 있는 재사용 프롬프트입니다.
- `examples.md`: before/after 비교와 문서 유형별 축약 예시입니다.

## 라우팅 원칙

넓은 요청은 `workflow.md`를 먼저 읽게 합니다. 예를 들어 "문서 전체를 봐줘", "초안을 개선해줘", "기술 문서를 새로 써줘" 같은 요청은 문서 유형, 정보 구조, 문장 품질을 모두 점검해야 하므로 `workflow.md`가 안전망 역할을 합니다.

좁은 요청은 해당 reference만 읽게 합니다.

- 문서 유형을 고르거나 템플릿이 필요하면 `document-types.md`
- 목차, 개요, 제목, 흐름을 다루면 `information-architecture.md`
- 문장 표현을 고치면 `sentence-editing.md`
- AI 프롬프트가 필요하면 `prompts.md`
- 구체적인 샘플이나 before/after가 필요하면 `examples.md`

## 관리 원칙

- `SKILL.md`에는 트리거, 진행 방식, reference 라우팅처럼 실행에 꼭 필요한 내용만 둡니다.
- 상세 지침, 예시, 긴 체크리스트는 `references/`로 옮깁니다.
- reference 파일은 한 단계 깊이만 유지합니다. `SKILL.md`에서 직접 링크할 수 있어야 합니다.
- 같은 내용은 한 곳에만 둡니다. 중복이 필요해 보이면 더 일반적인 reference로 합칩니다.
- 예시는 짧게 유지하고, 원칙을 설명하는 데 필요한 만큼만 둡니다.

## 검증

스킬 구조를 수정한 뒤에는 다음 명령으로 기본 형식을 검증합니다.

```bash
python3 /Users/yusunsang/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/yusunsang/Downloads/technical-writing-master
```

정상이라면 다음 메시지가 출력됩니다.

```text
Skill is valid!
```

## 출처와 라이선스

이 스킬은 Toos의 테크니컬 라이팅 가이드 자료를 기반으로 정리했습니다.

원 자료의 라이선스는 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License(CC BY-NC-SA 4.0)입니다.

https://creativecommons.org/licenses/by-nc-sa/4.0/
https://github.com/toss/technical-writing