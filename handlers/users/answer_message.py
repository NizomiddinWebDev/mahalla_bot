from aiogram import types

from filters.private_chat_filter import IsPrivate
from loader import dp, bot
from utils.db_api.model import get_user_name


@dp.message_handler(IsPrivate())
async def answer_user(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            await message.bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            try:
                user = await get_user_name(full_name=message.reply_to_message.forward_sender_name)
                await message.bot.send_message(user.tg_user_id, message.text)
            except:
                await message.answer("<b>Bu foydalanuvchining Maxfiylik sozlamalari tufayli xabar yuborib bo'lmadi!</b>")

