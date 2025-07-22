"""
웹 관련 실제 필요한 툴들 (외부 API 호출)
"""

from __future__ import annotations

import requests
from typing import Dict, List, Any


def web_search(query: str, num_results: int = 5) -> Dict[str, Any]:
    """
    실제 웹 검색 (Google Search API 등 필요)
    
    Args:
        query: 검색 쿼리
        num_results: 반환할 결과 수
    
    Returns:
        검색 결과
    """
    # 실제로는 Google Custom Search API를 사용
    # 현재는 모킹 데이터
    return {
        "query": query,
        "results": [
            {
                "title": f"'{query}' 검색 결과 {i+1}",
                "url": f"https://example.com/result{i+1}",
                "snippet": f"'{query}'에 대한 실제 웹 검색 결과입니다."
            }
            for i in range(num_results)
        ]
    }


def fetch_url_content(url: str) -> Dict[str, Any]:
    """
    URL 내용 가져오기
    
    Args:
        url: 가져올 URL
    
    Returns:
        URL 내용
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        return {
            "url": url,
            "status_code": response.status_code,
            "content": response.text[:5000],  # 처음 5000자만
            "content_type": response.headers.get('content-type', ''),
            "success": True
        }
    except Exception as e:
        return {
            "url": url,
            "error": str(e),
            "success": False
        }


def send_webhook(url: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    웹훅 전송 (외부 서비스 연동)
    
    Args:
        url: 웹훅 URL
        data: 전송할 데이터
    
    Returns:
        전송 결과
    """
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        
        return {
            "status": "success",
            "status_code": response.status_code,
            "response": response.text
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }