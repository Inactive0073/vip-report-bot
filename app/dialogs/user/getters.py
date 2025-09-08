from typing import TYPE_CHECKING, Dict, cast
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao import UserDAO, AdminDAO
from app.db.models import User

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner  # type:ignore


async def get_common_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
) -> Dict[str, str]:
    return {
        "back": i18n.start.,
        "hello_guest": i18n.customer.hello.message(),
    }


async def get_customer_menu_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> Dict[str, str | bool] | None:
    session = cast(AsyncSession, dialog_manager.middleware_data["session"])
    user_dao = UserDAO(session=session)
    is_admin = is_employee = False
    user = await user_dao.get_by_telegram_id(event_from_user.id)
    if not user:
        return None

    if user.is_employee:
        admin_dao = AdminDAO(session=session)
        admin = await admin_dao.get_by_telegram_id(event_from_user.id)
        if admin:
            is_admin = True
        else:
            is_employee = True
    return {
        "menu_info_message": i18n.customer.menu.info.message(),
        "is_admin": is_admin,
        "is_employee": is_employee,
        "to_admin_menu": i18n.admin.comeback.btn(),
    }
