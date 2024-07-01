# To-Do List Application

## Description

This is a simple command-line to-do list application where users can register, log in, and manage their tasks. Users can add, view, edit, complete, delete, sort, and filter tasks based on priority and deadlines.

## Features

- User Registration
- User Login
- Add Tasks with Priority and Deadline
- View Tasks
- Edit Tasks
- Mark Tasks as Completed
- Delete Tasks
- Sort Tasks by Priority
- Sort Tasks by Deadline
- Filter Tasks by Completion Status

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/realharshita/todo
    cd todo
    ```

2. **Run the application:**
    ```sh
    python main.py
    ```

3. **Follow the on-screen prompts to interact with the application.**

## File Structure

- `main.py`: The main entry point of the application.
- `auth.py`: Handles user registration and login.
- `user_data.py`: Manages saving and loading user data and to-do lists.
- `todo.py`: Contains functions for managing tasks.

## Getting Started

1. **Register:**
    - Select the "Register" option.
    - Enter a username and password.

2. **Login:**
    - Select the "Login" option.
    - Enter your username and password.

3. **Manage Tasks:**
    - After logging in, you can add, view, edit, complete, delete, sort, and filter tasks.

## Task Management Commands

- **Add Task:**
    - Enter the task description, priority (Low, Medium, High), and deadline (YYYY-MM-DD or No deadline).
- **View Tasks:**
    - Displays all tasks with their details.
- **Edit Task:**
    - Select a task number and enter new details.
- **Complete Task:**
    - Select a task number to mark as completed.
- **Delete Task:**
    - Select a task number to delete.
- **Sort Tasks:**
    - Sort tasks by priority or deadline.
- **Filter Tasks:**
    - Filter tasks by completed or pending status.

## Saving Data

- User data and to-do lists are saved in `users.json` and `todo_lists.json` files, respectively.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
