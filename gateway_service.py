import logging
from enum import Enum

import requests

import config

logging = logging.getLogger("app")

url = config.GATEWAY_URL + "/page"
headers = {'Content-Type': 'application/json'}


class Status(Enum):
    OK = 1
    ERROR = 2


def save_page(page):
    try:
        payload = {'service': 'telegram', 'page': page}
        response = requests.post(url, json=payload, headers=headers)
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
        response = requests.get(url)
        if response.status_code == 200:
            logging.debug(str(response))
            return response.text
        else:
            logging.error(response.status_code)
            return Status.ERROR
    except requests.RequestException as e:
        return Status.ERROR
