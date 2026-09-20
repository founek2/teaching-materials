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

# proměnná  reprezentující první číslo
operand_1 = 0

# proměnná reprezentující operátor
operator = ""

# proměnná  reprezentující druhé číslo
operand_2 = 0

while True:
    vstup = input("Zadejte vstup: ")

    while not (vstup in operator_list or is_float(vstup)):
        print("Nezadali jste žádný podporovaný oparátor nebo číslo")
        vstup = input("Zadejte vstup: ")

    if vstup in operator_list:
        # první zadal uživatel operátor -> nastavím si operátor, operand_1 již obsahuje předchozí vásledek
        operator = vstup
        if operator == "q":
            break

        # načtu druhé číslo
        operand_2 = float(input("Zadejte číslo: "))
    else:
        # první zadal uživatel číslo -> načtu operátor, číslo
        operand_1 = float(vstup)
        operator = input(
            "Zadejte matematický operátor, Kalkulačka umožňuje +,-,*,/ : ")
        while operator not in operator_list:
            operator = input(
                "Nezadali jste žádný podporovaný oparátor, zadejte ho znovu: ")
        if operator == "q":
            break

        operand_2 = float(input("Zadejte číslo: "))

    if operator == "+":
        vysledek = operand_1 + operand_2
    elif operator == "-":
        vysledek = operand_1 - operand_2
    elif operator == "*":
        vysledek = operand_1 * operand_2
    elif operator == "/":
        vysledek = operand_1 / operand_2

    print(f"Výsledek je: {vysledek}")

    # nastavím operand_1 na aktuální výsledek -> příprava pro další iteraci
    operand_1 = vysledek

print("Program byl ukončen")
