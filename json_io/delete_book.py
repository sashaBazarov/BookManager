from book import Book
import os
from .books_directory import BOOKS_DIRECTORY


def delete_book(book: Book):
    """
    Deletes a book from the specified directory.

    Args:
        book (Book): The book object to be deleted.

    Raises:
        ValueError: If the book with the specified ID does not exist.

    """
    path = f"{BOOKS_DIRECTORY}/{book.id}.json"

    if not os.path.exists(path):
        raise ValueError(f"Book with id {book.id} does not exist.")

    os.remove(path)
