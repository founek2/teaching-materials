# 8. Lekce: Traits, generika a closures

## Cíl lekce

Vytvářet obecné, ale stále čitelné funkce. Traits popisují chování typů, generika dovolují napsat algoritmus jednou pro více typů a closures předávají chování jako hodnotu.

## Generická funkce

```rust
fn first<T>(values: &[T]) -> Option<&T> {
    values.first()
}
```

`T` zastupuje libovolný typ. Funkce neporovnává ani nekopíruje prvky, proto nemusí požadovat žádný trait.

Když chceme hodnoty porovnávat, přidáme omezení:

```rust
fn largest<T: Ord>(values: &[T]) -> Option<&T> {
    values.iter().max()
}
```

## Vlastní trait

```rust
trait Summary {
    fn summary(&self) -> String;
}

impl Summary for Task {
    fn summary(&self) -> String {
        let mark = if self.done { "x" } else { " " };
        format!("[{mark}] {}", self.title)
    }
}
```

Trait je smlouva: každý typ implementující `Summary` umí vrátit textové shrnutí. Funkce pak může pracovat s libovolným vhodným typem:

```rust
fn print_summary(item: &impl Summary) {
    println!("{}", item.summary());
}
```

## Closures

Closure je anonymní funkce. Už jsme je použili v `filter` a `map`.

```rust
fn select_tasks<F>(tasks: &[Task], predicate: F) -> Vec<&Task>
where
    F: Fn(&Task) -> bool,
{
    tasks.iter().filter(|task| predicate(task)).collect()
}

let open_tasks = select_tasks(&tasks, |task| !task.done);
```

`Fn(&Task) -> bool` říká, že `predicate` je funkce nebo closure přijímající `&Task` a vracející `bool`. Takové funkce oddělují obecný postup od konkrétní podmínky.

## Cvičení

### 8.1 Obecná kontrola

Napište generickou funkci `contains<T: PartialEq>(values: &[T], searched: &T) -> bool`. Porovnejte ji s metodou `contains`, kterou už kolekce nabízí.

### 8.2 Zobrazitelné úkoly

Vytvořte trait `DisplayLine` s metodou `line(&self) -> String`. Implementujte jej pro `Task` a pro vlastní `Book` z lekce 4.

### 8.3 Vlastní filtr

Napište funkci podobnou `select_tasks`. Pomocí ní vytvořte seznam hotových úkolů a seznam úkolů, jejichž název obsahuje zadané slovo. Všimněte si, že algoritmus zůstává stejný, mění se jen closure.