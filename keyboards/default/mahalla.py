from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.all_data import mahalla


async def mahalla_btn():
    btn = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    btn.add(*(KeyboardButton(item) for item in mahalla.values()))
    btn.add(KeyboardButton("ortga"))
    return btn

aloqa_btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖇️ Bog'lanish")],
        [KeyboardButton(text="🔙ortga")]
    ],
    resize_keyboard=True
)