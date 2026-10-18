import sqlite3

def get_books():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    connection.close()

    result = []

    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "author": book[2]
        })
    
    return result

def add_book(book):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO books (id, title, author) VALUES (?, ?, ?)",
        (book.id, book.title, book.author)
    )

    connection.commit()
    connection.close()

def delete_book(book_id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id)
    )

    connection.commit()
    connection.close()
