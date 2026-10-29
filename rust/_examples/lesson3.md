

```rust
#[derive(Default, Clone, Debug, PartialEq)]
enum Color {
    #[default]
    Black,
    White,
    Blue,
}

impl Color {
    fn convert_to_hex(&self) -> String {
        match *self {
            Color::Black => {
                let a = "";
                String::from("#000000")
            }
            Color::White => String::from("#000000"),
            Color::Blue => String::from("#000000"),
        }
    }
}

#[derive(Default, Clone, Debug)]
struct Person {
    skin_color: Color,
    number_of_legs: i32,
    number_of_hands: i32,
}

trait ChangableColor {
    fn change_color(&mut self, color: Color);

    fn change_to_black(&mut self) {
        self.change_color(Color::Blue);
    }
}

impl Person {
    fn change_skin_color(&mut self, color: Color) {
        self.skin_color = color;
    }

    fn number_of_hands(&self) -> i32 {
        return self.number_of_hands;
    }
}

impl ChangableColor for Person {
    fn change_color(&mut self, color: Color) {
        self.change_skin_color(color);
    }
}

fn change_color_black(person: &mut dyn ChangableColor) {
    ChangableColor::change_color(person, Color::Black);
    // person.change_skin_color("black");
    // person
}

fn main() {
    println!("Hello, world!");

    let mut person = Person {
        number_of_hands: 3,
        ..Default::default()
    };

    change_color_black(&mut person);
    println!("{:?}", person);
    println!("hex: {}", person.skin_color.convert_to_hex());
    // person.change_skin_color("black");
    // let aaa = person.number_of_hands();
}
```