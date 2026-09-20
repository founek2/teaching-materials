text = input("Zadejte první číslo: ")

num1 = int(text)
num2 = int(input("Zadejte druhé číslo: "))
operator = input("Zadej matematickou operaci: ")

result = 0
if operator == "+":     # přidáním dalšího elif lze rozšířit podporované operátory
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f'Nepodporovaný operátor: "{operator}"')
    exit(1)

print(f'Výsledek: {result}')
