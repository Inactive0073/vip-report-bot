from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import (
    Group,
    Button,
    Row,
    RequestContact,
    Start,
)
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory

from app.bot.states.user.user import UserSG
from .getters import get_common_data, get_customer_menu_data


user_dialog = Dialog(
    Window(
        Format("{}"),
        getter=get_customer_menu_data,
        state=UserSG.start
    ),
    getter=get_common_data,
)
