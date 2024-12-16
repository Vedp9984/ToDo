import os
import datetime

HISTORY_FILE = os.path.expanduser("~/todo_history.log")
def log_history(command: str):
    timestamp = datetime.datetime.now().isoformat()
    with open(HISTORY_FILE, "a") as file:
        #print(f"writing to log : {timestamp} - {command}")
        file.write(f"{timestamp} - {command}\n")

def print_history():
    if not os.path.exists(HISTORY_FILE):
        print("No history found!")
        return
    with open(HISTORY_FILE, "r") as file:
        for line in file:
            print(line, end="")