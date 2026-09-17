# Eval: 여러 문서 중복 정리

## Fixtures

- `../fixtures/ko/multi-doc-dedup/README.md`
- `../fixtures/ko/multi-doc-dedup/architecture.md`
- `../fixtures/ko/multi-doc-dedup/onboarding.md`

## User request

> 세 문서의 인증 설명 중복을 정리해줘. 필요한 맥락은 남기되 같은 사실을 여러 곳에서 따로 유지보수하지 않게 해줘.

## Pass criteria

- 세 파일을 하나의 documentation system으로 분석한다.
- 문장 일치가 아니라 의미 중복을 찾는다.
- `architecture.md`가 토큰 저장, 갱신 조건, 실패 처리까지 가장 상세하므로 상세 인증 구조의 Source of Truth 후보로 판단할 수 있다.
- README와 onboarding에서 독자에게 필요한 짧은 맥락은 유지하고 Architecture로 연결하는 방안을 제시한다.
- 무조건 모든 중복 문장을 삭제하지 않는다.
- 세 문서의 토큰 저장 설명이 완전히 동일하지 않다는 점(README는 Refresh Token 저장 위치를 생략)을 의미 차이로 인식한다.
