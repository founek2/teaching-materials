# 1. Lekce: Rychlé opakování syntaxe

## Cíl lekce

Založit projekt v Cargo, rychle projít známé konstrukce a ukázat, že Rust kontroluje typy již při překladu. Dnes ještě neřešíme všechny důvody chyb od překladače; důležité je naučit se jeho výstup číst.

## První projekt

```sh
cargo new kalkulacka
cd kalkulacka
cargo run
```

Zdrojový kód aplikace je v `src/main.rs`. Užitečné příkazy:

```sh
cargo check  # rychlá kontrola bez vytvoření spustitelného souboru
cargo run    # přeložení a spuštění
cargo fmt    # formátování zdrojových souborů
```

## Proměnné a základní typy

Proměnné jsou ve výchozím stavu neměnné. Změnu hodnoty musíme vyjádřit klíčovým slovem `mut`.

```rust
fn main() {
    let name = "Ada";
    let mut score: i32 = 10;
    score += 5;

    let ratio: f64 = 0.75;
    let active: bool = true;

    println!("{name}: {score}, {ratio}, {active}");
}
```

Časté celočíselné typy jsou `i32`, `i64`, `u32` a `usize`. Typ `usize` se používá zejména pro indexy a velikosti kolekcí. Typ často nemusíme psát: překladač jej odvodí z použití hodnoty.

## Podmínky, cykly a funkce

`if` je výraz, může tedy vrátit hodnotu. Blok bez středníku na posledním řádku vrací hodnotu tohoto výrazu.

```rust
let age = 20;

let text = if age >= 18 { "dospělý" } else { "nezletilý" };
// or
let text: &str;
if age >= 18 {
    text = "dospělí";
} else {
    text = "nezletilý";
}
```

```rust
fn category(age: u8) -> &'static str {
    if age >= 18 {
        "dospělý"
    } else {
        "nezletilý"
    }
}

fn main() {
    for number in 1..=5 {
        println!("{number}");
    }

    let mut attempts = 3;
    while attempts > 0 {
        attempts -= 1;
    }

    println!("{}", category(20));
}
```

Rozsah `1..5` obsahuje čísla 1 až 4, kdežto `1..=5` i pětku. Funkce musí uvádět typy parametrů; návratový typ se zapisuje za `->`.

## Vstup z terminálu

```rust
use std::io;

fn main() {
    let mut input = String::new();
    println!("Zadej své jméno:");
    io::stdin().read_line(&mut input).expect("Vstup se nepodařilo načíst");

    println!("Ahoj, {}!", input.trim());
}
```

`String::new()` vytváří prázdný měnitelný text. Proč je proměnná `input` označena jako `mut`, budeme přesněji řešit ve třetí lekci.

## Cvičení

### 1.1 Teplota

Napište funkci `celsius_to_fahrenheit`, která převede `f64` ze stupňů Celsia na Fahrenheity. Výsledek vypište se zaokrouhlením na jedno desetinné místo: `println!("{value:.1}")`.

### 1.2 FizzBuzz

Vypište čísla od 1 do 100. Pro násobky 3 vypište `Fizz`, pro násobky 5 `Buzz` a pro násobky obou `FizzBuzz`.

### 1.3 Kalkulačka

Načtěte dvě celá čísla a operátor `+`, `-`, `*` nebo `/`. Operátor vyhodnoťte pomocí `match` a výsledek vypište. Neplatný vstup zatím může program ukončit pomocí `panic!`.

## Na závěr

Spusťte `cargo fmt` a `cargo check`. Chybové hlášky překladače jsou součást práce v Rustu: vždy si přečtěte řádek s popisem chyby i návrh opravy pod ním.

Vyzkoušejte na následujícícm kódu:
```rust
fn main() {
    let vysledek = 10 + "2";
    println!("{vysledek}");
}
```