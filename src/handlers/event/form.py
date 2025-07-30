from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from src.states.event import EventForm
from src.services.sender import send_to_channel_and_backend
from datetime import datetime

router = Router()


@router.message(EventForm.name)
async def get_event_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Организатор / Компания:")
    await state.set_state(EventForm.company)


@router.message(EventForm.company)
async def get_event_company(message: types.Message, state: FSMContext):
    await state.update_data(company=message.text)
    await message.answer("Описание мероприятия:")
    await state.set_state(EventForm.description)


@router.message(EventForm.description)
async def get_event_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Дата мероприятия (в формате ДД.ММ.ГГГГ):")
    await state.set_state(EventForm.date)


@router.message(EventForm.date)
async def get_event_date(message: types.Message, state: FSMContext):
    text = message.text.strip()
    try:
        parsed_date = datetime.strptime(text, "%d.%m.%Y").date()
        await state.update_data(date=str(parsed_date))
    except ValueError:
        await message.answer("❗️ Неверный формат даты. Пожалуйста, введите в формате ДД.ММ.ГГГГ.")
        return

    await send_event_data(message, state)


async def send_event_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await send_to_channel_and_backend(data)
    await message.answer("✅ Событие успешно отправлено в it-nomads и скоро появится в канале!")
    await state.clear()
