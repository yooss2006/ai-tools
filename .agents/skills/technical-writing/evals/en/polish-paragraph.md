# Eval: Polish one English technical paragraph

## Fixture

`../fixtures/en/polish-paragraph/input.md`

## User request

> Polish only the supplied paragraph for clarity. Preserve every technical fact, condition, number, and requirement level. Do not fact-check it unless you need to flag a suspicious claim.

## Pass criteria

- Do not expand into document profile/type analysis.
- Preserve `45 seconds`, `CACHE_TTL=45`, production scope, and the mandatory restart requirement.
- Do not silently change or delete the React 19 / `useEffect` claim.
- If the claim is treated as suspicious, flag it separately rather than rewriting the fact during prose polishing.
- Return a polished paragraph, not a full-document rewrite.
