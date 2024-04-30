from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

start_router = Router()


@start_router.message(CommandStart())
async def welcome(message: Message):
	
	await message.reply(text=f"Salom {message.from_user.first_name}!", parse_mode=ParseMode.HTML)
