# Essential shell functions - for history and readline
import os
import datetime
import readline

HISTORY_FILE = os.path.expanduser("~/.todo_history.log")
def log_history(command: str):
    timestamp = datetime.datetime.now().isoformat()
    with open(HISTORY_FILE, "a") as file:
        #print(f"writing to log : {timestamp} - {command}")
        file.write(f"{timestamp} - {command}\n")

def print_history():
    i = 0
    if not os.path.exists(HISTORY_FILE):
        print("No history found!")
        return
    with open(HISTORY_FILE, "r") as file:
        for line in file:
            i = i + 1
            print(f"{i} {line}", end="")
            #print(line, end="")

def setup_readline():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            for line in file:
                #print(f"it is {line}")
                command = line.split(" - ", 1)[1].strip()
                #print(f"Adding to history: {command}")
                readline.add_history(command.strip())
    readline.set_history_length(1000)
    #atexit.register(readline.write_history_file, HISTORY_FILE)

