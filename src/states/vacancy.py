from aiogram.fsm.state import StatesGroup, State


class VacancyForm(StatesGroup):
    position = State()
    company = State()
    company_link = State()
    company_description = State()
    city = State()
    salary_from = State()
    salary_to = State()
    experience = State()
    work_type = State()
    level = State()
    responsibilities = State()
    requirements = State()
    description = State()
    contacts = State()
    confirm_username = State()
