from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from data.all_data import data_all
from data.config import ADMINS
from keyboards.default.startKeyboard import start_button, contact_button, contact_button_ru
from loader import dp, bot
from states.startState import StartState
from utils.db_api.model import new_user_add, setUserLang, getUserLang


@dp.message_handler(text="🇺🇿 O'zbek tili", state=StartState.langState)
async def lang_func(message: types.Message, state: FSMContext):
    try:
        await setUserLang(message.from_user.id, 'uz')
        text = f"<b>Telefon raqamingizni yuboring😉</b>"
        await message.answer(text, reply_markup=contact_button)
        await state.update_data({"lang": message.text})
        await StartState.phoneState.set()
    except:
        await message.answer("Xatolik yuz berdi qayta kiriting!")
        await state.finish()


@dp.message_handler(text="🇷🇺 Русский язык", state=StartState.langState)
async def lang_func(message: types.Message, state: FSMContext):
    try:
        await setUserLang(message.from_user.id, 'ru')
        text = f"<b>Отправьте пожалуйста номер телефона😉</b>"
        await message.answer(text, reply_markup=contact_button_ru)
        await state.update_data({"lang": message.text})
        await StartState.phoneState.set()
    except:
        await message.answer("Xatolik yuz berdi qayta kiriting!")
        await state.finish()


@dp.message_handler(content_types=['contact'], state=StartState.phoneState)
async def get_contacts(message: types.Message, state: FSMContext):
    await state.update_data({"phone": message.contact.phone_number})
    lang = await getUserLang(message.from_user.id)
    if lang.lang == "uz":
        text = data_all['uz']['first_name']
    else:
        text = data_all['ru']['first_name']
    await message.answer(f"{text}")
    await StartState.nameState.set()


@dp.message_handler(state=StartState.nameState)
async def get_name(message: types.Message, state: FSMContext):
    lang = await getUserLang(message.from_user.id)
    if lang.lang == "uz":
        text1 = data_all['uz']['register']
    else:
        text1 = data_all['ru']['register']
    data = await state.get_data()
    phone = data['phone']
    lang = data['lang']
    text = f"<b>Client:</b>{message.text}\n<b>Telegram:</b> @{message.from_user.username}\n<b>Telefon: </b>{phone}\n<b>Tanlangan til: </b>{lang}"
    await bot.send_message(ADMINS[0], text)
    await message.answer(f"<b>{text1}</b>",reply_markup=ReplyKeyboardRemove())
    await state.finish()

