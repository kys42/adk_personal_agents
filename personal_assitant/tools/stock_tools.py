"""
주식 관련 실제 필요한 툴들 (외부 API 호출)
"""

from __future__ import annotations

import os
import requests
from typing import Dict, List, Any
from datetime import datetime, timedelta


def get_stock_price(symbol: str) -> Dict[str, Any]:
    """
    실시간 주식 가격 조회 (외부 API 필요)
    
    Args:
        symbol: 주식 심볼 (예: "AAPL", "005930.KS")
    
    Returns:
        주식 가격 정보
    """
    # 실제로는 Alpha Vantage, Yahoo Finance API 등을 사용
    # 현재는 모킹 데이터
    return {
        "symbol": symbol,
        "current_price": 150.25,
        "change": 2.15,
        "change_percent": 1.45,
        "volume": 1234567,
        "market_cap": 2500000000000,
        "last_updated": datetime.now().isoformat()
    }


def get_portfolio_data(user_id: str = "default") -> str:
    """
    사용자의 포트폴리오 데이터를 텍스트 형식으로 불러옵니다.

    Args:
        user_id: 사용자 ID

    Returns:
        포트폴리오 데이터가 담긴 텍스트. 데이터가 없을 경우 안내 메시지를 반환합니다.
    """
    portfolio_path = os.path.join("data", "portfolio", f"{user_id}_portfolio.txt")
    if not os.path.exists(portfolio_path):
        return "저장된 포트폴리오 데이터가 없습니다."
    
    with open(portfolio_path, "r", encoding="utf-8") as f:
        return f.read()


def save_portfolio_data(user_id: str, portfolio_text: str) -> Dict[str, str]:
    """
    포트폴리오 데이터를 텍스트 형식으로 저장합니다.

    Args:
        user_id: 사용자 ID
        portfolio_text: 저장할 포트폴리오 내용 (텍스트)
    
    Returns:
        저장 결과
    """
    try:
        data_dir = os.path.join("data", "portfolio")
        os.makedirs(data_dir, exist_ok=True)
        portfolio_path = os.path.join(data_dir, f"{user_id}_portfolio.txt")
        
        with open(portfolio_path, "w", encoding="utf-8") as f:
            f.write(portfolio_text)
            
        return {"status": "success", "message": f"포트폴리오가 {portfolio_path}에 성공적으로 저장되었습니다."}
    except Exception as e:
        return {"status": "error", "message": f"포트폴리오 저장 중 오류 발생: {e}"}