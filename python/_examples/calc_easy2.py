"""
Důležité je si uvědomit, že nezáleží jak máme hodnoty uložené.
Ať použijeme více promněných nebo jedno pole důležité je,
že někde hodnoty máme a umíme se na ně odkázat.

Například textace nyní máme v jednom poly - na jednom místě
a pokud by jsme chtěli změnit text/opravit chybu v textu, tak
nemusíme procházet celý kód, ale vše máme na jednom místě
"""
texts = ["Zadejte první číslo: ", "Zadejte matematický operátor: ", "Zadejte druhé číslo: "]
values = []

for i in range(3):
    value = input(texts[i])
    values.append(value)

operator = values[1]
num1 = int(values[0])
num2 = int(values[2])

result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print(f'nepodporovaný operátor: "{operator}"')
    exit(1)

print(f'Výsledek: {result}')
