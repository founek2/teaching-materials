# 1. Lekce

> Stolní pc:
>
> - user: Guest
> - password: Akademie19

## Co je python?

- skriptovací programovací jazyk
  - výchozí interpret CPython
- Vznikl v roce 1991
- často využíván v OS Linux, Data science
- dobře čitelný - narozdíl od Javy C++ a jiných

## Jak ho zapnout?

V terminálu lze jednoduše vyvolat interpret příkazem: `python3`.
Spustí se prostředí a nyní lze přímo psát python kód, kde po stisknutí klávesy enter se řádek vyhodnotí a zobrazí se jeho výstup (přesněji hodnota daného výrazu).

## Proměnné I

- symbolické jméno pro hodnotu
- krabička s názvem

## Primitivní datové typy

- str - string, textová hodnota `promnena = "nějaká hodnota"`
- bool - `promnena = True`
- int - `promnena = 123`
- float - `promnena = 0.981`

## Podmínky

```python
promena = 3
if promena > 4:                      # vyhodnotí se False
    print("promena je větší než 4")
elif promena < 1:                    # vyhodnotí se False
    print("promena je menší než 1")
else:                                # výchozí chování, pokud žádný if nebyl splněn
    print("promena je v rozsahu: 1 <= promnena <= 4")
```

## Volání funkce?

Každá funkce má nějaký název, pomocí kterého na ni lze odkázat. Při volání za jméno přidáme závorky. Tedy pokud chceme zavolat funkci pro výpis textu s názvem print, tak stačí `print()`. Takto ale funkce neví, co má vypsat, takže je potřeba ji předat nějakou hodnotu. To lze udělat tak, že se jednotlivé hodnoty napíší do závorek. Pokud jich je více, tak se oddělují čárkou. Např. výpis slova "#strahov" -`print("#strahov")`. Jednotlivé hodnoty v závorkách se označují jako `parametry`.

## Základní vestavěné funkce (built-in)

- `print()` - parametry: co chci vypsat
- `input()` - parametr: text který se zobrazí uživateli
- `range()` - parametry: (od, do, krok) - do je exkluzivní, tedy range(1, 9) jsou čísla 1-8
- `len()` - parametr: textový řetězec (vrátí počet jeho znaků)

## Cvičení

### 1.1.1 Čísla

- Sečtěte čísla 1, 5 a 98
- Spočtěte třetí mocninu čísla 11
- Spočtěte kolikrát se vejde číslo 7 do 51
- Zjistěte zbytek po dělení 15 / 4 (nápověda: výsledek je celočíselný 0 <= x < 4)

> CheatSheet pro matematické operátory:
>
> - `+` sčítání: 3 + 10 -> 13
> - `-` odčítání: 3 - 10 -> -7
> - `/` dělení: 9 / 2 -> 4.5
> - `//` celočíselné dělení (odsekne zbytek) 9 // 2 -> 4
> - `%` zbytek po dělení 9 % 2 -> 1
> - `**` umocní číslo před operátorem na číslo za operátorem 2 \*\* 3 -> 8

### 1.1.2

Ukázka kódu, který kontroluje podle počtu uzlů grafu, zda se může jednat o graf:

```python
edges = 4

if  edges > 0:
    is_graph = True
elif edges == 4:
    has_four = True
else:
    is_graph = False
```

- Jakou hodnotu budou mít proměnné `is_graph` a `has_four`?
- Jak lze kód úpravit, aby graf mohl mít 0 hran? (pokud má 1 vrchol, tak má 0 hran a jedná se o graf)
- pomocí funkce `input` načtěte své jméno do proměnné `name` a následně vypište text "Tvé jméno je Martin a jsi na hodině Pythonu" - místo "Martin" dosaďte obsah proměnné `name` (tedy své jméno)

## Řetězce

U řetězcu se dá doptat na jednotlivé znaky pomocí pozice. Pozice vždy začíná na 0 a získat n-tý znak se dá takto:

```python
text = "Nice kitty"
text[0]     –> "N"
text[1]     –> "i"
text[2]     –> "c"
text[3]     –> "e"
text[4]     –> " "
.
.
text[9]     –> "y"
```

Dále funguje také dotazování na pozice od zadu (záporná adresace). Poslední znak získáme `text[-1]`, předposlední `text[-2]` atd.

### 1.2.{1-3} Řetězce

- Vypište počet znaků ve vašem jméně. Pro načtení jména použijte funkci `input()`.
- Vypište 3. znak z vašeho jména.
- Vypište poslední znak z vašeho jména.

> ## Řetězce formátování
>
> Jednotlivé řetězce jdou spojovat pomoci operátoru `+` nebo lze využít moderní přístup tzv. f-strings. Stačí před uvozovky řetězce dát písmeno `f` a v řetezci lze do závorek `{}` napsat proměnnou, která si při zpracování nahradí svojí hodnotou.
>
> ```python
> game = 'Lineage II'
> 'Moje nejoblíbenější pc hra je' + ' ' + game # výstup -> "Moje nejoblíbenější pc hra je Lineage II"
> f'Moje nejoblíbenější pc hra je {game}' # výstup -> "Moje nejoblíbenější pc hra je Lineage II"
> ```

### 1.2.4 Řetězce

Vypište následující text s použitím pouze jednoho volání funkce print, `jméno` a `počet` nepište do textu napřímo, ale uložte si je do proměnné a ty využijte pro výpis.

```python
Jmenuji se {vaše jméno} a na Strahově jsem již {počet} let
```
