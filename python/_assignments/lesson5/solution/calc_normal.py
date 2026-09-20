operator_list = ["+", "-", "/", "*", "q"]
print("Byl spuštěn program Kalkulačka, který umožnuje sčítaní, odečítání, násobení a dělení")
print("Program Vás nejprve vyzve pro zadání čísla, následně Vás vyzve pro zadání matematického operátoru (+,-,*,/), poté k dalšímu číslu")
print("Pokud zadáte matematický operátor jako první operand se bude brát předešlý výsledek, pokud číslo tak program Vás postupně vyzve pro zadání operátoru a poté čísla, pokud zadáte q program se ukončí. Pokud zadáte operátor a číslo a ještě žádný předešlý výsledek neexistuje, tak se vezme jako výchozí hodnota 0.")


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def nacteni_cisla():
    string = input("Zadejte číslo: ")

    while is_float(string) == False:
        print("Nezadali jste číslo, zadejte ho znovu!")
        cislo = input("Zadejte číslo: ")

    cislo = float(string)
    return cislo


operand_1 = 0

while True:
    vstup = input("Zadejte vstup: ")

    while not (vstup in operator_list or is_float(vstup)):
        print("Nezadali jste žádný podporovaný oparátor nebo číslo")
        vstup = input(
            "Zadejte vstup: ")

    if vstup == "q":
        break

    if vstup in ["+","-","/", "*"]:
        operator = vstup
        # TODO nekontroluje se, zda bylo zadáno číslo
        operand_2 = nacteni_cisla()
    else:
        operand_1 = float(vstup)
        operator = input(
            "Zadejte matematický operátor, Kalkulačka umožňuje +,-,*,/ : ")
        while operator not in operator_list:
            operator = input(
                "Nezadali jste žádný podporovaný oparátor, zadejte ho znovu: ")

        # TODO tady se číslo kontroluje
        operand_2 = nacteni_cisla()

    if operator == "+":
        vysledek = operand_1 + operand_2
    elif operator == "-":
        vysledek = operand_1 - operand_2
    elif operator == "*":
        vysledek = operand_1 * operand_2
    elif operator == "/":
        vysledek = operand_1 / operand_2

    operand_1 = vysledek
    print(f"Výsledek je: {vysledek}")

# TODO program nikdy nedojde sem na konec - nelze ukončit pomocí "q"
print("Program byl ukončen")
