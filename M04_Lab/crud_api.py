"""
After watching the video, create a CRUD API for a Book instead of a Drink in the video example above.  The Book model should have the following parameters:
id
book_name
author
publisher
"""


# import requests
# import json


# in terminal:
# export FLASK_APP=crud_api.py
# export FLASK_ENV=development

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher,
        }

with app.app_context():
    db.create_all()

# Create Routes
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the Books API"})


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict())
    else:
        return jsonify({"error":"Book not found!"}), 404

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    
    new_book = Book(book_name=data["book_name"],
                    author=data["author"],
                    publisher=data["publisher"])
    
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    book = Book.query.get(book_id)
    if book:
        book.book_name = data.get("book_name", book.book_name)
        book.author = data.get("author", book.author)
        book.publisher = data.get("publisher", book.publisher)

        db.session.commit()

        return jsonify(book.to_dict())
    else:
        return jsonify({"error":"Book not found!"}), 404

@app.route("/books/<int:book_id>",methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()

        return jsonify({"message":"Book was deleted!"})
    else:
        return jsonify({"error":"Book not found!"}), 404 


if __name__ == "__main__":
    app.run(debug=True)
