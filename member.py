from library import ask_yes_or_no
import json

# TODO: if the highest-numbered member is removed, this reuses their ID
# next_number = max(...)


def register_member(members):
    while True:
        details = input("Enter your first and last name: ").strip().title()
        if not details:
            print("User names cannot be empty!")
            continue
        elif details.isdigit():
            print("User names cannot be a number!")
            continue
        break

    next_number = max(
        (int(m["member_id"][2:]) for m in members), default=0
    ) + 1
    member_id = f"AL{next_number:03d}"

    new_member = {
        "member_id": member_id,
        "name": details,
        "borrowed_books": []
    }
    members.append(new_member)

    print("Member registed successfully!")
    print(f"ID: {new_member['member_id']}")
    print(f"Name: {new_member['name']}")
    print("Keep this ID safe, you need it to log in.")


def remove_member(members):
    if not members:
        print("There are no registered members!")
        return
    
    while True:
        info = input("Enter member ID (or press c to cancel): ").strip()

        if info.lower() == 'c':
            print("Cancelled!")
            return
        
        found = None
        for member in members:
            if member["member_id"] == info:
                found = member
                break

        if found is None:
            print(f'There is no member with ID {info}')
            continue

        if found["borrowed_books"]:
            print("This member still has borrowed books.")
            print("Ensure all books are returned before removing this member.")
            continue
        
        else:
            print("Member Details")
            print(
                f"ID: {found['member_id']}\n"
                f"Name: {found['name']}"
            )
            
        choice = ask_yes_or_no("Are you sure you want to remove this member? (Y/N): ")

        if choice:
            members.remove(found)
            print("Member removed successfully!")
        else:
            print("Removal Cancelled!")


        if not members:
            print("No member left.")
            break

        if not ask_yes_or_no("Do you want to delete another member? (Y/N)"):
            break


def view_all_members(members):
    if not members:
        print("There are no registered members!")
        return
    
    header = (
        f"{'No':<5} {'Member ID':^20} {'Name':^20} "
        f"{'Books Borrowed':^16}"
    )

    print(header)
    print("-" * len(header))

    for numbers, item in enumerate(members, start=1):
        print(
            f"{numbers:<5} {item['member_id']:^20} "
            f"{item['name']:^20} {len(item['borrowed_books']):^16}"
        )


def save_member_json(members):
    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)


def load_member_json():
    try:
        with open("members.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("members.json not found or corrupted, starting fresh.")
        return []
