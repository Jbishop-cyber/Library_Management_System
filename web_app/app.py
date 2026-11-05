from flask import render_template
from flask import Flask

app = Flask(__name__)

library_books = [
        {"isbn": "9780132343218", "title": "Clean Code", "description": "A book about writing clean, readable and maintainable code."},
        {"isbn": "9780132570631", "title": "A Song of Ice and Fire", "description": "An epic dark-fantasy saga that intertwines a brutal medieval power struggle for the Iron Throne among rival noble families in Westeros with an ancient, existential war against the icy Others and fiery dragons."},
        {"isbn": "9781289053731", "title": "Harry Potter", "description": "An orphaned boy who discovers on his eleventh birthday that he is a wizard, attends Hogwarts School of Witchcraft and Wizardry, and ultimately fulfills his destiny by defeating the dark wizard Lord Voldemort."}
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():
    # library_books = [
    #     {"id": 1, "title": "Clean Code"},
    #     {"id": 2, "title": "A Song of Ice and Fire"},
    #     {"id": 3, "title": "Harry Potter"}
    # ]
    return render_template("books.html", library_books=library_books)

@app.route("/books/<int:book_isbn>")
def book_details(book_isbn):
    for book in library_books:
        if book["isbn"] == str(book_isbn):
            return render_template("book_details.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
