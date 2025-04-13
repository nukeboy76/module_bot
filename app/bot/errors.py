from aiogram import types

async def on_callback_error(update: types.Update, exception):
    print(f"Ошибка в callback: {exception}")
