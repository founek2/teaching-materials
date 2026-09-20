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
    print("""
        Show all - s
        Show done - d
        Show incomplete - i
        Add task - a
        Change state - c
        Show menu - m
        Delete task - del
        Quit - q
    """)


def quit():
    print("Exiting program")
    exit(0)


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


show_menu()
while True:
    action = input(">> ")   # s / d / i

    if action not in ["s", "d", "i", "a", "c", "m", "q"]:
        print("Nepodporovaná akce!")
        continue

    if action == "s":
        show_tasks()
    elif action == "d":
        show_done()
    elif action == "i":
        show_incomplete()
    elif action == "a":
        add_task()
    elif action == "c":
        change_state()
    elif action == "m":
        show_menu()
    elif action == "q":
        quit()
