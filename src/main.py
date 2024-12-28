from . import todo as Todo
from . import history as Readline

def main():
    Readline.setup_readline()
    print(f"\n{Todo.Colors.HEADER}To-Do List Manager{Todo.Colors.ENDC}")
    Todo.menu()
    while True:
        tokens = Todo.take_input()
        Todo.execute(tokens) if tokens else 1
