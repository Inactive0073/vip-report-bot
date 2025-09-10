from typing import Dict, cast
from aiogram.types import User
from aiogram_dialog import DialogManager

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao import UserDAO, AdminDAO
from app.db.models import User



async def get_user_menu_data(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs,
) -> Dict[str, str | bool]:
    session = cast(AsyncSession, dialog_manager.middleware_data["session"])
    user_dao = UserDAO(session=session)
    is_admin = is_employee = False
    user = await user_dao.get_by_telegram_id(event_from_user.id)
    if not user:
        return {}

    if user.is_employee:
        admin_dao = AdminDAO(session=session)
        admin = await admin_dao.get_by_telegram_id(event_from_user.id)
        if admin:
            is_admin = True
        else:
            is_employee = True
    return {
        "is_admin": is_admin,
        "is_employee": is_employee,
    }
