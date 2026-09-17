# Eval: 기존 ADR 리뷰

## Fixture

`../fixtures/ko/review-existing-adr/adr.md`

## User request

> 이 ADR을 점검해줘. 문제점과 왜 문제인지, 어떻게 고치면 좋을지만 알려줘. 문서 자체는 아직 수정하지 마.

## Pass criteria

- ADR profile을 감지하되 문서를 RFC처럼 확장하지 않는다.
- `배경 및 결정`, `대안과 영향` 섹션에서 Context/Decision/Alternatives/Consequences가 섞여 있어 탐색성이 낮다는 점을 지적한다.
- 현재 결정(`React Query 사용`, 기존 SWR은 점진 전환)을 임의로 변경하지 않는다.
- 각 지적에 실제 섹션이나 문장을 근거로 제시한다.
- 기본 결과는 **문제점 + 근거 + 수정 방향**으로 끝낸다.
- 사용자가 수정 금지를 명시했으므로 전체 수정본이나 재작성된 ADR을 제공하지 않는다.
