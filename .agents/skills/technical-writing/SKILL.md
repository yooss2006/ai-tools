---
name: technical-writing
description: End-to-end technical documentation writing, review, restructuring, and polishing. Use for tutorials, how-to and troubleshooting guides, references, explanations, README, ADR, RFC/technical proposals, architecture docs, incident/postmortem docs, migration guides, developer onboarding docs, and multi-document information architecture. Do not use for general email/chat rewriting, marketing copy, essays, pure code refactoring/debugging, simple translation, or research that is not being turned into technical documentation.
---

# Technical Writing Skill

Create and improve technical documentation so readers can learn, solve a problem, look up exact information, or understand a system with minimal unnecessary cognitive load.

This file is the **workflow orchestrator**. Do not preload every reference. Load only the references needed for the current stage.

## Instruction precedence

When guidance conflicts, use this order:

1. The user's explicit requirements.
2. Project or organization style guides and required templates.
3. The existing document's consistent style and terminology.
4. `MUST` rules in this skill.
5. `SHOULD` rules in this skill.
6. `HEURISTIC` rules in this skill.

Do not follow a higher-priority style rule when doing so would knowingly introduce a factual error or make the meaning materially ambiguous. Surface the conflict instead.

## Semantic preservation guardrail

Apply this guardrail to **every** review, rewrite, revision, and sentence/paragraph polish task, including tasks that do not run the full workflow.

Unless the user explicitly asks to change or verify the underlying facts, preserve:

- technical behavior and system semantics;
- conditions, exceptions, thresholds, quantities, units, and versions;
- negation and causal relationships;
- actor/responsibility and scope;
- requirement level and modality, such as MUST/SHOULD/MAY or `반드시`/`권장`/`가능`;
- project terminology whose meaning is already established.

Do not replace a technical action with a superficially similar term when the replacement could imply different behavior, such as attach vs upload, local save vs server persistence, or cache invalidation vs cache deletion.

If a claim looks suspicious during a **polish-only or review-only** task, do not silently correct it. Preserve its intended meaning in the edited wording and surface it as a fact that may need verification. Load `references/extensions/verification.md` only when the user asks for verification/correction or when the broader task requires factual validation.

## Scope first

Match the workflow to the requested scope. Do not run the full workflow for a small task.

- **Full document creation or major rewrite**: run the full workflow below.
- **Structure/outline only**: stop after information architecture and the requested structure output.
- **Review / inspection**: identify issues, show the supporting evidence or location when available, and explain the correction direction. Do **not** produce a full revised document unless the user explicitly asks to revise, rewrite, fix, or directly edit it.
- **Sentence/paragraph polish**: apply the semantic preservation guardrail and load only the writing and language references needed for the text.
- **Document-set cleanup**: analyze the collection as a documentation system, not as isolated files.
- **Template request**: load the relevant document type/profile and return a reusable template without running unnecessary drafting steps.

## Full workflow

### 1. Understand the assignment

Extract what is already known:

- document goal;
- target reader and assumed knowledge;
- project context;
- constraints such as format, length, tooling, version, or publication location;
- whether the input is a new document, an existing draft, or a collection of documents.

Ask only for **missing information that materially changes the result**. Do not ask again for information already provided.

### 2. Detect a practical document profile when applicable

For established engineering document forms, detect the profile automatically when the intent is clear.

Core profiles:

- README
- ADR
- RFC / technical proposal
- Architecture document

Additional profiles:

- Incident / postmortem
- Migration guide
- Developer onboarding

If choosing between two profiles would materially change the document and the intent is genuinely ambiguous, ask one focused question. Otherwise choose the best-fitting profile and continue.

A practical profile controls the document's **outer form and expected sections**. A document type controls **how the information is communicated**.

### 3. Select a primary document type and optional secondary type

Load `references/core/document-types.md` when type selection is needed.

Choose one primary type:

- Learning
- Problem solving
- Reference
- Explanation

Add a secondary type only when it solves a real reader need. Do not blend types merely because multiple types are available.

### 4. Design the information architecture

Load `references/core/information-architecture.md` for new documents, major rewrites, or structural review.

For an existing draft:

- preserve the current structure when it already serves the reader;
- reorganize, merge, split, or remove sections when the structure materially harms comprehension or findability.

For multiple documents, also load `references/extensions/documentation-system.md`.

### 5. Use the structure approval gate only for new material decisions

The gate exists to protect user intent, not to re-confirm work the user already authorized.

**Proceed without another approval** when the user's current request explicitly authorizes the relevant class of change, such as:

- restructure or substantially rewrite the document;
- split one document into multiple documents;
- merge documents;
- convert the document to a named practical profile;
- reorganize a document set.

Ask for approval only when **you must introduce a material decision that is not already authorized or recoverable from the request/context**, for example:

- changing the document's purpose or target audience;
- changing a major conclusion, recommendation, or policy meaning;
- choosing between materially different document profiles when that choice changes the outcome;
- splitting/merging files when the user did not authorize file-boundary changes;
- expanding the task into a broader scope than requested.

When approval is needed, show only:

- document goal;
- target reader;
- practical profile, if any;
- primary and secondary document types;
- the new decision that requires approval;
- major structural changes;
- proposed table of contents.

Do not expose a long internal outline unless the user asks for it. Do not ask for approval solely because a change is large; ask only because it requires a **new user decision**.

### 6. Draft or revise

Preserve the input format when practical:

- Markdown -> Markdown
- HTML -> HTML
- AsciiDoc -> AsciiDoc
- existing project template -> same template

For a new document with no required format, default to Markdown.

Preserve stable metadata such as front matter, IDs, slugs, anchors, and links unless the content change would break them. Repair broken references caused by an approved structural change.

Use tables automatically when structured comparison or lookup benefits from them, for example:

- parameters and options;
- alternatives and tradeoffs;
- environment differences;
- error codes;
- configuration values.

Use Mermaid when a diagram materially reduces cognitive load, especially for:

- architecture relationships;
- data flow;
- state transitions;
- request/response sequences;
- multi-step processes.

Do not add diagrams or tables decoratively.

### 7. Verify selectively

Load `references/extensions/verification.md` only when verification triggers are present.

Verification is expected for claims such as:

- version-specific behavior;
- API contracts;
- configuration or command behavior;
- library/framework support;
- implementation-specific behavior;
- code examples that must actually run.

Prefer official sources. Inspect the codebase only when the requested documentation depends on the actual implementation or existing project conventions.

Do not turn technical-writing work into an unsolicited code refactor. Modify code examples only when required for correctness, consistency with the explanation, or clarity of the teaching goal.

### 8. Refine the prose

Load:

- `references/core/writing-principles.md`; and
- the relevant language file, such as `references/language/ko.md`.

Preserve the existing voice and level of formality unless it harms clarity or consistency.

### 9. Final review

Check for:

- goal and reader alignment;
- missing overview or prerequisites where needed;
- duplicated information;
- inconsistent terminology;
- logical ordering;
- broken cross-references;
- code/explanation mismatches;
- unsupported or unresolved factual claims;
- unnecessary depth or mixed goals;
- metadata damage caused by editing.

Automatically fix low-risk issues such as terminology consistency, small redundancies, heading consistency, and minor overview/body mismatches.

Do not silently decide an unresolved product, architecture, or policy question that would change the document's meaning.

## Uncertainty handling

Never invent missing technical facts to make a document look complete.

When a required fact cannot be verified or inferred safely:

1. avoid stating it as fact in the main text;
2. complete the parts that are supported;
3. add an `확인 필요 사항` / `Open questions` section when appropriate.

## Multi-document behavior

When the input contains multiple documents, treat them as one documentation system.

Analyze:

- semantic duplication, not just identical sentences;
- which document should be the source of truth;
- contradictions;
- whether to merge, summarize-and-link, or intentionally keep repeated context;
- missing cross-links;
- document boundaries and hierarchy.

Use `references/extensions/documentation-system.md` as the canonical source for these rules.

## Reference loading map

Load references progressively.

| Task stage | Load |
|---|---|
| Type selection | `references/core/document-types.md` |
| Practical profile | matching file under `references/profiles/` |
| Structure design | `references/core/information-architecture.md` |
| Multiple documents | `references/extensions/documentation-system.md` |
| Fact/code verification | `references/extensions/verification.md` |
| Draft/polish | `references/core/writing-principles.md` + relevant `references/language/*` |
| Need a concrete pattern | one matching file under `references/examples/` |
| Skill maintenance/provenance | `references/meta/provenance.md` |

Do not load all profiles or all examples by default.

## Default output contract

For a completed writing or revision task, return:

1. the finished document;
2. a short `주요 변경 사항` / `Major changes` summary;
3. `확인 필요 사항` / `Open questions` only when unresolved information remains.

For a **review / inspection** request, return by default:

1. major issues;
2. supporting evidence, location, or rationale when available;
3. correction direction.

Add revised text or a full revised document only when the user explicitly asks for rewriting, fixing, or direct editing. A request such as `점검해줘`, `리뷰해줘`, or `문제만 찾아줘` does not by itself authorize a full rewrite.

When the user explicitly asks for a file, create the file. Otherwise the finished content may be returned directly in chat.
