import re as regular_expression

from aiogram import F
from aiogram.filters.command import CommandStart
from aiogram.types import Message

import src.utils.answer_util as answer_util
from src.utils.status_util import Status


def get_username(message):
    return message.from_user.username


class TelegramController:

    def __init__(self, log, dispatcher, keyboard_configuration, book_service):
        self.log = log
        self.book_service = book_service
        self.keyboard_configuration = keyboard_configuration
        self.initialize_handlers(dispatcher)

    def initialize_handlers(self, dispatcher):
        dispatcher.message(CommandStart())(self.cmd_start)
        dispatcher.message(F.text.lower() == "📖")(self.cmd_current_book)
        dispatcher.message(F.text.lower() == "📚")(self.cmd_get_all_books)
        dispatcher.message(lambda message: regular_expression.fullmatch(r'^\d+$', message.text))(self.cmd_save_page)

    async def cmd_start(self, message: Message):
        username = get_username(message)
        self.log.info("start command for = " + username)
        answer = answer_util.answer_response_for_start_cmd(username)
        await message.answer(answer, reply_markup=self.keyboard_configuration.get_keyboard())

    async def cmd_current_book(self, message: Message):
        username = get_username(message)
        self.log.info("current book command for = " + username)
        book = self.book_service.get_current_book()
        if book != Status.ERROR:
            answer = answer_util.answer_response_for_current_book_cmd(book)
            await message.answer(answer, parse_mode='HTML')
        else:
            answer = answer_util.wrong_answer_response_for_current_book()
            await message.answer(answer)

    async def cmd_get_all_books(self, message: Message):
        username = get_username(message)
        self.log.info("all books command for = " + username)
        all_books = self.book_service.get_all_books()
        if all_books != Status.ERROR:
            answer = answer_util.answer_response_for_all_books_cmd(all_books)
            await message.answer(answer)
        else:
            answer = answer_util.wrong_answer_response_for_all_books_cmd()
            await message.answer(answer)

    async def cmd_save_page(self, message: Message):
        username = get_username(message)
        self.log.info("save page command for = " + username)
        status = self.book_service.save_page(int(message.text))
        if status != Status.ERROR:
            answer = answer_util.answer_response_for_save_page_cmd()
            await message.answer(answer)
        else:
            answer = answer_util.wrong_answer_response_for_save_page_cmd()
            await message.answer(answer)
