import json

def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump(users, file)
    print("User data saved.")

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
