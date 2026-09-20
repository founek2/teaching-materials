# 5. Lekce

### 5.1.1 Kalkulačka - zjednodušená II

Využijte již naprogramovanou zjednodušenou kalkulačku, ale místo použití 3 promněných pro každou hodnotu, která se načítá od uživatele využijte list a cyklus. Stejně tak pro hlášky, které vypisujete uživateli.

[Referenční_řešení](_examples/calc_easy2)

## Funkce pokračování

S funkcemi jsme se již několikrát setkali a např. funkci `print()` využíváme s velkou oblibou pro výpisy. Co se ale za tímto jednoduchým zavoláním `print()` vlastně skrývá? V kostce: funkce musí přijmout parametry, co ji předáme v závorkách, následně je převést na text, potom nahrát do nějakého bufferu a přimět operační systém, aby vám výsledný text zobrazil na obrazovku. Poměrně složitá věc se skrývá za pěti písmeny, že? A v tom je právě kouzlo funkcí, skrytí něčeho komplikovaného, co napíšeme jednou za jednoduché zavolání, které můžeme využívat opakovaně.

Funkce můžeme obecně rozdělit na dvě fáze. S jednou z nich jsme se již setkali a tou je volání funkcí - již náme např. `range(2, 10)`. Toto nám umožňuje v kódu využívat funkcionalitu, kterou nám již někdo připravil. Ještě před tím než funkci můžeme zavolat, někdo ale musel nadefinovat jakým způsobem se má funkce chovat / co má dělat. Tomuto kroku se říká definice funkce. Proč vlastně bychom chtěli mít možnost definovat vlastní funkci? Možná jste si již vyzkoušeli, že při programování složitějších úloh se vám začíná tzv. "duplikovat kód" - některé řádky/úseky se opakují a vyskytují na více místech. To je poměrně pracné napsat, i když se zkratkami ctl+C, ctrl+V se mnoho ulehčí. Problém však nastává ve chvíli, když zjistíte, že tento úsek co máte na 10 různých místech, tak obsahoval chybu a potřebujete opravit jeho chování. To znamená všechna místa najít a provést úpravu - často se při tomto kroku na nějakou část zapomene a to způsobí "prapodivné" chování celého programu.

A na pomoc s tímto a jinými problémy nám přicházejí právě funkce. Umožnují nám vytvořit definici jejich chování - řádký kódu, které označíme identifikátorem (názvem funkce) a tento kód následně můžeme kdykoliv dle potřeby jinde v kódu zavolat a předat případně nějaké hodnoty (argumenty/parametry) důležité pro běh funkce a následně po vykonání funkce (až se zpracují všechny řádky její definice) získat nějakou výslednou hodnotu (návratovou).

Jak si tedy vlastní funkci zadefinovat? Používá se pro to klíčové slovo `def`, za kterým následuje název funkce a v závorkách názvy proměnných, do kterých se nám vloží parametry, pokud naší funkci někdo zavolá a nějaké parametry zadá. Předem tedy musíme vědět s kolika parametry chceme naší funkci vytvořit/zadefinovat - toto se odvíjí od toho, zda funkci při volání budeme chtít předávat nějaké hodnoty. Pokud napíšeme např. následující definici, tak python dané řádky kódu nijak nevyhodnocuje, pouze si poznamená, že funkci s daným názvem exisuje a vyhodnocuje se až ve chvíli, kdy Python narazí na řádek, kde funkci někdo zavolá - tedy až v míste `kill_program(2, 'I don't like it')`.

```python
def kill_program(id, reasson):
    print(f'program with id: {id} was killed')
    print(f'Reason for kill: {reasson}')

    for i in range(15):
        ... # some black magic

    return True         # návratová hodnota

kill_program(2, 'I don`t like it')
```

Všimněte si slova `return` na konci funkce. Každá funkce může vracet nějakou hodnotu (stejně jako range nám vrací posloupnost či input vrací uživatelský vstup), který se nachází za slovem return. Pokud při zpracování funkce Python narazí na klíčové slove `return`, tak tam zastaví vyhodnocování funkce a rovnou vrátí hodnotu za tímto slovem - tedy i když bude kód za `return`, tak se neprovede. Pokud definice funkce neobsahuje `return`, tak se automaticky vrací výchozí hodnota `None`. Příklad použtí:

```python
outcome = kill_program(1, 'Too high memory usage')

if outcome == True:
    print('Successfully killed')
else:
    print('Unable to kill')
```

### 5.2.1 Cvičení funkce

- napište funkci `add`, která vezme dva argumenty a vrátí jejich součet
    `add(4, 6) -> 10`
- Napište funkci `is_bigger`, která rozhodne, jestli první argument (číslo) je větší než druhý (číslo) -> vrátí True pokud ano, jinak False
- napište funkci `show` která dostane jako parametr list a vypíše jeho obsah do konzole - list projděte pomocí for cyklu

```python
print(add(7, 2)) # 9

print(is_bigger(7, 2)) # True

numbers = [1, 2, 4]
show(numbers) # -> nic nemusí vracet
```

### 5.2.2 Výpočet součtu

Napište program, který se uživatele bude dokola ptát na číslo. Toto číslo budete přičítat k dosavadnímu celkovému součtu předchozích čísel. (Využijte předchozí funkci `add`, kterou jste si napsali)

## Packing parameters

V pythonu lze napsat funkci, která bude přijímat libovolný počet argumentů. Lze toho dosáhnout pomocí "sbalení" parametrů do listu.

```python
def count(*params):
    return len(params)

count(1, 41, "Kitty", "SH", 0.1, False)     # -> 6

def count2(first, *others):
    return 1 + len(others)

count2(1, 41, "Kitty", "SH", 0.1, False)     # -> 6
```

## Str - split

Na každý řetězec lze zavolat metodu split, která nám umožňuje rozdělit řetězec na víc částí. Jako parametr se udává oddělovač, který split bude hledat v řetězci a v daném místě provede rozdělení. Návratová hodnota je List obsahující jednotlivé části.

```python
text = 'Příliš žluťoučký kůň úpěl ďábelské ódy'
text.split(' ')     # -> ['Příliš', 'žluťoučký', 'kůň', 'úpěl', 'ďábelské', 'ódy']
```

### 5.3.1 Statistika listu

Napište tyto 3 funkce:

- `incList` - parametr dostane list čísel a její úkol je přičíst ke každému číslu 1 a list vrátit
- `maxList` - parametr dostane list čísel a vrátí maximum
- `minList` - parametr dostane list čísel a vrátí minimum
- `sumList` - parametr dostane list čísel a vrátí součet

> Můžete použít naivní řešení - cyklem projdete pole a v globální proměnné budete mít minimum (analogicky max), které porovnáte se všemi prvky

```python
incList([10,3,1])   # [11, 4, 2]
maxList([10,3,1])   # 10
minList([10,3,1])   # 1
sumList([10,3,1])   # 14
```

- Vytvořte skript, který se zeptá uživatele na čísla oddělená čárkou. Načte vstup jako string, potom pomocí metody `split` převede na list a následně vypíše zajímavé statistiky v tomto formátu:

```text
inc: {seznam zadaných hodnot zvýšený o jedna}
max: {max. ze zadaných hodnot}
min: {min. ze zadaných hodnot}
sum: {součet hodnot}
```

<!-- Nejprve napsat vše do cyklu, potom vylepšit separací kódu do funkce-->