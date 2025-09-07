import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from sqlalchemy.ext.asyncio import AsyncSession


commands_router = Router(name=__name__)

logger = logging.getLogger(__name__)


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    dialog_manager: DialogManager,
    session: AsyncSession,
) -> None:
    username = message.from_user.username
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    