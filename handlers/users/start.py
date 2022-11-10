from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from data.all_data import data_all
from keyboards.default.mahalla import mahalla_btn
from keyboards.default.startKeyboard import start_button
from loader import dp, bot
from states.startState import StartState
from utils.db_api.model import new_user_add, getUserLang


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def show_channels(message: types.Message):
    mahalla_bt = await mahalla_btn()
    text = f"<b>Assalomu alaykum! Parkent tumani mahallari bilan bog'lanish botiga hush kelibsiz\n\nMahallani tanlang👇🏻</b>"
    try:
        await new_user_add(message.from_user.id, 'user', 'true', message.from_user.full_name)
        await message.answer(text, reply_markup=mahalla_bt)
    except:
        await message.answer(text, reply_markup=mahalla_bt)

