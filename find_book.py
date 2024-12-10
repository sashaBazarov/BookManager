from json_io import load_books

def find_book(book_id):

    books = load_books()

    for book in books:
        if book.id == book_id:
            return book
        else:
            continue
    
    return None
