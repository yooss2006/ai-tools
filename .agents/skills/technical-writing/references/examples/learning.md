# Example — Learning Document

This example demonstrates the pattern; it is not a canonical rule source.

# Vite에서 환경 변수 사용하기

Vite 프로젝트에서 API 기본 URL을 환경 변수로 분리하고 애플리케이션 코드에서 읽는 방법을 익힙니다. 완료하면 개발 환경별 URL을 코드 수정 없이 바꿀 수 있습니다.

## Goal

- `.env` 파일에 값을 정의합니다.
- `import.meta.env`로 값을 읽습니다.
- 브라우저에서 적용 여부를 확인합니다.

## Prerequisites

- 실행 가능한 Vite 프로젝트
- Node.js와 패키지 설치 완료

## 1. 환경 변수 추가하기

프로젝트 루트의 `.env`에 `VITE_` 접두사가 붙은 변수를 추가합니다.

```dotenv
VITE_API_BASE_URL=https://api.example.test
```

## 2. 애플리케이션에서 읽기

```ts
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
console.log(apiBaseUrl);
```

## 3. 결과 확인하기

개발 서버를 다시 시작한 뒤 브라우저 콘솔에서 설정한 URL이 출력되는지 확인합니다.

## FAQ

### 값이 `undefined`입니다

변수 이름이 `VITE_`로 시작하는지 확인하고 개발 서버를 다시 시작합니다.
