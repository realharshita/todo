todo_lists = {}

def add_task(username, task):
    if username not in todo_lists:
        todo_lists[username] = []
    todo_lists[username].append({"task": task, "completed": False})
    print(f"Task added to {username}'s to-do list.")

def view_tasks(username):
    if username not in todo_lists or not todo_lists[username]:
        print("No tasks found.")
        return
    for idx, task in enumerate(todo_lists[username], 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

def complete_task(username, task_number):
    if username in todo_lists and 0 < task_number <= len(todo_lists[username]):
        todo_lists[username][task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(username, task_number):
    if username in todo_lists and 0 < task_number <= len(todo_lists[username]):
        todo_lists[username].pop(task_number - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")
