def div(x, y):
    try:
        return (x/y, False)
    except ZeroDivisionError:
        return (None, True)


print("1", div(3, 2))
print("2", div(14, 0))
while True:
    a = input ("cislo")
    b = input ("cislo")

    try: 
        result = int(a) / b
        print (f"vysledek {result}")
    except ZeroDivisionError:
        print("dělitel nesmí být dva")
        exit()

    print(result)
    


print(int("12ahoj"))

# class CustomError(Exception):
#     pass
