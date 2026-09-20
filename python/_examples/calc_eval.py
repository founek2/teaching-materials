print("Ahoj, toto je kalkulacka, ktera skoro nic neumi.")
print("Budes postupne zadavat operandy a zakladni operatory.")
print("Kalkulacka pote vrati vysledek.")
print()


def give_me_operator():
    operator = input("Zadej operator: ")
    while operator not in operators:
        print("Chybny operator.")
        operator = input("Zadej operator (+, -, *, /): ")

    return operator


operators = ["+", "-", "*", "/"]
konec = "a"
prev_result = 0

while konec != "q":
    operand_a = input("Zadej vstup: ")

    if operand_a in operators:
        operator = operand_a
        operand_a = str(prev_result)
    elif operand_a == "q":
        exit()
    else:
        operator = give_me_operator()

    operand_b = input("Zadej druhy vstup: ")
    prev_result = eval(operand_a + operator + operand_b)
    print(f"vysledek je {prev_result}")
