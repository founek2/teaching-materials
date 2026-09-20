def int2():
    raise Exception("Nastala chyba")
    return False


def int3():
    return (None, True)


print("ahoj")
res, err = int3()
if err:
    print("nastala chyba except")

print("potom")

# print("ahoj")
# try:
#     print(int2())
# except Exception:
#     print("nastala chyba except")

# print("potom")
