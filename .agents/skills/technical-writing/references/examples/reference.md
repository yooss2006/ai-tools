# Example — Reference Document

This example demonstrates the pattern; it is not a canonical rule source.

# `retry` 옵션

`retry`는 실패한 요청을 다시 시도하는 횟수를 설정합니다.

## Type

```ts
retry: number
```

## Default

`0`

## Constraints

- 0 이상의 정수를 사용합니다.
- `0`이면 자동 재시도를 수행하지 않습니다.

## Example

```ts
createClient({
  retry: 3,
});
```

## Related options

- `retryDelay`: 재시도 사이의 대기 시간을 설정합니다.
