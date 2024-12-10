from typing import Set
from book import Book

def filter_books(books: Set[Book], author: str = None, year: str = None, keywords: str = None):
    """
    Filters a set of books based on the given criteria.

    Args:
        books (Set[Book]): The set of books to filter.
        author (str, optional): The author name to filter by. Defaults to None.
        year (str, optional): The publication year to filter by. Defaults to None.
        keywords (str, optional): The keywords to filter by. Defaults to None.

    Returns:
        List[Book]: The filtered list of books.
    """

    if keywords:
        keyword_list = keywords.lower().split()
        books = filter_books_by_keyword(books, keyword_list)

    filtered_books = [
        book
        for book in books
        if (author is None or book.author.lower() == author.lower()) and
           (year is None or book.year.lower() == year.lower())
    ]

    return filtered_books


def filter_books_by_keyword(books, keyword_list):

    def calculate_similarity(word1: str, word2: str) -> float:
        """
        Calculate the similarity between two words based on character matches.
        """
        matches = sum(1 for c1, c2 in zip(word1, word2) if c1 == c2)
        length = max(len(word1), len(word2))
        return matches / length

    def is_keyword_similar(keyword: str, title: str, threshold: float = 0.6) -> bool:
        """
        Check if the keyword is similar to any word in the title based on the threshold.
        """
        title_words = title.lower().split()
        return any(
            calculate_similarity(keyword, word) >= threshold
            for word in title_words
        )

    return [
        book
        for book in books
        if any(
            is_keyword_similar(keyword, book.title)
            for keyword in keyword_list
        )
    ]
