from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func
from datetime import datetime


class Base(DeclarativeBase):
    """Класс для корректной работы аннотаций"""

    pass


class WhiteUser(Base):
    """Модель пользователя, которому разрешено использовать бота"""

    __tablename__ = 'white_user'

    id: Mapped[int] = mapped_column(
        Integer,
		primary_key=True,
		name='id'
    )
    
    chat_id: Mapped[int] = mapped_column(
        Integer,
        name='id чата',
        nullable=False
    )

    user_name: Mapped[str | None] = mapped_column(
        String(length=200),
        name='никнейм'
    )

    first_name: Mapped[str] = mapped_column(
        String(length=200),
        name='имя',
        nullable=False
    )

    last_name: Mapped[str | None] = mapped_column(
        String(length=200),
        name='фамилия'
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        name='дата создания',
        default=datetime.now,
        server_default=func.now()
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        name='дата обновления',
        onupdate=func.now()
    )
