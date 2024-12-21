import os
import json
import datetime
import readline
import atexit
from . import history as History
import fnmatch

TODO_FILE = os.path.expanduser("~/.todo_list.json")

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup_readline():
    if os.path.exists(History.HISTORY_FILE):
        with open(History.HISTORY_FILE, "r") as file:
            for line in file:
                #print(f"it is {line}")
                command = line.split(" - ", 1)[1].strip()
                #print(f"Adding to history: {command}")
                readline.add_history(command.strip())
    readline.set_history_length(1000)
    #atexit.register(readline.write_history_file, HISTORY_FILE)

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

def display_todos(todos, pattern=None):
    if not todos:
        print(f"{Colors.WARNING}No to-do items found!{Colors.ENDC}")
        return

    filtered_todos = todos
    if pattern:
        #print(f"Pattern is {pattern}")
        filtered_todos = [todo for todo in todos if fnmatch.fnmatch(todo["taskname"], pattern)]

    if not filtered_todos:
        print(f"{Colors.WARNING}No to-do items matching the pattern '{pattern}' found!{Colors.ENDC}")
        return

    print(f"\n{Colors.OKBLUE}To-Do List:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")
    for idx, todo in enumerate(filtered_todos, 1):
        status = f"{Colors.FAIL}[ ]{Colors.ENDC}" if not todo["done"] else f"{Colors.OKGREEN}[x]{Colors.ENDC}"
        print(f"{idx}. {todo['taskname']}: {status} ({todo['priority']}) {todo['task']} [Deadline: {todo['deadline']}]")
    print(f"{Colors.OKBLUE}{'-' * 35}{Colors.ENDC}")

def add_todo(token: list[str]):
    todos = load_todos()
    taskname = input("Enter a task name: ") if len(token) == 1 else token[1]
    task = input("Enter task description: ")
    priority = input("Enter the priority (high/medium/low): ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    if not task:
        print(f"{Colors.FAIL}Task cannot be empty!{Colors.ENDC}")
    elif " " in taskname or any(todo["taskname"] == taskname for todo in todos):
        print(f"{Colors.FAIL}Task name must be unique and one word!{Colors.ENDC}")
    else:
        new_todo = {
            "task": task,
            "priority": priority,
            "done": False,
            "taskname": taskname,
            "timestamp": datetime.datetime.now().isoformat(),
            "deadline": deadline
        }
        todos.append(new_todo)
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task added!{Colors.ENDC}")

def mark_done(tokens, todos, done=True):
    pattern = input("Enter the task name or pattern to mark as done: ") if len(tokens) == 1 else tokens[1]
    matching_indices = [index for index, todo in enumerate(todos) if fnmatch.fnmatch(todo["taskname"], pattern)]
    
    if not matching_indices:
        print(f"{Colors.FAIL}No tasks matching the pattern '{pattern}' found!{Colors.ENDC}")
    else:
        for index in matching_indices:
            todos[index]["done"] = done
        save_todos(todos)
        print(f"{Colors.OKGREEN}Tasks matching the pattern '{pattern}' marked as {'done' if done else 'not done'}!{Colors.ENDC}")

def gettimestamp(tokens: list[str]):
    todos = load_todos()
    task_name = input("Enter the task name to get timestamp: ") if len(tokens) == 1 else tokens[1]
    task = next((todo for todo in todos if todo["taskname"] == task_name), None)
    if task is None:
        print(f"{Colors.FAIL}Invalid task name!{Colors.ENDC}")
    else:
        print(f"{Colors.OKBLUE}Timestamp for task '{task_name}': {task['timestamp']}{Colors.ENDC}")

def edit_todo(tokens: list[str]):
    todos = load_todos()
    display_todos(todos) if len(tokens) == 1 else None
    task_name = input("Enter the task name to edit: ") if len(tokens) == 1 else tokens[1]
    task_index = next((index for (index, d) in enumerate(todos) if d["taskname"] == task_name), None)
    if task_index is None:
        print(f"{Colors.FAIL}Invalid task name!{Colors.ENDC}")
    else:
        new_task = input("Enter the new task text (leave empty to keep current): ")
        new_priority = input("Enter the new priority (high/medium/low, leave empty to keep current): ")
        new_deadline = input("Enter the new deadline (YYYY-MM-DD, leave empty to keep current): ")
        
        if new_task:
            todos[task_index]["task"] = new_task
        if new_priority:
            todos[task_index]["priority"] = new_priority
        if new_deadline:
            todos[task_index]["deadline"] = new_deadline
        
        save_todos(todos)
        print(f"{Colors.OKGREEN}Task edited!{Colors.ENDC}")

def delete_todo(tokens: list[str]):
    todos = load_todos()
    #display_todos(todos)
    pattern = input("Enter the task name or pattern to delete: ") if len(tokens) == 1 else tokens[1]
    matching_indices = [index for index, todo in enumerate(todos) if fnmatch.fnmatch(todo["taskname"], pattern)]
    
    if not matching_indices:
        print(f"{Colors.FAIL}No tasks matching the pattern '{pattern}' found!{Colors.ENDC}")
    else:
        for index in sorted(matching_indices, reverse=True):
            todos.pop(index)
        save_todos(todos)
        print(f"{Colors.OKGREEN}Tasks matching the pattern '{pattern}' deleted!{Colors.ENDC}")

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
    command = " ".join(tokens)
    History.log_history(command)
    
    todos = load_todos()
    todos = validate_todos(todos)
    action = tokens[0]
    if action == 'show' or action == '1' or action == 'list' or action == 'ls':
        display_todos(todos, pattern=tokens[1] if len(tokens) > 1 else None)
    elif action == 'add' or action == '2':
        add_todo(tokens)
    elif action == 'done' or action == '3':
        mark_done(tokens, todos, done=True)
    elif action == 'notdone' or action == '4':
        mark_done(tokens, todos, done=False)
    elif action == 'timestamp':
        gettimestamp(tokens)
    elif action == 'edit' or action == '5':
        edit_todo(tokens)
    elif action == 'delete' or action == '6':
        delete_todo(tokens)
    elif action == 'sort' or action == '7':
        sort_todos()
    elif action == 'history':
        History.print_history()
    elif action == 'exit' or action == '8':
        exit()
    elif action == 'help':
        menu()
    else:
        print(f"{Colors.FAIL}Invalid command!{Colors.ENDC}\n\nUse \"help\" for a list of available commands")
        return 1
    return 0

