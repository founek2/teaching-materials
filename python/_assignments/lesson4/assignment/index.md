V příloze úplně dole máte soubory, které využijte jako šablonu pro řešení. Je v nich vždy název funkce, kterou máte doplnit. Pod funkcí je vždy assert. Ten je pro vás, abyste věděli, zda máte správné řešení (v případě, že máte funkci špatně implementovanou, tak program po spštění "spadne" (hodí chybu) na nějakém assertu). U assertů vidíte jakým způsobem je očekávané, že se funkce bude volat a s jakými parametry.
Pro bonusovou úlohu máte přiložen archiv bonus_tests.zip. Po jeho rozbalení budete mít soubory test0_input.txt - test7_input.txt, které znázorňují vstupy pro vás program a test0_output.txt - test7_output.txt, které znázorňují očekávaný výstup vašeho programu.

1. Napište funkci, která přijme list čísel a vrátí jejich součet. Pro implementaci použijte cyklus (ne funkci sum).
2. Napište funkci, která na základě 4 zadaných bodů rozhodne, zda-li tyto 4 body tvoří obdélník, či nikoliv. Bod je tvořen listem o dvou prvcích: [souřadnice X, souřadnice Y]. Čtverec je speciální případ obdélníku - tedy ten považujte taky za obdélník. Zde by se mohlo hodit porovnávání floatů. Porovnání floatů se dělá takto: místo a == b píšeme abs(a - b) < 1e-16. Takto víme, že prvních 16 desetinných míst nám sedí co je dál nás nezajímá (kvůli binární reprezentaci můžeš nastat drobná nepřesnost, proto se kontroluje pouze prvních N míst), tedy rozdíl může být menší. Kdo si pamatuje úplný prd z geometrie stejně jako já - nebojte se najít si, jak se zjišťuje ze 4 bodů, jestli se jedná o obdélník.
3. Napište 2 funkce:

-   první is_descending, která přijímá jeden parametr list a kontroluje jestli se jedná o klesající posloupnost tj. první prvek v listu musí být větší než druhý, druhý větší než třetí, třetí než čtvrtý atd... Návratová hodnota je True/False
-   add_and_increase - funkce přijímá dva parametry. První parametr dostane hodnotu, kterou má přidat do globálního listu "values". Druhý parametr je hodnota o kterou má zvýšit všechny čísla v listu, tedy druhý parametr přičíst ke každému prvku v listu a daný list vrátí jako návratovou hodnotu

Materiál na funkce: https://python.iotplatforma.cloud/#/?id=funkce-pokračování

`Bonusová úloha`:
Napište program, který bude simulovat šíření nákazy v kanceláři. Vypočítejte a vypište dobu šíření a počet infikovaných pracovníků. Vstupem programu bude vždy počet řádku a počet sloupců dané mapy kanceláře a následně mapa kanceláře například:
oooo
oooo
ooo.
!ooo
Písmeno "o" znamená zdravý pracovník.
Písmeno "." znamená neobsazená pozice.
Písmeno "!" znamená infikovaný pracovník.
Nákaza se šíří do 4 směrů. Nahoru, Dolů, Doleva, Doprava. Neobsazené místo berme jako zeď. Přes toto místo dál se tedy nákaza nešíří.
Příklad:
!...
....
oooo
oooo
Doba šíření nákazy je 0 dní a nikdo nebyl infikován. Analogicky pro tuto mapu:
.o..ooo
o!o.ooo
.o..ooo
Bude doba šíření infekce = 1 a počet nakažených je 5 lidí.
Pokud je vstup neplatný, program to musí detekovat:
Neplatné písmeno při zadávání mapy.
Mapa nemá obdélníkový tvar o zadaném rozměru,
V příloze bonus_tests.zip máte příklad vstupů a výstupů, jak by měly vypadat.
Snažte se tuto úlohu řešit co nejefektivněji. Její řešení lze udělat v čase O(m\*n), kde m je počet řádku a n počet sloupců. Nepočítá se zde načítání vstupů apod. Počítá se algoritmus samotný
O složitostech programů/algoritmů více zde:
https://cs.wikipedia.org/wiki/Asymptotick%C3%A1_slo%C5%BEitost
https://www.algoritmy.net/article/102/Asymptoticka-slozitost
