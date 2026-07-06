import sqlite3
from dataclasses import dataclass

DB_PATH: str = "instance/books.db"

@dataclass
class Book:
    book_name: str
    author: str
    publisher: str

def add_book(db_path: str, book: Book):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        insert_query = "INSERT INTO book (book_name, author, publisher) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (book.book_name, book.author, book.publisher))
        conn.commit()
        print(f"Successfully added {book.book_name}!")
    
    except sqlite3.Error as e:
        print("Failed to add book:", e)
    
    finally:
        cursor.close()
        conn.close()

def main():
    book = Book(
        "Harry Potter and the Prisoner of Azkaban",
        "J.K. Rowling",
        "Scholastic"
    )
    add_book(DB_PATH, book)

if __name__ == "__main__":
    main()

