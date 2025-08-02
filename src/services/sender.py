import aiohttp
from aiogram import Bot
from src.configs.bot import bot_settings
from src.configs.backend import backend_settings
from src.services.formatter import Formatter


class Sender:
    bot = Bot(token=bot_settings.TOKEN)

    @classmethod
    async def send_vacancy(cls, data: dict):
        title = "📝 Новая вакансия"
        text = await Formatter.format_vacancy(data)
        await cls._send_to_channel(title, text, data)

    @classmethod
    async def send_event(cls, data: dict):
        title = "📣 Новое мероприятие"
        text = await Formatter.format_event(data)
        await cls._send_to_channel(title, text, data)

    @classmethod
    async def _send_to_channel(cls, title: str, text: str, data: dict):
        text = f"{title}\n\n{text}"
        await cls.bot.send_message(chat_id=bot_settings.CHANNEL_ID, text=text)
        # async with aiohttp.ClientSession() as session:
        #     await session.post(backend_settings.URL, json=data)
