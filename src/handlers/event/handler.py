from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states.event import EventForm

router = Router()


@router.message(F.text == "Опубликовать event")
async def publish_event(message: Message, state: FSMContext):
    await message.answer("Название event")
    await state.set_state(EventForm.name)

