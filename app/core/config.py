import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, field_validator, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    LOG_FILENAME: str = "app.log"

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    
    # Oracle settings
    ORACLE_HOST: str = "localhost"
    ORACLE_PORT: int = 1521 # Default Oracle port
    APP_USER: str # Application user from docker-compose
    APP_USER_PASSWORD: str # Application user password from docker-compose
    ORACLE_SERVICE_NAME: str = "FREEPDB1" # Default service for oracle-free
    ORACLE_PASSWORD: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        # Construct the Oracle connection string
        # Format: oracle+oracledb://user:password@host:port/?service_name=service_name
        return "oracle+oracledb://SYSTEM:wildlife@localhost:1521/?service_name=FREEPDB1"


settings = Settings() 