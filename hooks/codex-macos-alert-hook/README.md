# Codex macOS Alert Hook

Codex Desktop 앱과 Codex CLI에서 작업이 멈추거나 끝났을 때 macOS 확인 창을 띄우는 `Stop` hook 패키지입니다.

이 패키지는 `PermissionRequest` hook을 등록하지 않습니다. 현재 Codex 0.142.5에서는 auto-review 권한 검토와 실제 사용자 승인 대기를 hook payload만으로 구분할 수 없어, `PermissionRequest` alert를 켜면 중간 false alert가 발생할 수 있습니다.

## 포함 파일

```text
codex-macos-alert-hook/
├── assets/
│   ├── hamster-alert-icon.icns
│   └── hamster-alert-icon.png
├── hooks/
│   └── codex_macos_alert.py
├── hooks.stop.snippet.json
├── install.sh
└── README.md
```

## 설치

압축을 푼 폴더에서 실행합니다.

```bash
chmod +x install.sh
./install.sh
```

설치 스크립트가 하는 일:

- `~/.codex/hooks/codex_macos_alert.py`로 hook 파일을 복사합니다.
- `~/.codex/hooks/hamster-alert-icon.icns`로 alert 아이콘을 복사합니다.
- 기존 `~/.codex/hooks.json`이 있으면 `hooks.json.bak.YYYYMMDDHHMMSS`로 백업합니다.
- 기존 hook 설정을 유지한 채 `Stop` hook만 추가합니다.
- 이미 같은 alert hook이 있으면 중복 추가하지 않습니다.

설치 후 Codex Desktop 앱을 재시작하거나 새 Codex CLI 세션을 열어 적용합니다.

## 수동 설치

자동 설치를 쓰지 않으려면 아래 순서로 적용합니다.

```bash
mkdir -p ~/.codex/hooks
cp hooks/codex_macos_alert.py ~/.codex/hooks/codex_macos_alert.py
cp assets/hamster-alert-icon.icns ~/.codex/hooks/hamster-alert-icon.icns
chmod +x ~/.codex/hooks/codex_macos_alert.py
```

그다음 `~/.codex/hooks.json`의 `hooks` 객체 안에 `hooks.stop.snippet.json`의 `Stop` 항목을 병합합니다. 기존 `UserPromptSubmit`, `PreToolUse` 같은 다른 hook은 지우지 마세요.

## 동작

상태별 제목과 아이콘:

| 상태 | 제목 | 아이콘 |
| --- | --- | --- |
| 정상 완료 | `Codex 작업 완료` | `hamster-alert-icon.icns` |
| 사용자 응답 필요 | `Codex 사용자 응답 필요` | `hamster-alert-icon.icns` |
| 오류 또는 차단 | `Codex 확인 필요` | `hamster-alert-icon.icns` |

메시지는 Codex 마지막 응답에서 첫 문장만 짧게 요약합니다. 같은 alert는 30초 안에 중복 표시하지 않습니다.
아이콘을 바꾸려면 같은 이름의 `.icns` 파일로 `~/.codex/hooks/hamster-alert-icon.icns`를 교체하세요.

## 검증

alert를 실제로 띄우지 않고 캡처 파일로 확인하려면 다음 명령을 실행합니다.

```bash
tmp=/tmp/codex-alert-test.jsonl
printf '%s' '{"hook_event_name":"Stop","last_assistant_message":"작업이 완료되었습니다."}' \
  | CODEX_MACOS_ALERT_CAPTURE="$tmp" /usr/bin/python3 ~/.codex/hooks/codex_macos_alert.py
cat "$tmp"
```

출력에 `Codex 작업 완료`와 `hamster-alert-icon.icns` 경로가 보이면 hook 파일은 정상입니다.

실제 macOS 확인 창을 테스트하려면 `CODEX_MACOS_ALERT_CAPTURE`를 빼고 실행합니다.

## 문제 해결

- alert가 뜨지 않으면 Codex를 재시작하거나 새 세션을 여세요. 실행 중인 세션은 hook 설정을 다시 읽지 않을 수 있습니다.
- `~/.codex/hooks.json`이 깨졌다면 설치 전 생성된 `hooks.json.bak.*` 파일로 복구하세요.
- 다른 hook이 사라졌다면 수동 병합 중 `hooks` 객체 전체를 덮어쓴 것입니다. 백업 파일에서 기존 항목을 되돌린 뒤 `Stop` 항목만 추가하세요.
- auto-review 중 권한 검토 alert는 의도적으로 지원하지 않습니다. 실제 사용자 승인 대기와 구분할 수 있는 필드가 Codex hook payload에 추가되면 `PermissionRequest` hook을 다시 켤 수 있습니다.
