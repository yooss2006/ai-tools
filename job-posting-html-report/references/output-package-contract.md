# Output Package Contract

Create a static HTML package in the current workspace unless the user specifies another output path.

## Folder Naming

Use the report generation date:

```text
YYYY-MM-company-name/
```

Examples:

- `2026-06-toss/`
- `2026-06-당근/`

Normalize company names for filesystem safety. Use Korean, English, digits, and hyphens when possible. Avoid path separators and punctuation that can break shell or browser usage.

## Required Files

```text
YYYY-MM-company-name/
  index.html
  styles.css
  assets/
  data/
  sources/
```

`script.js` is optional. Include it only when it improves reading convenience.

## Data Preservation

Save non-sensitive source material for later review:

- Extracted posting text
- Structured posting data
- Company research notes
- Source list
- Evidence and judgment notes

Use Markdown or JSON when useful. Prefer clear filenames over clever naming.

## Sensitive Inputs

Do not save user-provided resume, cover letter, private career notes, or personal identifiers unless the user explicitly asks for storage. If used only for analysis, keep the final report focused on derived fit guidance.

## HTML Requirements

- `index.html` must be the main artifact.
- The report must be readable without JavaScript.
- CSS must be local.
- Do not hotlink fragile decorative assets.
- Source links may point to original web pages.
- Include accessed dates for researched sources.

## Final Chat Response

Return:

- Output folder path
- Very short overall judgment
- Major unavailable information
- Verification result

Do not paste the full report into chat.
