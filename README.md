# AxLIP-telegram

**Проверка всех зависимостей**

   ```bash
   pip freeze
   ```

**Установка зависимостей**:

   ```bash
   pip install -r требования.txt
   ```

## Запуск проекта в контейнере

Можно локально создать файл .env и добавить в него переменную TG_TOKEN(Пункт 3)

Для того чтобы проект корректно запустился, необходимо выполнить следующие шаги:

1. **Собрать образ**:

    ```bash
    docker build -t ax-lip .
    ```

2. **Запустить контейнер**:

    ```bash
    docker run -it -e TG_TOKEN=$TOKEN --rm --name ax-lip ax-lip
    ```

3. **Переменная окружения в файле .env**:

   ```bash
   TG_TOKEN=token
   ```

# AxLIP

## Запуск приложения с базой данных

Для того чтобы Postgres корректно запустился, необходимо выполнить следующие шаги:

1. **Запустить сбор контейнеров**:

    ```bash
    docker-compose up -d
    ```

2. **Создать схему базы данных**:

   ```sql
   DROP TABLE IF EXISTS books;
   
   CREATE TABLE books (
   book_id SERIAL PRIMARY KEY,
   book_name VARCHAR(64) NOT NULL,
   book_description VARCHAR(255),
   book_link VARCHAR(128) NOT NULL,
   book_img_link VARCHAR(128),
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   priority bigint,
   book_page numeric
   ); 
   ```

3. **Тестовые данные для проверки**:

   ```sql
   INSERT INTO books (book_name, book_description, book_link, book_img_link, priority, book_page) VALUES
   ('Test book 1', 'Test description 1', 'https://test.com', 'https://test.com/img', 1, 1),
   ('Test book 2', 'Test description 2', 'https://test.com', 'https://test.com/img', 2, 2),
   ('Test book 3', 'Test description 3', 'https://test.com', 'https://test.com/img', 3, 3),
   ('Test book 4', 'Test description 4', 'https://test.com', 'https://test.com/img', 4, 4),
   ('Test book 5', 'Test description 5', 'https://test.com', 'https://test.com/img', 5, 5);
   ```