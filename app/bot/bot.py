from fluentogram import TranslatorHub
from app.config import Config, load_config
from .setup import DependeciesConfig

import logging


async def main():
    logger = logging.getLogger(__name__)
    logger.info("Bot starting...")
    config: Config = load_config()
    dependecies_config = DependeciesConfig(config)
    dp = await dependecies_config.setup_dispatcher()
    bot = dependecies_config.setup_bot()

    await dependecies_config.set_commands(bot)
    engine, Sessionmaker = await dependecies_config.setup_database()

    dependecies_config.register_middlewares_and_routers(
        dp=dp,
        Sessionmaker=Sessionmaker,
        config=config,
    )
    await dp.start_polling(bot)
