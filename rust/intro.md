## Popis kurzu

Kurz je určený pro studenty, kteří už znají základní pojmy programování: proměnnou, podmínku, cyklus a funkci. Rust si proto na začátku rychle zasadíme do známého kontextu a potom se zaměříme na to, co je pro něj typické: vlastnictví dat, výpůjčky, silný typový systém, algebraické datové typy a bezpečné zpracování chyb.

Každá lekce trvá 90 minut. Doporučený rytmus je přibližně 35 minut výkladu a společných ukázek, 40 minut samostatné práce a 15 minut na rozbor řešení a otázky. Cvičení na sebe navazují v malé konzolové aplikaci pro evidenci úkolů.

Po dokončení kurzu by měl student umět:

- vytvořit a spustit Rust projekt pomocí Cargo,
- číst chybové hlášky překladače a využívat je při návrhu programu,
- bezpečně pracovat s vlastnictvím, odkazy a měnitelnými daty,
- používat `struct`, `enum`, `Option`, `Result`, kolekce a iterátory,
- rozdělit aplikaci do modulů, napsat testy a vytvořit malou konzolovou aplikaci.

## Potřebné nástroje

Na počítači musí být nainstalovaný Rust přes [rustup](https://rustup.rs/). Ověření instalace:

```sh
rustc --version
cargo --version
```

Nový projekt vznikne příkazem:

```sh
cargo new rust-kurz
cd rust-kurz
cargo run
```