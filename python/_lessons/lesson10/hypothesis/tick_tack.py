""" Tic Tac Toe
----------------------------------------
"""
import random
player1 = "X"
player2 = "O"
empty = " "

shape = (7, 7)
win_count = 3
plane = [[empty for i in range(shape[1])] for i in range(shape[0])]


def space_exist():
    for row in plane:
        if empty in row:
            return True

    return False


def print_plane():
    print("   ", end="")
    for i in range(shape[1]):
        print(i, end="   ")
    print()

    for (row, rowNum) in zip(plane, range(shape[0])):
        print(rowNum, end="  ")
        for mark in row[: -1]:
            print(mark, end=" | ")
        print(row[-1], end="")
        print()


def won(player, r, c):
    cnt_horizontal = 0
    for char in reversed(plane[r][0:c]):
        if char == player:
            cnt_horizontal += 1
        else:
            break
    for char in plane[r][c:]:
        if char == player:
            cnt_horizontal += 1
        else:
            break

    cnt_vertical = 0
    for i in reversed(range(r)):
        char = plane[i][c]
        if char == player:
            cnt_vertical += 1
        else:
            break
    for i in range(r, len(plane)):
        char = plane[i][c]
        if char == player:
            cnt_vertical += 1
        else:
            break

    return cnt_vertical >= win_count or cnt_horizontal >= win_count


def player_to_text(player):
    return "Player1" if player == player1 else "Player2"


print(f'Player1 is [{player1}] and player2 is [{player2}]')

player = player1
while space_exist():
    print("--------\n")
    print_plane()
    print(
        f'#{player_to_text(player)} your move ! [0-9][0-9] : ', end='')
    [rowNumber, columnNumber] = input()
    rowNumber, columnNumber = int(rowNumber), int(columnNumber)

    if plane[rowNumber][columnNumber] != empty:
        print("!Occupied!")
        continue

    plane[rowNumber][columnNumber] = player

    if won(player, rowNumber, columnNumber):
        print_plane()
        print(f'{player_to_text(player)} have won!')
        exit()

    player = player2 if player == player1 else player1
