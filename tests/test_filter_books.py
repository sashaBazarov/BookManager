import unittest
from typing import Set
from book import Book
from commands.filter_books import filter_books, filter_books_by_keyword


class TestFilterBooks(unittest.TestCase):
    def setUp(self):
        self.books: Set[Book] = {
            Book("1", "The Great Gatsby", "F. Scott Fitzgerald", "1925"),
            Book("2", "1984", "George Orwell", "1949"),
            Book("3", "To Kill a Mockingbird", "Harper Lee", "1960"),
            Book("4", "The Catcher in the Rye", "J.D. Salinger", "1951"),
        }

    def test_filter_by_author(self):
        filtered = filter_books(self.books, author="George Orwell")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].author, "George Orwell")

    def test_filter_by_year(self):
        filtered = filter_books(self.books, year="1949")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].year, "1949")

    def test_filter_by_keywords(self):
        filtered = filter_books(self.books, keywords="mockingbird")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "To Kill a Mockingbird")

    def test_filter_by_author_and_year(self):
        filtered = filter_books(self.books, author="J.D. Salinger", year="1951")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "The Catcher in the Rye")

    def test_filter_books_by_keyword_similarity(self):
        keyword_list = ["Gatsby"]
        filtered = filter_books_by_keyword(self.books, keyword_list)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "The Great Gatsby")

    def test_no_matching_books(self):
        filtered = filter_books(self.books, author="Unknown Author")
        self.assertEqual(len(filtered), 0)
