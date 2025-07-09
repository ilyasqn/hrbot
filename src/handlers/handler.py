from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.keyboards import main

router = Router()


@router.message(CommandStart(), F.chat.type == "private")
async def start(message: Message):
    await message.answer(
        "Привет! Я HR-бот и помогу тебе опубликовать вакансии, ивенты и прочее",
        reply_markup=main.kb
    )
