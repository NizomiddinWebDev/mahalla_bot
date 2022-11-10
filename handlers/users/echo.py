import re

from aiogram.types import ReplyKeyboardRemove

from keyboards.default.adminKeyboard import back
from keyboards.default.mahalla import aloqa_btn, mahalla_btn
from loader import bot
from aiogram.dispatcher import filters, FSMContext
from aiogram import types
from loader import dp
from data.all_data import mahalla, rais, phone, yil
from states.startState import AloqaState
from utils.db_api.model import get_user_name

REGEX = f""


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def allChat(message: types.Message, state: FSMContext):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            await message.bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await message.bot.send_message(user.chat_id, message.text)
            except:
                await message.answer(
                    "<b>Bu foydalanuvchining Maxfiylik sozlamalari tufayli xabar yuborib bo'lmadi!</b>")

    elif message.text in mahalla.values():
        value = [i for i in mahalla if mahalla[i] == message.text]
        text = f"<b>Yoshlar yetakchisi:</b> {rais.get(value[0])}\n<b>Tug'ilgan yili:</b> {yil.get(value[0])} yil\n<b>Phone:</b> {phone.get(value[0])}"
        await message.answer(text, reply_markup=aloqa_btn)
        await state.update_data({"key": value[0]})
        await AloqaState.aloqaState.set()
    elif message.text == "ortga":
        await message.answer("ortga qaytildi", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), state=AloqaState.aloqaState, text="🖇️ Bog'lanish")
async def allChat(message: types.Message, state: FSMContext):
    await message.answer("Habaringizni Yozing!", reply_markup=back)


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), state=AloqaState.aloqaState, text="🔙ortga")
async def allChat(message: types.Message, state: FSMContext):
    mahalla_bt = await mahalla_btn()
    await message.answer("Bosh Menu", reply_markup=mahalla_bt)
    await state.finish()


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), state=AloqaState.aloqaState)
async def allChat(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        key = data.get("key")
        await message.forward(1987938749)
        await message.answer("<b>Habaringiz yuborildi!\n\nhabar yubormasangiz pastdagi tugmani bosing!👇🏻</b>")
    except:
        await message.answer("<b>Habar yuborib bo'lmadi!</b>")