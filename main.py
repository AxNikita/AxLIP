import asyncio
import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters.command import CommandStart

import config

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("ping"))
async def cmd_ping(message: types.Message):
    await message.answer("pong")


@dp.message(lambda message: re.fullmatch(r'^\d+$', message.text))
async def cmd_number(message: types.Message):
    try:
        num = int(message.text)
        await message.answer(message.from_user.username + " SEND: " + str(num))
    except Exception:
        logging.error("ERROR")


async def main():
    bot = Bot(token=config.TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
