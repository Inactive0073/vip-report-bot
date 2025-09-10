from sqlalchemy.ext.asyncio import AsyncSession


from .base import BaseDAO
from app.db.models import Admin


class AdminDAO(BaseDAO[Admin]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Admin)
