import logging
from aiogram import Router
from aiogram.types import Message

echo_router = Router()


@echo_router.message()
async def echo(message: Message):
	try:
		await message.send_copy(chat_id=message.from_user.id)
	except Exception as e:
		logging.exception(e)
		await message.answer("Ma'lumot turi aniqlanmadi.")
		