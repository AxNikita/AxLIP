import logging
from enum import Enum

import requests

import config

logging = logging.getLogger("app")

book_url = config.GATEWAY_URL + "/book"
headers = {'Content-Type': 'application/json'}


class Status(Enum):
    OK = 1
    ERROR = 2


def save_page(page):
    try:
        payload = {'service': 'telegram', 'page': page}
        response = requests.post(book_url + "/savePage", json=payload, headers=headers)
        return check_response_and_return_status(response)
    except requests.RequestException:
        return Status.ERROR


def get_current_book():
    try:
        response = requests.get(book_url + "/current")
        return check_response(response).json()
    except requests.RequestException:
        return Status.ERROR


def get_all_books():
    try:
        response = requests.get(book_url + "/all")
        return check_response(response).json()
    except requests.RequestException:
        return Status.ERROR


def check_response_and_return_status(response):
    if response.status_code == 200:
        logging.debug(str(response))
        return Status.OK
    else:
        logging.error(response.status_code)
        return Status.ERROR


def check_response(response):
    if response.status_code == 200:
        logging.debug(str(response))
        return response
    else:
        logging.error(response.status_code)
        return Status.ERROR
