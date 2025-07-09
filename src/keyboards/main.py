from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Опубликовать вакансию')],
    [KeyboardButton(text='Инструкция по публикации')],
    [KeyboardButton(text='Опубликовать event')],
    [KeyboardButton(text='Помощь')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите действие')