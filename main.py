import asyncio
import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters.command import CommandStart

import config
import sender_service

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("ping"))
async def cmd_ping(message: types.Message):
    await message.answer("pong")


@dp.message(lambda message: re.fullmatch(r'^\d+$', message.text))
async def cmd_page(message: types.Message):
    try:
        page = int(message.text)
        sender_service.send_page(page)
        await message.answer(message.from_user.username + " мы сохранили вашу страницу!")
    except (ValueError, TypeError):
        logging.error("ERRRROOOR")


async def main():
    bot = Bot(token=config.TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
