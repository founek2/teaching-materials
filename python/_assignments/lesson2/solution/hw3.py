text = "Zadejte cele cislo: "

a = int(input(text))

suma = 0
while a != 0:
    suma = suma + a
    print("Aktualni suma = ", suma)
    print("Pro ukonceni napište 0")
    a = int(input(text))
