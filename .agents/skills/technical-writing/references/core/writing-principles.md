# Writing Principles

This file is the canonical source for language-independent sentence-level technical-writing rules.

## WR-SUBJECT — Make the actor and action clear

**Strength:** SHOULD

Write so the reader can tell who or what performs an action.

When the reader/developer performs the task, instruction-oriented phrasing is often clearer than making a tool the grammatical actor.

**Before**

> 설정이 배포 전에 완료되어야 합니다.

**After**

> 배포하기 전에 설정을 완료하세요.

A system or tool can still be the subject when the purpose is to explain its behavior.

## WR-ACTIVE — Prefer active constructions when they clarify responsibility

**Strength:** SHOULD

Use active voice when passive wording hides the responsible actor or makes instructions harder to follow. Do not mechanically rewrite every passive sentence if the actor is irrelevant or obvious.

## WR-ONE-THOUGHT — Keep one main thought per sentence

**Strength:** SHOULD

Split a sentence when it carries independent actions, conditions, or conclusions that readers must track separately.

**Before**

> 설정 파일을 변경한 후 저장하고 변경 사항을 확인한 다음 필요하면 서버를 다시 시작해야 합니다.

**After**

> 설정 파일을 변경한 후 저장하세요. 변경 사항을 확인하고, 필요하면 서버를 다시 시작하세요.

## WR-META — Minimize metadiscourse

**Strength:** SHOULD

Remove phrases that talk about the document instead of communicating the technical information, unless they genuinely help navigation.

Common low-value forms:

- “앞서 설명했듯이”
- “이제 알아보겠습니다”
- “아시다시피”
- “결론적으로”

Cross-references that help the reader locate a dependency are useful and are not low-value metadiscourse.

## WR-VERB — Prefer direct verbs over abstract action nouns

**Strength:** SHOULD

Use direct verbs when nominalized phrasing hides the actual operation.

**Before**

> 코드 최적화 진행 후 배포 수행이 필요합니다.

**After**

> 코드를 최적화한 후 배포하세요.

Language-specific details for Korean are in `../language/ko.md`.

## WR-CONCRETE — Use precise, supported language

**Strength:** MUST for claims where precision affects correct use; otherwise SHOULD.

Prefer concrete conditions, locations, units, actors, and effects when they are known.

Write enough information that the reader does not have to guess:

- who performs the action;
- what is changed;
- where it is changed;
- under what condition it applies;
- what result should be observed.

Do **not** replace legitimate uncertainty with invented certainty. If the evidence is uncertain, state the uncertainty or move it to an open-question section.

**Before**

> 에러가 발생하면 로그를 확인하세요.

**After**

> 결제 요청이 실패하면 API 서버의 결제 오류 로그를 확인하세요.

Add an exact file path only when it is known and stable.

## WR-MEASURE — Give measurable criteria when measurement matters

**Strength:** SHOULD

Replace terms such as “많다”, “크다”, “빠르다”, or “느리다” with a measurable threshold when the threshold is actually known and relevant.

Never fabricate a threshold for stylistic neatness.

## WR-REFER — Explain forward and backward references

**Strength:** SHOULD

When a value or concept is introduced for later use, say what it will be used for. When it reappears after a long gap, remind the reader where it came from or link to the source section.

## WR-TERMS — Use one term for one concept

**Strength:** MUST unless a terminology change is itself being explained.

- follow official product/library names and capitalization;
- avoid switching between synonyms for the same technical concept without a reason;
- preserve project-specific domain terms from the project's style guide or glossary;
- if terminology is changing, state the old and new term explicitly.

**Before**

> 파일을 첨부하려면 `파일 선택` 버튼을 클릭하세요. 파일을 추가한 뒤 저장하면 첨부가 완료됩니다. 필요한 경우 파일을 다시 넣을 수 있습니다.

**After**

> 파일을 첨부하려면 `파일 선택` 버튼을 클릭하세요. 파일을 첨부한 뒤 저장하면 첨부가 완료됩니다. 필요한 경우 파일을 다시 첨부할 수 있습니다.

The revision unifies terminology without changing the underlying action from attachment to a different operation such as upload.

## WR-ABBREV — Expand unfamiliar abbreviations on first use

**Strength:** SHOULD

Introduce an abbreviation with its full name on first meaningful use unless the abbreviation is universally known to the target audience or the project style guide says otherwise.

Example:

> 서버 사이드 렌더링(Server-Side Rendering, SSR)

After that, use the abbreviation consistently.

## Sentence review checklist

- [ ] Is the actor/action clear where responsibility matters?
- [ ] Does each sentence carry one main thought?
- [ ] Can low-value metadiscourse be removed?
- [ ] Are direct verbs available instead of abstract action nouns?
- [ ] Are conditions, units, locations, and effects concrete when known?
- [ ] Is uncertainty represented honestly?
- [ ] Is one term used consistently for one concept?
- [ ] Are abbreviations and official names introduced consistently?
