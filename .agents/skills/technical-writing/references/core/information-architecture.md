# Information Architecture

This file is the canonical source for page-level technical-document structure. Do not duplicate these rules in other references; link or refer to the rule ID instead.

## Strength levels

- `MUST`: violating the rule is likely to make the document incorrect, misleading, or unusable.
- `SHOULD`: apply by default, but a clear document-specific reason can justify an exception.
- `HEURISTIC`: a diagnostic signal, not a mechanical requirement.

## IA-ONE — Keep one primary goal per page

**Strength:** SHOULD

A page should have one clear reader goal. Multiple related concepts may support that goal, but unrelated goals should not compete for attention.

**Signals that the scope may be too broad:**

- two or more independent reader goals;
- the same page acts as tutorial, full reference, and troubleshooting guide at substantial depth;
- readers must skip large sections to reach what they came for;
- heading depth keeps increasing to contain unrelated branches.

**HEURISTIC:** H4 (`####`) or deeper headings are a signal to inspect the page boundary. They are not an automatic reason to split a document.

**Before**

```text
# React 사용법
## Components
### JSX
#### JSX edge cases
## State management
### useState
#### useState edge cases
```

**After**

```text
react/
├── components.md
├── state-management.md
└── overview.md
```

Use an overview page to connect focused pages when readers still need the big picture.

## IA-VALUE — Put reader value before implementation detail

**Strength:** SHOULD

Before listing features, options, history, or configuration details, explain what problem the document helps solve or what capability the reader gains.

**Before**

> 이 설정에는 여러 timeout과 retry 옵션이 있습니다.

**After**

> 이 설정을 적용하면 일시적인 네트워크 실패에서 요청을 자동으로 복구할 수 있습니다.

Do not invent benefits or quantitative gains that are not supported.

## IA-HEADING — Write informative, scannable headings

**Strength:** SHOULD

Headings should let readers predict the content without reading the section first.

- include the key term readers are likely to scan or search for;
- keep sibling headings grammatically consistent;
- prefer descriptive statements or task-oriented phrases over vague questions;
- keep headings concise enough to scan.

**HEURISTIC:** about 30 Korean characters can be a useful brevity target, not a hard limit.

**Before**

```text
## 어떻게 해야 할까요?
## 설정
## 확인하는 법
```

**After**

```text
## API 키 설정하기
## 환경 변수 등록하기
## 연결 확인하기
```

## IA-OVERVIEW — Provide an overview that orients the reader

**Strength:** SHOULD

At the beginning of a substantial document, tell the reader:

- what the document covers;
- what they can accomplish or understand after reading it;
- the most important context needed to decide whether the document is relevant.

Do not spend the opening on deep history when the reader first needs to know whether the page solves their problem.

## IA-PREDICT — Make the structure predictable

**Strength:** SHOULD

Readers should be able to infer where information will appear.

- keep equivalent sections at equivalent heading levels;
- use a repeated section order for repeated entities;
- explain before showing a complex example when the example otherwise forces readers to reverse-engineer the intent;
- keep the conceptual progression stable across a document set.

Terminology consistency is governed by `WR-TERMS` in `writing-principles.md`; do not duplicate that rule here.

## IA-SEQUENCE — Arrange information in dependency order

**Strength:** SHOULD

Present information in the order readers need it.

Common patterns include:

```text
concept -> usage -> example -> advanced detail
```

```text
symptom -> cause -> resolution -> verification
```

```text
goal -> prerequisite -> action -> result
```

Avoid using a concept substantially before defining it unless the target reader can safely be assumed to know it.

## IA-CONTEXT — Explain required background and behavior

**Strength:** SHOULD

Do not force readers to infer information required to use the feature correctly.

When relevant, explain:

- what a new concept means;
- why the reader needs it;
- conditions under which behavior changes;
- units, defaults, boundaries, and state-dependent behavior;
- where a value comes from and where it will be used later.

**Before**

> `session.duration`: 세션 지속 시간입니다.

**After**

> `session.duration`은 로그인 세션이 유지된 시간이며 밀리초 단위입니다. 세션이 시간 초과로 종료되면 마지막 활동 시점까지의 시간을 사용합니다.

Only include behavior you can support; do not add invented specificity.

## Structure review checklist

- [ ] Can the reader state the page's primary goal after reading the title and overview?
- [ ] Does every major section support that goal?
- [ ] Is the value/problem visible before low-level detail?
- [ ] Are headings predictable and consistent?
- [ ] Are prerequisites and concept dependencies introduced before use?
- [ ] Would splitting the page improve findability or maintenance?
- [ ] If split, is there a clear overview/cross-link path between the resulting pages?
