#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
# --- How to run ---
# python3 /Users/yusunsang/.codex/hooks/codex_macos_alert.py < sample-hook.json

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Final, List, Optional, Tuple, Union

Json = Union[None, bool, int, float, str, List["Json"], Dict[str, "Json"]]
JsonDict = Dict[str, Json]

CODEX_HOME: Final = Path(__file__).resolve().parent.parent
WINDOW: Final = 30.0
MAX_CHARS: Final = 84
DEFAULT_WAITING: Final = "Codex가 사용자 답변을 기다리고 있습니다."
DEFAULT_COMPLETE: Final = "Codex 작업이 완료되었습니다."
DEFAULT_CHECK: Final = "Codex가 멈췄습니다. 계속하려면 현재 상태를 확인해야 합니다."
LOCAL_ICON: Final = Path(__file__).resolve().with_name("hamster-alert-icon.icns")
PACKAGE_ICON: Final = Path(__file__).resolve().parent.parent / "assets" / "hamster-alert-icon.icns"
ALERT_ICON: Final = str(LOCAL_ICON if LOCAL_ICON.exists() else PACKAGE_ICON)
ICON_BY_STYLE: Final[Dict[str, str]] = {
    "critical": ALERT_ICON,
    "warning": ALERT_ICON,
    "informational": ALERT_ICON,
}

EVENT_KEYS: Final = ("hook_event_name", "hookEventName", "event_name", "event")
ASSISTANT_KEYS: Final = ("final_response", "finalResponse", "last_assistant_message", "lastAssistantMessage", "assistant_message", "assistantMessage", "response", "message")
PROBLEM_WORDS: Final = ("blocked", "failed", "failure", "cannot continue", "can't continue", "unable to continue", "error:", "exception", "차단", "실패", "오류", "에러", "진행할 수 없")
WAIT_WORDS: Final = ("do you want", "would you like", "should i", "please confirm", "please choose", "please provide", "답변", "선택", "승인", "허용", "알려주세요", "입력", "확인해 주세요")


@dataclass(frozen=True)
class Alert:
    title: str
    style: str
    summary: str


def main() -> int:
    try:
        payload = read_payload()
        alert = classify(payload) if payload else None
        if alert is not None and not duplicate(payload, alert):
            dispatch(alert)
    except Exception:
        return 0
    return 0


def read_payload() -> Optional[JsonDict]:
    raw = sys.stdin.read()
    if not raw.strip():
        return None
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, dict):
        return None
    return {key: value for key, value in parsed.items() if isinstance(key, str)}


def classify(payload: JsonDict) -> Optional[Alert]:
    event = pick(payload, EVENT_KEYS)
    if event == "PermissionRequest":
        return None
    if event == "Stop":
        return stop_alert(payload)
    return None


def stop_alert(payload: JsonDict) -> Alert:
    message = assistant_message(payload)
    haystack = ("%s %s" % (" ".join(strings(payload, 60)), message)).lower()
    if any(word in haystack for word in PROBLEM_WORDS):
        return Alert("Codex 확인 필요", "critical", summarize(message, DEFAULT_CHECK))
    if waiting(message):
        return Alert("Codex 사용자 응답 필요", "warning", wait_summary(message))
    return Alert("Codex 작업 완료", "informational", summarize(message, DEFAULT_COMPLETE))


def pick(value: Json, keys: Tuple[str, ...]) -> str:
    if isinstance(value, dict):
        for key in keys:
            found = value.get(key)
            if isinstance(found, str) and found.strip():
                return found.strip()
        for child in value.values():
            found = pick(child, keys)
            if found:
                return found
    if isinstance(value, list):
        for child in value:
            found = pick(child, keys)
            if found:
                return found
    return ""


def strings(value: Json, limit: int) -> List[str]:
    result: List[str] = []

    def visit(item: Json) -> None:
        if len(result) >= limit:
            return
        if isinstance(item, str):
            text = item.strip()
            if text:
                result.append(text)
        elif isinstance(item, dict):
            for child in item.values():
                visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)

    visit(value)
    return result


def assistant_message(payload: JsonDict) -> str:
    direct = pick(payload, ASSISTANT_KEYS)
    if direct:
        return direct
    transcript = pick(payload, ("transcript_path", "transcriptPath"))
    return transcript_message(Path(transcript)) if transcript else ""


def transcript_message(path: Path) -> str:
    try:
        with path.open("rb") as transcript_file:
            transcript_file.seek(0, os.SEEK_END)
            transcript_file.seek(max(0, transcript_file.tell() - 1_048_576))
            raw = transcript_file.read().decode("utf-8", "replace")
    except OSError:
        return ""
    for line in reversed(raw.splitlines()):
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        text = assistant_text(parsed)
        if text:
            return text
    return ""


def assistant_text(value: Json) -> str:
    if isinstance(value, dict):
        if value.get("role") == "assistant":
            return content_text(value.get("content"))
        kind = value.get("type")
        if isinstance(kind, str) and "assistant" in kind.lower():
            return content_text(value.get("message")) or content_text(value.get("content"))
        for key in ("payload", "message", "content"):
            text = assistant_text(value.get(key))
            if text:
                return text
    if isinstance(value, list):
        for child in reversed(value):
            text = assistant_text(child)
            if text:
                return text
    return ""


def content_text(value: Json) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        for key in ("text", "message", "content"):
            text = content_text(value.get(key))
            if text:
                return text
    if isinstance(value, list):
        return " ".join(text for text in (content_text(item) for item in value) if text).strip()
    return ""


def waiting(text: str) -> bool:
    normalized = normalize(text).lower()
    return normalized.endswith(("?", "？")) or any(word in normalized for word in WAIT_WORDS)


def wait_summary(text: str) -> str:
    summary = summarize(text, DEFAULT_WAITING)
    return summary if summary == DEFAULT_WAITING else trim("Codex가 사용자 답변을 기다립니다: %s" % summary)


def summarize(text: str, default: str) -> str:
    normalized = normalize(text)
    if not normalized:
        return default
    return trim(re.split(r"(?<=[.!?。！？])\s+", normalized, maxsplit=1)[0] or default)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" -`")


def trim(text: str) -> str:
    return text if len(text) <= MAX_CHARS else "%s..." % text[: MAX_CHARS - 3].rstrip()


def duplicate(payload: JsonDict, alert: Alert) -> bool:
    state_dir = Path(os.environ.get("CODEX_MACOS_ALERT_STATE_DIR") or str(CODEX_HOME / "state" / "codex-alerts"))
    state_path = state_dir / "dedupe.json"
    now = time.time()
    fingerprint = digest(payload, alert)
    try:
        state_dir.mkdir(parents=True, exist_ok=True)
        state = read_state(state_path)
        if fingerprint in state and now - state[fingerprint] < WINDOW:
            return True
        state[fingerprint] = now
        state = {key: stamp for key, stamp in state.items() if now - stamp <= WINDOW * 4}
        tmp = state_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, separators=(",", ":")), encoding="utf-8")
        tmp.replace(state_path)
    except OSError:
        return False
    return False


def read_state(path: Path) -> Dict[str, float]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(parsed, dict):
        return {}
    return {key: float(value) for key, value in parsed.items() if isinstance(key, str) and isinstance(value, (int, float))}


def digest(payload: JsonDict, alert: Alert) -> str:
    parts = {
        "event": pick(payload, EVENT_KEYS),
        "title": alert.title,
        "summary": alert.summary,
        "tool": pick(payload, ("tool_name", "toolName", "tool")),
        "cwd": pick(payload, ("cwd", "working_directory", "workingDirectory")),
        "session": pick(payload, ("session_id", "sessionId", "thread_id", "threadId")),
    }
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def dispatch(alert: Alert) -> None:
    icon = icon_path(alert.style)
    capture = os.environ.get("CODEX_MACOS_ALERT_CAPTURE")
    if capture:
        Path(capture).parent.mkdir(parents=True, exist_ok=True)
        with Path(capture).open("a", encoding="utf-8") as capture_file:
            capture_file.write(json.dumps({"title": alert.title, "style": alert.style, "icon": icon, "message": alert.summary}, ensure_ascii=False) + "\n")
        return
    if platform.system() != "Darwin":
        return
    osascript = shutil.which("osascript")
    if osascript is None:
        return
    script = (
        "const app = Application.currentApplication();"
        "app.includeStandardAdditions = true;"
        "app.displayDialog(%s, {withTitle: %s, buttons: [\"확인\"], "
        "defaultButton: \"확인\", withIcon: Path(%s)});"
    ) % (js_string(alert.summary), js_string(alert.title), js_string(icon))
    try:
        subprocess.Popen([osascript, "-l", "JavaScript", "-e", script], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True, close_fds=True)
    except OSError:
        return


def icon_path(style: str) -> str:
    return ICON_BY_STYLE.get(style, ICON_BY_STYLE["informational"])


def js_string(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)


if __name__ == "__main__":
    raise SystemExit(main())
