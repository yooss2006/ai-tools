# Verification

Use this reference only when the document contains claims whose correctness depends on external facts, versions, APIs, configuration, or the actual codebase.

## VER-SELECTIVE — Verify selectively

**Strength:** MUST

Technical writing is not automatically a research project. Verify when an error would materially mislead the reader or when a claim is plausibly stale/incorrect.

Common triggers:

- exact library/framework/version behavior;
- API signature, parameter, return, or support claims;
- command/configuration semantics;
- operating-system differences;
- security-sensitive instructions;
- code claimed to be executable;
- implementation documentation that may have drifted from the codebase.

## VER-SOURCE — Prefer authoritative sources

**Strength:** SHOULD

Preferred order depends on the claim, but normally:

1. project/technology official documentation, specification, or source;
2. the actual project repository/configuration for implementation-specific claims;
3. primary release notes or changelogs;
4. reputable secondary sources when primary sources are unavailable.

Do not cite a secondary blog as stronger evidence than an available official source for an API contract.

## VER-REPO — Inspect the codebase only when it matters

**Strength:** SHOULD

Inspect relevant code/configuration when the requested document describes the actual project implementation, terminology, file paths, architecture, commands, or behavior.

Do not scan the entire repository when the supplied context already answers the documentation task or when the document is intentionally generic.

## VER-CODE — Modify examples only for documentation correctness

**Strength:** SHOULD

Change example code when:

- it contradicts the explanation;
- it is incomplete in a tutorial that promises executable steps;
- it uses an API incorrectly;
- unnecessary complexity obscures the concept being taught.

Do not modernize syntax, change libraries, or refactor production code merely because a newer pattern exists.

## VER-CITATION — Add sources to the finished document only when useful to the reader

**Strength:** SHOULD

External verification does not require turning every sentence into a citation-heavy document.

Include source links when they add reader value, such as:

- version-specific behavior;
- standards/specifications;
- official API constraints;
- important compatibility/support boundaries;
- an existing `References` section.

Otherwise verification can remain an internal quality-control step.

## VER-UNKNOWN — Do not fill evidence gaps with guesses

**Strength:** MUST

If a required fact remains unresolved:

- do not state a guessed value as fact;
- phrase uncertainty accurately if the uncertainty itself matters;
- move missing decisions/facts to `확인 필요 사항` / `Open questions` when appropriate.
