# that takes a list and returns a new list with unique elements of the first list

def uniq(list):
    values = []

    for x in list:
        if x not in values:
            values.append(x)

    return values


assert uniq([1, 2, 3]) == [1, 2, 3]
assert uniq([10, 10, 3]) == [10, 3]
assert uniq([10, 2, 10]) == [10, 2]
assert uniq([15, 5, 0, -3, 2, 1, -1, 0, 0, 0, 0]) == [15, 5, 0, -3, 2, 1, -1]
assert uniq([]) == []
