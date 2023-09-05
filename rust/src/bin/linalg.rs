use std::fmt::Display;
fn main (){
    let mut v1 = Vector2D::new(1f64, 0f64);
    let v2 = Vector2D::new(0f64, 1f64);

    println!("{}", v1);
    println!("{}", v2);

    println!("{}", v1.add(&v2));

    println!("{}", v1.scale(29f64));

}
#[derive(Debug, Clone, Copy)]
struct Vector2D {
    x: f64,
    y: f64
}

impl Vector2D {
    fn new(x: f64, y: f64) -> Self {
        Vector2D { x, y }
    }

    fn add(self, other: &Vector2D) -> Self {
        Vector2D{x: self.x + other.x, y: self.y + other.y}
    }

    fn scale(self : &mut Self, factor: f64) -> Self {
        self.x *= factor;
        self.y *= factor;
        *self
    }
}


impl Display for Vector2D {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Vector2D({}, {})", self.x, self.y)
    }
}
#[derive(Debug, Clone, Copy)]
struct Matrix2D (
    Vector2D,
    Vector2D
);

impl Matrix2D {
    fn new(col1: Vector2D, col2: Vector2D) -> Self {
        Matrix2D(col1, col2)
    }

    fn matmult(&mut self, other: &Matrix2D) -> Self {
        todo!()
    }
}