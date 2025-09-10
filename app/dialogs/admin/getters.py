from typing import Dict, List, Optional, Sequence, Union, cast
from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Multiselect, Button

from sqlalchemy.ext.asyncio import AsyncSession 

from app.db.dao import StaffDAO, PointDAO
from app.db.models import Employee, Admin
from app.db.models.point import Point
from app.locales.i18n_format import I18N_FORMAT_KEY
from app.utils.schemas.enums_types import UserRole
from .services import format_stores


async def get_roles_data( **kwargs) -> Dict[str, Sequence[UserRole]]:
    roles = list(UserRole)
    return {
        "roles": roles
    }


async def get_kicking_data(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs,
) -> Dict[str, Union[List[str], List[Admin | Employee]]]:
    session = dialog_manager.middleware_data["session"]
    ms: Optional[Multiselect] = dialog_manager.find("ms_employees")
    if not ms:
        return {"selected_employees": [], "employees": []}
    selected_employees = ms.get_checked() # type: ignore
    employees = []
    dao = StaffDAO(session=session)
    for user in await dao.get_all_staff():
        user.username = "нет никнейма" if user.username is None else user.username
        if user.username != event_from_user.username:
            employees.append(user)

    return  {
        "selected_employees": selected_employees,
        "employees": employees,
    }


async def stores_getter(
       dialog_manager: DialogManager,
       **kwargs
) -> Dict[str, list[tuple[str, str]]]:
    session = dialog_manager.middleware_data["session"]
    dao = PointDAO(session=session)
    stores = format_stores(cast(Sequence[Point], await dao.get_all()))
    dialog_manager.dialog_data["local_stores"] = stores
    return {
        "stores": stores,
    }

async def get_store_approve_data(
    dialog_manager: DialogManager,
    **kwargs
) -> Dict[str, str]:
    store_name = dialog_manager.dialog_data["store_name"]
    store_address = dialog_manager.dialog_data["store_address"]
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    store_info = _("admin-store-check-data-store-msg", ({"store_name": store_name, "store_address": store_address}))
    
    return {
        "admin-store-check-data-store-msg": store_info,
    }

async def get_selected_store_info(
    dialog_manager: DialogManager,
    **kwargs
) -> Dict[str, str]:
    _ = dialog_manager.middleware_data[I18N_FORMAT_KEY]
    session = cast(AsyncSession, dialog_manager.middleware_data["session"])
    selected_store_id = int(dialog_manager.dialog_data["selected_store_id"])
    point_dao = PointDAO(session)

    selected_store = await point_dao.get_by_id(selected_store_id)
    if selected_store:
        selected_store_fmt = f"Имя: {selected_store.name}\nАдрес: {selected_store.address}"
    else:
        selected_store_fmt = "No data"
    visits = await point_dao.get_visits(selected_store_id)

    return {
        "admin-store-full-info-msg": _("admin-store-full-info-msg", ({"store_info": selected_store_fmt}))
    }