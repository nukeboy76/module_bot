import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import settings
from bot.handlers import register_handlers
from database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    register_handlers(dp)

    await init_db()

    try:
        logger.info("Начало поллинга бота...")
        await dp.start_polling(bot)
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())