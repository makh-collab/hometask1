from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Yes'), 
        KeyboardButton(text='No')]
    ], resize_keyboard=True, one_time_keyboard=True
)
