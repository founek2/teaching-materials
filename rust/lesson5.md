# 5. Lekce: Kolekce a iterátory

## Cíl lekce

Pracovat s více hodnotami idiomaticky. Iterátory jsou v Rustu důležitý nástroj funkcionálního stylu: data prochází a transformují bez ručního indexování a bez zbytečné změny vstupu.

## `Vec<T>` a `HashMap<K, V>`

```rust
use std::collections::HashMap;

fn main() {
    let mut tasks = vec![String::from("Nakoupit"), String::from("Odeslat e-mail")];
    tasks.push(String::from("Zacvičit"));

    let mut scores = HashMap::new();
    scores.insert(String::from("Ada"), 10);
    println!("{:?}", scores.get("Ada"));
}
```

`get` vrací `Option<&V>`, protože hledaný klíč nemusí existovat. Vektor zachovává pořadí, mapa rychle hledá podle klíče.

## Tři způsoby iterace

```rust
let names = vec![String::from("Ada"), String::from("Linus")];

for name in &names {       // &String: pouze čtení
    println!("{name}");
}

for name in &mut names.clone() { // &mut String: změna prvků
    name.make_ascii_uppercase();
}

for name in names {        // String: převezme vlastnictví prvků
    println!("{name}");
}
```

Metoda `iter()` odpovídá `&collection`, `iter_mut()` odpovídá `&mut collection` a `into_iter()` spotřebuje kolekci.

## Transformace dat

```rust
fn completed_titles(tasks: &[Task]) -> Vec<String> {
    tasks
        .iter()
        .filter(|task| task.done)
        .map(|task| task.title.clone())
        .collect()
}

fn total(values: &[i32]) -> i32 {
    values.iter().sum()
}
```

`filter` vybírá prvky, `map` každý prvek transformuje a `collect` vytvoří výslednou kolekci. Uzávěr `|task| ...` je anonymní funkce. Všimněte si, že `completed_titles` nemění vstupní slice.

## Kdy nepoužívat řetězec metod

Pokud transformace potřebuje složitější větvení, pojmenovaný mezivýsledek nebo vedlejší efekt, bývá čitelnější obyčejný `for` cyklus. Funkcionální styl je nástroj pro přehlednou transformaci dat, ne povinná soutěž o nejdelší řetězec metod.

## Cvičení

### 5.1 Sudé čtverce

Ze slice celých čísel vytvořte nový `Vec<i32>` obsahující čtverce pouze sudých čísel. Použijte `iter`, `filter`, `map` a `collect`.

### 5.2 Statistiky úkolů

Pro `&[Task]` napište `count_done` a `titles_in_uppercase`. První vrátí počet hotových úkolů, druhá nový vektor názvů velkými písmeny. Vstupní úkoly se nesmí změnit.

### 5.3 Počet slov

Z textu sestavte `HashMap<String, usize>`, která spočítá výskyt každého slova bez ohledu na velikost písmen. Pro vložení použijte `entry(word).or_insert(0)`.