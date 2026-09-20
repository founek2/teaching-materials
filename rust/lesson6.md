# 6. Lekce: Chyby a práce se soubory

## Cíl lekce

Rozlišovat očekávanou chybu od chyby v programu a bezpečně ukládat data. Rust pro očekávané neúspěchy používá `Result<T, E>` místo skrytých výjimek.

## `Option` versus `Result`

- `Option<T>`: výsledek může chybět a absence není chyba, například nenalezený úkol.
- `Result<T, E>`: operace může selhat a potřebujeme znát důvod, například nečitelný soubor.

```rust
use std::num::ParseIntError;

fn parse_count(input: &str) -> Result<u32, ParseIntError> {
    input.trim().parse::<u32>()
}

fn main() {
    match parse_count("12") {
        Ok(count) => println!("Počet: {count}"),
        Err(error) => println!("Neplatný počet: {error}"),
    }
}
```

Nepoužívejte `unwrap()` pro vstup od uživatele, síť ani soubory. `unwrap` program při chybě ukončí; pro výukovou ukázku je někdy vhodný, ale v aplikaci musíme chybu zpracovat nebo předat volajícímu.

## Operátor `?`

`?` vrátí chybu z aktuální funkce, pokud je výsledek `Err`, jinak rozbalí hodnotu `Ok`.

```rust
use std::fs;
use std::io;

fn load_tasks(path: &str) -> Result<String, io::Error> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}
```

Totéž lze krátce napsat `fs::read_to_string(path)`. Delší verze ukazuje, co `?` dělá: ukončí právě tuto funkci a chybu předá jejímu volajícímu.

## Zápis do souboru

```rust
use std::fs;
use std::io;

fn save_tasks(path: &str, lines: &[String]) -> Result<(), io::Error> {
    fs::write(path, lines.join("\n"))
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let tasks = vec![String::from("Nakoupit"), String::from("Odeslat e-mail")];
    save_tasks("tasks.txt", &tasks)?;
    println!("Uloženo");
    Ok(())
}
```

Návratový typ `Result<(), ...>` říká, že funkce při úspěchu nevrací data, ale může selhat. V `main` používáme `Box<dyn Error>` jako jednoduchý společný typ pro chyby v malé aplikaci.

## Cvičení

### 6.1 Bezpečný vstup

Napište `read_number(input: &str) -> Result<i32, String>`. Pro neplatný vstup vraťte srozumitelnou vlastní zprávu. Nápověda: `map_err(|_| String::from("..."))`.

### 6.2 Uložení poznámek

Vytvořte `Vec<String>` s poznámkami. Napište funkce `save_notes` a `load_notes`, které pracují se souborem `notes.txt`. Každý řádek souboru je jedna poznámka.

### 6.3 Odolné načtení

Upravte načítání tak, aby neexistující soubor znamenal prázdný seznam, ale jiné chyby se zobrazily uživateli. Použijte `match` nad `fs::read_to_string` a `error.kind()`.