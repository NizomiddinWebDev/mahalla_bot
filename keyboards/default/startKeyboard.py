from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek tili"),
            KeyboardButton(text="🇷🇺 Русский язык")
        ]
    ],
    resize_keyboard=True
)

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact yuborish", request_contact=True)
        ]
    ],
resize_keyboard=True
)

contact_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="отправит", request_contact=True)
        ]
    ],
resize_keyboard=True
)
