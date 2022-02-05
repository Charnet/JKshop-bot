from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("products", "Продукция"),
            types.BotCommand("price", "Прайс"),
            types.BotCommand("documents", "Документация"),
        ]
    )
