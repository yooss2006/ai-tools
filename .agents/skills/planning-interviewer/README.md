# Planning Interviewer Skill

`planning-interviewer` is an interview-driven planning skill for ChatGPT and Codex.

It does **not** plan a product on the user's behalf. It extracts, tests, connects, and structures the user's own decisions through an adaptive interview.

## What it is for

Use it when you want to:

- discover a problem before choosing a solution;
- validate an existing product/service idea;
- turn a rough idea into a concrete plan;
- review an existing PRD or planning document;
- identify contradictions, missing policies, edge cases, or unnecessary scope;
- prepare an implementation-independent planning handoff.

The default focus is digital products and services, but the interview method can also be used for other planning work.

## What it deliberately does not do

While the planning session is active, the skill does not decide or recommend:

- programming languages or frameworks;
- API design;
- database design;
- architecture;
- infrastructure;
- libraries;
- source-code structure;
- implementation strategy.

Technical questions are translated into product/planning requirements when possible.

## Explicit invocation only

This package sets:

```yaml
policy:
  allow_implicit_invocation: false
```

in `agents/openai.yaml`.

### ChatGPT

After the skill is installed in a ChatGPT environment that supports Skills, invoke it explicitly:

```text
@planning-interviewer
새로운 서비스를 생각하고 있어. 인터뷰하면서 구체화해줘.
```

### Codex

Invoke it explicitly with `$` or select it from `/skills`:

```text
$planning-interviewer
이 기능을 구현하기 전에 기획부터 정리하자.
```

For a personal Codex skill, place the unzipped folder under:

```text
~/.agents/skills/planning-interviewer
```

For a repository-specific skill, place it under:

```text
<repo>/.agents/skills/planning-interviewer
```

## Conversation model

Once invoked, the skill stays in the planning role for the current planning topic.

Typical behavior:

1. understand the current plan instead of starting from a fixed questionnaire;
2. reconstruct what is fact, decided, hypothetical, open, or dropped;
3. find the highest-value uncertainty;
4. ask one core decision at a time;
5. update the plan and re-check affected decisions;
6. move between exploration, validation, elaboration, review, external validation, and synthesis as needed;
7. stop when the plan is sufficiently coherent and the user chooses to finalize.

## Example prompts

### Start from a vague idea

```text
@planning-interviewer
요즘 사이드 프로젝트를 하나 만들고 싶은데 아이디어가 아직 명확하지 않아.
```

The skill should start with problem discovery rather than dumping app ideas.

### Validate an existing idea

```text
@planning-interviewer
회의 내용을 AI로 자동 정리하는 서비스를 생각 중이야. 내 생각부터 인터뷰해줘.
```

The skill should preserve the solution idea but investigate the underlying problem and desired outcome first.

### Review an existing plan

```text
$planning-interviewer
이 PRD를 기준으로 이미 결정된 내용은 다시 묻지 말고 빈칸과 모순부터 인터뷰해줘.
```

### Control scope

```text
$planning-interviewer
기획이 너무 커진 것 같아. 핵심 목표 기준으로 범위를 다시 검증해줘.
```

### Create a handoff only when requested

```text
지금 상태를 다음 대화에서 이어갈 수 있게 planning-handoff.md로 정리해줘.
```

## Package structure

```text
planning-interviewer/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── interview-principles.md
│   ├── planning-state.md
│   ├── state-strategies.md
│   ├── boundaries.md
│   ├── external-validation.md
│   └── output-guide.md
└── evals/
    ├── 01-problem-discovery.md
    ├── 02-idea-validation.md
    ├── 03-existing-plan.md
    ├── 04-contradiction.md
    ├── 05-technical-detour.md
    ├── 06-scope-reduction.md
    ├── 07-delegated-decision.md
    ├── 08-plan-change.md
    ├── 09-completion.md
    └── 10-resume-handoff.md
```

## Design principles

- Interview before proposing.
- Ask only what materially changes the plan.
- One core decision per turn by default.
- Do not ask again when the answer is already known.
- Recommendations are permitted; silent decisions are not.
- Track facts, decisions, hypotheses, open items, and dropped directions separately.
- Keep the latest plan as the source of truth and preserve only important decision history.
- External research validates the plan; it does not replace the user's decisions.
- UX and product behavior are in scope. Visual design and implementation are not.
- File writes happen only on explicit request.

## Evals

The `evals/` directory contains behavior-based scenarios. They test whether the skill behaves like an interviewer rather than a plan generator, including technical detours, contradictions, delegated decisions, scope reduction, completion, and handoff resumption.

## Validation

From the repository root, run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .agents/skills/planning-interviewer
```

A valid skill should report `Skill is valid!`.
