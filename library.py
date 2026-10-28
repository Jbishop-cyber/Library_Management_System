def ask_copies(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number of copies must be greater than zero!")
                continue
            return number
        except ValueError:
            print("Invalid! Enter the number of copies in digits!")


def ask_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        print("Invalid input! Enter Y or N.")


def display_books(books):
    if not books:
        print("There are no books in the library!")
        return

    header = (
        f"{'No':<5} {'Title':<25} {'Author':^20} "
        f"{'ISBN':^13} {'Total_Copies':^12} {'Copies_Left':^12}"
    )

    print(header)
    print("-" * len(header))

    for number, item in enumerate(books, start=1):
        print(
            f"{number:<5} {item['title']:<25} {item['author']:^20} "
            f"{item['isbn']:<13} {item['total_copies']:^12} "
            f"{item['copies_left']:^12}"
        )


def add_book(books):
    while True:
        # ISBN
        while True:
            isbn = input("Enter ISBN number: ").strip()
            if not isbn:
                print("ISBN cannot be empty!")
                continue
            if not isbn.isdigit():
                print("ISBN must contain only digits!")
                continue
            if len(isbn) != 13:
                print("ISBN must be 13 digit!")
                continue
            break
        # Looking for an existing book
        existing = None
        for item in books:
            if item["isbn"] == isbn:
                existing = item
                break

        if existing:
            print(f"'{existing['title']}' already exists in the library.")
            extra = ask_copies("How many copies do you want to add? ")
            existing["total_copies"] += extra
            existing["copies_left"] += extra
            print("Copies added successfully!")

        else:
            # To add a brand new book
            while True:
                title = input("Enter the book title: ").strip().title()
                if not title:
                    print("Book title cannot be empty!")
                    continue
                elif title.isdigit():
                    print("Book title cannot be a number!")
                    continue
                break

            while True:
                author = input("Author's name: ").strip().title()
                if not author:
                    print("Author's name cannot be empty!")
                    continue
                elif author.isdigit():
                    print("Author's name cannot be a number")
                    continue
                break

            total_copies = ask_copies("Enter how many copies: ")

            new_book = {
                "title": title,
                "author": author,
                "isbn": isbn,
                "total_copies": total_copies,
                "copies_left": total_copies
            }

            books.append(new_book)
            print("Book added successfully!")

        # To add another book
        if not ask_yes_or_no("Add another book (Y/N): "):
            break


def remove_book(books):
    if not books:
        print("No books found")
        return

    while True:
        while True:
            isbn_no = input(
                "Enter the book's isbn number (or press 'c' to cancel): "
            ).strip()

            if isbn_no.lower() == 'c':
                print("Removal cancelled!")
                return

            if not isbn_no:
                print("ISBN cannot be empty!")
                continue
            if not isbn_no.isdigit():
                print("ISBN must contain only digits!")
                continue
            if len(isbn_no) != 13:
                print("ISBN must be 13 digit!")
                continue
            break

        found = None
        for book in books:
            if book["isbn"] == isbn_no:
                found = book
                break

        if found:
            print(
                f"ISBN: {found['isbn']}\nTitle: {found['title']}\n"
                f"Author: {found['author']}\n"
                f"Total Copies: {found['total_copies']}\n"
                f"Copies Left: {found['copies_left']}"
            )
            remove = ask_copies("How many copies do you want to remove? ")

            if remove > found['copies_left']:
                print(
                    f"Only {found['copies_left']} copies of {found['title']} "
                    f"are available to remove"
                )
            elif not ask_yes_or_no(
                f"Remove {remove} copies of '{found['title']}'? (Y/N): "
            ):
                print("Removal cancelled.")
            else:
                found['copies_left'] -= remove
                found['total_copies'] -= remove
                print(f"You removed {remove} copies of {found['title']}")

                if found['total_copies'] == 0:
                    books.remove(found)
                    print(
                        f"All copies gone! '{found['title']}' has been "
                        f"deleted from the library"
                    )
        else:
            print(f"No book found with ISBN {isbn_no}")

        if not books:
            print("No more books left in the library.")
            break

        if not ask_yes_or_no("Do you want to remove another book (Y/N): "):
            break


def search_books(books):
    if not books:
        print("There are no books available in the library!")
        return

    # search book in the library
    while True:
        print("Search by:")
        print("1.Title")
        print("2.Author")
        print("3.ISBN (the first or last 5 digits)")
        print("4.Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 4:
            print("Returning to menu!")
            return

        if choice not in (1, 2, 3):
            print("Invalid option, Choose between option 1-4")
            continue

        search_term = input("Select a keyword: ").strip().lower()
        if not search_term:
            print("Search term cannot be empty!")
            continue

        if choice == 3:
            if not search_term.isdigit():
                print("ISBN search term must contain digit only!")
                continue
            if len(search_term) < 5:
                print("Enter at list 5 digits of the ISBN!")
                continue

        matches = []
        for item in books:
            if choice == 1 and search_term in item['title'].lower():
                matches.append(item)
            elif choice == 2 and search_term in item['author'].lower():
                matches.append(item)
    # a user can search with the first or last five digit of the isbn number
            elif choice == 3 and (item['isbn'].startswith(search_term)
                                  or item['isbn'].endswith(search_term)):
                matches.append(item)

        if not matches:
            print(f"No books found for '{search_term}'.")
        else:
            display_books(matches)

        if not ask_yes_or_no("Do you want to search for another book (Y/N)? "):
            break


def borrow_book(books, member):
    if not books:
        print("There are no books inside the library!")
        return

    while True:
        isbn_no = input(
            "Enter the ISBN of the book you want to borrow (or c to cancel): "
        ).strip()

        if isbn_no.lower() == "c":
            print("Borrowing cancelled!")
            return
        if not isbn_no.isdigit():
            print("ISBN must contain only digits!")
            continue
        if len(isbn_no) != 13:
            print("ISBN must be 13 digits!")
            continue

        found = None
        for book in books:
            if book['isbn'] == isbn_no:
                found = book
                break

        if found is None:
            print(
                f"No book found with {isbn_no}"
            )
            continue

        if found['copies_left'] <= 0:
            print(
                f"Sorry, no copies of '{found['title']}' are available."
            )
            continue

        if isbn_no in member["borrowed_books"]:
            print("You have already borrowed this book!")
            continue

        if ask_yes_or_no(
            f"Borrow '{found['title']}' by {found['author']}? (Y/N):"
        ):
            found['copies_left'] -= 1
            member['borrowed_books'].append(isbn_no)
            print(
                f"You borrowed '{found['title']}'. Enjoy!"
            )
        else:
            print("Borrowing cancelled.")
        return


def return_book(books, member):
    if not member['borrowed_books']:
        print("You have not borrowed any books!")
        return

    while True:
        print("Book(s) you have borrowed:")
        for isbn in member['borrowed_books']:
            for book in books:
                if book['isbn'] == isbn:
                    print(
                        f"'{book['title']}' by {book['author']} (ISBN: {isbn})"
                    )

        ret_isbn = input(
            "Enter the ISBN number of the book you want to return "
            "(or press c to cancel): "
        ).strip()

        if ret_isbn.lower() == "c":
            print("Cancelled.")
            return
        if not ret_isbn.isdigit():
            print("ISBN must contain only digits!")
            continue
        if len(ret_isbn) != 13:
            print("ISBN must be 13 digits!")
            continue

        if ret_isbn not in member['borrowed_books']:
            print("You have not borrowed a book with that ISBN!")
            continue

        found = None
        for book in books:
            if book['isbn'] == ret_isbn:
                found = book
                break

        if found is None:
            print(
                "This book is not in the library!"
            )
            continue

        if ask_yes_or_no(
            f"Return '{found['title']}' by {found['author']}? (Y/N): "
        ):
            found['copies_left'] += 1
            member['borrowed_books'].remove(ret_isbn)
            print(
                f"You returned '{found['title']}' by {found['author']}."
            )
        else:
            print("Return cancelled!")
        return


def view_available_books(books):
    if not books:
        print("No books found!")
        return

    available_books = []
    for items in books:
        if items['copies_left'] > 0:
            available_books.append(items)

    if not available_books:
        print("No books available right now!")
    else:
        display_books(available_books)


def view_borrowed_books(books, members=None):
    borrowed_books = []
    for book in books:
        if book["total_copies"] - book["copies_left"] > 0:
            borrowed_books.append(book)

    if not borrowed_books:
        print("No books are currently borrowed.")
        return

    header = (
        f"{'No':<5} {'Title':<25} {'Author':^20} "
        f"{'ISBN':^13} {'Borrowed':^10} {'Copies_Left':^12}"
    )
    if members is not None:
        header += f" {'Borrowed By':<25}"

    print(header)
    print("-" * len(header))

    for number, book in enumerate(borrowed_books, start=1):
        borrowed = book["total_copies"] - book["copies_left"]
        row = (
            f"{number:<5} {book['title']:<25} {book['author']:^20} "
            f"{book['isbn']:<13} {borrowed:^10} {book['copies_left']:^12}"
        )

        if members is not None:
            holders = []
            for member in members:
                if book["isbn"] in member["borrowed_books"]:
                    holders.append(member["name"])
            row += f" {', '.join(holders):<25}"

        print(row)
