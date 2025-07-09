from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=True,
        env_prefix='BOT__',
        extra='ignore'
    )
    TOKEN: str
    CHANNEL_ID: str


bot_settings = Settings()
