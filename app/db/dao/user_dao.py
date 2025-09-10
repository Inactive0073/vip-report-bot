from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from .base import BaseDAO
from app.db.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User)

    async def upsert(
        self,
        telegram_id: int,
        first_name: str,
        last_name: str | None = None,
        username: str | None = None,
    ) -> User | None:
        stmt = (
            insert(User)
            .values(
                telegram_id=telegram_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            .on_conflict_do_update(
                index_elements=["telegram_id"],
                set_={
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                },
            )
        )
        await self.session.execute(stmt)
        await self.session.commit()
        user = await self.get_by_telegram_id(telegram_id)
        if user:
            return user
