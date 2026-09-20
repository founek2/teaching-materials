texts = ["Zadejte první číslo: ", "Zadejte matematický operátor: ", "Zadejte druhé číslo: "]
allowed_operators = ['+', '-', '/', '*', '**', '%']

def is_float(value: str): 
    try:
        float(value)
        return True
    except:
        return False

def calculate(value_list: list):
    #[ 1, "+", 1]
    num1, operator, num2 = value_list

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2

# input("Zadej mi hodnotu: ") # return value_from_user
# print(calculate([1, "+", 1])) # 2
# print(len([1,2]))

last_result = None
while True:

    values = []  # [3, "+", 3]
    i = 0
    # for i in range(3):
    while i < 3:
        value = input("Zadej hodnotu: ")

        if value == "q":    # ukončení programu
            exit(0)

        # pokud je zadán operátor, tak zachovat řetězec,
        # jinak převést na číslo
        if value in allowed_operators:
            values.append(value)  # [+]
        else:
            # kontrola zda lze převést na číslo
            if is_float(value):
                values.append(float(value))  # [3.3]
            else:
                print("Zadal jsi nepodporovanou hodnotu. Zkus to znovu!")
                continue

        # pokud je zadán operátor jako první, tak
        # kontrola jestli existuje minulý výsledek
        # pokud ano, tak ho přidat jako první číslo
        # do pole hodnot -> Důvod? Abychom mohli využít
        # stejný kód pro výpočet v obou případech
        if value in allowed_operators and i == 0:
            if last_result == None:     # pokud není poslední výsledek -> zeptat znovu na hodnotu
                print("Předchozí výpočet neexistuje")
                values.pop()    # odeber operátor
                continue
            else:
                values.insert(0, last_result)
                i += 1      # v poli již máme operátor a insert přídal první číslo na pozici 0 -> již potřebujeme pouze jednu hodnotu načíst
        i += 1

    print("values: ", values)

    result = calculate(values)

    print(f'Výsledek: {result}')
    last_result = result
