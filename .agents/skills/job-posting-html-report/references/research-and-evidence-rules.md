# Research And Evidence Rules

Use these rules to extract the posting, research the company, and prevent unsupported certainty.

## Posting Extraction

Extract:

- 회사명
- 포지션명
- 기술스택
- 주요 업무
- 자격 요건
- 우대 사항
- 채용 절차
- 혜택/복지
- 근무 형태
- 근무지
- 고용 형태
- 경력 요건
- 마감일
- 원문 URL

If extraction fails, retry in this order:

1. Direct page body text
2. HTML metadata
3. Structured data in the page
4. Search engine result for the same posting
5. Company hiring page for the same position

If all attempts fail, continue with a failure section in the HTML report and record the reason.

## Company And Position Confirmation

Prefer the company name and position from the posting. If ambiguous, cross-check:

- Posting domain
- Hiring platform company profile
- Official homepage
- Business registry, disclosure, or news material

Warn in the report when there is a possible same-name company mismatch.

## Active Company Research

Always research actively. This skill is for decision-ready reports, not quick summaries.
For recent news, funding, financial status, leadership, hiring status, and other time-sensitive facts, verify with current sources before writing the report.

Check:

- Official homepage
- Official company profile
- Official hiring page
- Main products or services
- Main customers
- Business model
- Revenue sources
- Market or industry
- Recent news
- Funding history
- Financial statements or revenue/profit trend when available
- Engineering blog or hiring/culture blog
- Talent philosophy or core values
- Founder/executive interviews
- Public organization-culture material

## Source Priority

Use this priority:

1. Official company material
2. Disclosure, financial, investment material
3. Credible news
4. Hiring blog, engineering blog
5. Reputation sources such as Jobplanet, Blind, communities

Use reputation sources only as signals. Do not treat them as confirmed facts.

## Evidence Labels

Label information as:

- `확인`: directly supported by a source
- `추정`: inferred from context
- `확인 불가`: not found or not supported
- `추가 확인 필요`: important enough to ask before applying, interviewing, or accepting

Every major judgment should include a source or an explicit reason.

## Judgment Grades

Use one of:

- `긍정`
- `보통`
- `주의`
- `확인 불가`

For each judgment, include:

- What was found
- Why it matters
- What it means for the applicant
- Source or uncertainty note

## Risk Signals

Call out risks such as:

- Excessively broad role scope
- Unrealistic required and preferred qualifications
- Tech stack not matching actual work
- Unclear hiring process
- Missing work mode, location, compensation, or employment details
- Weak connection between company business and the role
- Financial, investment, or market uncertainty
