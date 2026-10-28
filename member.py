import json


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
