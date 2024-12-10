import unittest
from unittest.mock import patch
from commands.add_book import get_id

class TestGetID(unittest.TestCase):
    @patch('commands.add_book.find_book')
    def test_get_id_unique(self, mock_find_book):
        mock_find_book.side_effect = [True, False]

        result = get_id()
        self.assertEqual(len(result), 6)
        self.assertGreaterEqual(mock_find_book.call_count, 2)

    @patch('commands.add_book.find_book')
    def test_get_id_length(self, mock_find_book):
        mock_find_book.return_value = False

        result = get_id()
        self.assertEqual(len(result), 6)

    @patch('commands.add_book.find_book')
    def test_get_id_no_conflict(self, mock_find_book):
        mock_find_book.return_value = False

        result = get_id()
        self.assertEqual(mock_find_book.call_count, 1)
