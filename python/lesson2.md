# 2. Lekce

## Proměnné II

* jmenná konvence - angličtina, popisné názvy
* snake case - např. `car_color`

## Cykly

```python
for number in 0,1,2,3,4,5,6:
    print(number)   # vypíše všechna čísla od 0 do 6

for number in range(7):
    if number == 2:
        print(number)   # vypíše poze číslo 2

for number in range(1, 10):
    if 2 <= number <= 8:    # specialita Pythonu
        print(number)   # vypíše číslo v rozmezí daném podmínkou
```

## "Rozloučení" s interaktivním módem

Interpretr v interaktivním módu je užitečná věc, pokud si potřebujeme vyzkoušet 1 - 3 řádkové přikazy. Pokud ale chceme psát delší skripty nebo mít možnost se vracet do historie a opakovaně spouště více řádků, tak tento řežim je velmi nepraktický. Proto si ukážeme, jak spustit skript, který je uložený v souboru. Ale nebojte, s interaktivním režimem se jistě ještě potkáme, velice ho doporučují, pokud si potřebujete vyzkoušet kratší příkazy - velmi se hodí. Jak vlastně spustit soubory s python kódem? (název souboru s kódem je muj_skript.py)

```bash
python3 muj_skript.py
```

## Odsazení místo závorek

Z výše uvedené ukázky je vidět, že python nepoužívá závorky pro uvození bloku jako C jazyky, ale nad blokem je řádek končící dvojtečkou a pak každý rádek, který je odsazen patří do bloku. Blok končí prvním řádkem, který nemá dané odsazení. Je potřeba si na odsazení dávat pozor, protože rozdíl v jedné mezeře může vyvolat chybu. Bloky lze také libovolně vnořovat.

```python
for number in range(1, 10):             <- začátek bloku1
    print("Strahov je životní styl")
   _
   └───odsazení

    for number2 in range(1, 10):         <- nový vnořený blok2
        print(number)                   <- kód vnořeného bloku2
        print(number2)
    promnena = number + 1               <- uzavření bloku2 a kód pro blok1
    print("hodnota", promnena)
                                        <- uzavření bloku1
print("konec programu")                 <- globální kód
```

### 2.1.x Cykly

* Vypište přesně 11x vaše jméno
* Sečtěte všechna čísla od 0 do 49
* vypište všechna lichá čísla z intervalu <7, 19>
