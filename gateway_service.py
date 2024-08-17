import logging
from enum import Enum

import requests

import config

logging = logging.getLogger("app")

page_url = config.GATEWAY_URL + "/page"
book_url = config.GATEWAY_URL + "/book"
headers = {'Content-Type': 'application/json'}


class Status(Enum):
    OK = 1
    ERROR = 2


def save_page(page):
    try:
        payload = {'service': 'telegram', 'page': page}
        response = requests.post(page_url, json=payload, headers=headers)
        if response.status_code == 200:
            logging.debug(str(response))
            return Status.OK
        else:
            logging.error(response.status_code)
            return Status.ERROR
    except requests.RequestException as e:
        return Status.ERROR


def get_page_link():
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            logging.debug(str(response))
            return response.text
        else:
            logging.error(response.status_code)
            return Status.ERROR
    except requests.RequestException as e:
        return Status.ERROR


def get_all_books():
    try:
        response = requests.get(book_url + "/all")
        if response.status_code == 200:
            logging.debug(str(response))
            return response.text
        else:
            logging.error(response.status_code)
            return Status.ERROR
    except requests.RequestException as e:
        return Status.ERROR
