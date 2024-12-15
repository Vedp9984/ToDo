# To-Do List Manager

This is a simple command-line To-Do List Manager written in Python. It allows you to manage your tasks efficiently by adding, displaying, editing, deleting, and sorting them based on priority.

## Features

- Add new tasks with a name, description, priority, and deadline.
- Display all tasks with their status, priority, and deadline.
- Mark tasks as done or not done.
- Edit existing tasks.
- Delete tasks.
- Sort tasks by priority.
- Get the timestamp of a task.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vedp9984/ToDo.git
    ```
2. Navigate to the project directory:
    ```sh
    cd todo-list-manager
    ```

## Usage

Run the main script to start the To-Do List Manager:
```sh
python main.py
```

### Commands

- `show` or `1`: Display the To-Do List.
- `add [taskname]` or `2`: Add a new task.
- `done [taskname]` or `3`: Mark a task as done.
- `notdone [taskname]` or `4`: Mark a task as not done.
- `edit [taskname]` or `5`: Edit an existing task.
- `delete [taskname]` or `6`: Delete a task.
- `sort` or `7`: Sort tasks by priority.
- `exit` or `8`: Exit the application.
- `help`: Display the list of available commands.

## File Structure

- `main.py`: Entry point of the application.
- `todo.py`: Contains all the functions for managing the to-do list.
- `.gitignore`: Specifies files and directories to be ignored by git.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the `json` module for data storage.
- Special thanks to all contributors and users.
