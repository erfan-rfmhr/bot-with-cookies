from typing import Sequence, TypeVar, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

ChatId = TypeVar("ChatId", bound=int)

class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file="config/.env", frozen=True, str_strip_whitespace=True)
    BOT_TOKEN: str
    DATABASE_URL: Optional[str] = None
    ADMINS: Sequence[ChatId]


__all__ = ["BotSettings"]
