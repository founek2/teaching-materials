# 9. Lekce: Návrh konzolové aplikace

## Cíl lekce

Spojit dosavadní znalosti do malé aplikace pro evidenci úkolů. Dnes vytvoříme funkční jádro a otestujeme jej; uživatelské rozhraní a uložení dat dokončíme příště.

## Požadavky projektu

Aplikace musí umět:

- přidat úkol,
- vypsat všechny, hotové nebo rozpracované úkoly,
- označit úkol jako hotový,
- uložit data při ukončení a načíst je při startu,
- korektně reagovat na chybný příkaz nebo neexistující index.

Rozdělte zodpovědnosti:

| Modul | Zodpovědnost |
| --- | --- |
| `task` | `Task`, stav a pravidla jednoho úkolu |
| `app` | operace nad seznamem úkolů |
| `store` | uložení a načtení souboru |
| `main` | dialog s uživatelem |

## Funkční jádro

```rust
#[derive(Debug, Clone, PartialEq)]
pub struct Task {
    pub title: String,
    pub done: bool,
}

pub fn add_task(tasks: &mut Vec<Task>, title: &str) -> Result<(), String> {
    let title = title.trim();
    if title.is_empty() {
        return Err(String::from("Název úkolu nesmí být prázdný"));
    }

    tasks.push(Task { title: title.to_owned(), done: false });
    Ok(())
}

pub fn mark_done(tasks: &mut [Task], index: usize) -> Result<(), String> {
    let task = tasks.get_mut(index).ok_or_else(|| String::from("Úkol neexistuje"))?;
    task.done = true;
    Ok(())
}
```

`get_mut` vrací `Option<&mut Task>` a `ok_or_else` jej převede na `Result`. Hranice aplikace může chybu zobrazit; logika ji pouze popíše.

## Testy před UI

```rust
#[test]
fn marking_existing_task_sets_done() {
    let mut tasks = vec![Task { title: String::from("Nakoupit"), done: false }];

    mark_done(&mut tasks, 0).unwrap();

    assert!(tasks[0].done);
}
```

Napište testy pro prázdný název, neexistující index a zachování pořadí úkolů. Teprve po zelených testech začněte psát menu.

## Cvičení

### 9.1 Kostra projektu

Vytvořte Cargo projekt `todo`. Přidejte moduly z tabulky a datový typ `Task`. Projekt musí projít přes `cargo fmt`, `cargo check` a `cargo test`.

### 9.2 Logika aplikace

Implementujte `add_task`, `mark_done` a `list_by_status(tasks: &[Task], done: Option<bool>) -> Vec<&Task>`. `None` znamená všechny úkoly.

### 9.3 Testovací sada

Napište alespoň pět testů pro logiku. Testy nesmí číst ze standardního vstupu ani zapisovat do souboru.

## Domácí příprava

Dokončete logiku a připravte si seznam otázek z chyb překladače. V další lekci budeme propojovat vrstvy aplikace, takže funkční jádro musí být v samostatných modulech.