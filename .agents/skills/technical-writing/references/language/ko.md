# Korean Technical Writing

Apply this file only to Korean technical documents. General sentence rules remain in `../core/writing-principles.md`.

## KO-TONE — Preserve a consistent speech level

**Strength:** SHOULD

Preserve the existing document's consistent tone (`합니다`, `해요`, command style, etc.) unless the user or organization style guide requests a change.

Do not change a consistent `합니다` document into `해요` merely because one form feels friendlier.

## KO-NOMINAL — Reduce unnecessary Sino-Korean nominalization

**Strength:** SHOULD

Korean technical prose is often clearer when the action is expressed as a verb instead of layered nouns such as `수행`, `진행`, `처리`, or `실시`.

**Before**

> 설정 변경을 수행한 후 적용을 진행합니다.

**After**

> 설정을 바꾼 뒤 적용합니다.

Do not remove a noun when it is an established domain term or when the noun is the actual subject being discussed.

## KO-TRANSLATION — Rewrite translationese into natural Korean

**Strength:** SHOULD

Prefer natural Korean action structure over literal English nominal phrases.

**Before**

> API 키를 이용한 사용자 인증 처리가 완료된 후 데이터베이스 접속 설정 진행이 가능합니다.

**After**

> API 키로 사용자를 인증한 후 데이터베이스 접속을 설정할 수 있습니다.

## KO-PARTICLE — Prefer compact, direct particles when meaning is unchanged

**Strength:** HEURISTIC

Avoid needlessly formal or translated forms such as `~을 통해` when a simpler particle or verb communicates the same relation.

Example:

> 이 API를 통해 데이터를 가져옵니다.

can often become:

> 이 API로 데이터를 가져옵니다.

Keep the longer form when it expresses a real path, medium, or causal relationship that the shorter form would blur.

## KO-TECH-TERM — Follow official and industry-recognizable technical naming

**Strength:** SHOULD

- prefer the official spelling/capitalization for products, languages, libraries, and APIs;
- when Korean transliteration has a strongly established industry form, reader familiarity may outweigh a mechanically strict loanword spelling;
- follow the project's terminology guide when one exists.

Do not use search popularity as an automatic rule. Treat prevalence as supporting evidence, not as the sole source of truth.

## KO-ABBREV — Introduce English technical terms deliberately

**Strength:** SHOULD

When a Korean reader benefits from both forms, introduce the Korean concept with the original English term or abbreviation once, then keep one stable form.

Example:

> 클라이언트 사이드 렌더링(Client-Side Rendering, CSR)

Do not repeat the full expansion in every section.

## Korean review checklist

- [ ] Is the speech level consistent?
- [ ] Can `수행/진행/처리/실시` be replaced with a direct verb?
- [ ] Does any sentence read like a literal English translation?
- [ ] Are official technical names and project terminology preserved?
- [ ] Are Korean and English forms introduced consistently instead of alternated randomly?
