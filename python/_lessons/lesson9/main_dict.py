from typing import NamedTuple
from collections import namedtuple


# def namedtuple(name, fields):
#     def fn():
#         pass

#     return fn


store = []
mappingToText = {True: "Complete", False: "Incomplete"}
mappingToBool = {"Complete": True, "Incomplete": False}

# title, done - True/False
Task = namedtuple("Task", "title done")


# t = Ahoj("jmeno", "nazev", False)
# t.title # t[0] "nazev"
# t.done # False

t = ("nazev", False)
t[0]
t[1]

# task = Task("Posekat zahradu", False)
# task[0]
# task[1]

# task.title
# task.done


def export_to_file():
    with open("ukoly.txt", "w") as file:

        for task in store:
            # title:True
            # "task.title task.done"
            file.write(f"{task.title}:{task.done}\n")


def show_menu():
    print("Menu: (pro výběr stiskněte danou klávesu)")
    for (shortcut, (text, action)) in menu.items():
        print(f"{text} - {shortcut}")


def quit():
    print("Exiting program")
    # save to save...
    export_to_file()
    exit()


def show_done():
    print("Hotové úkoly:")
    for task in store:
        if task.done:
            print(f"{task.title} - Complete")


def show_incomplete():
    print("Nehotové úkoly:")
    for task in store:
        if not task.done:
            print(f"{task.title} - Incomplete")


def add_task():
    title = input("zadej název úkolu: ")
    print(Task)
    task = Task(title, False)
    store.append(task)


def change_state():
    # 1. vypsat úkoly s indexi
    # 0 - Posekat - Incomplete
    # 2. načíst od uživatele index a nový stav
    # >> 0 Complete

    print_all_with_index()

    # vstup = input("Zadej číslo a nový stav: ")
    # [idStr, newState] = vstup.split(" ")
    # idx = int(idStr)

    # origTask = store[idx]
    # store[idx] = Task(origTask.title, mappingToBool[newState])

    # Varianta 2, uživatel zadá pouze index, a stav znegujeme
    vstup = input("Zadej číslo: ")
    idx = int(vstup)

    origTask = store[idx]
    store[idx] = Task(origTask.title, not origTask.done)


def print_all_with_index():
    print("Všechny úkoly:")
    for i in range(len(store)):
        task = store[i]
        print(f"{i} {task.title} - {mappingToText[task.done]}")


def show_tasks():
    """"
        Všechny úkoly:
        Posekat trávu - Incomplete
        Vyvenčit psa - Incomplete
    """

    # Variant 1
    # for task in store:
    #     if task.done:
    #         print(f"{task.title} - Complete")
    #     else:
    #         print(f"{task.title} - Incomplete")

    # Variant 2
    print("Všechny úkoly:")
    for task in store:
        print(f"{task.title} - {mappingToText[task.done]}")

    # Variant 3
    # for task in store:
    #     if task.done:
    #         status = "Complete"
    #     else:
    #         status = "Incomplete"

    #     print(f"{task.title} - {status}")

    # # Variant 4
    # for task in store:
    #     status = "Complete" if task.status else "Incomplete"
    #     print(f"{task.title} - {status}")


def remove_task():
    print_all_with_index()

    idx = int(input("Zadej číslo> "))

    store.pop(idx)


menu = {
    "s": ("Show tasks", show_tasks),
    "q": ("Quit", quit),
    "d": ("Show done", show_done),
    "i": ("Show incomplete", show_incomplete),
    "a": ("Add task", add_task),
    "c": ("Change state", change_state),
    "m": ("Show menu", show_menu),
    "r": ("Remove task", remove_task)
}


show_menu()
while True:
    action = input(">> ")   # s / d / i

    # if action not in menu.keys():
    if action not in menu:
        print("Nepodporovaná akce!")
        continue

    # handle appropriate action

    # menu[action][1]()
    # VS
    text, fn = menu[action]
    fn()
