from typing import NamedTuple
from collections import namedtuple

task = []


# title, done - True/False
Task = namedtuple("Task", "title status")

# task = Task("Posekat zahradu", False)
# task[0]
# task[1]

# task.title
# task.status


def show_menu():
    print("Menu: (pro výběr stiskněte danou klávesu)")
    for (shortcut, (text, _action)) in menu.items():
        print(f"{text} - {shortcut}")


def quit():
    print("Exiting program")


def show_done():
    pass


def show_incomplete():
    pass


def add_task():
    pass


def change_state():
    pass


def show_tasks():
    pass


menu = {
    "s": ("Show tasks", show_tasks),
    "q": ("Quit", quit),
    "d": ("Show done", show_done),
    "i": ("Show incomplete", show_incomplete),
    "a": ("Add task", add_task),
    "c": ("Change state", change_state),
    "m": ("Show menu", show_menu)
}


show_menu()
while True:
    action = input(">> ")   # s / d / i

    # if action not in menu.keys():
    if action not in menu:
        print("Nepodporovaná akce!")
        continue

    # handle appropriate action
