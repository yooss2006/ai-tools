# Widget SDK 사용법

Widget SDK를 설치하고 사용하는 방법과 전체 옵션, 장애 해결 방법을 설명합니다.

## 설치

```bash
npm install @acme/widget
```

## 첫 위젯 만들기

```ts
import { createWidget } from '@acme/widget';

const widget = createWidget({ target: '#app' });
widget.mount();
```

브라우저에서 위젯이 표시되면 설치가 완료된 것입니다.

## 옵션

### target

위젯을 마운트할 CSS selector입니다. 필수 값입니다.

### theme

`light` 또는 `dark`를 사용할 수 있습니다. 기본값은 `light`입니다.

### retry

초기화 실패 시 재시도 횟수입니다. 기본값은 `2`입니다.

## 위젯이 표시되지 않을 때

1. `target` selector가 실제 DOM 요소와 일치하는지 확인합니다.
2. 개발자 도구 콘솔에서 `WIDGET_TARGET_NOT_FOUND` 오류를 확인합니다.
3. 위젯을 생성하기 전에 대상 DOM이 렌더링됐는지 확인합니다.

## 인증 오류

`WIDGET_UNAUTHORIZED`가 발생하면 발급받은 API 키가 현재 도메인에서 사용 가능한지 확인합니다.
