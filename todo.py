from datetime import datetime

def add_task(username, task, priority="Medium", deadline="No deadline"):
    if not task:
        print("Task cannot be empty.")
        return
    if username not in todo_lists:
        todo_lists[username] = []
    todo_lists[username].append({"task": task, "priority": priority, "deadline": deadline, "completed": False})
    print(f"Task added to {username}'s to-do list.")

def view_tasks(username, sort_by=None, filter_by=None):
    if username not in todo_lists or not todo_lists[username]:
        print("No tasks found.")
        return
    
    tasks = todo_lists[username]

    if sort_by == "priority":
        tasks = sorted(tasks, key=lambda x: x["priority"])
    elif sort_by == "deadline":
        tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], '%Y-%m-%d') if x["deadline"] != "No deadline" else datetime.max)
    
    if filter_by == "completed":
        tasks = [task for task in tasks if task["completed"]]
    elif filter_by == "pending":
        tasks = [task for task in tasks if not task["completed"]]

    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['task']} - Priority: {task['priority']}, Deadline: {task['deadline']}, Status: {status}")

def complete_task(username, task_number):
    if not username in todo_lists or not 0 < task_number <= len(todo_lists[username]):
        print("Invalid task number.")
        return
    todo_lists[username][task_number - 1]["completed"] = True
    print("Task marked as completed.")

def delete_task(username, task_number):
    if not username in todo_lists or not 0 < task_number <= len(todo_lists[username]):
        print("Invalid task number.")
        return
    todo_lists[username].pop(task_number - 1)
    print("Task deleted.")
