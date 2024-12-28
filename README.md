# To-Do List Manager

This is a simple command-line To-Do List Manager written in Python. It allows you to manage your tasks efficiently by adding, displaying, editing, deleting, and sorting them based on priority.

## Features

- Add new tasks with a name, description, priority, and deadline.
- Display all tasks with their status, priority, and deadline.
- Mark tasks as done or not done.
- Edit existing tasks.
- Delete tasks.
- Sort tasks by priority.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vedp9984/ToDo.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ToDo
    ```
3. Run the comman:
    ```sh
    pip install -e .
    ```
    or if you do not want to break system packages
    ```sh
    pipx install -e .
    ```
## Updating

To update the To-Do List Manager to the latest version, follow these steps:

1. Navigate to the project directory:
    ```sh
    cd /path/to/your/ToDo
    ```
2. Pull the latest changes from the repository:
    ```sh
    git pull origin main
    ```
3. Reinstall the package:
    ```sh
    pip install -e .
    ```
    or if you do not want to break system packages
    ```sh
    pipx install -e .
    ```

## Usage

Type todo in your terminal to start the To-Do List Manager:
```sh
todo
```

### Commands

- `show`: Display the To-Do List.
- `add [taskname]`: Add a new task.
- `done [taskname]`: Mark a task as done.
- `notdone [taskname]`: Mark a task as not done.
- `edit [taskname]`: Edit an existing task.
- `delete [taskname]`: Delete a task.
- `sort`: Sort tasks by priority.
- `history`: Display history of last 100 typed commands
- `timestamp [taskname]`: Add a timestamp to a task.
- `exit`: Exit the application.
- `help`: Display the list of available commands.

### Further Information
- history stored at ~/.todo_history.log
- This project uses the `json` module for data storage.
- data stored at ~/.todo_list.json

## Credits
- mayank3135432 a.k.a ateium munol
- Vedp9984
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


