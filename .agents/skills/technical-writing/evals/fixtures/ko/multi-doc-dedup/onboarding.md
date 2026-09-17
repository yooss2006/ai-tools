# 신규 개발자 온보딩

## 인증 구조 이해하기

Access Token은 메모리에 저장합니다. API 요청 시 Axios interceptor가 토큰을 헤더에 넣습니다. Access Token이 만료되면 Refresh Token을 이용해 다시 발급합니다.

인증 관련 코드를 수정하기 전에 `src/auth`와 `src/api`를 확인하세요.
