# AxLIP-telegram

## Запуск

Для того чтобы проект корректно запустился, необходимо выполнить следующие шаги:

1. **Собрать образ**:

    ```bash
    docker build -t ax-lip-telegram-app .
    ```

2. **Запустить контейнер**:

    ```bash
    docker run -it -e TG_TOKEN=$TOKEN --rm --name ax-lip-telegram-app ax-lip-telegram-app
    ```