import unittest
from unittest.mock import patch, MagicMock
from commands.view_books import view_books


class TestViewBooks(unittest.TestCase):
    @patch('commands.view_books.load_books')
    @patch('commands.view_books.generate_table')
    @patch('builtins.print')
    def test_view_books_no_filters(self, mock_print, mock_generate_table, mock_load_books):
        mock_books = [
            MagicMock(to_table=lambda: ["Book1", "Author1", "2000", "Available", "1"]),
            MagicMock(to_table=lambda: ["Book2", "Author2", "2010", "Borrowed", "2"]),
        ]
        mock_load_books.return_value = mock_books
        mock_generate_table.return_value = "Generated Table"

        view_books()

        mock_load_books.assert_called_once()
        mock_generate_table.assert_called_once_with(
            [["Book1", "Author1", "2000", "Available", "1"], ["Book2", "Author2", "2010", "Borrowed", "2"]],
            ["Title", "Author", "Year", "Status", "ID"]
        )
        mock_print.assert_called_once_with("Generated Table")

    @patch('commands.view_books.load_books')
    @patch('commands.view_books.generate_table')
    @patch('builtins.print')
    def test_view_books_with_filters(self, mock_print, mock_generate_table, mock_load_books):
        mock_books = [
            MagicMock(to_table=lambda: ["Book1", "Author1", "2000", "Available", "1"]),
            MagicMock(to_table=lambda: ["Book2", "Author2", "2010", "Borrowed", "2"]),
        ]
        mock_load_books.return_value = mock_books

        with patch('commands.view_books.filter_books', return_value=[mock_books[0]]) as mock_filter_books:
            mock_generate_table.return_value = "Filtered Table"

            view_books(author="Author1")

            mock_filter_books.assert_called_once_with(mock_books, "Author1", None, None)
            mock_generate_table.assert_called_once_with(
                [["Book1", "Author1", "2000", "Available", "1"]],
                ["Title", "Author", "Year", "Status", "ID"]
            )
            mock_print.assert_called_once_with("Filtered Table")

    @patch('commands.view_books.load_books')
    @patch('builtins.print')
    def test_view_books_no_books(self, mock_print, mock_load_books):
        mock_load_books.return_value = []

        with patch('commands.view_books.filter_books', return_value=[]) as mock_filter_books:
            view_books(author="NonExistentAuthor")

            mock_filter_books.assert_called_once_with([], "NonExistentAuthor", None, None)
            mock_print.assert_called_once_with("No books found.")

if __name__ == "__main__":
    unittest.main()
