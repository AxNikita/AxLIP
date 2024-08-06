import asyncio
import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart

import config
import logging_config
import sender_service

dp = Dispatcher()
logging_config.setup_logging()
logging = logging.getLogger("app")


def get_username(message):
    return message.from_user.username


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    username = get_username(message)
    logging.info("start command = " + username)
    await message.answer("Hello " + username + " !")


@dp.message(lambda message: re.fullmatch(r'^\d+$', message.text))
async def cmd_page(message: types.Message):
    username = get_username(message)
    try:
        page = int(message.text)
        logging.info("page = " + str(page))
        sender_service.send_page(page)
        await message.answer(username + " мы сохранили вашу страницу!")
    except (ValueError, TypeError):
        logging.error("Ошибка конвертации текста в цифру = " + username)
        await message.answer(username + " мы не смогли сохранить вашу страницу, возникла ошибка!")


async def main():
    bot = Bot(token=config.TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
