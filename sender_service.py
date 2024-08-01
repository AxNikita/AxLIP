import requests
import config

url = config.GATEWAY_URL + "/page"

def send_page(page):
    payload = {'service': 'telegram', 'page': page}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Ошибка: {response.status_code}")
