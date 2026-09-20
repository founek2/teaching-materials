# 3. Lekce

### 3.1 Kalkulačka - zjednodušená

Vytvořte program, který se uživatele zeptá nejprve na jedno číslo, matematický operátor a nakonec na druhé číslo. Tyto 3 vstupy uložte do přemněných a pomocí podmínek otestujte jestli operátor je jeden z `+ - * /`, pokud ano, tak spočítejte hodnotu výrazu a zobrazte ji uživateli. Pokud operátor není jeden z povolených, tak vypište nějaký text jako chybovou hlášku a zavolejte funkci `exit` s parametrem 1 - funkce exit ukončí běh programu a číslo 1 signalizuje, že nastala chyba.

[Referenční_řešení](_examples/calc_easy)

## Komentáře v kóde

```python
# tento blok dělá nějaký
# magic
if 99 < 10 and 30 > 1:
    ...

"""
Víceřádkový dokumentační
řetězec - primárně pro komentáře funkcí/objektů
"""
```

## Fce Range - parametry

Funkci range lze zavolat s různým počtem parametrů. Pokud dostane pouze jeden argument `n`, tak vrátí posloupnost začínající od 0 s n prvky -> tedy 0,1,2,...,n-1  
Pokud předáme parametry 2 např. `range(2, 10)`, tak návratová hodnotu bude posloupnost začínající číslem 2 a končí číslem 9 (parametr je exkluzivní) -> tedy 2,3,4,...,9  
Další možnost je předat parametry 3 např. `range(1, 10, 2)`. První parametr opět udává počátek posloupnosti a druhý exkluzivní maximální hodnotu, třetí parametr určuje krok. Tedy v našem případě výsledná posloupnost bude 1,3,5,7,9

## List

Dalším důležitým datovým typem je List (v jiných jazycích známí jako pole). V tomto typu lze uložit libovolné množství dat, která spolu často nějak souvisí ale nemusí, a následně na ně přistupovat pomocí indexů. S tímto přístupem jsme se již setkali při přistupování na jednotlivá písmena v řetězci. Výhoda je že pro tisíc hodnot nemusíme mít tisíc promněných ale pouze jednu typu List a jednotlivé hodnoty jsou přistupné pomocí indexů. Příklad použití:

```python
promnena = [14, 20, 10, 1, 60, "Kitty", -0.24]      # Do listu lze ukládat současně hodnoty různých typů
          #  └──index začíná na 0

promnena[0]     # -> 14
promnena[5]     # -> "Kitty"

for prvek in promnena:
    print(prvek)        # -> bude vypisovat jednotlivé prvky od nultého indexu až po poslední

promnena.append("Hello")    # přidá nový prvek na konec listu
# promnena = [14, 20, 10, 1, 60, "Kitty", -0.24, "Hello"] 

promnena.pop()    # Odebere poslední prvek
# promnena = [14, 20, 10, 1, 60, "Kitty", -0.24] 
```

### 3.2.x Cvičení na pole

* Vytvořte promněnou s prázdnám polem a vložte do něj prvky 100 až 199 (nedělejte to manuálně, ale použijte cyklus). Následně vypište každý třetí prvek z daného pole.
* Vytvořte list s alespoň 10 čísly a následně spočítejte průměr z hodnot

## Tuple

Datový typ tuple není nic jiného než n-tice. Lze si ho představit jako list, které pokud je jednou vytvořen, tak nelze měnit jeho prvky ani je přidávat či odebírat. Pro procházení lze využít stejný způsob jako u listu.

```python
ntice = (14, 20, 10, 1, 60, "Kitty", -0.24)      # Do listu lze ukládat současně hodnoty různých typů
      #  └──index začíná na 0

ntice[0]     # -> 14
ntice[5]     # -> "Kitty"

for prvek in ntice:
    print(prvek)        # -> bude vypisovat jednotlivé prvky od nultého indexu až po poslední
```

## While cyklus

```python
i = 0
while i < 10:
    ... # some magic

    print(i)
    i += 1

for i in range(10):
    ...

    print(i)

# Výstup obou cyklů bude identický - vypíší čísla od 0 až do 9
```

Cyklus while se nejčastěji využívá pokud předem nevíme kolikrát budeme potřebovat kód zopakovat. Můžeme v průběhu měnit hodnotu řídící promněné - snižovat/zvyšovat. Díky tomu získáme cyklus s promněnou délkou opakování. Další časté využití:

```python
running = True
while running:
    ... # some magic

    if promnena == 3:
        running = False
```

## Konstruktory primitivů

Není '3' (textový řetězec) stejné jako 3 (celé číslo)

* 3 / `int`
* 0\. / `float`
* `bool`
* `''` / `""` / `str()`
* `[]` / `list()`
* `,` / `tuple()`
