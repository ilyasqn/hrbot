from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from src.states.vacancy import VacancyForm
from src.services.sender import send_to_channel_and_backend
from src.keyboards.vacancy import kb
from src.keyboards import base

router = Router()


@router.message(VacancyForm.position)
async def get_position(message: types.Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("Компания")
    await state.set_state(VacancyForm.company)


@router.message(VacancyForm.company)
async def get_company(message: types.Message, state: FSMContext):
    await state.update_data(company=message.text)
    await message.answer("Адрес(ссылка) компании (для пропуска отправьте '-')")
    await state.set_state(VacancyForm.company_link)


@router.message(VacancyForm.company_link)
async def get_company_link(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text == '-':
        await state.update_data(company_link=None)
    else:
        await state.update_data(company_link=text)
    await message.answer("О компании (для пропуска отправьте '-')")
    await state.set_state(VacancyForm.company_description)


@router.message(VacancyForm.company_description)
async def get_company_description(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text == '-':
        await state.update_data(company_description=None)
    else:
        await state.update_data(company_description=text)
    await message.answer("Локация:", reply_markup=kb.location_kb)
    await state.set_state(VacancyForm.city)


@router.message(VacancyForm.city)
async def get_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("Зарплата от: ")
    await state.set_state(VacancyForm.salary_from)


@router.message(VacancyForm.salary_from)
async def get_salary_from(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if not text.isdigit():
        await message.answer("Пожалуйста, введите зарплату только числом")
        return
    await state.update_data(salary_from=int(text))
    await message.answer("Зарплата до: ")
    await state.set_state(VacancyForm.salary_to)


@router.message(VacancyForm.salary_to)
async def get_salary_to(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if not text.isdigit():
        await message.answer("Пожалуйста, введите зарплату только числом")
        return
    await state.update_data(salary_to=int(text))
    await message.answer("Опыт в годах: ", reply_markup=kb.experience_kb)
    await state.set_state(VacancyForm.experience)


@router.message(VacancyForm.experience)
async def get_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await message.answer("Формат работы:", reply_markup=kb.work_type_kb)
    await state.set_state(VacancyForm.work_type)


@router.message(VacancyForm.work_type)
async def get_work_type(message: types.Message, state: FSMContext):
    await state.update_data(work_type=message.text)
    await message.answer("Уровень:", reply_markup=kb.level_kb)
    await state.set_state(VacancyForm.level)


@router.message(VacancyForm.level)
async def get_level(message: types.Message, state: FSMContext):
    await state.update_data(level=message.text)
    await message.answer("Обязанности:")
    await state.set_state(VacancyForm.responsibilities)


@router.message(VacancyForm.responsibilities)
async def get_responsibilities(message: types.Message, state: FSMContext):
    await state.update_data(responsibilities=message.text)
    await message.answer("Требования:")
    await state.set_state(VacancyForm.requirements)


@router.message(VacancyForm.requirements)
async def get_requirements(message: types.Message, state: FSMContext):
    await state.update_data(requirements=message.text)
    await message.answer("Дополнительно:")
    await state.set_state(VacancyForm.description)


@router.message(VacancyForm.description)
async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    if message.from_user.username:
        await state.set_state(VacancyForm.confirm_username)
        await message.answer(
            f"Контакты:\n"
            f"Можем оставить ваш Telegram username: @{message.from_user.username}?\n"
            f"Или введите другой контакт (например, номер или email).",
            reply_markup=base.kb
        )
    else:
        await state.set_state(VacancyForm.contacts)
        await message.answer("Пожалуйста, введите ваш контакт (например, телефон или email):")


@router.message(VacancyForm.confirm_username)
async def handle_confirm_username(message: types.Message, state: FSMContext):
    if message.text.strip().lower() == "да":
        await state.update_data(contacts=f"@{message.from_user.username}")
    else:
        await state.update_data(contacts=message.text)

    await send_data(message=message, state=state)


async def send_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await send_to_channel_and_backend(data)
    await message.answer("✅ Данные отправлены в it-nomads и скоро опубликуются на канале!в Спасибо.")
    await state.clear()
