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


while True:
    vstup = input("Zadejte vstup: ")

    while not (vstup in operator_list or is_float(vstup)):
        print("Nezadali jste žádný podporovaný oparátor nebo číslo")
        vstup = input(
            "Zadejte vstup: ")

    if vstup in operator_list:
        operator = vstup
        # TODO nekontroluje se, zda bylo zadáno číslo
        operand_2 = float(input("Zadejte číslo: "))
    else:
        operand_1 = float(vstup)
        operator = input(
            "Zadejte matematický operátor, Kalkulačka umožňuje +,-,*,/ : ")
        while operator not in operator_list:
            operator = input(
                "Nezadali jste žádný podporovaný oparátor, zadejte ho znovu: ")

        # TODO tady se číslo kontroluje
        operand_2 = input("Zadejte číslo: ")
        while not is_float(operand_2):
            operand_2 = input("Zadejte číslo: ")
        operand_2 = float(operand_2)

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
