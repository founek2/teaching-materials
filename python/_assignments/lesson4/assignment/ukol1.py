def suma_hodnot():
    ...


assert suma_hodnot([10]) == 10
assert suma_hodnot([20, 30]) == 50
assert suma_hodnot([10, 10, 10, 10, 10]) == 50
assert suma_hodnot([1, 2, 3, 4, 5]) == 15
assert suma_hodnot([20, 20]) == 40
hodnoty = []
for i in range(100):
    hodnoty.append(i)
assert suma_hodnot(hodnoty) == 4950
assert suma_hodnot([1, 1, 1]) == 3

