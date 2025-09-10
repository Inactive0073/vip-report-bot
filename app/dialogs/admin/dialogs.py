from typing import Callable
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.text import List, Format
from aiogram_dialog.widgets.kbd import (
    Button,
    Group,
    SwitchTo,
    Start,
    Select,
    ScrollingGroup,
    Multiselect,
    Back
)
from aiogram_dialog.widgets.input import TextInput

from app.locales.i18n_format import I18NFormat
from app.bot.states.admin import AdminSG
from app.utils.schemas.enums_types import UserRole
from .getters import (
    get_kicking_data,
    get_roles_data,
    get_selected_store_info,
    get_store_approve_data,
    stores_getter,
)
from .filters import filter_message_to_find_username_or_id
from .handlers import (
    add_signal_store_mode,
    edit_signal_store_mode,
    process_approve_adding_store,
    process_edit_store,
    process_to_select_role,
    process_kick_button,
    process_to_select_store,
    process_to_store_address,
    process_to_store_name,
    process_username_or_id,
    process_view_visits
)
from .services import get_role_id, parse_username_or_id_data, get_telegram_id


admin_dialog = Dialog(
    Window(
        I18NFormat("admin-hello-message"),
        SwitchTo(I18NFormat("admin-team-window"), id="team_selected", state=AdminSG.team),
        SwitchTo(
            I18NFormat("admin-reports-window"), id="reports_selected", state=AdminSG.reports
        ),
        SwitchTo(
            I18NFormat("admin-stores-window"), id="stores_selected", state=AdminSG.stores
        ),
        state=AdminSG.start,
    ),
    # Отчеты
    Window(
       I18NFormat("reports_msg"),
        Group(
            SwitchTo(
               I18NFormat("reports_users"),
                id="reports_users_selected",
                state=AdminSG.report_users,
            ),
            # заморожено
            # SwitchTo(
            #    I18NFormat("reports_scheduled_posts"),
            #     id="reports_scheduled_posts_selected",
            #     state=AdminSG.report_posts,
            # ),
            SwitchTo(
               I18NFormat("reports_bonus_records"),
                id="reports_bonus_records_selected",
                state=AdminSG.report_bonuses,
            ),
            width=2,
        ),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.start),
        state=AdminSG.reports,
    ),
    # Команда
    Window(
       I18NFormat("admin-team-menu-msg"),
        Group(
            SwitchTo(
               I18NFormat("admin-team-invite-btn"),
                id="add_selected",
                state=AdminSG.selecting_role,
            ),
            SwitchTo(
               I18NFormat("admin-team-kick-btn"),
                id="kick_selected",
                state=AdminSG.selecting_employee,
            ),
            width=2,
        ),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.start),
        state=AdminSG.team,
    ),
    # Выдача отчетов
    # Window(),


    # Управление магазинами
    Window(
        I18NFormat("admin-store-hello-msg"),
        ScrollingGroup(
            Select(
                Format("{item[0]}"),
                id="selected_store",
                item_id_getter=lambda item: item[1],
                items="stores",
                on_click=process_to_select_store
            ),
            id="stores_scroll",
            width=1,
            height=8
        ),
        SwitchTo(I18NFormat("add-store-window"), id="add_store", state=AdminSG.add_store, on_click=add_signal_store_mode),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.start),
        state=AdminSG.stores,
        getter=stores_getter
    ),

    ########
    # Управление магазином, анализ по магазину
    Window(
        Format("{admin-store-full-info-msg}"),
        SwitchTo(I18NFormat("edit"), id="on_edit_store", state=AdminSG.add_store, on_click=edit_signal_store_mode),
        Button(I18NFormat("admin-store-view-visits"), id="on_view_visits", on_click=process_view_visits),
        Back(I18NFormat("back")),
        state=AdminSG.process_store,
        getter=get_selected_store_info
    ),
    Window(
        Format("{admin-store-check-data-store-msg}"),
        Button(I18NFormat("approve"), id="approve_edit_store", on_click=process_edit_store),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.process_store),
        state=AdminSG.approve_edit_store,
        getter=get_store_approve_data
    ),

    ########
    Window(
        I18NFormat("admin-store-create-store-msg"),
        TextInput(
            id="listen_store_name",
            on_success=process_to_store_name
        ),
        Back(I18NFormat("back")),
        state=AdminSG.add_store
    ),
    Window(
        I18NFormat("admin-store-add-store-address-msg"),
        TextInput(
            id="listen_store_name",
            on_success=process_to_store_address
        ),
        Back(I18NFormat("back")),
        state=AdminSG.process_address
    ),
    Window(
        Format("{admin-store-check-data-store-msg}"),
        Button(I18NFormat("approve"), id="on_approve_adding_store", on_click=process_approve_adding_store),
        Back(I18NFormat("back")),
        state=AdminSG.approve_adding_store,
        getter=get_store_approve_data
    ),
    # Управление командой
    # раздел добавления
    Window(
       I18NFormat("admin-team-select-role-msg"),
        Group(
            Select(
               Format("{item.value[1]}"),
                id="selected_role",
                item_id_getter=get_role_id,
                items="roles",
                on_click=process_to_select_role,
            ),
            width=2,
        ),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.team),
        state=AdminSG.selecting_role,
        getter=get_roles_data,
    ),
    Window(
       I18NFormat("admin-team-invite-msg"),
        TextInput(
            id="processing_invite_new_member",
            type_factory=parse_username_or_id_data,
            on_success=process_username_or_id,
            filter=filter_message_to_find_username_or_id,
        ),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.team),
        state=AdminSG.invite,
    ),
    # раздел удаления
    Window(
       I18NFormat("admin-team-kick-msg"),
        List(
           Format(
                "{pos}. @{item.username} | {item.first_name} <b>ID:<code>{item.telegram_id}</code></b>"
            ),
            items="employees",
            id="list_employees",
            page_size=12,
        ),
        ScrollingGroup(
            Multiselect(
               Format("✓ {item.first_name} | {item.username}"),
               Format("{item.first_name} | {item.username}"),
                id="ms_employees",
                items="employees",
                item_id_getter=get_telegram_id,
            ),
            id="sg_employees",
            width=2,
            height=6,
            on_page_changed=sync_scroll("list_employees"),
            hide_on_single_page=True,
        ),
        SwitchTo(
           I18NFormat("next"),
            id="to_kick_employees",
            state=AdminSG.kick,
            when="selected_employees",
        ),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.team),
        state=AdminSG.selecting_employee,
        getter=get_kicking_data,
        preview_data=get_kicking_data,
    ),
    Window(
       I18NFormat("admin-team-approve-kick-msg"),
        Button(I18NFormat("yes"), id="on_kick_selected", on_click=process_kick_button),
        SwitchTo(I18NFormat("back"), id="__back__", state=AdminSG.selecting_employee),
        state=AdminSG.kick,
    ),
)
