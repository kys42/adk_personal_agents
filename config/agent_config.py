"""
에이전트 설정 관리
"""

from __future__ import annotations

import os
from typing import Dict, Any
from pathlib import Path


class AgentConfig:
    """에이전트 설정 관리 클래스"""
    
    def __init__(self):
        self.load_env_config()
        
    def load_env_config(self):
        """환경 변수에서 설정 로드"""
        
        # 기본 설정
        self.google_api_key = os.getenv("GOOGLE_API_KEY", "")
        self.use_vertex_ai = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() == "TRUE"
        
        # OAuth 설정
        self.oauth_client_id = os.getenv("OAUTH_CLIENT_ID", "")
        self.oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET", "")
        
        # 사용자 설정
        self.user_id = os.getenv("USER_ID", "default")
        self.user_name = os.getenv("USER_NAME", "사용자")
        
        # 파일 경로 설정
        self.data_path = Path(os.getenv("DATA_PATH", "./data"))
        self.data_path.mkdir(exist_ok=True)
        
        # 웹 서버 설정
        self.web_host = os.getenv("WEB_HOST", "localhost")
        self.web_port = int(os.getenv("WEB_PORT", "8000"))
        
        # 로그 설정
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
    
    def get_model_config(self) -> Dict[str, str]:
        """LLM 모델 설정 반환"""
        return {
            "primary": "gemini-2.0-flash",
            "fast": "gemini-1.5-flash", 
            "analysis": "gemini-2.0-flash"
        }
    
    def get_agent_config(self, agent_type: str) -> Dict[str, Any]:
        """특정 에이전트 타입의 설정 반환"""
        
        base_config = {
            "model": self.get_model_config()["primary"],
            "user_id": self.user_id,
            "data_path": self.data_path
        }
        
        agent_specific = {
            "portfolio": {
                "model": self.get_model_config()["analysis"],
                "data_file": self.data_path / "portfolio" / f"{self.user_id}_portfolio.json"
            },
            "diary": {
                "model": self.get_model_config()["primary"], 
                "data_dir": self.data_path / "diaries" / self.user_id
            },
            "main": {
                "model": self.get_model_config()["primary"],
                "host": self.web_host,
                "port": self.web_port
            }
        }
        
        config = base_config.copy()
        config.update(agent_specific.get(agent_type, {}))
        
        return config
    
    def validate_config(self) -> bool:
        """필수 설정이 있는지 확인"""
        if not self.google_api_key:
            print("❌ GOOGLE_API_KEY가 설정되지 않았습니다.")
            return False
            
        return True
    
    def setup_directories(self):
        """필요한 디렉터리들 생성"""
        directories = [
            self.data_path,
            self.data_path / "portfolio",
            self.data_path / "diaries" / self.user_id,
            self.data_path / "logs"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
        
        print(f"✅ 데이터 디렉터리 설정 완료: {self.data_path}")


# 전역 설정 인스턴스
config = AgentConfig()