from typing import TypeVar, Generic, Type, Sequence
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

import logging

from app.db.models.base_model import BaseIDModel
from app.db.models.mixins import TelegramProfileMixin


logger = logging.getLogger(__name__)

Model = TypeVar("Model", bound=BaseIDModel)


class BaseDAO(Generic[Model]):
    def __init__(self, session: AsyncSession, model: Type[Model]) -> None:
        self.session = session
        self.model = model

    async def get_all(self) -> Sequence[Model]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, id: int) -> Model | None:
        return await self.session.get(self.model, id)

    async def add(self, **kwargs) -> Model:
        """Добавление объекта в БД"""
        instance = self.model(**kwargs)
        try:
            self.session.add(instance)
            await self.session.commit()
            return instance
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"Error adding {self.model.__name__}: {e}")
            raise SQLAlchemyError

    async def update(self, id: int, **kwargs) -> Model | None:
        """Обновление данных модели"""
        try:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(**kwargs)
                .returning(self.model)
            )
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"Error updating {self.model.__name__}: {e}")
            raise SQLAlchemyError

    async def delete(self, id: int) -> None:
        """Удаление по ID"""
        instance = await self.get_by_id(id)
        if not instance:
            return
        try:
            await self.session.delete(instance)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"Error deleting {self.model.__name__}: {e}")

    async def get_by_username(self, username: str) -> Model | None:
        if not issubclass(self.model, TelegramProfileMixin):
            raise TypeError(
                f"Model {self.model.__name__} does not inherit TelegramProfileMixin"
            )
        try:
            result = await self.session.execute(
                select(self.model).where(self.model.username == username)
            )
            return result.scalars().first()
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"Error getting {self.model.__name__} by username: {e}")
            


    async def get_by_telegram_id(self, telegram_id: int) -> Model | None:
        if not issubclass(self.model, TelegramProfileMixin):
            raise TypeError(
                f"Model {self.model.__name__} does not inherit TelegramProfileMixin"
            )
        try:
            result = await self.session.execute(
                select(self.model).where(self.model.telegram_id == telegram_id)
            )
            return result.scalars().first()
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"Error getting {self.model.__name__} by telegram_id: {e}")
            raise

