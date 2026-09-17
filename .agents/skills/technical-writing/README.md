# Technical Writing Skill

A technical-writing Skill for creating, reviewing, restructuring, and polishing engineering documentation.

It turns a broad technical-writing guide into a progressive workflow with canonical references, practical document profiles, and behavioral evals.

## What it handles

- tutorials and getting-started guides;
- how-to and troubleshooting docs;
- API/configuration/reference docs;
- concept and domain explanations;
- README;
- ADR;
- RFC / technical proposals;
- architecture docs;
- incident/postmortem docs;
- migration guides;
- developer onboarding;
- multi-document deduplication and information architecture.

It is not intended for generic email/chat rewriting, marketing copy, essays, pure code refactoring/debugging, simple translation, or research that is not being turned into technical documentation.

## Design

The Skill is intentionally split into a small orchestrator and lazily loaded references.

```text
technical-writing-skill/
├── SKILL.md
├── references/
│   ├── core/
│   ├── language/
│   ├── extensions/
│   ├── profiles/
│   ├── examples/
│   └── meta/
└── evals/
    ├── ko/
    ├── en/
    └── fixtures/
```

### Canonical-source rule

A writing rule should have one canonical home. Other files should refer to the rule instead of copying its full text.

### Progressive loading

The Skill loads references by stage:

1. document type / practical profile;
2. information architecture;
3. drafting and verification;
4. sentence/language refinement;
5. examples only when a concrete pattern is needed.

This keeps small tasks small while still supporting full document creation.

## Typical workflow

```text
request
  -> identify missing critical context
  -> detect practical profile
  -> choose primary + optional secondary document type
  -> design structure
  -> ask only for material decisions not already authorized
  -> draft/revise
  -> verify selectively
  -> polish
  -> final review
  -> finished document + major changes + open questions if any
```

## Behavioral evals

Evals use concrete fixture documents/repositories under `evals/fixtures/` rather than placeholders. Each eval defines a user request plus observable pass/fail criteria so routing, scope control, semantic preservation, and documentation-system behavior can be compared across Skill revisions without requiring one exact wording as the golden answer.

## Source and attribution

The core technical-writing principles are a condensed and reorganized adaptation of the **Technical Writing Guide** published at https://technical-writing.dev/ by Viva Republica, Inc.

The supplied source states:

- Copyright © 2024 Viva Republica, Inc.
- CC BY-NC-SA 4.0

See [`NOTICE.md`](NOTICE.md) and [`references/meta/provenance.md`](references/meta/provenance.md) for source and extension boundaries.

This repository is an independent Skill adaptation and is not presented as an official Toss/Viva Republica product.

## License

A repository-level licensing decision for the combined Skill has intentionally not been finalized in this draft. Review the original source license and the intended distribution model before publishing the repository.
