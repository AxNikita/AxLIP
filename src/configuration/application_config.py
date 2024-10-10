from aiogram import Bot, Dispatcher

from src.configuration import env_config
from src.configuration.keyboard_config import KeyboardConfiguration
from src.configuration.logging_config import LoggerConfiguration
from src.configuration.postgres_configuration import PostgresConfiguration
from src.controller.telegram_controller import TelegramController
from src.repository.book_repository import BookRepository
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


def bean_postgres_configuration():
    return PostgresConfiguration()


def bean_book_repository(engine):
    return BookRepository(engine)


def bean_book_service(log, book_repository):
    return BookService(log, book_repository)


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
        postgres_configuration = bean_postgres_configuration()
        book_repository = bean_book_repository(postgres_configuration.get_engine())
        book_service = bean_book_service(log_configuration, book_repository)
        tg_controller = bean_telegram_controller(log_configuration, dispatcher, keyboard_configuration, book_service)

        await dispatcher.start_polling(bot)

# ===========================================================
