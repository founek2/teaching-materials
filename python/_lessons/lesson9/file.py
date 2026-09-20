# f = open("data.raw", "w")

# f.write("ahoj1")
# f.write("ahoj2")
# f.write("ahoj3")

# f.close()

# with open("data.raw", "w") as f:
#     f.write("ahoj1")
#     f.write("ahoj2")
#     f.write("ahoj3")

with open("data.raw", "r") as f:
    # line1 = f.readline()
    # line2 = f.readline()
    # line3 = f.readline()

    for line in f:
        print(line)
