from datetime import datetime
from uuid import uuid1
from book import Book
from json_io import save_book
from find_book import find_book


def add_book(title: str, author: str, year: str):
    book: Book = Book(get_id(), title, author, year)
    save_book(book)
    
    print("Book added successfully!")

def get_id():
    """
    Генерирует уникальный идентификатор книги длиной 6 символов.

    Эта функция генерирует уникальный идентификатор книги, создавая UUID и 
    беря первые 6 символов. Она гарантирует уникальность идентификатора, 
    проверяя его по существующим идентификаторам задач и регенерируя при необходимости.

    Возвращает:
        str: Уникальный идентификатор книги длиной 6 символов.
    """

    while find_book(book_id := str(uuid1())[:6]):
        pass
    return book_id
