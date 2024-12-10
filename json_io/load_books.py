import os
import json
from typing import Tuple
from book import Book
from .books_dirrctory import BOOKS_DIRECTORY

def load_books() -> Tuple[Book]:
    """
    Load books from JSON files in the specified directory.

    Returns:
        A tuple of Book objects representing the loaded books.
    """
    return tuple(
        book
        for file in os.listdir(BOOKS_DIRECTORY) if file.endswith(".json")
        for book in [load_book(os.path.join(BOOKS_DIRECTORY, file))]
        if book is not None
    )


def load_book(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return Book(**json.load(f))
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error loading book from '{file_path}': {e}")
        return None
    