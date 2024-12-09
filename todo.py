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
    for todo in todos:
        if "done" not in todo:
            todo["done"] = False
        if "priority" not in todo:
            todo["priority"] = "low"
        if "task" not in todo:
            todo["task"] = "Unnamed task"
    return todos

def display_todos(todos):
    if not todos:
        print(f"{Colors.WARNING}No to-do items found!{Colors.ENDC}")
        return

    print(f"\n{Colors.OKBLUE}To-Do List:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")
    for idx, todo in enumerate(todos, 1):
        status = f"{Colors.FAIL}[ ]{Colors.ENDC}" if not todo["done"] else f"{Colors.OKGREEN}[x]{Colors.ENDC}"
        print(f"{idx}. {status} ({todo['priority']}) {todo['task']}")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")

def add_todo():
    task = input("Enter a new to-do item: ")
    priority = input("Enter the priority (high/medium/low): ")
    if not task:
        print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")
    else:
        todos = load_todos()
        todos.append({"done": False, "priority": priority, "task": task})
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task added!{Colors.ENDC}")

def mark_done(todos, done=True):
    display_todos(todos)
    task_num = input("Enter the task number to mark as done: ")
    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(todos):
        print(f"{Colors.FAIL}Invalid task number!{Colors.ENDC}")
    else:
        todos[int(task_num) - 1]["done"] = done
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task marked as {'done' if done else 'not done'}!{Colors.ENDC}")

def edit_todo():
    todos = load_todos()
    display_todos(todos)
    task_num = input("Enter the task number to edit: ")
    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(todos):
        print(f"{Colors.FAIL}Invalid task number!{Colors.ENDC}")
    else:
        new_task = input("Enter the new task text: ")
        new_priority = input("Enter the new priority (high/medium/low): ")
        if not new_task:
            print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")
        else:
            todos[int(task_num) - 1].update({"task": new_task, "priority": new_priority})
            save_todos(todos)
            print(f"{Colors.OKGREEN}Task edited!{Colors.ENDC}")

def delete_todo():
    todos = load_todos()
    display_todos(todos)
    task_num = input("Enter the task number to delete: ")
    if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(todos):
        print(f"{Colors.FAIL}Invalid task number!{Colors.ENDC}")
    else:
        todos.pop(int(task_num) - 1)
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task deleted!{Colors.ENDC}")

def sort_todos():
    todos = load_todos()
    todos.sort(key=lambda x: (x["priority"], x["done"]))
    save_todos(todos)
    print(f"{Colors.OKGREEN}Tasks sorted by priority!{Colors.ENDC}")

def main():
    while True:
        print(f"\n{Colors.HEADER}To-Do List Manager{Colors.ENDC}")
        print("1. Display To-Do List")
        print("2. Add To-Do Item")
        print("3. Mark Item as Done")
        print("4. Mark Item as Not Done")
        print("5. Edit To-Do Item")
        print("6. Delete To-Do Item")
        print("7. Sort Tasks by Priority")
        print("8. Exit")
        option = input("Choose an option: ")

        todos = load_todos()
        todos = validate_todos(todos)

        if option == '1':
            display_todos(todos)
        elif option == '2':
            add_todo()
        elif option == '3':
            mark_done(todos, done=True)
        elif option == '4':
            mark_done(todos, done=False)
        elif option == '5':
            edit_todo()
        elif option == '6':
            delete_todo()
        elif option == '7':
            sort_todos()
        elif option == '8':
            break
        else:
            print(f"{Colors.FAIL}Invalid option! Please choose again.{Colors.ENDC}")

if __name__ == "__main__":
    main()
