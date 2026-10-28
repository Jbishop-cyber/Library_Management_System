import subprocess

from library import (
    add_book, remove_book, search_books, borrow_book, return_book,
    view_available_books, view_borrowed_books,
)

from book import (load_book_json, save_book_json)

from member import (register_member, load_member_json, save_member_json)

ADMIN_PASSWORD = "Admin"


def clear_screen():
    subprocess.run(["clear"])


def admin_login():
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        password = input("Enter admin password (or c to cancel): ").strip()

        if password.lower() == "c":
            print("Log In Cancelled")
            return False
        if password == ADMIN_PASSWORD:
            return True
        else:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(
                    f"Wrong password! {remaining} attempt(s) left."
                )

    print("Too many attempts.")
    return False


def member_login(members):
    if not members:
        print("No members are registered yet!")
        return None

    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        entry = input(
            "Enter your member ID (or c to cancel): ").strip()

        if entry.lower() == "c":
            print("Log In Cancelled")
            return None

        for member in members:
            if member["member_id"] == entry:
                return member

        remaining = max_attempts - attempt
        if remaining > 0:
            print(
                f"Member ID not found! {remaining} attempt(s) left."
            )

    print("Too many attempts.")
    return None


def admin_menu(books, members):
    while True:
        print("\n--- MENU ---")
        print("1. Add books")
        print("2. Remove books")
        print("3. Search for books")
        print("4. Register members")
        print("5. View available books")
        print("6. View borrowed books")
        print("7. Log out")

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Your choice must be in digit")
            continue
        clear_screen()

        if choice == 1:
            add_book(books)
            save_book_json(books)
        elif choice == 2:
            remove_book(books)
            save_book_json(books)
        elif choice == 3:
            search_books(books)
        elif choice == 4:
            register_member(members)
            save_member_json(members)
        elif choice == 5:
            view_available_books(books)
        elif choice == 6:
            view_borrowed_books(books, members)
        elif choice == 7:
            print("Logged out.")
            return
        else:
            print("Invalid option, Try again!")


def member_menu(books, members, member):
    while True:
        print(f"\n Welcome {member['name']}!")
        print("\n--- MENU ---")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Search for books")
        print("4. View available books")
        print("5. View borrowed books")
        print("6. Log out")

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Your choice must be in digit")
            continue
        clear_screen()

        if choice == 1:
            borrow_book(books, member)
            save_book_json(books)
            save_member_json(members)
        elif choice == 2:
            return_book(books, member)
            save_book_json(books)
            save_member_json(members)
        elif choice == 3:
            search_books(books)
        elif choice == 4:
            view_available_books(books)
        elif choice == 5:
            view_borrowed_books(books)
        elif choice == 6:
            print("Logged out.")
            return
        else:
            print("Invalid option, Try again!")


def main():
    books = load_book_json()
    members = load_member_json()

    print("Welcome to the library management system!")

    while True:
        print("\n1. Admin")
        print("2. Member")
        print("3. Exit")

        try:
            choice = int(input("Log in as: "))
        except ValueError:
            print("Your choice must be in digit")
            continue

        if choice == 1:
            if admin_login():
                admin_menu(books, members)
        elif choice == 2:
            member = member_login(members)
            if member is not None:
                member_menu(books, members, member)
        elif choice == 3:
            print("Thanks for using this application, Goodbye!")
            break
        else:
            print("Invalid option, Try again!")


main()
