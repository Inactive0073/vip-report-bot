from typing import Sequence

from app.db.models import User
from app.utils.schemas.enums_types import UserRole
from app.db.models import Point
from .handlers import process_to_select_store

def parse_username_or_id_data(data: str) -> str:
    if data.startswith("@"):
        return data.replace("@", "")
    if data.isdigit():
        return data
    raise ValueError(
        "Неподходящий формат сообщения для добавления нового юзера в команду. Допустимый формат 665323 или @username"
    )


def get_telegram_id(user: User):
    return user.telegram_id


def get_role_id(user_role: UserRole):
    return user_role.role_id


def format_stores(stores: Sequence[Point]) -> list[tuple[str, str]]:
    return [
        (f"Имя: {store.name}\nАдрес: {store.address}", str(store.id))
        for store in stores
    ]
