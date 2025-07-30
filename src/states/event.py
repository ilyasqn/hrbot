from aiogram.fsm.state import StatesGroup, State


class EventForm(StatesGroup):
    name = State()
    company = State()
    description = State()
    date = State()