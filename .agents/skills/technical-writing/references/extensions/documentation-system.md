# Documentation System

Use this reference when reviewing or reorganizing multiple documents. It extends the source guide's multi-page structure and cross-link ideas with rules for semantic duplication, sources of truth, and conflicts.

## DS-GOAL — Treat the document set as one information system

**Strength:** MUST for multi-document cleanup.

Do not optimize each file independently if that creates duplication, contradictory guidance, or navigation gaps across the set.

Map each document to:

- its reader goal;
- its practical profile/type;
- the knowledge it owns;
- the knowledge it only summarizes or links to.

## DS-DUP — Detect semantic duplication

**Strength:** SHOULD

Two passages are duplicate candidates when they independently maintain the same fact, rule, or procedure, even if the wording differs.

Do not label all topic overlap as harmful duplication. A README may summarize a system whose full explanation lives in architecture documentation.

## DS-SOT — Prefer one source of truth for maintainable facts

**Strength:** SHOULD

When multiple documents maintain the same changing fact, designate one canonical location when practical.

Other documents may:

- summarize the fact briefly;
- link to the canonical document;
- repeat only the context needed to make the local document understandable.

The goal is not zero repetition. The goal is to avoid independently maintained copies that can drift.

## DS-ACTION — Choose merge, summary+link, or intentional repetition

**Strength:** SHOULD

For each duplicate candidate, choose deliberately:

### Merge/remove

Use when the passages serve the same reader goal and one location is sufficient.

### Summary + link

Use when the same knowledge is needed in different document contexts but one location should own the full detail.

### Keep intentional repetition

Use when the local context is essential for comprehension, the repeated content is short/stable, and forcing a link would materially harm the task flow.

## DS-CONFLICT — Resolve contradictions by evidence, not convenience

**Strength:** MUST

When documents disagree:

1. determine whether both may be valid in different contexts/versions;
2. identify evidence relevant to the document's purpose;
3. resolve automatically only when the evidence is strong enough;
4. otherwise record the contradiction under `확인 필요 사항` / `Open questions`.

Possible evidence includes:

- active runtime configuration or code for a document describing current implementation;
- an accepted/current ADR or policy for a document describing intended architectural policy;
- versioned official documentation for version-specific behavior;
- dates and status metadata when comparing superseded decisions.

Do not apply a universal rule such as “code always wins.” Code may represent current behavior while an accepted proposal represents intended future behavior.

## DS-SPLIT — Split documents when reader goals diverge

**Strength:** SHOULD

Propose a split when one file has multiple independent goals, grows into deep heading branches, or forces different audiences through irrelevant sections.

Do not split silently during a major rewrite. Use the structure approval gate.

## DS-LINK — Design cross-links around reader transitions

**Strength:** SHOULD

Link when a reader is likely to need the adjacent detail next.

Good transitions include:

- overview -> how-to;
- tutorial -> reference;
- README -> architecture;
- error catalog -> troubleshooting;
- ADR -> detailed design/RFC;
- onboarding -> contribution workflow.

Avoid link dumps that do not explain why the target is relevant.

## DS-META — Preserve metadata and navigation integrity

**Strength:** MUST when editing existing documentation systems.

Preserve front matter, slugs, IDs, anchors, and relative links unless an approved structure change requires updates.

After renaming/splitting/moving:

- repair relative links;
- check anchors/headings;
- update navigation metadata when required;
- avoid unnecessary tag/sidebar churn.

## Multi-document review output

When useful, summarize findings as:

| Knowledge area | Current owners | Recommended source of truth | Action |
|---|---|---|---|
| ... | ... | ... | merge / summary+link / keep / verify conflict |
