import logging

from aiogram_dialog import DialogManager, ShowMode, StartMode

from app.bot.states import UserSG

logger = logging.getLogger(__name__)


async def on_unknown_intent(event, dialog_manager: DialogManager):
    # Example of handling UnknownIntent Error and starting new dialog.
    logging.error(
        f"Restarting dialog: {event.exception}",
    )
    await dialog_manager.start(
        UserSG.start,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )


async def on_unknown_state(event, dialog_manager: DialogManager):
    # Example of handling UnknownState Error and starting new dialog.
    logging.error(f"Restarting dialog: {event.exception}")
    await dialog_manager.start(
        UserSG.start,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )
