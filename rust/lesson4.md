# 4. Lekce: Datové typy a pattern matching

## Cíl lekce

Modelovat doménu programu pomocí `struct` a `enum` místo řetězcových příznaků a `null` hodnot. Tyto typy dobře fungují s funkcemi, protože nutí popsat všechny možné stavy.

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

### 4.1 Knihovna

Vytvořte `struct Book` s názvem, autorem a rokem vydání. Přidejte konstruktor `new` a metodu `description`, která vrátí `String`.

### 4.2 Stav objednávky

Vytvořte `enum OrderState` s variantami `Created`, `Paid`, `Sent` a `Cancelled`. Napište funkci, která pro každý stav vrátí text pro zákazníka. Využijte `match`.

### 4.3 Vyhledání úkolu

Napište funkci `find_task(tasks: &[Task], title: &str) -> Option<&Task>`. Nepoužívejte index ani `unwrap`; výsledek ošetřete pomocí `match`.