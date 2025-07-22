"""
일기 관련 실제 필요한 툴들 (파일 시스템 접근)
"""

from __future__ import annotations

import os
import json
from typing import Dict, List, Any
from datetime import datetime


def save_diary_entry(entry: Dict[str, Any], user_id: str = "default") -> Dict[str, str]:
    """
    일기 항목 저장
    
    Args:
        entry: 일기 데이터
        user_id: 사용자 ID
    
    Returns:
        저장 결과
    """
    # 실제 파일 시스템에 저장
    diary_dir = f"/home/kys/projects/adk_agent/personal_assistant/data/diaries/{user_id}"
    os.makedirs(diary_dir, exist_ok=True)
    
    entry_id = entry.get("id", datetime.now().strftime("%Y%m%d_%H%M%S"))
    file_path = f"{diary_dir}/{entry_id}.json"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(entry, f, ensure_ascii=False, indent=2)
        
        return {
            "status": "success",
            "message": f"Diary entry saved: {entry_id}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Failed to save diary entry: {str(e)}"
        }


def load_diary_entries(user_id: str = "default", limit: int = 10) -> Dict[str, Any]:
    """
    일기 항목들 로드
    
    Args:
        user_id: 사용자 ID
        limit: 로드할 항목 수
    
    Returns:
        일기 항목들
    """
    diary_dir = f"/home/kys/projects/adk_agent/personal_assistant/data/diaries/{user_id}"
    
    if not os.path.exists(diary_dir):
        return {"entries": [], "total": 0}
    
    entries = []
    files = sorted([f for f in os.listdir(diary_dir) if f.endswith('.json')], reverse=True)
    
    for file_name in files[:limit]:
        file_path = os.path.join(diary_dir, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
                entries.append(entry)
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
    
    return {
        "entries": entries,
        "total": len(files),
        "loaded": len(entries)
    }


def search_diary_entries(query: str, user_id: str = "default") -> Dict[str, Any]:
    """
    일기 검색
    
    Args:
        query: 검색어
        user_id: 사용자 ID
    
    Returns:
        검색 결과
    """
    all_entries = load_diary_entries(user_id, limit=100)["entries"]
    
    matching_entries = []
    for entry in all_entries:
        content = entry.get("content", "").lower()
        title = entry.get("title", "").lower()
        
        if query.lower() in content or query.lower() in title:
            matching_entries.append(entry)
    
    return {
        "query": query,
        "matches": matching_entries,
        "total_matches": len(matching_entries)
    }