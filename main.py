import asyncio
import logging
import re

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import KeyboardButton

import config
import gateway_service
import logging_config

dp = Dispatcher()
logging_config.setup_logging()
logging = logging.getLogger("app")


def get_username(message):
    return message.from_user.username


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    username = get_username(message)
    logging.info("start command = " + username)
    kb = [
        [
            KeyboardButton(text="📖"),
            KeyboardButton(text="📚")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Введите вашу страницу"
    )
    await message.answer("Привет " + username + " !", reply_markup=keyboard)


@dp.message(F.text.lower() == "📖")
async def cmd_get_page(message: types.Message):
    page_link = gateway_service.get_page_link()
    if page_link != gateway_service.Status.ERROR:
        html_message = f'<a href="{page_link}">Ссылка</a>'
        await message.answer("✅ " + " Ваша ссылка на траницу в книге:\n\n" + html_message, parse_mode='HTML')
    else:
        await message.answer("❌ " + " Не смогли получить ссылку на книгу, возникла ошибка!")


@dp.message(F.text.lower() == "📚")
async def cmd_get_books(message: types.Message):
    all_books = gateway_service.get_all_books()
    if all_books != gateway_service.Status.ERROR:
        await message.answer("✅ " + " Ваши книги:\n\n" + all_books)
    else:
        await message.answer("❌ " + " Не смогли получить книги из вашей библиотеки, возникла ошибка!")


@dp.message(lambda message: re.fullmatch(r'^\d+$', message.text))
async def cmd_save_page(message: types.Message):
    page = int(message.text)
    logging.info("page = " + str(page))
    status = gateway_service.save_page(page)
    if status == gateway_service.Status.OK:
        await message.answer("✅ " + " Страница сохранена!")
    else:
        await message.answer("❌ " + " Не смогли сохранить вашу страницу, возникла ошибка!")


async def main():
    bot = Bot(token=config.TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
