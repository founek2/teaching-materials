# 8. Lekce

## Cesta k TODO aplikaci

Nyní již známe základní "stavební" prvky a je na čase si napsat složitější aplikaci. Zde je zadáno několik cvičení, které zdánlivě spolu nesouvisí, ale jsou sestavená tak, abyste si osvojili a vyzkoušeli si vše, co budete potřebovat pro závěrečnou aplikaci. Výsledkem bude TODO aplikace - pro ty co nevědí, tak se jedná o aplikaci, do které si poznamenáte úkol (co chcete udělat) a následně vidíte přehled všech úkolů a jejich stav - jestli jsou hotové nebo ne. Tedy aplikace se bude skládat z těchto funkcionalit:

Vytvoření nového úkolu

- Zobrazení všech úkolů
- Zobrazení hotových
- Zobrazení nehotových
- Změna stavu úkolu na hotový/nehotový

Později rozšíříme o tyto:

- Při vypnutí uložení úkolů do souboru
- Po zapnutí načtení úkolů ze souboru

## Namedtuple

Již jsme si představili datový typ [tuple](#tuple). Namedtuple je vylepšená varianta. Pokud u klasického tuplu chceme přistupovat na určitou pozici, tak musíme využít indexaci a to není moc přehledné. Např. `pozice[3]` nám na první pohled nic moc neřekne, ale pokud bysme mohli toto `pozice.osaY`, tak by to bylo mnohem čitelnější. A to je přesně to, co nám namedTuple nabízí. Ve své podstatě se chová stále stejně jako obyčejný tuple, ale kromě adresace přes index nám přidává možnost přístupu přes názvy viz ukázka:

```python
from collections import namedtuple

Point = namedtuple('Point', 'x y')

point1 = Point(10, 15)
point1.x    # -> 10
point1[0]   # -> 10
point1.y    # -> 15
point1[1]   # -> 15

type(point1)    # -> <class '__main__.Point'>


Dog = namedtuple('Dog', 'legs head color')

my_dog = Dog(10, 1, 'red')
my_dog.color       # -> 'red'

type(point1)    # -> <class '__main__.Dog'>
```

## Exceptions

V každém programovacím jazyce++++++++

+++6
+
+
3
++++

.3+-

+-+
+.63
+
.36+9*-9+3
.3+69

+-
+-je potřeba nějakým způsobem signalizovat chybový stav. Např. pokud se snažíme dělit nulou, předáme do funkce jiný počet parametrů než je povoleno atd... Nejpoužívánější jsou dva přístupy - první pomocí Exceptions (vyjímek) které využívá python a druhá možnost je v návratové hodnotě funkce vždy s výslednou hodnotou předat chybový stav. Malá ukázka:

```python
# Exceptions
try:
    number = int('Kitty')
except Exception:
    print('Some error occurred')


# Předání chyby návratovou hodnotou
# pouze ukázka, v Pythonu fce int() takto nefunguje

number, error = int('Kitty')

if error:
    print('Some error occurred')
```

Oba přístupy mají svoje výhody a nevýhody. Python se rozhodl pro variantu s Exceptions a té se budeme věnovat i my (druhá metoda jde ve vlastních funkcí používat i v Pythonu, ale konvence je používat všude Exceptions).

> seznam [built-in exceptions](https://docs.python.org/3.8/library/exceptions.html)

### Jak to funguje?

Funkce u které se předpokládá, že může nastat chyba (např. funkce int() - chyba např. při volání `int('21at')` - neobsahuje pouze čísla) a potřebuje o tom informovat toho kdo jí volá, tak může vyhodit vyjímku. Jak to udělat? Na to existuje klíčové slovo `raise` - tímto Python zařídí že v daném místě se přeruší vykonávání kódu a vyhodí vyjímku. Zpracování kódu pokračuje v místě kde je odchycení vyjímku - blok `expect`, pokud daná funkce nebyla v bloku `try` a vyhodí vyjímku, tak python ukončí celá skript. Ukázka:

```python
def fn_only_str(param):
    if type(param) == str:
        return True
    else:
        raise Exception('Invalid Parametr')

try:
    fn_only_str("Ahoj 23")
    print('1 was a str')
    fn_only_str([])     # -> raise Eception -> stop execution -> continue in except
    print('2 was a str')
except Exception:
    print("exception called")   # Python continues here

```

Na ukázce víše jsou vidět nová klíčová slova `try` a `except`. Slovo `try` uvozuje začátek bloku kde se předpokládá, že nějaká chyba může nastat. A jak poznáme že může nastat? U vlastních funkcí víme jestli mohou vyhodit nějakou exceptions a u vestavěných funkcí se musíme podívat do dokumentace. Dále slovo `except` uvozuje blok kódu, který se vykonná v případě, že v `try` nastane nějaká vyjímka - všimněte si, že za slovem `except` následuje ještě slovo `Exception` - to označuje pro jaký druh vyjímky se blok má provést. Vyjímek máme spoustu druhé a všechny jsou potomkem `Exception`. Jestli nevíte co je potomek nevadí, pro nás to znamená, že pokud chceme except využít pro libovolnou vyjímku, tak stačí dát Exception. Ukázka pro různé druhy vyjímek:

```python
try:
    number = int(input('Zadej číslo'))
except ValueError:
    print('Passed bad value')
except IOError:
    print("problem with file")  # could happend if in try was operation with file for example
except Exception:   # Other exceptions
    print("Something bad happend")
```

## import os

Modul [os](https://docs.python.org/3/library/os.html) obsahuje nástroje pro práci s operačním systémem - např. pro práci se soubory, terminálem a spoustu dalšího. Nás tu bude zajímat jedna funkce a to `os.system()`, které můžeme předat v argumentu příkaz, který vykoná v terminálu. U konzolových aplikací občas potřebujeme vyčistit výstup terminálu od výpisů a to můžeme právě pomocí této funkce.

> Slovem `import` můžeme načíst další moduly, které rozšiřují funkcionalitu, kterou můžeme využít. Počet built-in funkcí je omezen a občas se hodí i jiné. Např. pro dělení jsme si ukazovali modul [math](https://docs.python.org/3/library/math.html), které obsahuje pokročilejší matematické operace.

Ukázka:

```python
import os

-+
+-os.system('clear')      # OS Linux/Mac
os.system('cls')        # Windows

import math
math.sqrt(4)        # 2.0
```

Co se stane? Python spustí subshell (podproces) ve kterém zavolá daný příkaz - tedy otevře terminál a tam zadá text "clear" a dá entr.

## Fce Fce Fce

Zde vás chci upozornit, aby jste se nebáli používat funkce co nejčastěji. Souvislý kód dlouhý napříkad 300 řádků je sice hezký a 5 minut po tom, co ho napíše se v něm ještě vyznáte, ale za půl hodiny již budete ztracení. Proto je lepší klidně zadefinovat 10 funkcí, každá bude mít 10 řádků, ale výsledek bude mnohem čitelnější, protože názvem funkce do kódu vkládáte jakýsi komentář. Ukázka:

```python
# blok bez funkcí
ab = (abs(point_a[0] - point_b[0]), abs(point_a[1] - point_b[1]))
ac = (abs(point_a[0] - point_c[0]), abs(point_a[1] - point_c[1]))
ad = (abs(point_a[0] - point_d[0]), abs(point_a[1] - point_d[1]))
bc = (abs(point_b[0] - point_c[0]), abs(point_b[1] - point_c[1]))
bd = (abs(point_b[0] - point_d[0]), abs(point_b[1] - point_d[1]))
cd = (abs(point_c[0] - point_d[0]), abs(point_c[1] - point_d[1]))

# To stejné s funkcemi
def calc_distance(a, b):
    return abs(a[0] - b[0]), abs(a[1] - b[1])

ab = calc_distance(point_a, point_b)
ac = calc_distance(point_a, point_c)
ad = calc_distance(point_a, point_d)
bc = calc_distance(point_b, point_c)
bd = calc_distance(point_b, point_d)
cd = calc_distance(point_c, point_d)
```

### 1.1 Namedtuple

Nadefinujte namedtuple House - vymyslete mu 5 vlastností, vytvořte si proměnnou s daným namedtuple. Vypište si jednotlivé vlastností pomocí indexace a pomocí tečkové notace. Pokuste se pomocí `=` změnit hodnotu nějaké vlastnosti a zamyslete se nad výstupem (okomentujte, proč se to stalo).

### 1.2.1 Exceptions

Napište program, který bude ošetřovat vstup od uživatele. Potřebujete od něj načíst celé číslo, desetinné číslo, text minimální délky 10, bool hodnotu a matematický operátor (jeden z [+, -, \, =, %]). Vždy po zavolání fce `input` proveďte potřebnou kontrolu a přetypování pomocí [konstruktorů](#Konstruktory-primitivů). Pro kontrolu využijte vyjímky - při pokusu přetypování řetězce od uživatele konstruktory mohou vyhodity při chybě vyjímku... využijte toho

### 1.2.2

Napište vlastní funkci, která bude brát dva parametry - první typu number a druhý typu list. Pokud se typy budou lišit vyhoďte `ValueError`, jinak zjistěte index v listu pro číslo v prvním parametru. Pokud ho najdete -> vraťte, jinak vyhodtě vyjímku `LookupError`. Ve vašem programu zavolejte vaší funkce s různými parametry a ošetřete možnost vyhození vyjímky pomocí try, except - vyzkoušejte si více except pro různé typy vyjímek.

### 1.3 os

Napište program, který vypíše nějaký text a bude čekat dokola na uživatelský vstup - pokud dostane "a" (again), tak text vypíše znovu, pokud dostane "c" (clear), tak vymaže výstup terminálu. Při stisknutí ctrl+c musí program tuto akci odchytit a korektně se ukončit.

> Program si můžete dle libosti upravit a vylepšit

## Zadání TODO aplikace

A je to tu. Napište konzolovou aplikaci, která bude mít uživatelské rozhraní - v terminálu zobrazí učivateli menu a uživatel se bude moci v něm pohybovat pomocí zkratek (napíše např. začáteční písmeno). A bude mít tuto [funkčnost](#cesta-k-todo-aplikaci)

```
Menu: (pro výběr stiskněte danou klávesu)
Show all - s
Show done - d
Show incomplete - i
Add task - a
Change state - c
Show menu - m
Quit - q
```

Ukázka možnéno rozhraní (">" vždy označuje uživatelský vstup):

```
Menu: (pro výběr stiskněte danou klávesu)
Show all - s
Show done - d
Show incomplete - i
Add task - a
Change state - c
Show menu - m
Quit - q

>a
Co? Posekat trávu
Přidáno

>s
Všechny úkoly:
Posekat trávu - Incomplete

>c
Select task:
[0] Posekat trávu - Incomplete

ID done/inc> 0 done

>s
Všechny úkoly:
Posekat trávu - Done

>i
Nedokončené úkoly:

>d
Hotové úkoly:
Posekat trávu - Done

>q
```
