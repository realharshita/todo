from auth import register, users
from user_data import save_users, load_users

def main():
    global users
    users = load_users()

    print("Welcome to the To-Do List Application")
    
    while True:
        print("\n1. Register")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register(username, password):
                save_users(users)
        elif choice == "2":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
