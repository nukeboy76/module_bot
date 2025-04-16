from aiogram import Router, types
from aiogram.filters import Command
from app.bot.keyboards import main_menu_keyboard
from app.bot.services import get_welcome_message

router = Router()

@router.message(Command("start", "help"))
async def start_command(message: types.Message):
    welcome_text = get_welcome_message()
    await message.answer(welcome_text, reply_markup=main_menu_keyboard())
