# 10. Lekce: Dokončení projektu

## Cíl lekce

Dokončit konzolovou aplikaci, propojit vstup, logiku a souborové úložiště, projít chyby a udělat krátkou prezentaci řešení.

## Menu a parsování příkazů

Nenechávejte logiku menu promíchanou s funkcemi pro úkoly. Nejprve převeďte text na příkaz, potom příkaz proveďte.

```rust
enum Command {
    Add(String),
    ListAll,
    ListDone,
    ListOpen,
    Done(usize),
    Quit,
    Help,
}

fn parse_command(input: &str) -> Result<Command, String> {
    let mut parts = input.trim().splitn(2, ' ');
    match parts.next() {
        Some("add") => parts
            .next()
            .map(|title| Command::Add(title.to_owned()))
            .ok_or_else(|| String::from("Použití: add <název>")),
        Some("list") => Ok(Command::ListAll),
        Some("done") => parts
            .next()
            .ok_or_else(|| String::from("Použití: done <index>"))?
            .parse::<usize>()
            .map(Command::Done)
            .map_err(|_| String::from("Index musí být číslo")),
        Some("quit") => Ok(Command::Quit),
        Some("help") => Ok(Command::Help),
        _ => Err(String::from("Neznámý příkaz; napiš help")),
    }
}
```

`splitn(2, ' ')` rozdělí vstup jen na příkaz a zbytek řádku. Název úkolu tedy může obsahovat mezery.

## Jednoduchý formát souboru

Pro závěrečný projekt stačí řádkový formát:

```text
0|Nakoupit
1|Odeslat e-mail
```

První znak označuje stav (`0` rozpracováno, `1` hotovo), zbytek řádku je název. Při načítání každý řádek validujte a neplatný řádek nahlaste s číslem řádku. Nepoužívejte `unwrap` na data ze souboru.

## Kontrolní seznam

- `cargo fmt --check` projde bez změn.
- `cargo test` projde.
- Prázdný a neplatný příkaz aplikaci neukončí.
- Neexistující index úkolu zobrazí chybu.
- Po restartu jsou uložené úkoly zpět.
- `main.rs` obsahuje pouze řízení programu; logika je v modulech.

## Závěrečné cvičení

Dokončete aplikaci a ukažte vyučujícímu tyto scénáře:

1. Přidání dvou úkolů a výpis seznamu.
2. Dokončení jednoho úkolu a filtrování podle stavu.
3. Pokus o dokončení neexistujícího indexu.
4. Uložení, ukončení a opětovné načtení aplikace.
5. Spuštění testů.

## Možná rozšíření

- priorita a termín úkolu,
- odstranění úkolu,
- řazení podle stavu nebo názvu,
- export do jiného formátu,
- nahrazení vlastního formátu JSONem pomocí `serde`.

Před rozšířením vždy přidejte test pro nové pravidlo. Rustův kompilátor a testy potom společně hlídají, aby změna nerozbila dříve funkční části programu.