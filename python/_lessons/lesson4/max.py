# Write a Python function to find the Max of three numbers
def max(a, b, c):
    # if a <= b >= c: je ekvivalentní zápis s tímto:
    if b >= a and b >= c:
        return b
    if c <= a >= b:
        return a
    if a <= c >= b:
        return c


assert max(1, 2, 3) == 3
assert max(10, 10, 10) == 10
assert max(3, 2, 1) == 3
assert max(-10, -2, 0) == 0
