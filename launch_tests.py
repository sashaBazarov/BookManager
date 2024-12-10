import unittest
from unittest.mock import patch
from commands.add_book import add_book, get_id
from json_io import save_book

class AddBookTestCase(unittest.TestCase):
    @patch('json_io.save_book')
    @patch('add_book.get_id')
    def test_add_book(self, mock_get_id, mock_save_book):
        # Mock the return values of get_id and save_book
        mock_get_id.return_value = 'abc123'
        
        # Call the add_book function
        add_book('Title', 'Author', '2022')
        
        # Assert that get_id was called once
        mock_get_id.assert_called_once()
        
        # Assert that save_book was called once with the correct arguments
        mock_save_book.assert_called_once_with('abc123', 'Title', 'Author', '2022')
        
        # You can also add more assertions to check the behavior of the function
        
if __name__ == '__main__':
    unittest.main()