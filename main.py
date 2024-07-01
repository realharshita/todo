from auth import register, login, users
from user_data import save_users, load_users, save_todo_lists, load_todo_lists
from todo import add_task, view_tasks, complete_task, delete_task, edit_task, todo_lists

def main():
    global users, todo_lists
    users = load_users()
    todo_lists = load_todo_lists()

    print("Welcome to the To-Do List Application")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register(username, password):
                save_users(users)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                while True:
                    print(f"\nWelcome, {username}")
                    print("1. Add task")
                    print("2. View tasks")
                    print("3. Mark task as complete")
                    print("4. Delete task")
                    print("5. Edit task")
                    print("6. Sort tasks by priority")
                    print("7. Sort tasks by deadline")
                    print("8. Filter tasks by completed")
                    print("9. Filter tasks by pending")
                    print("10. Logout")
                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == "1":
                        task = input("Enter task: ")
                        priority = input("Enter priority (Low, Medium, High): ")
                        deadline = input("Enter deadline (YYYY-MM-DD or No deadline): ")
                        add_task(username, task, priority, deadline)
                        save_todo_lists(todo_lists)
                    elif user_choice == "2":
                        view_tasks(username)
                    elif user_choice == "3":
                        try:
                            task_number = int(input("Enter task number to mark as complete: "))
                            complete_task(username, task_number)
                            save_todo_lists(todo_lists)
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    elif user_choice == "4":
                        try:
                            task_number = int(input("Enter task number to delete: "))
                            delete_task(username, task_number)
                            save_todo_lists(todo_lists)
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    elif user_choice == "5":
                        try:
                            task_number = int(input("Enter task number to edit: "))
                            new_task = input("Enter new task description: ")
                            new_priority = input("Enter new priority (Low, Medium, High): ")
                            new_deadline = input("Enter new deadline (YYYY-MM-DD or No deadline): ")
                            edit_task(username, task_number, new_task, new_priority, new_deadline)
                            save_todo_lists(todo_lists)
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    elif user_choice == "6":
                        view_tasks(username, sort_by="priority")
                    elif user_choice == "7":
                        view_tasks(username, sort_by="deadline")
                    elif user_choice == "8":
                        view_tasks(username, filter_by="completed")
                    elif user_choice == "9":
                        view_tasks(username, filter_by="pending")
                    elif user_choice == "10":
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            save_users(users)
            save_todo_lists(todo_lists)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
