---
name: job-posting-html-report
description: Create a decision-ready Korean HTML report from a job posting URL. Use when the user wants to analyze a recruitment posting, research the company, evaluate role fit, produce application/interview strategy, and generate a Linear-style static HTML report package with sources and extracted data.
---

# Job Posting HTML Report

Use this skill to turn a job posting URL into a static HTML report package for application decisions and interview preparation. The final artifact is the HTML package, not the chat summary.

## Required Input

- Job posting URL

If the URL is missing, ask for it and stop.

## Optional Inputs

Use these when provided:

- Candidate seniority, current role, current tech stack
- Interest criteria: growth, stability, compensation, engineering culture, work-life balance, domain, remote work
- Conditions to avoid
- Resume or cover letter draft

Treat resume, cover letter, and personal career material as sensitive. Use them for analysis only. Do not save them into the output package unless the user explicitly asks you to store them.

## Read References

Before producing the report, read the relevant files:

- `references/research-and-evidence-rules.md` for extraction, research, source priority, and evidence labels
- `references/report-template.md` for report sections and required content
- `references/output-package-contract.md` for folder and file output rules
- `references/linear-report-rules.md` for report-specific Linear design rules
- `references/linear.app/DESIGN.md` as the canonical design source when visual rules are ambiguous
- `references/verification-checklist.md` before claiming the report is complete

## Workflow

1. Confirm the job posting URL.
2. Extract the posting body. If extraction fails, follow the fallback order in `research-and-evidence-rules.md`.
3. Confirm company name and position. Cross-check ambiguous names.
4. Research the company actively using official, financial, investment, news, hiring, and engineering sources.
5. Structure the evidence as confirmed information, inference, missing information, and items to verify before applying.
6. Analyze business model, growth, stability, role expectations, role risks, and applicant fit.
7. Generate application strategy: appeal points, motivation material, resume keywords, interview questions, risk questions, and join/no-join criteria.
8. Create a static HTML package under `YYYY-MM-company-name/`.
9. Verify evidence coverage, output files, Linear design compliance, and rendering when possible.
10. Return only a short completion summary with the output path, key judgment, major unknowns, and verification result.

## Output Requirements

Create a folder named from the report generation date and company name, for example:

```text
2026-06-company-name/
  index.html
  styles.css
  assets/
  data/
  sources/
  script.js  # optional
```

`index.html` must be readable without JavaScript. Use JavaScript only for reading convenience such as section highlighting or disclosure controls.

## Design Requirement

The generated HTML must follow the Linear design reference. Prefer a dense product-dashboard feel: near-black canvas, charcoal panels, thin borders, restrained lavender-blue accent, low radius, compact information hierarchy, and clear badges for judgment, risk, evidence, and unknowns.

Do not create a marketing landing page. Do not hide missing information. Do not make unsupported claims.

## Final Response

Keep the final chat response short:

- Output folder path
- Very short overall judgment
- Major information that remained unavailable
- Design/rendering verification result
