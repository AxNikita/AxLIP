from aiogram import Bot, Dispatcher

from src.configuration import env_config
from src.configuration.keyboard_config import KeyboardConfiguration
from src.configuration.logging_config import LoggerConfiguration
from src.controller.telegram_controller import TelegramController
from src.repository.postgres_repository import PostgresTemplate
from src.services.book_service import BookService


# ============ Config your dependencies here ============


def bean_aiogram_dispatcher():
    return Dispatcher()


def bean_aiogram_bot():
    return Bot(token=env_config.TG_TOKEN)


def bean_keyboard_configuration():
    return KeyboardConfiguration()


def bean_application_logging_configuration():
    return LoggerConfiguration().init_logger()


def bean_postgres_template(log):
    return PostgresTemplate(log)


def bean_book_service(log, postgres_template):
    return BookService(log, postgres_template)


def bean_telegram_controller(log, dispatcher, keyboard_configuration, book_service):
    return TelegramController(log, dispatcher, keyboard_configuration, book_service)


# ============ Initialize your dependencies here ============

class Application:

    @staticmethod
    async def run():
        bot = bean_aiogram_bot()
        dispatcher = bean_aiogram_dispatcher()
        log_configuration = bean_application_logging_configuration()
        keyboard_configuration = bean_keyboard_configuration()
        postgres_template = bean_postgres_template(log_configuration)
        book_service = bean_book_service(log_configuration, postgres_template)
        tg_controller = bean_telegram_controller(log_configuration, dispatcher, keyboard_configuration, book_service)

        await dispatcher.start_polling(bot)

# ===========================================================
