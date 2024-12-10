# Book Manager CLI

A simple command-line interface (CLI) for managing a book collection. This application allows users to add, edit, search, delete books, and clear the console.

## Features

- Add books with title, author, and year.
- Edit book details using its ID.
- Display all books or search for specific books using keywords.
- Delete books by ID.
- Clear the console like Unix systems.
- Exit the application.

## Commands Overview

### 1. Add a Book
Add a new book to the collection.

**Syntax:**
```plaintext
addbook title author year
```

**Example:**
```plaintext
addbook "Crime and Punishment" "Fyodor Dostoevsky" 1866
```

---

### 2. Edit a Book
Edit the details of an existing book by its ID.

**Syntax:**
```plaintext
editbook id kwargs
```

**Example:**
```plaintext
editbook 1 title="Crime and Punishment" year=1867
```

---

### 3. Clear the Console
Clear the console screen, similar to Unix systems.

**Syntax:**
```plaintext
clear
```

**Example:**
```plaintext
clear
```

---

### 4. Exit the Application
Exit the CLI program.

**Syntax:**
```plaintext
exit
```

**Example:**
```plaintext
exit
```

---

### 5. Display or Search Books
Display all books or search for books based on specific criteria.

**Syntax:**
```plaintext
books [optional arguments]
```

**Optional Arguments:**
- `keywords=""` - Search by keywords in title or author.
- `title=""` - Search by title.
- `author=""` - Search by author.
- `year=""` - Search by year.

**Examples:**
```plaintext
books
```
Displays all books.

```plaintext
books title="Crime and Punishment"
```
Searches for books with the title "Crime and Punishment."

---

### 6. Delete a Book
Remove a book from the collection using its ID.

**Syntax:**
```plaintext
del id
```

**Example:**
```plaintext
del 1
```

---

## Notes

- Use double quotes (`""`) for strings that contain spaces, such as book titles or author names.
- Ensure that all commands are typed correctly; invalid commands will not be executed.

---

## Requirements

- Python 3.x

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-manager-cli.git
   ```
2. Navigate to the project directory:
   ```bash
   cd book-manager-cli
   ```
3. Run the script:
   ```bash
   python book_manager.py
   ```

