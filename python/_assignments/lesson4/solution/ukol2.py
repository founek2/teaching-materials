def is_rectangle(point_a, point_b, point_c, point_d):
    ...


assert is_rectangle([0, 0], [20, 0], [20, 50], [0, 50])
assert is_rectangle([-10.5, 15.8], [178.23, 15.8],
                    [178.23, -67.2], [-10.5, -67.2])
assert is_rectangle([0, -4], [4, 0], [0, 4], [-4, 0])
assert is_rectangle([0, -4], [4, 0], [0, 4], [-6, 0]) == False
assert is_rectangle([0, 0], [20, 0], [0, 50], [20, 30]) == False
