# Eval: Write a README from a minimal repository

## Fixture repository

`../fixtures/en/write-readme/`

Relevant files:

- `package.json`
- `src/index.ts`
- `tsconfig.json`

## User request

> Write a concise README for this repository. Use the actual scripts and CLI interface in the fixture; do not invent publishing or installation details that are not present.

## Pass criteria

- Detect the README profile.
- Use the actual project name/purpose from the repository rather than inventing a different tool.
- Include the real scripts `npm run build` and `npm test` when build/test instructions are shown.
- Reflect the actual CLI shape: `json-csv <input> --output <path>` (or `-o <path>`).
- Do not claim the package is published to npm or tell users to install it globally from npm, because the fixture does not establish publication.
- Do not load or apply Korean-specific language rules.
- Keep the README focused on what the tool does, setup/build if useful, and basic usage supported by the fixture.
