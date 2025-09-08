from typing import TypeVar, Generic, Type, Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.base_model import BaseIDModel
from app.db.models.mixins import TelegramProfileMixin

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
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def delete(self, id: int) -> None:
        instance = await self.get_by_id(id)
        if instance:
            await self.session.delete(instance)
            await self.session.commit()

    async def get_by_telegram_id(self, telegram_id: int) -> Model | None:
        if not issubclass(self.model, TelegramProfileMixin):
            raise TypeError(
                f"Model {self.model.__name__} does not inherit TelegramProfileMixin"
            )
        
        result = await self.session.execute(
            select(self.model).where(self.model.telegram_id == telegram_id)
        )
        return result.scalars().first()