class BookService:

    def __init__(self, log, postgres_template):
        self.log = log
        self.postgres_template = postgres_template

    def get_all_books(self):
        return self.postgres_template.get_all_books()

    def get_current_book(self):
        return self.postgres_template.get_current_book()

    def save_page(self, page):
        return self.postgres_template.save_page(page)
