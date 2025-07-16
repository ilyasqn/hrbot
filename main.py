import asyncio
import logging
import sys

import src.utils.logger
from aiogram import Bot, Dispatcher
from src.handlers.handler import router as start_router
from src.handlers.vacancy.handler import router as vacancy_router
from src.handlers.vacancy.form import router as vacancy_form
from src.configs.bot import bot_settings

logger = logging.getLogger(__name__)

bot = Bot(token=bot_settings.TOKEN)
logger.info("Bot is initializing...")
dp = Dispatcher()


async def main():
    try:
        logger.info("🔧 Initializing bot...")
        dp.include_router(start_router)
        dp.include_router(vacancy_router)
        dp.include_router(vacancy_form)
        logger.info("✅ Routers registered.")

        logger.info("🚀 Starting polling...")
        await dp.start_polling(bot)

    except KeyboardInterrupt:
        logger.warning("🛑 Bot stopped by user (KeyboardInterrupt)")
    except Exception as e:
        logger.exception(f"❌ Unexpected error: {e}")
        sys.exit(1)
    finally:
        logger.info("👋 Bot shutdown complete.")


if __name__ == '__main__':
    asyncio.run(main())
