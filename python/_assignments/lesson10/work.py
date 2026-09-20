shape = (2, 2)

plane = []  #
for i in range(shape[0]):
    plane.append([])
    for col in range(shape[1]):
        plane[i].append(" ")

# [[" " for r in range(shape[1])] for i in range(shape[0])]


def show_plane():

    for i in range(shape[0]):
        print(f"   {i}", end="")
    print()

    for i in range(shape[0]):
        print(i, end="  ")
        # print("  ", end="")
        for col in range(shape[1] - 1):
            print(plane[i][col], end="")
            # if col != shape[1] - 1:
            #   print(" | ", end="")
            print(" | ", end="")
        print(plane[i][-1])


def space_exists():
    # a =  [1, 2, 3, 4, 5]
    # for val in a:
    #     if val == 1:
    #         return True

    for row in plane:
        for mark in row:
            if mark == " ":
                return True

    return False


def won(player, row_number, column_number):
    # 3 kombinace
    # row = plane[row_number]
    # cnt = 0
    # if row[column_number - 1] == player:
    #     cnt += 1
    # if row[column_number + 1] == player:
    #     cnt += 1

    # if cnt == 2:
    #     return True

    row = plane[row_number]

    cnt = 0
    for val in row[column_number + 1:]:
        if val == player:
            cnt += 1
        else:
            break

    for val in reversed(row[0:column_number]):
        if val == player:
            cnt += 1
        else:
            break

    return cnt >= 2


show_plane()

player = "X"    # "X" | "O"
while space_exists():
    name = "Hráč2" if player == "O" else "Hráč1"
    text = input(f'Hraje {name}, zadej [0-9][0-9]:')
    # [row, col] = text.split(",")
    row = int(text[0])
    col = int(text[1])

    if plane[row][col] != " ":
        print("Již obsazeno!")
        continue

    plane[row][col] = player

    print("-------\n")
    show_plane()

    # player = "X" if player == "O" else "O"
    if player == "O":
        player = "X"
    else:
        player = "O"

print("Hra skončila - remíza")
