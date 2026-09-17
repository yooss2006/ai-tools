# 인증 아키텍처

## 토큰 저장

Access Token은 브라우저 메모리에만 보관합니다. Refresh Token은 HttpOnly 쿠키로 관리합니다.

## API 요청

Axios interceptor가 Access Token을 `Authorization: Bearer <token>` 헤더에 추가합니다.

## 갱신 흐름

API가 401을 반환하고 Access Token 만료가 확인되면 `/auth/refresh`를 호출합니다. 서버는 HttpOnly 쿠키의 Refresh Token을 검증한 뒤 새 Access Token을 반환합니다. 갱신에 실패하면 클라이언트는 세션을 종료하고 로그인 화면으로 이동합니다.
