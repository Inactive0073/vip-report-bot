import logging
from aiogram.types import (
    Message,
    CallbackQuery,
)
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select, Multiselect
from aiogram_dialog.widgets.input import ManagedTextInput

from sqlalchemy.ext.asyncio import AsyncSession

from typing import cast

from app.bot.states.admin.admin import AdminSG
from app.db.dao import UserDAO, AdminDAO, EmployeeDAO, StaffDAO, PointDAO
from app.locales.i18n_format import I18N_FORMAT_KEY
from app.utils.schemas.enums_types import StoreMode, UserRole




logger = logging.getLogger(__name__)


async def process_to_select_role(
    callback: CallbackQuery, _: Select, dialog_manager: DialogManager, data: str
):
    dialog_manager.dialog_data["selected_role"] = data
    await dialog_manager.switch_to(AdminSG.invite)


async def process_username_or_id(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
):
    session = cast(AsyncSession, dialog_manager.middleware_data.get("session"))
    user_dao = UserDAO(session)
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    role_id = int(dialog_manager.dialog_data["selected_role"])
    role = UserRole.get_role_by_id(role_id)
    if not role:
        return
    
    # Получаем пользователя по username или telegram_id
    if text.isdigit():
        user = await user_dao.get_by_telegram_id(int(text))
    else:
        user = await user_dao.get_by_username(text)

    if not user:
        await message.answer(_("admin-not-found-user"))
        return

    logger.info(
        f"Запрос на добавление пользователя {user.telegram_id} с ролью {role.label}. Запросил: {message.from_user.id if message.from_user else 'unknown'}"
    )

    try:
        if role == UserRole.EMPLOYEE:
            dao = EmployeeDAO(session)
        else:
            dao = AdminDAO(session)

        await dao.add(
            telegram_id=user.telegram_id,
            first_name=user.first_name,
            username=user.username,
            last_name=user.last_name,
        )

        await message.answer(_("admin-team-invite-success"))
        await dialog_manager.switch_to(AdminSG.start)

    except Exception as e:
        logger.exception(f"Ошибка при добавлении роли: {e}")
        await message.answer(_("admin-team-invite-unsuccess"))


async def process_kick_button(
    callback: CallbackQuery, _: Button, dialog_manager: DialogManager
):
    session = dialog_manager.middleware_data["session"]
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    ms: Multiselect = dialog_manager.find("ms_employees") # type: ignore
    selected_employees = list(map(int, ms.get_checked())) # type: ignore
    dao = StaffDAO(session)
    if await dao.delete_by_telegram_ids(selected_employees):
        callback.message.answer(_("admin-team-kick-success")) # type: ignore
        await dialog_manager.switch_to(AdminSG.start)
    else:
        callback.message.answer(_("admin-team-kick-unsuccess")) # type: ignore
        await dialog_manager.switch_to(AdminSG.selecting_employee)

async def add_signal_store_mode(
    callback: CallbackQuery, _: Button, dialog_manager: DialogManager
):
    dialog_manager.dialog_data["STORE_MODE"] = StoreMode.ADD.value
    await dialog_manager.switch_to(AdminSG.add_store)

async def edit_signal_store_mode(
    callback: CallbackQuery, _: Button, dialog_manager: DialogManager
):
    dialog_manager.dialog_data["STORE_MODE"] = StoreMode.EDIT.value
    await dialog_manager.switch_to(AdminSG.add_store)


async def process_to_select_store(
    callback: CallbackQuery, _: Select, dialog_manager: DialogManager, item_id: str
):
    dialog_manager.dialog_data["selected_store_id"] = item_id
    await dialog_manager.switch_to(AdminSG.process_store)


async def process_to_store_name(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
):
    dialog_manager.dialog_data["store_name"] = text
    await dialog_manager.switch_to(AdminSG.process_address)


async def process_to_store_address(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
):
    dialog_manager.dialog_data["store_address"] = text
    STORE_MODE = dialog_manager.dialog_data["STORE_MODE"]
    if STORE_MODE == StoreMode.ADD.value: 
        await dialog_manager.switch_to(AdminSG.approve_adding_store)
    else:
        await dialog_manager.switch_to(AdminSG.approve_edit_store)

async def process_approve_adding_store(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager
):
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    session = cast(AsyncSession, dialog_manager.middleware_data.get("session"))
    store_name = dialog_manager.dialog_data["store_name"]
    store_address = dialog_manager.dialog_data["store_address"]

    try:
        point_dao = PointDAO(session)
        await point_dao.add(
            name=store_name,
            address=store_address
        )
        await callback.message.answer(_("admin-store-create-store-success")) # type: ignore
        await dialog_manager.switch_to(AdminSG.start)

    except Exception as e:
        logger.exception(f"Ошибка при добавлении магазина: {e}")
        await callback.message.answer(_("admin-store-create-store-unsuccess")) # type: ignore

async def process_edit_store(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager
):
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    session = cast(AsyncSession, dialog_manager.middleware_data.get("session"))
    store_id = int(dialog_manager.dialog_data["selected_store_id"])

    try:
        point_dao = PointDAO(session)
        store = await point_dao.get_by_id(int(store_id))
        if not store:
            await callback.message.answer(_("admin-store-edit-not-found")) # type: ignore
            return

        await point_dao.update(
            id=store_id,
            name=dialog_manager.dialog_data["store_name"],
            address=dialog_manager.dialog_data["store_address"]
        )
        await callback.message.answer(_("admin-store-edit-success")) # type: ignore
        await dialog_manager.switch_to(AdminSG.start)

    except Exception as e:
        logger.exception(f"Ошибка при редактировании магазина: {e}")
        await callback.message.answer(_("admin-store-edit-unsuccess")) # type: ignore

async def process_view_visits(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager
):
    pass