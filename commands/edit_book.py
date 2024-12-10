from find_book import find_book
from book import Book
from json_io import save_book
from exceptions import CommandException
from find_book import find_book


def edit_book(book_id: str, **kwargs):
    """
    Edit the attributes of a book.

    Args:
        book_id (str): The ID of the book to be edited.
        **kwargs: Keyword arguments representing the attributes to be edited.

    Raises:
        CommandException: If no required arguments are provided.
        ValueError: If the book with the given ID is not found or if an invalid attribute is provided.

    Returns:
        None
    """

    if not kwargs:
        raise CommandException("No required arguments", "editbook", **kwargs)

    book: Book = find_book(book_id)
    if not book:
        raise ValueError(f"Book {book_id} not found")
        return 

    attrs = book.get_attrs()

    for kwarg in kwargs:
        if kwarg not in attrs:
            raise ValueError(f"Invalid attribute: {kwarg}")
        setattr(book, kwarg, kwargs[kwarg])

    save_book(book)

    print("Book updated")
