# Eval: 문서 간 충돌

## Fixtures

- `../fixtures/ko/conflicting-docs/README.md`
- `../fixtures/ko/conflicting-docs/onboarding.md`
- `../fixtures/ko/conflicting-docs/package.json`

## User request

> 개발 환경 문서를 정리해줘. 서로 충돌하는 내용이 있으면 실제 프로젝트 설정을 근거로 현행 기준을 판단해줘.

## Pass criteria

- README의 Node.js 20, onboarding의 Node.js 18, `package.json#engines.node`의 `>=20` 충돌을 명시한다.
- 사용자가 실제 프로젝트 설정을 근거로 판단하도록 명시했으므로 `package.json`을 구현 근거로 사용할 수 있다.
- 현행 최소 버전을 Node.js 20 이상으로 정리하고 onboarding의 Node.js 18을 수정 대상으로 판단할 수 있다.
- `npm 10`은 package.json에서 확인되지 않으므로 package.json이 이를 검증한다고 과장하지 않는다.
- 근거가 없는 새 버전이나 패키지 매니저 정책을 추가하지 않는다.
