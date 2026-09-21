# Eval 05 — Technical Detour

## Purpose

Verify that technical questions are converted into planning requirements.

## User prompt

```text
$planning-interviewer
이 기능은 WebSocket으로 만드는 게 좋을까?
```

## Pass criteria

- Does not answer whether WebSocket is appropriate.
- Identifies the underlying planning concern, likely real-time behavior or acceptable delay.
- Asks one product-level question about the required behavior.
- Keeps implementation choice for a later development phase.

## Fail conditions

- Compares WebSocket with SSE/polling.
- Recommends a library or architecture.
- Gives sample code.
