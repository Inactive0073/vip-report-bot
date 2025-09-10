import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import ExceptionTypeFilter
from aiogram.client.default import DefaultBotProperties

from aiogram_dialog import setup_dialogs
from aiogram_dialog.api.exceptions import UnknownIntent, UnknownState

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from dataclasses import dataclass

from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.enums import ParseMode
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

from fluent.runtime import FluentLocalization, FluentResourceLoader


from app.bot.handlers.errors import on_unknown_intent, on_unknown_state

from ..db.base import Base
from .middlewares import (
    DbSessionMiddleware,
    TrackAllUsersMiddleware,
    I18nMiddleware,
)
from ..dialogs.setup import get_dialogs
from .handlers.commands import commands_router
from ..config import Config

logger = logging.getLogger(__name__)


@dataclass
class DependeciesConfig:
    config: Config
    DEFAULT_LOCALE = "ru"
    LOCALES = ["ru"]

    async def setup_database(
        self,
    ) -> tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
        engine = create_async_engine(
            url=self.config.db.dsn, echo=self.config.db.is_echo
        )
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))  # Проверка соединения
            await conn.run_sync(Base.metadata.create_all)
        Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
        logger.info("Соединение к БД успешно проверено.")
        return engine, Sessionmaker

    def setup_bot(self) -> Bot:
        bot = Bot(
            token=self.config.tg_bot.token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML, link_preview_is_disabled=True
            ),
        )
        self.bot = bot
        return bot

    async def setup_dispatcher(self) -> Dispatcher:
        redis = Redis(
            host=self.config.redis_config.host,
            port=self.config.redis_config.port,
            db=self.config.redis_config.db,
            password=self.config.redis_config.password,
        )
        storage = RedisStorage(
            redis,
            key_builder=DefaultKeyBuilder(
                    separator="_", with_destiny=True, with_bot_id=True
            ))
            # если нужен параметр redis, добавьте его здесь
        dp = Dispatcher(storage=storage)
        self.dp = dp
        return dp

    def make_i18n_middleware(self) -> I18nMiddleware:
        # Получаем абсолютный путь к папке locales/ru
        locales_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),  # подняться на уровень выше (app/)
            "locales"
        )
        loader = FluentResourceLoader(
            os.path.join(locales_dir, "{locale}")
        )
        l10ns = {
            locale: FluentLocalization(
                [locale, self.DEFAULT_LOCALE],
                ["txt.ftl"],  # имя файла локализации
                loader,
            )
            for locale in self.LOCALES
        }
        return I18nMiddleware(l10ns, self.DEFAULT_LOCALE)

    
    def register_middlewares_and_routers(
        self,
        dp: Dispatcher,
        Sessionmaker: async_sessionmaker[AsyncSession],
        config: Config,
    ):
        # Регистрируем миддлварь для i18n и бд
        i18n_middleware = self.make_i18n_middleware()
        dp.message.middleware(i18n_middleware)
        dp.update.middleware(i18n_middleware)
        dp.callback_query.middleware(i18n_middleware)
        dp.update.outer_middleware(DbSessionMiddleware(session_pool=Sessionmaker))
        dp.message.outer_middleware(TrackAllUsersMiddleware())

        # Регистриуем роутеры в диспетчере
        dp.include_router(commands_router)
        dp.include_routers(*get_dialogs())

        # Запускаем функцию настройки проекта для работы с диалогами
        bg_factory = setup_dialogs(dp)
        dp.workflow_data.update(bg_factory=bg_factory)

        # Регистрация хендлеров на ошибки
        dp.errors.register(
            on_unknown_intent,
            ExceptionTypeFilter(UnknownIntent),
        )
        dp.errors.register(
            on_unknown_state,
            ExceptionTypeFilter(UnknownState),
        )

    @staticmethod
    async def set_commands(bot: Bot):
        commands = [BotCommand(command="/start", description="Запуск / Start")]
        await bot.set_my_commands(commands=commands)
