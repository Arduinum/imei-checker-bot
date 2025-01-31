from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, PostgresDsn
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = '.env', 
        env_file_encoding='utf-8',
        extra='ignore'
    )


class SettingsDb(ModelConfig):
    """Класс для данных бд"""

    type_and_driver_db: str
    name_db: str
    user_db: str
    password_db: SecretStr
    host_db: str
    port_db: int
    url_db: PostgresDsn | None = None

    def __init__(self, **kwargs):  
        super().__init__(**kwargs)  
        if not self.url_db:  
            self.url_db = PostgresDsn.build(  
                scheme=self.type_and_driver_db,  
                username=self.user_db,  
                password=self.password_db.get_secret_value(),  
                host=self.host_db,  
                port=self.port_db,  
                path=self.name_db,  
            )


class Settings(ModelConfig):
    """Класс для данных конфига"""
    
    db_settings: SettingsDb = SettingsDb()
    token: SecretStr


settings = Settings()

bot = Bot(
    token=settings.token.get_secret_value(), 
    default=DefaultBotProperties(parse_mode='Markdown')
)
