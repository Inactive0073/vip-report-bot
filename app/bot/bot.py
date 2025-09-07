from fluentogram import TranslatorHub
from app.utils import (
    create_translator_hub
)
from app.config import Config, load_config
from .setup import DependeciesConfig

async def main():
    config: Config = load_config()
    dependecies_config = DependeciesConfig(config)
    dp = await dependecies_config.setup_dispatcher()
    bot = dependecies_config.setup_bot()


    await dependecies_config.set_commands(bot)
    translator_hub: TranslatorHub = create_translator_hub()
    engine, Sessionmaker = await dependecies_config.setup_database()


    dependecies_config.register_middlewares_and_routers(
        dp=dp,
        Sessionmaker=Sessionmaker,
        translator_hub=translator_hub,
        config=config,
        )
    await dp.start_polling(bot)
    
