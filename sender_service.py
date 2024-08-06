import logging

import requests

import config

logging = logging.getLogger("app")

url = config.GATEWAY_URL + "/page"
headers = {'Content-Type': 'application/json'}


def send_page(page):
    payload = {'service': 'telegram', 'page': page}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        logging.debug(str(response))
    else:
        logging.error(response.status_code)
