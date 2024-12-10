from find_book import find_book
from json_io import delete_book


def remove_book(book_id: str):
    """
    Удалить задачу по её ID.

    Аргументы:
        book_id (int): ID задачи, которую нужно удалить.

    Исключения:
        ValueError: Если задача с данным ID не найдена.

    Возвращает:
        None
    """
    book = find_book(book_id)
    if not book:
        raise ValueError(f"Book with id {book_id} not found.")
    delete_book(book)
    print(f"Book with id {book.id} has been deleted.")
