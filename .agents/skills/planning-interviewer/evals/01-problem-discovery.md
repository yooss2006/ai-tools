# Eval 01 — Problem Discovery

## Purpose

Verify that the skill discovers problems instead of immediately generating product ideas.

## User prompt

```text
$planning-interviewer
사이드 프로젝트 하나 하고 싶은데 아직 아이디어가 없어. 뭐 만들지 같이 정해보자.
```

## Pass criteria

- Does not immediately output a list of app/SaaS ideas.
- Recognizes that the user is in an exploratory state.
- Starts with one high-value problem-discovery question.
- Preferably asks about recurring frustration, workaround, wasted effort, or an area the user understands.
- Does not discuss implementation technology.

## Strong behavior example

The response briefly explains that it will start from problems rather than solutions, then asks one free-form question such as a recent recurring frustration.

## Fail conditions

- Produces 10 startup ideas.
- Starts asking about framework, platform, or database.
- Asks a long questionnaire in one turn.
- Treats a guessed problem as a confirmed user problem.
