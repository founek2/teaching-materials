# 2. Lekce: Vlastnictví a neměnnost

## Cíl lekce

Pochopit, proč Rust hlídá práci s pamětí, a používat přesuny hodnot, kopírování a klonování vědomě. Funkcionální styl stojí často na neměnných datech a na funkcích, které místo úpravy vstupu vrací novou hodnotu.

## Tři pravidla vlastnictví

1. Každá hodnota má právě jednoho vlastníka.
2. Když vlastník skončí, hodnota se uvolní.
3. Vlastníka lze změnit přesunem hodnoty.

```rust
fn main() {
    let first = String::from("Ahoj");
    let second = first;

    // println!("{first}"); // chyba: hodnota byla přesunuta do second
    println!("{second}");
}
```

`String` obsahuje data na haldě. Prosté přiřazení proto nepřiděluje druhého vlastníka, ale vlastnictví přesune. Tím Rust brání dvojímu uvolnění stejné paměti.

## Typy `Copy` a metoda `clone`

Jednoduché hodnoty jako `i32`, `bool` nebo `f64` implementují trait `Copy`, takže se při přiřazení zkopírují.

```rust
let first = 42;
let second = first;
println!("{first}, {second}");

let original = String::from("data");
let duplicate = original.clone();
println!("{original}, {duplicate}");
```

`clone()` vytváří skutečnou kopii dat. Používejte jej pouze tehdy, když jsou opravdu potřeba dva vlastníci; jeho cena závisí na velikosti dat.

## Vlastnictví ve funkcích

Funkce může hodnotu převzít a vrátit ji, nebo si ji jen vypůjčit. Výpůjčky rozebereme příště.

```rust
fn add_exclamation(mut text: String) -> String {
    text.push('!');
    text
}

fn main() {
    let greeting = String::from("Ahoj");
    let excited = add_exclamation(greeting);
    println!("{excited}");
}
```

Funkce je snadněji testovatelná, pokud její vstup a výstup jasně popisují změnu: přijme `String`, vrátí nový `String`.

## Shadowing

Jméno proměnné lze znovu použít. Nejde o změnu původní hodnoty, ale o novou proměnnou.

```rust
let spaces = "   ";
let spaces = spaces.len();
```

To je užitečné při postupné transformaci dat. Se `mut` by nešlo změnit typ proměnné z `&str` na `usize`.

## Cvičení

### 2.1 Vlastník textu

Vytvořte funkci `normalize_name(name: String) -> String`, která odstraní mezery na začátku a na konci a vrátí jméno velkými písmeny. Nápověda: `trim()` vrací výpůjčku `&str`, `to_uppercase()` vytváří `String`.

### 2.2 Pokus o přesun

Vytvořte `String`, předejte jej funkci, která jej pouze vypíše, a potom jej zkuste znovu použít v `main`. Opravte program nejprve návratem hodnoty a potom si připravte otázku, jak by šla použít výpůjčka.

### 2.3 Čistá transformace

Napište funkci `with_tax(price: f64, rate: f64) -> f64`. Vstupní hodnoty neměňte, pouze vypočítejte a vraťte cenu s daní. Otestujte ji pro několik sazeb.