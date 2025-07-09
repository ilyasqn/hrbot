from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Да")]],
    resize_keyboard=True,
    one_time_keyboard=True
)
