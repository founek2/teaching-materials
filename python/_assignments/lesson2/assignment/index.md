1. Nalezněte všechna sudá čísla v intervalu <100, 200> a vypište je. Následně nalezněte všechna lichá čísla ze stejného intervalu a ty také vypište.
   HINT: Zjištění, jestli je číslo sudé nebo liché, je velmi jednoduché. K tomu nám může pomoct operátor % (modulo/dělení se zbytkem). Tento operátor po vydělení dvou čísel vrací zbytek. Tedy např. 4 % 2 = 0, 3 % 2 = 1, ...

2. Napište program, který požádá uživatele, aby zadal dvě čísla. Tyto čísla budou reprezentovat interval <prvni, druhé>. První číslo musí být menší než druhé (ověřte, že tomu tak opravdu je, pokud ne, vypiště nějakou hlášku, že zadal špatné hodnoty a požádejte ho o vstup znovu). Mezi těmito čísly (včetně těch krajních) spočtěte součet.
   HINT:
   Funkce input() vrací textový řetězec i v případě, když uživatel zadáná číslo. Tedy je potřeba řetězec převést na číslo. To lze udělat pomocí funkce int() - např. int("33") vrací číslo 33
   https://docs.python.org/3/library/functions.html#input
   https://docs.python.org/3/library/functions.html#int
   https://docs.python.org/3/library/stdtypes.html#range

3. Napiště program, který bude po uživateli chtít stále dokola načíst celé číslo (můžete využít velkou posloupnost). Toto číslo vždy připočtěte k nějakému dosavadnímu celkovému součtu všech zadaných čísel a vypiště ve tvaru "Actual sum = suma_cisel". Pokud bude zadáno číslo 0, tak cyklus ukončete a vypiště celkový součet zadaných čísel.
   HINT:
   funkce exit() ukončí běh programu

4. BONUS: Napište program, který požádá uživatele, aby zadal celé číslo větši nebo rovno 0. Toto číslo potom pomocí cyklu while převeďte do binární podoby. Svůj výstup můžete porovnat pomocí built-in funkce bin. Použití je jednoduchý (bin(2)) např.
   HINT:
   https://python.iotplatforma.cloud/#/?id=while-cyklus

PS: Jednotlivé úkoly jsou nezávislé, tak prosím každy napište do vlastního souboru -> při vypracování všech 4 úkolu odevzdáváte 4 soubory
