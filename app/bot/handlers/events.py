
from aiogram_dialog import DialogManager
import logging

logger = logging.getLogger(__name__)

async def on_shutdown(event, dialog_manager: DialogManager):
    logger.info("The bot is shutting down...")
    