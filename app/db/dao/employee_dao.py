from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from app.db.models import Employee


class EmployeeDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Employee)
