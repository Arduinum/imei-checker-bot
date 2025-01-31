from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    AsyncEngine
)
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from imei_checker_bot.settings import settings
from imei_checker_bot.logger import logger


logger.name = __name__


def get_session(async_engine: AsyncEngine) -> AsyncSession:
    """Функция для получения сессии"""

    try:
        # подключаемся к бд асинхронно и создаём сессию
        AsyncSessionMaker = async_sessionmaker(
            bind=async_engine, 
            class_=AsyncSession,
            expire_on_commit=False
        )
        return AsyncSessionMaker()
    # временное решение
    except Exception as err:
        message = f'Неудалось создать сессию - {err.__class__.__name__}: {err}'
        logger.error(message)


async_engine = create_async_engine(settings.db_settings.url_db.unicode_string())