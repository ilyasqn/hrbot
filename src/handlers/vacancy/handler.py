from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states.vacancy import VacancyForm

router = Router()


@router.message(F.text == "Опубликовать вакансию")
async def publish_vacancy(message: Message, state: FSMContext):
    await message.answer("Введите должность")
    await state.set_state(VacancyForm.position)

