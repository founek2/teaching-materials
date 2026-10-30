# Bonus

## Procvičení struktur a traits
```rust
struct Dog {
    name: String
}

impl Dog {
    fn woof(&self) -> &'static str {
        "woof"
    }
}

struct Cat {
    // TODO
}

trait MakeSound {
    // TODO
}

// Do not touch function definition, just the body
fn make_animal_sound(animal: impl MakeSound) {
    println!("{}", ?);
}

fn main() {
    let dog = Dog { name: String::from("Ralf") };
    make_animal_sound(dog);

    let cat = Cat { name: String::from("Snowball") };
    make_animal_sound(cat);
}
```

### Rozšíření traitu
Přidání sdílené funkcionality - vynutíme, aby všechny implementace vraceli jména na `name()` a potom můžeme toho využít a přímo implementovat funkcionalitu.
```rust
trait MakeSound {
    // you previos impl + addition below
    fn name(&self) -> &str;
    fn say_hi(&self) {
        println!("{} says hi!", self.name());
    }
}
```

## Rustlings

[100 malých úkolů na procvičení syntaxe a řešení chyb kompilátoru.](https://rustlings.rust-lang.org/)
> Doporučuji cvičení na structs, enums, options, error handling