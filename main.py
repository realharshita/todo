from auth import register, login, users
from user_data import save_users, load_users
from todo import add_task, view_tasks, complete_task, delete_task, todo_lists

def main():
    global users, todo_lists
    users = load_users()

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
                    print("5. Logout")
                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == "1":
                        task = input("Enter task: ")
                        add_task(username, task)
                    elif user_choice == "2":
                        view_tasks(username)
                    elif user_choice == "3":
                        task_number = int(input("Enter task number to mark as complete: "))
                        complete_task(username, task_number)
                    elif user_choice == "4":
                        task_number = int(input("Enter task number to delete: "))
                        delete_task(username, task_number)
                    elif user_choice == "5":
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
