# Checkout Frontend

결제 프론트엔드입니다.

## 인증

사용자가 로그인하면 브라우저는 Access Token을 메모리에 보관합니다. API 요청은 Axios interceptor에서 Access Token을 `Authorization` 헤더에 추가합니다. Access Token이 만료되면 Refresh Token으로 새 Access Token을 발급받습니다.

## 개발 문서

- `architecture.md`
- `onboarding.md`
