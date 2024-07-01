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

def save_todo_lists(todo_lists, filename="todo_lists.json"):
    with open(filename, "w") as file:
        json.dump(todo_lists, file)
    print("To-do lists saved.")

def load_todo_lists(filename="todo_lists.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
