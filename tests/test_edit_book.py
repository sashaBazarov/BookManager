import unittest
from unittest.mock import patch, MagicMock
from commands.edit_book import edit_book
from exceptions.commandexception import CommandException

class TestEditBook(unittest.TestCase):
    @patch('commands.edit_book.find_book')
    @patch('commands.edit_book.save_book')
    def test_edit_book_success(self, mock_save_book, mock_find_book):

        mock_book = MagicMock()
        mock_book.get_attrs.return_value = {"title": "old title", "author": "old author", "year": "2000"}
        mock_find_book.return_value = mock_book

        edit_book("123456", title="new title", author="new author")

        mock_book.get_attrs.assert_called_once()
        mock_book.title = "new title"
        mock_book.author = "new author"
        mock_save_book.assert_called_once_with(mock_book)

    @patch('commands.edit_book.find_book')
    def test_edit_book_not_found(self, mock_find_book):
        mock_find_book.return_value = None

        with self.assertRaises(ValueError) as context:
            edit_book("123456", title="new title")
        self.assertEqual(str(context.exception), "Book 123456 not found")

    @patch('commands.edit_book.find_book')
    def test_edit_book_invalid_attribute(self, mock_find_book):
        mock_book = MagicMock()
        mock_book.get_attrs.return_value = {"title": "old title", "author": "old author", "year": "2000"}
        mock_find_book.return_value = mock_book

        with self.assertRaises(ValueError) as context:
            edit_book("123456", invalid_attr="value")
        self.assertEqual(str(context.exception), "Invalid attribute: invalid_attr")

    def test_edit_book_no_arguments(self):
        with self.assertRaises(CommandException) as context:
            edit_book("123456")
        self.assertIn("No required arguments", str(context.exception))
