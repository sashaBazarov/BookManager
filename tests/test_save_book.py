import unittest
from unittest.mock import patch, mock_open, MagicMock
from json_io.save_book import save_book
from json_io.books_directory import BOOKS_DIRECTORY
from book import Book


class TestSaveBook(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_save_book_success(self, mock_open):
        mock_book = MagicMock()
        mock_book.id = "123"
        mock_book.to_json.return_value = '{"id": "123", "title": "Test Book", "author": "Author1", "year": "2023"}'

        save_book(mock_book)

        mock_open.assert_called_once_with(f"{BOOKS_DIRECTORY}/{mock_book.id}.json", "w+", encoding="utf-8")
        mock_open().write.assert_called_once_with(mock_book.to_json())

    @patch("builtins.open", side_effect=IOError("Unable to write to file"))
    def test_save_book_io_error(self, mock_open):
        mock_book = MagicMock()
        mock_book.id = "123"
        mock_book.to_json.return_value = '{"id": "123", "title": "Test Book", "author": "Author1", "year": "2023"}'

        with self.assertRaises(IOError) as context:
            save_book(mock_book)

        self.assertEqual(str(context.exception), "Unable to write to file")
        mock_open.assert_called_once_with(f"{BOOKS_DIRECTORY}/{mock_book.id}.json", "w+", encoding="utf-8")
