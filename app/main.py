from flask import Flask, jsonify
import psycopg2 
from flask_json import FlaskJSON

app = Flask(__name__)
FlaskJSON(app)

class Book:
    def __init__(self):
        self.id = None
        self.name = None

class BookDAO:

    def get_books(self):
        sql = 'select id, name from books'
        conn = psycopg2.connect("dbname=docker-user user=docker-user password=sample host=postgresql port=5432")
        cur = conn.cursor()
        cur.execute(sql)
        records = cur.fetchall()
        books = []
        for record in records:
            book = Book()
            book.id = record[0]
            book.name = record[1]
            books.append(book)
        conn.close()
        return books


@app.route('/')
def get_books():
    books_dao = BookDAO()
    books = books_dao.get_books()
    for book in books:
        print(book.__dict__)
    books_dict = map(lambda book: book.__dict__ , books )
    return jsonify(books_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')



