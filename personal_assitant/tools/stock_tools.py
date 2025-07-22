"""
주식 관련 실제 필요한 툴들 (외부 API 호출)
"""

from __future__ import annotations

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


def get_portfolio_data(user_id: str = "default") -> Dict[str, Any]:
    """
    사용자 포트폴리오 데이터 조회 (파일 시스템 또는 DB 접근)
    
    Args:
        user_id: 사용자 ID
    
    Returns:
        포트폴리오 데이터
    """
    # 실제로는 파일이나 DB에서 읽어옴
    return {
        "user_id": user_id,
        "holdings": [
            {"symbol": "AAPL", "shares": 10, "avg_cost": 145.50},
            {"symbol": "GOOGL", "shares": 5, "avg_cost": 2800.00},
            {"symbol": "005930.KS", "shares": 20, "avg_cost": 75000}
        ],
        "cash": 50000,
        "last_updated": datetime.now().isoformat()
    }


def save_portfolio_data(user_id: str, portfolio_data: Dict[str, Any]) -> Dict[str, str]:
    """
    포트폴리오 데이터 저장
    
    Args:
        user_id: 사용자 ID
        portfolio_data: 저장할 포트폴리오 데이터
    
    Returns:
        저장 결과
    """
    # 실제로는 파일이나 DB에 저장
    return {
        "status": "success",
        "message": f"Portfolio data saved for user {user_id}",
        "timestamp": datetime.now().isoformat()
    }