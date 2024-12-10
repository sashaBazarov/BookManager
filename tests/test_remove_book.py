import unittest
from unittest.mock import patch, MagicMock
from commands.remove_book import remove_book

class TestRemoveBook(unittest.TestCase):
    @patch('commands.remove_book.find_book')
    @patch('commands.remove_book.delete_book')
    def test_remove_existing_book(self, mock_delete_book, mock_find_book):
        mock_book = MagicMock()
        mock_book.id = "123456"
        mock_find_book.return_value = mock_book

        remove_book("123456")

        mock_find_book.assert_called_once_with("123456")
        mock_delete_book.assert_called_once_with(mock_book)

    @patch('commands.remove_book.find_book')
    def test_remove_nonexistent_book(self, mock_find_book):
        mock_find_book.return_value = None

        with self.assertRaises(ValueError) as context:
            remove_book("999999")
        self.assertEqual(str(context.exception), "Book with id 999999 not found.")

        mock_find_book.assert_called_once_with("999999")

    @patch('commands.remove_book.find_book')
    @patch('commands.remove_book.delete_book')
    def test_remove_book_output(self, mock_delete_book, mock_find_book):
        mock_book = MagicMock()
        mock_book.id = "123456"
        mock_find_book.return_value = mock_book

        with patch('builtins.print') as mock_print:
            remove_book("123456")
            mock_print.assert_called_once_with("Book with id 123456 has been deleted.")

if __name__ == "__main__":
    unittest.main()
