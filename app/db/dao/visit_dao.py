from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Sequence

from .base import BaseDAO
from app.db.models import Visit


class VisitDAO(BaseDAO[Visit]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Visit)

    async def get_by_period(
        self, start_date: datetime, end_date: datetime
    ) -> Sequence[Visit]:
        result = await self.session.execute(
            select(Visit)
            .where(Visit.created_at.between(start_date, end_date))
            .order_by(Visit.created_at.desc())
        )
        return result.scalars().all()

    async def get_by_point_id(self, point_id: int) -> Sequence[Visit]:
        result = await self.session.execute(
            select(Visit)
            .where(Visit.point_id == point_id)
            .order_by(Visit.created_at.desc())
        )
        return result.scalars().all()
