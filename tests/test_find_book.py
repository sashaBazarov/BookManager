import unittest
from unittest.mock import patch, MagicMock
from find_book import find_book
from book import Book


class TestFindBook(unittest.TestCase):
    @patch("find_book.load_books")
    def test_find_book_exists(self, mock_load_books):
        mock_books = [
            MagicMock(id="1", title="Book One"),
            MagicMock(id="2", title="Book Two"),
        ]
        mock_load_books.return_value = mock_books

        book = find_book("1")

        self.assertIsNotNone(book)
        self.assertEqual(book.id, "1")
        self.assertEqual(book.title, "Book One")

    @patch("find_book.load_books")
    def test_find_book_not_exists(self, mock_load_books):
        mock_books = [
            MagicMock(id="1", title="Book One"),
            MagicMock(id="2", title="Book Two"),
        ]
        mock_load_books.return_value = mock_books

        book = find_book("3")

        self.assertIsNone(book)

    @patch("find_book.load_books")
    def test_find_book_empty_collection(self, mock_load_books):
        mock_load_books.return_value = []

        book = find_book("1")

        self.assertIsNone(book)

