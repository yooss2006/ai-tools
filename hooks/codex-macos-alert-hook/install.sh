#!/bin/zsh
set -eu

SCRIPT_DIR=${0:A:h}
CODEX_DIR=${CODEX_HOME:-"$HOME/.codex"}
HOOK_DIR="$CODEX_DIR/hooks"
HOOK_FILE="$HOOK_DIR/codex_macos_alert.py"
ICON_FILE="$HOOK_DIR/hamster-alert-icon.icns"
HOOKS_JSON="$CODEX_DIR/hooks.json"
ALERT_COMMAND='/bin/zsh -lc '\''exec /usr/bin/python3 "${CODEX_HOME:-$HOME/.codex}/hooks/codex_macos_alert.py"'\'''

mkdir -p "$HOOK_DIR"
cp "$SCRIPT_DIR/hooks/codex_macos_alert.py" "$HOOK_FILE"
cp "$SCRIPT_DIR/assets/hamster-alert-icon.icns" "$ICON_FILE"
chmod +x "$HOOK_FILE"

if [[ -f "$HOOKS_JSON" ]]; then
  cp "$HOOKS_JSON" "$HOOKS_JSON.bak.$(date +%Y%m%d%H%M%S)"
fi

/usr/bin/python3 - "$HOOKS_JSON" "$ALERT_COMMAND" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

path = Path(sys.argv[1])
alert_command = sys.argv[2]

data: dict[str, Any] = {}
if path.exists() and path.read_text(encoding="utf-8").strip():
    parsed = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(parsed, dict):
        raise SystemExit("hooks.json must contain a JSON object.")
    data = parsed

hooks = data.setdefault("hooks", {})
if not isinstance(hooks, dict):
    raise SystemExit("hooks.json hooks field must be a JSON object.")

stop_hooks = hooks.setdefault("Stop", [])
if not isinstance(stop_hooks, list):
    raise SystemExit("hooks.Stop must be a JSON array.")

entry = {
    "hooks": [
        {
            "type": "command",
            "command": alert_command,
            "timeout": 5,
        }
    ]
}

def has_alert_hook(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    nested = item.get("hooks")
    if not isinstance(nested, list):
        return False
    for hook in nested:
        if isinstance(hook, dict) and "codex_macos_alert.py" in str(hook.get("command", "")):
            return True
    return False

if not any(has_alert_hook(item) for item in stop_hooks):
    stop_hooks.append(entry)

path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

echo "Installed Codex macOS alert hook at $HOOK_FILE"
echo "Installed alert icon at $ICON_FILE"
echo "Updated $HOOKS_JSON"
