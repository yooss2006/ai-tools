# Example — Problem-solving Document

This example demonstrates the pattern; it is not a canonical rule source.

# 개발 서버 포트 충돌 해결하기

개발 서버를 실행할 때 `address already in use` 오류가 발생하면 사용하려는 포트를 다른 프로세스가 점유하고 있는지 확인합니다.

## Problem

서버가 시작되지 않고 이미 사용 중인 포트라는 오류가 표시됩니다.

## Resolution

### 1. 포트를 점유한 프로세스 확인하기

macOS/Linux 예시:

```bash
lsof -i :3000
```

### 2. 프로세스를 종료하거나 다른 포트 사용하기

프로세스가 불필요하다면 정상 종료합니다. 기존 프로세스를 유지해야 한다면 개발 서버의 포트를 변경합니다.

## Verify the fix

개발 서버를 다시 실행하고 브라우저에서 새 주소로 접속합니다.
