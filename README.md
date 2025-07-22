# 개인 비서 에이전트 시스템

Google ADK Python을 사용한 심플하고 확장 가능한 개인 비서 AI 시스템입니다.

## 특징

- 🎯 **심플한 구조**: ADK의 기본 패턴을 따라 복잡하지 않게 설계
- 🔧 **모듈화**: 각 전문 에이전트가 독립적으로 동작
- 📈 **확장성**: 새로운 에이전트나 MCP 연동 쉽게 추가 가능
- 🛡️ **프라이버시**: 모든 개인 데이터는 로컬에 저장
- 🤖 **멀티 에이전트**: 작업별로 최적화된 전문 에이전트 활용

## 시스템 구조

```
personal_assistant/
├── agents/                    # 에이전트 모듈
│   ├── main_agent.py         # 메인 코디네이터 (root_agent)
│   ├── portfolio_agent.py    # 주식 포트폴리오 분석
│   └── diary_agent.py        # 개인 일기 정리
├── tools/                    # 실제 필요한 툴들만
│   ├── web_tools.py         # 웹 검색, URL 페칭
│   ├── stock_tools.py       # 주식 API 호출
│   └── diary_tools.py       # 파일 시스템 접근
├── config/                   # 설정 관리
│   ├── .env.example         # 환경 설정 예시
│   └── agent_config.py      # 설정 관리 클래스
└── data/                    # 로컬 데이터 (자동 생성)
    ├── portfolio/           # 포트폴리오 데이터
    └── diaries/            # 일기 데이터
```

## 에이전트 구성

### 1. 메인 개인 비서 (main_agent.py)
- 사용자 요청을 분석하여 적절한 전문 에이전트에게 위임
- 일반적인 질문은 직접 처리
- 복합적인 요청은 여러 에이전트 조합 활용

### 2. 주식 포트폴리오 분석 에이전트 (portfolio_agent.py)  
- 보유 주식 현황 및 수익률 분석
- 실시간 주가 정보 조회
- 시장 동향 및 관련 뉴스 검색
- 투자 정보 제공 (조언 아님)

### 3. 개인 일기 정리 에이전트 (diary_agent.py)
- 일기 작성 도우미 및 구조화
- 감정 상태 분석 및 건설적 피드백  
- 과거 일기 검색 및 회고
- 개인 성장 인사이트 도출

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install google-adk
```

### 2. 환경 설정
```bash
# .env 파일 생성 (config/.env.example 참고)
cp config/.env.example config/.env

# Google API 키 설정
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. 실행
```bash
# 개발 모드 (현재 디렉터리에서)
adk web

# 또는 특정 경로 지정
adk web /path/to/personal_assistant
```

### 4. 웹 인터페이스 접속
```
http://localhost:8000
```

## 사용 예시

### 주식 포트폴리오 분석
```
사용자: "내 주식 포트폴리오 현황 좀 확인해줘"
비서: "포트폴리오 분석 전문가에게 현재 주식 현황을 확인해보겠습니다."
→ portfolio_analyzer 에이전트가 처리
```

### 일기 작성 및 분석
```
사용자: "오늘 일기 쓰는데 도움이 필요해"
비서: "일기 작성을 도와드릴게요. 오늘 어떤 하루를 보내셨나요?"
→ diary_organizer 에이전트가 처리
```

### 일반 질문
```
사용자: "내일 날씨 어때?"
비서: "내일 날씨를 확인해드리겠습니다."
→ 메인 에이전트가 웹 검색으로 직접 처리
```

## 확장 계획

### 향후 추가 예정 에이전트들:
- **캘린더 관리 에이전트**: Google Calendar MCP 연동
- **노션 정리 에이전트**: Notion MCP 연동  
- **이메일 관리 에이전트**: Gmail API 연동
- **할일 관리 에이전트**: 태스크 추적 및 알림
- **건강 관리 에이전트**: 운동, 식단 기록

### MCP 통합:
```python
# 향후 확장 예시
calendar_agent = Agent(
    name="calendar_manager",
    tools=[calendar_mcp_tools],
    # ...
)

notion_agent = Agent(  
    name="notion_organizer",
    tools=[notion_mcp_tools],
    # ...
)
```

## 설계 철학

1. **심플함**: ADK의 기본 패턴을 따라 복잡하지 않게
2. **실용성**: 실제로 필요한 툴들만 구현 (외부 API 호출, 파일 접근)
3. **확장성**: 새로운 에이전트나 기능 추가가 쉽도록
4. **프라이버시**: 개인 데이터는 모두 로컬에 보관
5. **사용자 중심**: 친근하고 도움이 되는 개인 비서 경험

## 개발 가이드

### 새 에이전트 추가하기:
1. `agents/` 디렉터리에 새 에이전트 파일 생성
2. 필요한 툴을 `tools/` 디렉터리에 추가  
3. `main_agent.py`의 `sub_agents`에 추가
4. 위임 로직 업데이트

### 새 툴 추가하기:
1. 외부 API 호출이나 파일 시스템 접근이 필요한지 확인
2. 적절한 툴 파일에 함수 추가
3. `tools/__init__.py`에서 export
4. 에이전트별 툴 매핑 업데이트

이 시스템은 개인의 다양한 니즈에 맞춰 점진적으로 확장할 수 있도록 설계되었습니다.