import os
import platform
from functools import partial
from collections import namedtuple

clear_console = partial(os.system, 'cls' if platform.system() == 'Windows' else 'clear')


Task = namedtuple('Task', 'text state')
tasks = []

def to_text(state):
    return 'Done' if state else "Incomplete"

def show_all():
    print("Všechny úkoly:")

    for text, state in tasks:
        print(text, "-", to_text(state))

def show_done():
    print("Hotové úkoly:")

    for text, state in tasks:
        if state == True:
            print(text, "-", to_text(state))

def show_incomplete():
    print("Nedokončené úkoly:")

    for text, state in tasks:
        if state == False:
            print(text, "-", to_text(state))

def add_task():
    text = input("Co? ")
    while len(text) <= 1:   # možno přidat složitější validaci
        text = input("Co? ")

    tasks.append(Task(text, False))
    print("Přidáno")

def exit_program():
    exit()


def show_menu():
    clear_console()
    print("Menu: (pro výběr stiskněte danou klávesu)")
    for text, cmd, _ in MENU:
        print(text, '-', cmd)

def show_ids():
    print("Select task:")

    for i, task in enumerate(tasks):
        text, state = task
        print(f'[{i}]', text, "-", to_text(state))
    
def change_state():
    show_ids()

    text = input("\nID done/inc> ")
    num, state = text.split(' ')
    id = int(num)
    tasks[id] = Task(tasks[id].text, True if state == "done" else False)


MENU = (
    ('Show all', 's', show_all),
    ('Show done', 'd', show_done),
    ('Show incomplete', 'i', show_incomplete),
    ('Add task', 'a', add_task),
    ('Change state', 'c', change_state),
    ('Show menu', 'm', show_menu),
    ('Quit', 'q', exit_program),
)


if __name__ == "__main__":
    while(True):
        show_menu()

        while True:
            cmd = input("\n>")
            for _, cmd_ref, fn in MENU:
                if cmd == cmd_ref:
                    fn()
                    break