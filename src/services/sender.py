import asyncio
import aiohttp
from aiogram import Bot
from src.configs.bot import bot_settings
from src.configs.backend import backend_settings

bot = Bot(token=bot_settings.TOKEN)

async def safe_line(emoji: str, label: str, value: str) -> str:
    return f"{emoji} {label}: {value}" if value else ""


async def send_to_channel_and_backend(data: dict):
    text = "\n".join(filter(None, [
        await safe_line("🧑‍💼", "Должность", data.get('position')),
        await safe_line("🏢", "Компания", data.get('company')),
        await safe_line("🔗", "Сайт компании", data.get('company_link')),
        await safe_line("🏙️", "Описание компании", data.get('company_description')),
        await safe_line("📍", "Локация", data.get('city')),
        f"💰 Зарплата: от {data.get('salary_from')} до {data.get('salary_to')}" if data.get("salary_from") and data.get(
            "salary_to") else "",
        await safe_line("📅", "Опыт", f"{data.get('experience')} лет" if data.get("experience") else ""),
        await safe_line("🧭", "Формат работы", data.get('work_type')),
        await safe_line("📈", "Уровень", data.get('level')),
        f"🧑‍💼 Обязанности:\n{data.get('responsibilities')}" if data.get("responsibilities") else "",
        f"📌 Требования:\n{data.get('requirements')}" if data.get("requirements") else "",
        f"📝 Описание:\n{data.get('description')}" if data.get("description") else "",
        await safe_line("📞", "Контакты", data.get('contacts')),
    ]))

    await bot.send_message(chat_id=bot_settings.CHANNEL_ID, text="Текст поста для канала")
    await bot.send_message(chat_id=bot_settings.CHANNEL_ID, text=text)
    await bot.send_message(chat_id=bot_settings.CHANNEL_ID, text="Json для отправки в бэк сайта")
    await bot.send_message(chat_id=bot_settings.CHANNEL_ID, text=str(data))

    # async with aiohttp.ClientSession() as session:
    #     await session.post(backend_settings.URL, json=data)
