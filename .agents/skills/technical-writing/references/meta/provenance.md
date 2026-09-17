# Provenance and Maintenance Notes

This file is for maintainers of the Skill. It is not intended to be loaded for ordinary technical-writing tasks.

## Primary source-derived material

The core writing model was synthesized from:

- **Technical Writing Guide** — https://technical-writing.dev/
- Copyright © 2024 Viva Republica, Inc.
- The source states that its contents are licensed under **CC BY-NC-SA 4.0**.

The source document supplied for this Skill contained 22 pages covering:

- overview and tutorials;
- four reader-goal document types;
- information architecture;
- sentence-level technical writing;
- Korean technical-writing style.

### Source-derived areas in this Skill

- `references/core/document-types.md`
- `references/core/information-architecture.md`
- `references/core/writing-principles.md`
- `references/language/ko.md`
- the basic concepts of page splitting and cross-linking used by `documentation-system.md`
- the learning/problem-solving/reference/explanation examples as newly written examples demonstrating the source-derived principles

The Skill intentionally removes the source site's teaching repetition, GPT setup tutorial, exercises, and repeated prompt/checklist restatements. The rules are normalized into canonical locations so a rule is not maintained in multiple reference files.

## Skill extensions

The following are additions created for this Skill rather than direct sections of the Technical Writing Guide:

- progressive reference loading;
- practical engineering-document profiles;
- MUST / SHOULD / HEURISTIC strength labels;
- structure approval gate;
- selective technical verification;
- codebase-inspection policy;
- semantic duplicate detection across documents;
- source-of-truth selection;
- cross-document conflict handling;
- default output contract;
- behavioral eval scenarios.

## External conventions used for practical profiles

These sources informed the profile designs. They are not copied as mandatory templates.

### README

- GitHub Docs — About the repository README file
  - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

### ADR

- ADR GitHub organization — ADR Templates / Nygard ADR summary
  - https://adr.github.io/adr-templates/
- Nygard-style ADR uses title, status, context, decision, and consequences as the minimal form; considered options may be added when tradeoff history matters.

### RFC / technical proposal

- Rust RFC template
  - https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- Used as evidence for common proposal sections such as summary, motivation, detailed design, drawbacks, alternatives, and unresolved questions.

### Architecture

- arc42 documentation/template
  - https://arc42.org/overview/
  - https://docs.arc42.org/
- Used as evidence for common architecture concerns such as goals, constraints, context, building blocks, runtime/deployment views, decisions, quality requirements, risks, and glossary.

### Incident / postmortem

- Google SRE Workbook — Postmortem Culture
  - https://sre.google/workbook/postmortem-culture/
- Used as evidence for standardized, customizable postmortem templates and blameless learning orientation.

### Developer onboarding

- GitHub Docs — About repository READMEs / contributing guidance
  - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
  - https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors

## Attribution policy

Ordinary Skill outputs should not automatically mention the source guide. Attribution belongs in the public repository documentation/notice unless the user explicitly requests provenance.

## Maintenance rule

When adding or changing a rule:

1. pick exactly one canonical reference file;
2. assign/reuse a stable rule ID when the rule is testable;
3. make other files refer to the canonical rule rather than restating it;
4. add or update an eval when behavior changes;
5. record whether the rule is source-derived or a Skill extension here.
