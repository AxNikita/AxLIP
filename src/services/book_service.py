class BookService:

    def __init__(self, log, book_repository):
        self.log = log
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all_books()

    def get_current_book(self):
        return self.book_repository.get_current_book()

    def save_page(self, page):
        return self.book_repository.save_page(page)
