from aiogram import types
from loader import dp


@dp.message_handler(text='/price')
async def bot_products(message: types.Message):
    with open('files/price.txt', 'r', encoding='utf8') as file:
        text = file.read()
        await message.answer(text)