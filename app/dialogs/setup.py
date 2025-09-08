from typing import List
from aiogram_dialog import Dialog

from .admin.dialogs import admin_dialog
from .user.dialogs import user_dialog
from .calendar_dialog.dialogs import content_dialog


def get_dialogs() -> List[Dialog]:
    return [
        admin_dialog,
        user_dialog,
        content_dialog,
    ]
