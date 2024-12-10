import unittest
from unittest.mock import patch, mock_open
from json_io.load_books import load_books, load_book
from json_io.books_directory import BOOKS_DIRECTORY
from book import Book
import os


class TestLoadBooks(unittest.TestCase):
    @patch("os.listdir")
    @patch("json_io.load_books.load_book")
    def test_load_books_success(self, mock_load_book, mock_listdir):
        mock_listdir.return_value = ["book1.json", "book2.json"]
        mock_load_book.side_effect = [
            Book(id="1", title="Book1", author="Author1", year="2023"),
            Book(id="2", title="Book2", author="Author2", year="2022"),
        ]

        books = load_books()

        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Book1")
        self.assertEqual(books[1].author, "Author2")
        mock_listdir.assert_called_once()
        mock_load_book.assert_any_call(os.path.join(BOOKS_DIRECTORY, "book1.json"))
        mock_load_book.assert_any_call(os.path.join(BOOKS_DIRECTORY, "book2.json"))

    @patch("builtins.open", new_callable=mock_open, read_data='{"id": "1", "title": "Test Book", "author": "Author1", "year": "2023"}')
    def test_load_book_success(self, mock_open):
        book = load_book("fake_path.json")

        self.assertIsNotNone(book)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.year, "2023")

    @patch("builtins.open", new_callable=mock_open, read_data="Invalid JSON")
    def test_load_book_invalid_json(self, mock_open):
        book = load_book("fake_path.json")

        self.assertIsNone(book)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_book_file_not_found(self, mock_open):
        book = load_book("nonexistent_path.json")

        self.assertIsNone(book)

