def answer_response_for_start_cmd(username):
    answer = ("Привет " + username + " !\n\n"
              + "В этом боте только ты управляешь прогресом чтения своих книг.\n\n"
              + "Введи просто цифры страницы на которой остановился и я сохраню ее для тебя.")
    return answer


def answer_response_for_current_book_cmd(book):
    book_img_link = book.get('book_img_link')
    answer = ("✅  Книга: " + book.get('book_name') + "\n\n"
              + "Страница: " + str(book.get('book_page')) + "\n\n"
              + f'<a href="{book.get("page_link")}">Ссылка</a>')
    return answer


def wrong_answer_response_for_current_book():
    return "❌  Не смогли получить ссылку на книгу, возникла ошибка!"


def answer_response_for_all_books_cmd(all_books):
    answer = "✅  Ваши книги:\n\n"
    for book in all_books:
        answer += book.book_name + " : " + str(book.book_page) + "\n"
    return answer


def wrong_answer_response_for_all_books_cmd():
    return "❌  Не смогли получить книги из вашей библиотеки, возникла ошибка!"


def answer_response_for_save_page_cmd():
    return "✅  Страница сохранена!"


def wrong_answer_response_for_save_page_cmd():
    return "❌  Не смогли сохранить вашу страницу, возникла ошибка!"
