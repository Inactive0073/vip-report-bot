from typing import Callable, Awaitable, Dict, Any, cast
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, User
from cachetools import TTLCache
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger

from app.db.dao import UserDAO  # добавим импорт DAO


logger = getLogger(__name__)
    


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 6,  # 6 часов
        )

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        user = event.from_user
        if not user:
            return await handler(event, data)

        # Надо обновить данные пользователя, если он не в кэше
        if user.id not in self.cache:
            session: AsyncSession = data["session"]
            logger.info(
                "Обновление данных пользователя",
                extra={
                    "user_id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                },
            )
            dao = UserDAO(session)
            await dao.upsert(
                telegram_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
            )
            self.cache[user.id] = True

        return await handler(event, data)
