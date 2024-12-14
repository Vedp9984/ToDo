from todo import menu, take_input, execute, Colors
def main():
    print(f"\n{Colors.HEADER}To-Do List Manager{Colors.ENDC}")
    menu()
    while True:
        tokens = take_input()
        execute(tokens) if tokens else 1

if __name__ == "__main__":
    main()
