# 3. Lekce: Výpůjčky, odkazy a slices

## Cíl lekce

Předávat data funkcím bez zbytečného kopírování a chápat pravidla, která dovolují bezpečně kombinovat čtení a změny dat.

## Neměnná výpůjčka

Odkaz `&T` dočasně půjčuje hodnotu bez převzetí vlastnictví. Funkce může data číst, ale ne měnit.

```rust
fn word_count(text: &str) -> usize {
    text.split_whitespace().count()
}

fn main() {
    let sentence = String::from("Rust má silný typový systém");
    println!("{}", word_count(&sentence));
    println!("{sentence}");
}
```

Pro text, který pouze čteme, preferujte parametr `&str` před `&String`. Funkce potom přijme jak stringový literál, tak `String`.

## Měnitelná výpůjčka

Odkaz `&mut T` dovoluje hodnotu změnit. V jednom okamžiku smí existovat buď libovolný počet neměnných výpůjček, nebo právě jedna měnitelná výpůjčka.

```rust
fn append_period(text: &mut String) {
    text.push('.');
}

fn main() {
    let mut message = String::from("Hotovo");
    append_period(&mut message);
    println!("{message}");
}
```

Pravidlo zabraňuje situaci, kdy jeden kus kódu čte data právě ve chvíli, kdy je jiný mění. Překladač sleduje, kdy je výpůjčka naposledy použita, a potom ji uvolní.

## Slices

Slice je pohled na souvislou část dat. `&str` je slice textu, `&[i32]` slice pole nebo vektoru.

```rust
fn sum(values: &[i32]) -> i32 {
    values.iter().sum()
}

fn main() {
    let values = vec![4, 8, 15, 16, 23, 42];
    println!("{}", sum(&values[1..4])); // 8 + 15 + 16
}
```

Slice neownuje data. Proto nesmí původní kolekce během existence slice změnit velikost, například pomocí `push`.

## Návrh funkcí

Při návrhu API se ptejte:

- Potřebuje funkce data vlastnit i po skončení volání? Pak přijme `T`.
- Potřebuje je jen číst? Pak přijme `&T` nebo konkrétnější `&str`, `&[T]`.
- Musí je změnit? Pak přijme `&mut T`.

Čím menší oprávnění funkce dostane, tím snáz se kód používá a skládá dohromady.

## Cvičení

### 3.1 Nejdelší slovo

Napište `longest_word(text: &str) -> &str`, která vrátí nejdelší slovo ve větě. Pro prázdný text může vrátit prázdný řetězec. Využijte `split_whitespace` a ověřte, že výsledek lze vytisknout i po volání funkce.

### 3.2 Úprava seznamu

Napište `add_bonus(scores: &mut Vec<i32>, bonus: i32)`, která přičte bonus každému výsledku. Použijte `for score in scores` a dereferencování `*score`.

### 3.3 Průměr bez vlastnictví

Napište `average(values: &[f64]) -> Option<f64>`. Pro prázdný slice vraťte `None`; pro ostatní hodnoty `Some(průměr)`. `Option` probereme podrobně v další lekci, zatím stačí výsledek vypsat přes `println!("{:?}", average(&values))`.