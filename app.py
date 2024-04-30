import asyncio

from handlers.users.echo import echo_router
from handlers.users.start import start_router
from loader import dp, bot


async def main():
	dp.include_routers(
		start_router,
		echo_router
	)
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main(), debug=True)
	