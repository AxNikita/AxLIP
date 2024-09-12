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
    logging.info("start command for = " + username)
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
    greeting = ("Привет " + username + " !\n\n"
                + "В этом боте только ты управляешь прогресом чтения своих книг.\n\n"
                + "Введи просто цифры страницы на которой остановился и я сохраню ее для тебя.")
    await message.answer(greeting, reply_markup=keyboard)


@dp.message(F.text.lower() == "📖")
async def cmd_current_book(message: types.Message):
    book = gateway_service.get_current_book()
    if book != gateway_service.Status.ERROR:
        book_name = book.get('book_name')
        book_page = book.get('book_page')
        book_img_link = book.get('book_img_link')
        page_link = config.GATEWAY_URL + book.get('page_link')
        html_message = f'<a href="{page_link}">Ссылка</a>'
        answer = ("✅ " + " Книга: " + book_name + "\n\n"
                  + "Страница: " + str(book_page) + "\n\n"
                  + html_message)
        await message.answer(answer, parse_mode='HTML')
    else:
        await message.answer("❌ " + " Не смогли получить ссылку на книгу, возникла ошибка!")


@dp.message(F.text.lower() == "📚")
async def cmd_get_all_books(message: types.Message):
    all_books = gateway_service.get_all_books()
    if all_books != gateway_service.Status.ERROR:
        answer = "✅ " + " Ваши книги:\n\n"

        for book in all_books:
            answer += book.get('book_name') + " : " + str(book.get('book_page')) + "\n"

        await message.answer(answer)
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
