from sqlalchemy import select
from sqlalchemy.orm import Session

from src.repository.entity.book_entity import BookBase


class BookRepository:

    def __init__(self, engine):
        self.engine = engine

    def get_all_books(self):
        with Session(self.engine) as session:
            statement = select(BookBase)
            all_books = session.scalars(statement).all()
            return all_books

    def get_current_book(self):
        with Session(self.engine) as session:
            statement = select(BookBase).where(BookBase.priority == 1)
            most_priority_book = session.scalars(statement).first()
            book_directory = self.get_book_directory()
            page_link = f"{book_directory}{most_priority_book.book_link}#page={most_priority_book.book_page}"
            current_book = {
                'book_name': most_priority_book.book_name,
                'book_img_link': most_priority_book.book_img_link,
                'book_page': most_priority_book.book_page,
                'page_link': page_link
            }
            return current_book

    def save_page(self, page):
        with Session(self.engine) as session:
            statement = select(BookBase).where(BookBase.priority == 1)
            most_priority_book = session.scalars(statement).first()
            most_priority_book.book_page = page
            session.commit()
            return most_priority_book

    def get_book_directory(self):
        return "http://localhost:8080/"
