import json


def save_book_json(books):
    with open("Books.json", "w") as file:
        json.dump(books, file, indent=4)


def load_book_json():
    try:
        with open("Books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Books.json not found or corrupted, starting fresh.")
        return []
