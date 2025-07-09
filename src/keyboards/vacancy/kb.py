from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

work_type_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Удалённо")],
    [KeyboardButton(text="Офис")],
    [KeyboardButton(text="Гибрид")]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ввести свой вариант')

level_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Стажер")],
    [KeyboardButton(text="Junior")],
    [KeyboardButton(text="Middle")],
    [KeyboardButton(text="Senior")],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ввести свой вариант')

experience_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1+")],
    [KeyboardButton(text="3+")],
    [KeyboardButton(text="5+")],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ввести свой вариант')

location_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Алматы")],
    [KeyboardButton(text="Астана")],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ввести свой вариант')
