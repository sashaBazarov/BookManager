import unittest
from unittest.mock import patch, MagicMock
from json_io.delete_book import delete_book
from json_io.books_directory import BOOKS_DIRECTORY
from book import Book


class TestDeleteBook(unittest.TestCase):
    @patch("os.remove")
    @patch("os.path.exists", return_value=True)
    def test_delete_book_success(self, mock_exists, mock_remove):
        book = Book(id="123", title="Test Book", author="Author1", year="2023")

        delete_book(book)

        mock_exists.assert_called_once_with(f"{BOOKS_DIRECTORY}/{book.id}.json")
        mock_remove.assert_called_once_with(f"{BOOKS_DIRECTORY}/{book.id}.json")

    @patch("os.path.exists", return_value=False)
    def test_delete_book_not_found(self, mock_exists):
        book = Book(id="123", title="Test Book", author="Author1", year="2023")

        with self.assertRaises(ValueError) as context:
            delete_book(book)

        self.assertEqual(str(context.exception), "Book with id 123 does not exist.")
        mock_exists.assert_called_once_with(f"{BOOKS_DIRECTORY}/{book.id}.json")
