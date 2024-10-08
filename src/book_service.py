import logging
from enum import Enum

import db_utils

logging = logging.getLogger("app")

database = db_utils.DBUtils()


class Status(Enum):
    OK = 1
    ERROR = 2


def get_all_books():
    return database.get_all_books()


def get_current_book():
    return database.get_current_book()


def save_page(page):
    book_with_saved_page = database.save_page(page)
    if book_with_saved_page:
        return Status.OK
