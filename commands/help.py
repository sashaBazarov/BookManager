def help():
    
    help_text = """
    Help - List of available commands:

    1. addbook title author year
    Add a new book.
    Example: addbook "Crime and Punishment" "Fyodor Dostoevsky" 1866
    Or addbook title = "Crime and Punishment" author = "Fyodor Dostoevsky" year = 1866

    2. editbook id kwargs
    Edit book information.
    Example: editbook 1 title="Crime and Punishment" year=1867

    3. clear
    Clear the console.

    4. exit
    Exit the program.

    5. books [optional arguments]
    Without arguments: display the list of all books.
    With arguments:
        - keywords="" - search by keywords.
        - title="" - search by title.
        - author="" - search by author.
        - year="" - search by year.
    Example: books title="Crime and Punishment"

    6. del id
    Delete a book by ID.
    Example: del 1

    Note: Use double quotes "" to input strings, especially if they contain spaces. For example: "Crime and Punishment".
    """
    print(help_text)

