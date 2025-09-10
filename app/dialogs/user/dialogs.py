from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Group, Button, Back, Row, Start, SwitchTo
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory

from app.bot.states import UserSG, AdminSG, EmployeeSG
from app.locales.i18n_format import I18NFormat

from .getters import get_user_menu_data


user_dialog = Dialog(
    Window(
        I18NFormat("user-hello-message"),
        I18NFormat("user-menu-info-message"),
        Row(
            Start(
                I18NFormat("user-menu-admin-dialog"),
                id="to_admin_dialog",
                state=AdminSG.start,
            ),
            Start(
                I18NFormat("user-menu-employee-dialog"),
                id="to_employee_dialog",
                state=EmployeeSG.start,
            ),
        ),
        SwitchTo(
            I18NFormat("user-menu-support-button"),
            id="to_support_window",
            state=UserSG.support,
        ),
        getter=get_user_menu_data,
        state=UserSG.start,
    ),
    Window(
        I18NFormat("user-support-message"),
        Back(I18NFormat("back")),
        state=UserSG.support,
    ),
)
