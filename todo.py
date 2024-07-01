todo_lists = {}

def add_task(username, task):
    if username not in todo_lists:
        todo_lists[username] = []
    todo_lists[username].append(task)
    print(f"Task added to {username}'s to-do list.")

def view_tasks(username):
    if username not in todo_lists or not todo_lists[username]:
        print("No tasks found.")
        return
    for idx, task in enumerate(todo_lists[username], 1):
        print(f"{idx}. {task}")
