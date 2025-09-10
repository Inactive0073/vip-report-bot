import asyncio

from typing import Sequence
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.db.models import Admin, Employee

import logging

logger = logging.getLogger(__name__)

class StaffDAO:
    """DAO для работы с сотрудниками, охватывает Admin и Employee"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_staff(self) -> list[Admin | Employee]:
        """
        Возвращает список всех сотрудников (Admin и Employee).

        Returns:
            list[Admin | Employee]: все сотрудники
        """
        result_admins, result_employees = await asyncio.gather(
            self.session.execute(select(Admin)),
            self.session.execute(select(Employee))
        )
        return [a for a in result_admins.scalars().all()] + \
            [e for e in result_employees.scalars().all()]
    
    async def delete_by_telegram_ids(self, telegram_ids: Sequence[int]) -> int:
        """
        Удаляет всех сотрудников по telegram_id из таблиц Admin и Employee.

        Args:
            telegram_ids: Список telegram_id для удаления

        Returns:
            int: Общее количество удалённых записей
        """
        total_deleted = 0
        try:
            for model in (Admin, Employee):
                stmt = delete(model).where(model.telegram_id.in_(telegram_ids))
                result = await self.session.execute(stmt)
                total_deleted += result.rowcount or 0
            await self.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Error deleting instances: {e}")
            await self.session.rollback()
        return total_deleted
