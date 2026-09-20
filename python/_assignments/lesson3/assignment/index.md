Vaším cílem je v tomto úkolu vytvoření kalkulačky.

Pohled uživatele, očekávané chování:
Zapnu program a ten vypíše nějakou uvítací hlášku co jsem to vlastně spustil a jakým způsobem ho (program) mohu ovládat/používat. Následně bude očekávat zadání čísla, následně operátoru po jehož zadání program zkontroluje zda zadal operátor, který Vaše kalkulačka podporuje - pokud ne, tak vypíše chybu "Zadal jsi nepodporovaný operátor" a požádá o opětovné zadání. Následně požádá o zadání druhého čísla. Nakonec spočítá daný výraz a požádá uživatele o další vstup - pokud uživatel zadá operátor, tak se jako první operand bere předchozí výsledek. Pokud zadá číslo, tak to bude první operand, následně operátor a číslo. Opět zobrazí výsledek a stále dokola. Program se ukončí pokud uživatel kdykoli napíše na vstup "q".

Podporované operátory:
Vaše kalkulačka by měla podporat tyto základní operátory: +,-,/,\*
Doporučuji si s tím trochu pohrát a implementovat i jiné - nějaké si vymyslete

Ukázka výstupu:

```
-------- program byl spušten -------
Program kalkulačky, napiš číslo [enter], operátor [enter], číslo [enter] a zobrazí se výsledek. Následně můžeš pracovat s předchozím výsledek pokud zadáš rovou operátor a číslo, případně znovu zadávej číslo, operátor, číslo.

vstup: 10
vstup: +
vstup: 10
výpočet: 10 + 10 = 20
vstup: -
vstup: 1
výpočet: 20 - 1 = 19
vstup: 5
vstup: /
vstup: 2
výpočet: 5 / 2 = 2.5

vstup: q
--------- program byl ukončen -------
```

Jak začít:
Pokud nevíte odkud začít, tak doporučuji vytvořit program s minimální funkcionalitou, tedy: program načte číslo, operátor a číslo. Zkontrolujte, že operátor je validní (podporujete ho), spočítejte a vypište výsledek - to bude celý program pro začátek. Následně můžete řešit jakým způsobem udělat, aby se tento proces opakoval a případně lépe kontrolovat uživatelský vstup.

> HINT:

-   Kontrolu podporovaného operátoru lze provést několika podmínkami nebo je mít v listu a ten projít prvek po prvku a podívat se zda jeden prvek se rovná hledanému - nebo lze využít operátor "in" který vrátí True/Flase pokud je hodnota již obsažena v listu. Ukázka:
    if "+" in ["+","-","/","*","q"]:
    print("toto se vypíše")
    else:
    print("toto nenastane")

-   Z minula známe funkci int(), která převede string na celé číslo, naše kalkulačka by ale měla podporovat desetinná čísla a na to využijete funkci float("33.3") -> 33.3
    Před konverzí textu na číslo by jste správně měli zkontrolovat zda tento převod lze udělat, jinak vám skončí program s chybou. Toto jsme si ještě neukazovali, ale pokud si zkopírujete následující řádky na začátek programu, tak potom můžete voláním funkce s vaším řetězcem např. is_float("33.asd") získat True/False podle toho, zda lze konverzi provést

```python
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
```
