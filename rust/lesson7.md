# 7. Lekce: Moduly, crates a testování

## Cíl lekce

Rozdělit projekt do menších částí, znát rozdíl mezi binárkou a knihovnou a ověřovat chování automatickými testy.

## Struktura projektu

```
todo/
├── Cargo.toml
└── src/
    ├── main.rs   # binární aplikace, vstup a výstup
    ├── lib.rs    # veřejné moduly a logika
    ├── task.rs   # datový model
    └── store.rs  # uložení do souboru
```

`main.rs` má být tenká vrstva: načte vstup, zavolá logiku a vypíše výsledek. Logika bez přímého vstupu a výstupu se lépe testuje v `lib.rs` a jeho modulech.

```rust
// src/lib.rs
pub mod task;

// src/task.rs
#[derive(Debug, PartialEq)]
pub struct Task {
    pub title: String,
    pub done: bool,
}

pub fn create_task(title: &str) -> Task {
    Task { title: title.to_owned(), done: false }
}
```

`pub` zveřejní položku pro rodičovský modul nebo uživatele knihovny. Ve výchozím stavu jsou položky soukromé.

## Jednotkové testy

```rust
pub fn is_valid_title(title: &str) -> bool {
    !title.trim().is_empty() && title.len() <= 80
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn accepts_normal_title() {
        assert!(is_valid_title("Nakoupit"));
    }

    #[test]
    fn rejects_empty_title() {
        assert!(!is_valid_title("   "));
    }
}
```

Spuštění testů:

```sh
cargo test
cargo test rejects_empty_title
```

Testy musí být nezávislé: nespoléhají na pořadí spuštění ani na soubor, který vytvořil jiný test. Vstup a očekávaný výstup pojmenujte tak, aby selhání bylo čitelné.

## Závislosti a crates.io

Knihovny se zapisují do `Cargo.toml`. Například serializaci dat přidáme později přes `serde`. Než závislost přidáte, ověřte její dokumentaci, aktivitu a licenci. Pro tento kurz nejprve stavíme dostatek funkcí standardní knihovny.

## Cvičení

### 7.1 Rozdělení kódu

Přeneste typ `Task` z předchozích lekcí do `src/task.rs`. V `lib.rs` jej zveřejněte a z `main.rs` vytvořte úkol pomocí `use nazev_projektu::task::Task`.

### 7.2 Testování pravidel

Napište `is_valid_title` a alespoň čtyři testy: běžný název, prázdný text, pouze mezery a text delší než limit.

### 7.3 TDD malého pravidla

Nejprve napište selhávající test pro funkci `can_mark_done(task: &Task) -> bool`, která nesmí dokončit úkol s prázdným názvem. Teprve potom implementujte funkci a spusťte `cargo test`.