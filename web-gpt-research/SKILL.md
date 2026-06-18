---
name: web-gpt-research
description: Explicit-only workflow for preparing, user-approving, and then submitting a research prompt to ChatGPT/Web GPT through the user's signed-in Chrome profile. Use only when explicitly invoked as $web-gpt-research; do not use implicitly. Use Deep Research only when the user explicitly requests Deep Research.
---

# Web GPT Research

Use this skill only when the user explicitly invokes `$web-gpt-research`.

This skill delegates external web research to ChatGPT/Web GPT through the user's signed-in Chrome profile, but only after the user approves the exact prompt that will be submitted.

Do not use this skill for repository-local code investigation, debugging, implementation research, or ordinary web lookup that Codex can complete directly.

## Core Rules

- Use the Codex Chrome extension and the user's existing Chrome session.
- Require the Codex Chrome extension. If the extension is not installed, not connected, disabled, unavailable, blocked for the target site, or otherwise unusable, stop the request and report that Chrome extension access is required.
- Do not fall back to the in-app browser, generic browser automation, direct web search, or manual prompt submission unless the user explicitly starts a new request with different instructions.
- Never ask for, store, type, infer, or handle passwords, passkeys, recovery codes, OTPs, SSO credentials, or backup codes.
- If ChatGPT/Web GPT is not signed in, stop and ask the user to log in manually in Chrome. Resume only after the user confirms login is complete.
- Use normal ChatGPT/Web GPT research by default.
- Use Deep Research only when the user explicitly asks for "Deep Research", "deep research", "딥 리서치", or an equivalent instruction in the same request.
- Treat ChatGPT/Web GPT output as research leads, not final truth.

## Approval Loop

When the user invokes `$web-gpt-research` with a question:

1. Understand the user's research objective.
2. Decide whether the request asks for normal research or Deep Research.
3. Draft the exact prompt to send to ChatGPT/Web GPT.
4. Show the prompt to the user before opening or submitting anything.
5. Ask whether to submit it or revise it.
6. If the user suggests changes, revise the prompt and show the updated version.
7. Repeat until the user clearly approves submission.
8. Only after approval, open ChatGPT/Web GPT in Chrome and submit the approved prompt.

Do not submit an unapproved prompt.

## Prompt Requirements

The draft prompt should ask ChatGPT/Web GPT for:

- a direct answer first
- dated facts when recency matters
- source links
- conflicting evidence
- uncertainty notes
- claims that need verification
- a concise synthesis in the user's requested language and format

For Deep Research requests, make the prompt include:

- research question
- region or market
- time window
- source preferences
- exclusions
- desired output format

If Deep Research scope is ambiguous but still workable, choose conservative defaults and state them in the draft prompt. Ask the user a clarifying question only when ambiguity would materially change the result or create risk.

## Chrome Execution

Before submitting the approved prompt:

1. Verify the Codex Chrome extension is installed, connected, enabled, and allowed to access the target ChatGPT/Web GPT domain.
2. If Chrome extension access is unavailable, stop immediately and explain that the request cannot proceed without it.
3. Verify Chrome is using the expected ChatGPT/Web GPT domain.
4. Verify the user appears signed in.
5. If login is required, pause for manual user login.
6. Submit exactly the approved prompt.
7. Wait for the result.
8. Capture the answer and cited sources.

## Slow Response Handling

After submitting the approved prompt, monitor visible progress while waiting for the response.

For normal ChatGPT/Web GPT research, wait at least 2-3 minutes before treating the response as delayed. For Deep Research, expect long runtimes and wait at least 10-20 minutes unless the user requests otherwise.

If the response is still generating after the relevant wait window, report the status to the user and ask whether to keep waiting, capture the visible partial result, or stop.

If a partial answer is visible, capture it only as a partial result and clearly label it as incomplete.

If the page appears stuck, errored, or offers continue/regenerate controls, do not resubmit, restart, continue, or regenerate the research without user approval, because that may create duplicate or inconsistent research runs.

If Deep Research is still running, prefer waiting or asking the user whether to continue monitoring. Do not assume failure solely from a long wait.

## Final Synthesis

After receiving the ChatGPT/Web GPT result:

- verify important claims, especially dates, prices, laws, product specs, availability, statistics, and named people or company facts
- separate well-supported findings from uncertain or weakly supported claims
- include source links when available
- mention material claims that could not be independently verified
- produce the final answer in the format the user requested
