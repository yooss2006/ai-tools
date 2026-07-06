# AI Tools
에이전트용 개인 도구를 모아두는 저장소입니다.

직접 만든 스킬, 에이전트 설정, 프롬프트 워크플로, hook 등을 한곳에 정리합니다. 반복해서 쓰는 작업 방식을 파일로 남겨 두고, 필요할 때 바로 다시 사용할 수 있게 만드는 것이 목적입니다.

## 구성
### 스킬
- `technical-writing/`: 기술 문서 작성, 리뷰, 구조화, 한국어 문장 개선을 돕는 스킬입니다.
- `peer-clarify/`: 모호한 아이디어나 요청을 짧은 동료식 피드백으로 요구사항에 가깝게 정리하는 스킬입니다.
- `multi-ask/`: `$multi-ask`로 명시적으로 호출하면 ChatGPT web, Gemini web, Claude web에 같은 질문을 보내고 답변을 비교합니다.
- `web-gpt-research/`: `$web-gpt-research`로 명시적으로 호출하면 승인된 프롬프트를 ChatGPT/Web GPT에 보내 리서치를 진행합니다.
- `job-posting-html-report/`: 채용 공고 URL을 기반으로 회사 조사, 역할 적합도, 지원 전략, 출처 자료를 포함한 Linear 스타일 정적 HTML 리포트 패키지를 생성합니다.
- `safe-dependency-fix/`: OSV Scanner와 생태계별 audit 도구로 의존성 취약점을 dry-run으로 점검하고, 명시적 승인 후 최소 변경으로 수정합니다.

### 서브에이전트
- `agents/plan-critic.toml`: 계획서, PED, 아이디어를 검수하고 OKAY/REJECT로 실행 가능 여부를 판정하는 read-only 서브에이전트입니다.

### hooks
- `codex-macos-alert-hook` : 코덱스 작업 완료시 alert 창이 뜨는 hook입니다.

## 목적
새로운 스킬, 서브에이전트, hook, 프롬프트 패턴을 실험하고 검증한 뒤, 다시 쓸 만한 형태로 정리해 두는 공간입니다.
