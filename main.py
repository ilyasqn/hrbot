import asyncio
import logging

from aiogram import Bot, Dispatcher
from src.handlers.handler import router as start_router
from src.handlers.vacancy.handler import router as vacancy_router
from src.handlers.vacancy.form import router as vacancy_form
from src.configs.bot import bot_settings

bot = Bot(token=bot_settings.TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(vacancy_router)
    dp.include_router(vacancy_form)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
