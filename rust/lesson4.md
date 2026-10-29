# 4. Lekce: Datové typy a pattern matching

## Cíl lekce

Předávat data funkcím bez zbytečného kopírování a chápat pravidla, která dovolují bezpečně kombinovat čtení a změny dat.

Modelovat doménu programu pomocí `struct` a `enum` místo řetězcových příznaků a `null` hodnot. Tyto typy dobře fungují s funkcemi, protože nutí popsat všechny možné stavy.


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

Slice nevlastní data. Proto nesmí původní kolekce během existence slice změnit velikost, například pomocí `push`.

## Návrh funkcí

Při návrhu API se ptejte:

- Potřebuje funkce data vlastnit i po skončení volání? Pak přijme `T`.
- Potřebuje je jen číst? Pak přijme `&T` nebo konkrétnější `&str`, `&[T]`.
- Musí je změnit? Pak přijme `&mut T`.

Čím menší oprávnění funkce dostane, tím snáz se kód používá a skládá dohromady.

## Cvičení

### 4.1 Nejdelší slovo

Napište `longest_word(text: &str) -> &str`, která vrátí nejdelší slovo ve větě. Pro prázdný text může vrátit prázdný řetězec. Využijte `split_whitespace` a ověřte, že výsledek lze vytisknout i po volání funkce.

### 4.2 Úprava seznamu

Napište `add_bonus(scores: &mut Vec<i32>, bonus: i32)`, která přičte bonus každému výsledku. Použijte `for score in scores` a dereferencování `*score`.

### 4.3 Průměr bez vlastnictví

Napište `average(values: &[f64]) -> Option<f64>`. Pro prázdný slice vraťte `None`; pro ostatní hodnoty `Some(průměr)`. `Option` probereme podrobně v další lekci, zatím stačí výsledek vypsat přes `println!("{:?}", average(&values))`.

## Struct

`struct` sdružuje související hodnoty pod pojmenovanými poli.

```rust
#[derive(Debug, Clone)]
struct Task {
    title: String,
    done: bool,
}

impl Task {
    fn new(title: String) -> Self {
        Self { title, done: false }
    }
}
```

`#[derive(Debug)]` dovolí hodnotu jednoduše vypsat pomocí `{:?}`. `Self` označuje právě definovaný typ.

## Enum

Výčtový typ vyjadřuje, že hodnota je právě v jednom z předem známých stavů.

```rust
#[derive(Debug, Clone, Copy, PartialEq)]
enum Status {
    Open,
    Done,
}

enum Command {
    Add(String),
    List(Status),
    Quit,
}
```

Varianty mohou nést data. `Command::Add` proto obsahuje název úkolu, zatímco `Command::Quit` neobsahuje nic.

## `match` a `Option`

`match` musí obsloužit všechny varianty. Díky tomu nepřehlédneme stav, který program neumí zpracovat.

```rust
fn status_label(status: Status) -> &'static str {
    match status {
        Status::Open => "rozpracovaný",
        Status::Done => "hotový",
    }
}

fn show_task(task: Option<&Task>) {
    match task {
        Some(task) => println!("{}: {}", task.title, task.done),
        None => println!("Úkol neexistuje"),
    }
}
```

`Option<T>` nahrazuje nebezpečnou hodnotu `null`: obsahuje buď `Some(T)`, nebo `None`. Funkce, která může nic nenajít, to má v návratovém typu viditelně přiznané.

## `if let`

Když potřebujeme řešit jen jednu variantu, je kratší `if let`:

```rust
let selected: Option<i32> = Some(5);
if let Some(number) = selected {
    println!("Vybráno: {number}");
}
```

## Cvičení

### 4.4 Knihovna

Vytvořte `struct Book` s názvem, autorem a rokem vydání. Přidejte konstruktor `new` a metodu `description`, která vrátí `String`.

### 4.5 Stav objednávky

Vytvořte `enum OrderState` s variantami `Created`, `Paid`, `Sent` a `Cancelled`. Napište funkci, která pro každý stav vrátí text pro zákazníka. Využijte `match`.

### 4.6 Vyhledání úkolu

Napište funkci `find_task(tasks: &[Task], title: &str) -> Option<&Task>`. Nepoužívejte index ani `unwrap`; výsledek ošetřete pomocí `match`.