from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from app.db.models import Point, Visit


class PointDAO(BaseDAO[Point]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Point)

    async def get_visits(self, point_id: int, sorted_by_latest: bool = True) -> Sequence[Visit]:
        stmt = select(Visit).where(Visit.point_id == point_id)
        if sorted_by_latest:
            stmt = stmt.order_by(Visit.created_at.desc())
        else:
            stmt = stmt.order_by(Visit.created_at.asc())
        result = await self.session.execute(stmt)
        return result.scalars().all()