# 7. Lekce

## Procvičování funkcí

### Cvičení
<!-- This takes 2 hours for a single person -->
1. Write a Python function to find the Max of three numbers
2. that reverse a string
3. that accepts a string and calculate the number of upper case letters and lower case letters.
4. that takes a list and returns a new list with unique elements of the first list
5. that takes a number as a parameter and check the number is prime or not.
6. that checks whether a passed string is palindrome or not

[Referenční řešení](_examples/lesson4/index)

## Datové struktury 1

- tuple
- vektor
- matice

### Cvičení

1. sčítání matic
2. Načíst matici ze vstupu
    - uživatel zadá velikost: 4x3
    - následně jednotlivé řádky matice, čísla budou oddělena mezerou

## Datové struktury 2

- slovník

### Cvičení

1. překlad PSČ na název města

## List listů

U používání listů je potřeba si dát pozor, protože při jejich přiřazení, ať už do proměných nebo jiné využití, tak se listy na rozdíl od primitivních datových typů jako čísla či boolean nepředávají hodnotou, ale referencí (odkazem) - to způsobuje, že když např. předáme list jako parametr funkce, tak pokud funkce modifikuje nějakým způsobem tento list, tak změny se promítnou i do našeho listu, protože byl předán pouze referencí a tudíž tato reference odkazuje v obou případech na stejná data, která se modifikují. Co to pro nás znamená ukazuje následující ukázka:

```python
matrix_a = [[1, 2], [3, 4]]

radek_1 = [1, 2]
matrix_b = [radek_1, [3, 4]]   # -> [[1, 2], [3, 4]]

radek_1[0] = 0
matrix_b    # -> [[0, 2], [3, 4]]

def sum_matrixes(matrix_1, matrix_2):
    # potřebuji výstupní matici, který má správný rozměr
    result = matrix_1

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = suma(matrix1[i][j], matrix2[i][j])

    return result

# volání vrátí správný výsledek
sum_matrixes(matrix_a, matrix_b)    # -> [[2, 4], [6, 8]]
# ale došlo k modifikaci vstupního parametru, takové chování není u funkce pro sčítání chtěné!!
matrix_a    # -> [[2, 4], [6, 8]]
matrix_b    # -> [[0, 2], [3, 4]]
```

V ukázce vidíme, že operátor přiřazení `=` nekopíruje list, ale pouze předává referenci na daný list. Tedy pokud si potřebuji vytvořit nový list o stejném rozměru, tak si musím nový list vytvořit "ručně":

```python
def sum_matrixes(matrix_1, matrix_2):
    # varianta 1
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            # naplnění nulami
            result[i].append(0)

    # Varianta 2 s využitím násobení listů
    result = []
    for i in range(len(matrix1)):
        result.append([0] * len(matrix1[0]))

    # Intuitivně nás asi napadne i tato možnost, ovšem pozor, toto řešení není správné!!
    # vnitřní list reprezentující řádek se vytvoří jednou a pak se všude vloží jako reference - všechny řádky budou sdílet stejná data -> budou míst totožnou hodnotu při změně libovolného řádku
    result = [
            [0] * len(matrix1[0])
        ] * len(matrix1)
    # !! Chybné řešení
    ...

```

## Named parameters

Při volání funkce lze parametry předávat dle pořadí. Python je také umožňuje předávat jako tzv. "pojmenované parametry", kdy specifikuje název proměnné/parametru uvedeného v definici při volání, pak `=` a hodnotu, kterou má Python danému parametru přidělit. Toto zvyšuje v některých případech čitelnost. Např. v následující ukázce máme funkce se jménem `fce`, což nám moc neprozradí, co vlastně dělá. Ale pokud uvidímě její volání s pojmenovanými parametry `fce(delenec=10, delitel=5)`, tak nám to dává tušit, že by mohla dělit dvě čísla, aniž se podíváme do její definice.

```python
def fce(delenec, delitel, text = ""):
    print(text)
    return delenec / delitel

fce(10, 5)
fce(10, 5, "dělím čísla")
fce(10, delitel=5)
fce(delenec=10, delitel=5)
fce(delenec=10, delitel=5, text="Dělím dvě čísla")
fce(text="Dělím dvě čísla", delitel=5, delenec=10)
```

Dále si všimněte využití operátoru `=` v definici parametrů. Jedná se o tzv. "optional" neboli nepovinný parametr. Pokud při volání funkce zadáme jeho hodnotu, tak se tato hodnota nastaví, pokud však hodnotu tohoto parametru při volání nezadáme, tak se jako výchozi využije ta za operátorem `=`.
