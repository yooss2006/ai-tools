# Linear Report Rules

Use these rules when styling the generated job posting HTML report. If a rule here is ambiguous, consult `references/linear.app/DESIGN.md`.

## Visual Direction

- Make the report feel like a dense product dashboard, not a landing page.
- Use a near-black page canvas and charcoal panels.
- Use one restrained lavender-blue accent family for highlights, active states, and primary badges.
- Use thin borders, subtle shadows, and low-radius panels.
- Keep layout compact and scannable.
- Use clear visual hierarchy for judgment, risk, evidence, and unknowns.

## Layout

- Use a persistent or top section navigation with short labels: `Overview`, `Role`, `Company`, `Fit`, `Strategy`, `Sources`.
- Keep body headings and analysis text in Korean.
- Make the first viewport show company name, position, overall judgment, recommendation, and top risks.
- Use panels for repeated data groups. Do not nest cards inside cards.
- Use tables or definition lists for structured posting information.
- Keep source and evidence links visible near the claims they support, then collect all links again in `Sources`.

## Components

- Judgment badge: `긍정`, `보통`, `주의`, `확인 불가`.
- Evidence badge: `확인`, `추정`, `확인 불가`, `추가 확인 필요`.
- Risk item: concise title, explanation, applicant meaning, source or reason.
- Source item: title, URL, publisher or owner, accessed date, evidence type.
- Metric panel: label, value, judgment badge, short rationale.

## Typography

- Prefer system UI fonts.
- Use compact headings and readable body sizes.
- Avoid oversized hero typography.
- Do not scale font size with viewport width.
- Use `letter-spacing: 0`. Do not use negative letter spacing even if the source design mentions measured negative tracking.

## Color Discipline

- Avoid decorative gradients, color blobs, and large atmospheric effects.
- Avoid many accent colors.
- Use red/amber/green only as small semantic signals when needed; keep lavender-blue as the primary accent.
- Maintain readable contrast for body text, badges, borders, and links.

## Interaction

- The report must remain readable without JavaScript.
- JavaScript may enhance table of contents highlighting, disclosure controls, or copy-link buttons.
- Do not rely on JS to reveal core content.

## Must Not

- Do not create a marketing hero.
- Do not hide missing or weak evidence.
- Do not use stock-like decorative imagery as the main signal.
- Do not let text overlap or overflow panels.
- Do not use unsupported claims as visual callouts.
