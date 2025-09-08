import asyncio
import logging

from app.bot import bot

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
    "%(lineno)d - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    asyncio.run(bot.main())


