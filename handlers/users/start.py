from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.callback_datas import command_callback
from keyboards.inline.start_buutons import mian_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=mian_keyboard)
    elif message.from_user.language_code == "kz":
        await message.answer(f'Сәлем, {message.from_user.full_name}!', reply_markup=mian_keyboard)
    else:
        await message.answer(f'Hello, {message.from_user.full_name}!', reply_markup=mian_keyboard)


# @dp.callback_query_handler(command_callback.filter(command="start"))
# async def