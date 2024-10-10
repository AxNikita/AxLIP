import psycopg2
from psycopg2 import sql

connection_params = {
    'dbname': 'postgres',
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432'
}


class PostgresTemplate:

    def __init__(self, log):
        self.log = log
        self.connection = psycopg2.connect(**connection_params)
        self.cursor = self.connection.cursor()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.map_to_list_books()
        self.log.info(f"All books: {books}")
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
        self.log.info(f"Current book: {current_book}")
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
        self.log.info(f"Page is saved! {updated_book}")
        return updated_book

    def map_to_list_books(self):
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_book_directory(self):
        return "http://localhost:8080/"

    def __del__(self):
        self.cursor.close()
        self.connection.close()
