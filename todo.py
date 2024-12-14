import os
import json

TODO_FILE = os.path.expanduser("~/todo_list.json")

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def validate_todos(todos):
    task_names = set()
    for todo in todos:
        if "done" not in todo:
            todo["done"] = False
        if "priority" not in todo:
            todo["priority"] = "low"
        if "task" not in todo:
            todo["task"] = "Unnamed task"
        if "taskname" not in todo or not todo["taskname"] or " " in todo["taskname"] or todo["taskname"] in task_names:
            todo["taskname"] = f"task_{len(task_names) + 1}"
        task_names.add(todo["taskname"])
    return todos

def display_todos(todos):
    if not todos:
        print(f"{Colors.WARNING}No to-do items found!{Colors.ENDC}")
        return

    print(f"\n{Colors.OKBLUE}To-Do List:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")
    for idx, todo in enumerate(todos, 1):
        status = f"{Colors.FAIL}[ ]{Colors.ENDC}" if not todo["done"] else f"{Colors.OKGREEN}[x]{Colors.ENDC}"
        print(f"{idx}. {todo['taskname']}: {status} ({todo['priority']}) {todo['task']}")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")

def add_todo(token: list[str]):
    todos = load_todos()
    taskname = input("Enter a task name: ") if len(token) == 1 else token[1]
    task = input("Enter task description: ")
    priority = input("Enter the priority (high/medium/low): ")
    if not task:
        print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")
    elif " " in taskname or any(todo["taskname"] == taskname for todo in todos):
        print(f"{Colors.FAIL}Task name must be unique and one word!{Colors.ENDC}")
    else:
        new_todo = {
            "task": task,
            "priority": priority,
            "done": False,
            "taskname": taskname
        }
        todos.append(new_todo)
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task added!{Colors.ENDC}")

def mark_done(tokens, todos, done=True):
    display_todos(todos)
    task_name = input("Enter the task name to mark as done: ") if len(tokens) == 1 else tokens[1]
    task_index = next((index for (index, d) in enumerate(todos) if d["taskname"] == task_name), None)
    if task_index is None:
        print(f"{Colors.FAIL}Invalid task name!{Colors.ENDC}")
    else:
        todos[task_index]["done"] = done
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task marked as {'done' if done else 'not done'}!{Colors.ENDC}")

def edit_todo(tokens: list[str]):
    todos = load_todos()
    display_todos(todos)
    task_name = input("Enter the task name to edit: ") if len(tokens) == 1 else tokens[1]
    task_index = next((index for (index, d) in enumerate(todos) if d["taskname"] == task_name), None)
    if task_index is None:
        print(f"{Colors.FAIL}Invalid task name!{Colors.ENDC}")
    else:
        new_task = input("Enter the new task text: ")
        new_priority = input("Enter the new priority (high/medium/low): ")
        if not new_task:
            print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")
        else:
            todos[task_index].update({"task": new_task, "priority": new_priority})
            save_todos(todos)
            print(f"{Colors.OKGREEN}Task edited!{Colors.ENDC}")

def delete_todo(tokens: list[str]):
    todos = load_todos()
    display_todos(todos)
    task_name = input("Enter the task name to delete: ") if len(tokens) == 1 else tokens[1]
    task_index = next((index for (index, d) in enumerate(todos) if d["taskname"] == task_name), None)
    if task_index is None:
        print(f"{Colors.FAIL}Invalid task name!{Colors.ENDC}")
    else:
        todos.pop(task_index)
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task deleted!{Colors.ENDC}")

def sort_todos():
    todos = load_todos()
    todos.sort(key=lambda x: (x["priority"], x["done"]))
    save_todos(todos)
    print(f"{Colors.OKGREEN}Tasks sorted by priority!{Colors.ENDC}")

def menu():
    print("1. show: Display To-Do List")
    print("2. add [taskname]: Add To-Do Item")
    print("3. done [taskname]: Mark Item as Done")
    print("4. notdone [taskname]: Mark Item as Not Done")
    print("5. edit [taskname]: Edit To-Do Item")
    print("6. delete [taskname]: Delete To-Do Item")
    print("7. sort: Sort Tasks by Priority")
    print("8. exit: Exit")

def take_input():
    command = input("[ToDo]> ").lower()
    tokens = command.split()
    if not tokens:
        print(f"{Colors.FAIL}No command entered!{Colors.ENDC}")
        return []

    return tokens

def execute(tokens: list[str]):
    todos = load_todos()
    todos = validate_todos(todos)
    action = tokens[0]
    if action == 'show' or action == '1':
        display_todos(todos)
    elif action == 'add' or action == '2':
        add_todo(tokens)
    elif action == 'done' or action == '3':
        mark_done(tokens, todos, done=True)
    elif action == 'notdone' or action == '4':
        mark_done(tokens, todos, done=False)
    elif action == 'edit' or action == '5':
        edit_todo(tokens)
    elif action == 'delete' or action == '6':
        delete_todo(tokens)
    elif action == 'sort' or action == '7':
        sort_todos()
    elif action == 'exit' or action == '8':
        exit()
    elif action == 'help':
        menu()
    else:
        print(f"{Colors.FAIL}Invalid command!{Colors.ENDC}\nUse \"help\" for a list of available commands")
        return 1
    return 0

