import logging

import psycopg2
from psycopg2 import sql

logging = logging.getLogger("app")

conn_params = {
    'dbname': 'postgres',
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432'
}


class DBUtils:

    def __init__(self):
        self.connection = psycopg2.connect(**conn_params)
        self.cursor = self.connection.cursor()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        columns = [desc[0] for desc in self.cursor.description]
        books = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        logging.info(f"All books: {books}")
        return books

    def get_current_book(self):
        self.cursor.execute("SELECT * FROM books ORDER BY priority LIMIT 1")
        most_priority_book = dict(zip([desc[0] for desc in self.cursor.description], self.cursor.fetchone()))
        book_directory = self.get_book_directory()
        page_link = f"{book_directory}{most_priority_book['book_link']}#page={most_priority_book['book_page']}"
        current_book = {
            'book_name': most_priority_book['book_name'],
            'book_img_link': most_priority_book['book_img_link'],
            'book_page': most_priority_book['book_page'],
            'page_link': page_link
        }
        logging.info(f"Current book: {current_book}")
        return current_book

    def save_page(self, page):
        self.cursor.execute("SELECT * FROM books ORDER BY priority LIMIT 1")
        most_priority_book = dict(zip([desc[0] for desc in self.cursor.description], self.cursor.fetchone()))
        self.cursor.execute(
            sql.SQL("UPDATE books SET book_page = %s WHERE book_id = %s RETURNING *"),
            [page, most_priority_book['book_id']]
        )
        updated_book = dict(zip([desc[0] for desc in self.cursor.description], self.cursor.fetchone()))
        self.connection.commit()
        logging.info(f"Page is saved! {updated_book}")
        return updated_book

    def get_book_directory(self):
        return "http://localhost:8080/"

    def __del__(self):
        self.cursor.close()
        self.connection.close()
