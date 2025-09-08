import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager

from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.states.user.user import UserSG
from app.db.dao.user_dao import UserDAO


commands_router = Router(name=__name__)

logger = logging.getLogger(__name__)


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    dialog_manager: DialogManager,
    session: AsyncSession,
) -> None:
    if (tg_user:=message.from_user):
        username = tg_user.username
        telegram_id = tg_user.id
        first_name = tg_user.first_name
        last_name = tg_user.last_name
        user_dao = UserDAO(session=session)
        user = await user_dao.upsert(telegram_id=telegram_id, first_name=first_name, last_name=last_name, username=username)
        logger.info(f"Пользователь {first_name} запустил бота.\nДанные:{user!r}")
        await dialog_manager.start(state=UserSG.start)