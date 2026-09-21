# Eval 09 — Completion

## Purpose

Verify that the skill recognizes sufficient planning and does not interview forever.

## Conversation state

Assume the following are already coherent and confirmed:

- problem and user;
- core value;
- main journey;
- scope;
- material policies and exceptions;
- operating model;
- success criterion.

Remaining:

- one low-priority open policy;
- one external market hypothesis.

## User prompt

```text
이제 더 물어볼 거 있어?
```

## Pass criteria

- Performs a sufficiency judgment instead of inventing more mandatory questions.
- States that the core plan is sufficiently concrete if appropriate.
- Surfaces the remaining open item and hypothesis.
- Offers continue / finalize / external validation choices.
- Does not force the user to answer low-priority items before finalization.

## Fail conditions

- Starts another long checklist.
- Claims everything is fully validated when a hypothesis remains.
- Finalizes without user choice.
