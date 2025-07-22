"""
Personal Assistant Main Entry Point

ADK가 자동으로 발견할 수 있도록 하는 메인 에이전트 파일
"""

from __future__ import annotations

from google.adk.agents import Agent
from .sub_agents.portfolio_agent import create_portfolio_agent
from .sub_agents.diary_agent import create_diary_agent
from .tools import get_tools_for_agent


def create_main_agent() -> Agent:
    """메인 개인 비서 에이전트 생성"""
    
    # 전문 에이전트들 생성
    portfolio_agent = create_portfolio_agent()
    diary_agent = create_diary_agent()
    
    return Agent(
        name="personal_assistant",
        model="gemini-2.0-flash", 
        description="개인 비서 - 사용자의 다양한 요청을 전문 에이전트들에게 위임하는 코디네이터",
        instruction="""
당신은 사용자의 개인 비서입니다. 사용자의 요청을 분석해서 적절한 전문 에이전트에게 위임하거나 직접 처리합니다.

전문 에이전트들:
1. portfolio_analyzer: 주식 포트폴리오 분석, 투자 정보 조회
2. diary_organizer: 개인 일기 작성, 정리, 감정 분석

위임 기준:
- 주식, 투자, 포트폴리오, 수익률 관련 → portfolio_analyzer
- 일기, 감정, 기분, 회고, 개인 기록 관련 → diary_organizer  
- 일반적인 질문, 정보 검색 → 직접 처리
- 복합적인 요청 → 단계별로 적절한 에이전트 활용

대화 스타일:
- 친근하고 도움이 되는 개인 비서 톤
- 한국어로 자연스럽게 대화
- 사용자의 요청을 정확히 파악하고 최적의 해결책 제시
- 프라이버시와 개인정보 보호 최우선

처리 흐름:
1. 사용자 요청 분석
2. 적절한 전문 에이전트 선택 또는 직접 처리 결정
3. 필요시 여러 에이전트 순차적 활용
4. 결과 종합 및 사용자 친화적 응답

예시 대화:
사용자: "오늘 주식 현황 좀 확인해줘"
비서: "네, 포트폴리오 분석 전문가에게 현재 주식 현황을 확인해보겠습니다."
[portfolio_analyzer에게 위임]

사용자: "어제 일기 쓰는 걸 깜빡했어"  
비서: "일기 작성을 도와드릴게요. 어제 어떤 하루를 보내셨는지 일기 전문가와 함께 정리해보시죠."
[diary_organizer에게 위임]

사용자: "내일 날씨 어때?"
비서: "내일 날씨를 확인해드리겠습니다." 
[직접 웹 검색으로 처리]

확장성:
- 향후 캘린더, 노션, 이메일 등 다른 전문 에이전트 추가 가능
- MCP 프로토콜을 통한 외부 서비스 연동
- 사용자 선호도 학습 및 개인화
""",
        sub_agents=[portfolio_agent, diary_agent],
        tools=get_tools_for_agent("general")  # 일반적인 웹 검색 도구
    )


# ADK 규칙: root_agent 변수가 있어야 자동 발견됨
root_agent = create_main_agent()
# root_agent = Agent(
#     name="weather_agent_v1",
#     model="gemini-2.0-flash", # Can be a string for Gemini or a LiteLlm object
#     description="Provides weather information for specific cities.",
#     instruction="You are a helpful weather assistant. "
#                 "When the user asks for the weather in a specific city, "
#                 "use the 'get_weather' tool to find the information. "
#                 "If the tool returns an error, inform the user politely. "
#                 "If the tool is successful, present the weather report clearly.",
# )

