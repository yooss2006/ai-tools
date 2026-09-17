# Eval: 명시적으로 허용된 문서 분리

## Fixture

`../fixtures/ko/restructure-large-doc/monolith.md`

## User request

> 이 문서는 설치, 첫 사용 튜토리얼, API 옵션 참조, 장애 대응이 한 파일에 섞여 있어. 목적별 문서로 분리해서 구조를 재구성해줘. 파일을 여러 개로 나눠도 돼.

## Pass criteria

- Learning / Reference / Problem solving 성격이 섞여 있음을 인식한다.
- 사용자가 **분리와 재구성을 명시적으로 허용했으므로** 별도의 구조 승인 질문을 하지 않는다.
- 설치/첫 성공 흐름, 옵션 참조, 장애 대응의 reader goal을 분리한다.
- overview 또는 navigation 문서와 cross-link 계획을 포함할 수 있다.
- 기존 내용에 없는 API 동작이나 옵션을 새로 만들어내지 않는다.

## Fail examples

- "여러 파일로 나눠도 될까요?"처럼 이미 허용된 변경을 다시 확인한다.
- 원문에 없는 설정 옵션이나 오류 코드를 추가한다.
