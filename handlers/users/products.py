from aiogram import types
from loader import dp


@dp.message_handler(text='/products')
async def bot_products(message: types.Message):
    with open('files/products.txt', 'r', encoding='utf8') as file:
        text = file.read()
        await message.answer(text)
