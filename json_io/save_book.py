from book import Book
from .books_directory import BOOKS_DIRECTORY


def save_book(book: Book):
    """
    Сохранить задачу в файл JSON.

    Аргументы:
        book (Book): Объект задачи, который нужно сохранить. Он должен иметь атрибут `id` и метод `to_json`.

    Исключения:
        IOError: Если произошла ошибка при записи в файл.
    """
    with open(f"{BOOKS_DIRECTORY}/{book.id}.json", "w+", encoding="utf-8") as f:
        f.write(book.to_json())
