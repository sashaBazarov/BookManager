from json_io import load_books
from tables import generate_table
from .filter_books import filter_books


def view_books(category: str = None, author: str = None, year: str = None, keywords: str = None):
    """
    View books based on the specified filters.

    Args:
        category (str, optional): The category of the books. Defaults to None.
        author (str, optional): The author of the books. Defaults to None.
        year (str, optional): The year of publication of the books. Defaults to None.
        keywords (str, optional): Keywords to search for in the book titles. Defaults to None.

    Returns:
        None
    """

    books = load_books()
    # Фильтрует книги по аргументам
    filtered_books = list(map(lambda book: book.to_table(), filter_books(books, author, year, keywords)))

    headers = ["Title", "Author", "Year", "Status", "ID"]

    print(generate_table(filtered_books, headers)) #Выводим таблицу
