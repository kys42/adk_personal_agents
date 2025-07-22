"""
Personal Assistant Tools Collection

실제 외부 API 호출이나 파일 시스템 접근이 필요한 툴들만 모아놓은 중앙 집중식 툴 레지스트리입니다.
단순한 텍스트 분석, 감정 분석 등은 LLM 인스트럭션으로 처리합니다.
"""

from __future__ import annotations

from google.adk.tools import google_search
from .web_tools import web_search, fetch_url_content, send_webhook
from .stock_tools import get_stock_price, get_portfolio_data, save_portfolio_data
from .diary_tools import save_diary_entry, load_diary_entries, search_diary_entries

# 툴 카테고리별 그룹핑 (실제 외부 리소스 접근이 필요한 것들만)
WEB_TOOLS = [
    web_search,
    fetch_url_content,
    send_webhook
]


STOCK_TOOLS = [
    get_stock_price,
    get_portfolio_data, 
    save_portfolio_data
]

DIARY_TOOLS = [
    save_diary_entry,
    load_diary_entries,
    search_diary_entries
]

# 모든 툴을 하나의 딕셔너리로 관리
ALL_TOOLS = {
    "web": WEB_TOOLS,
    "stock": STOCK_TOOLS,
    "diary": DIARY_TOOLS
}

def get_tools_for_agent(agent_type: str, specific_tools: list = None) -> list:
    """
    에이전트 타입에 따른 툴 선택 함수
    
    Args:
        agent_type: 에이전트 타입 (portfolio, diary, general 등)
        specific_tools: 특정 툴 리스트 (선택사항)
    
    Returns:
        선택된 툴들의 리스트
    """
    if specific_tools:
        return specific_tools
    
    tool_mapping = {
        "portfolio": WEB_TOOLS + STOCK_TOOLS,
        "diary": DIARY_TOOLS,
        "general": WEB_TOOLS,
        "all": WEB_TOOLS + STOCK_TOOLS + DIARY_TOOLS
    }
    
    return tool_mapping.get(agent_type, WEB_TOOLS)