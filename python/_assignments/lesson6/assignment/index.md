V tomto ůkoli si vyzkoušíme nově představené datový typy.

-   Napište dvě funkce. Obě funkce budou mít parametr vektor se souřadnicemi X, Y, Z. Vracet budou velikost tohoto vektoru - výpočet velikosti: |u|=√(x²+y²+z²). Funkce se budou lišit pouze v tom, že jedna dostane vektor jako slovník, který bude mít klíče "x", "y", "z" a na nich příslučné hodnoty a druhá bude mít parametr tuple ve formátu (x, y, z). Ukázka: calc_dict(vector={"x": 2, "z": 1, "y": 10}) nebo calc_tuple(vector=(2, 10, 1))
-   Napište funkci, která vytvoří novou matici jejíž prvky budou mít specifikovanou hodnotu. Funkce tedy bude mít parametr "shape", který bude tuple ve formátu (pocet_radku, pocet_sloupcu) a druhý parametr bude hodnota, kterou mají mít všechny prvky. Ukázka volání: generate(shape=(2,3), value=0) vrátí hodnotu [[0,0,0], [0,0,0]]

`HINT`:
Pro získání hodnot z typu Tuple, využijte že znáte jak bude velký a můžeme použít destructuring - x, y, z = vector
Pro získání hodnot ze slovníku lze využit dva způsobi - slovnik.get("key") nebo slovnik["key"], tyto způsobi se liší v tom, jak řeší dotaz na neexistující klíč. V čem se liší nechám na vyzkoušení ;)
Reprezentace matice: https://python.iotplatforma.cloud/#/?id=list-list%C5%AF
Pojmenované parametry: https://python.iotplatforma.cloud/#/?id=named-parameters
