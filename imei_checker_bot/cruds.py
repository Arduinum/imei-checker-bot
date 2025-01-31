from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    AsyncEngine
)
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select

from imei_checker_bot.settings import settings
from imei_checker_bot.logger import logger
from imei_checker_bot.models import WhiteUser


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


async def check_chat_id(chat_id: int) -> bool | None:
    """Асинхронная функция для проверки наличия chat_id пользователя"""

    try:
        user = WhiteUser
        async with get_session(async_engine=async_engine) as async_session:
            query = select(user.chat_id).where(chat_id == user.chat_id)
            result = await async_session.execute(query)
            user_with_chat = result.mappings().first()
            
            if user_with_chat:
                return True
    # Todo - временное решение. Нужно будет отловить конкретные ошибки.
    except Exception as err:
        message = f'{err.__class__.__name__}: {err}'
        logger.error(message)
