fn main() {
    for i in 0..=20 {
        println!("{}! = {} = {}", i, factorial_recursive(i), factorial_functional(i));
        assert_eq!(factorial_functional(i), factorial_recursive(i));
    }
}

fn factorial_recursive(n: u128) -> u128 {
    if n == 0 { 1 }
    else {n * factorial_recursive(n-1)}
}

fn factorial_functional(n: u128) -> u128 {
    (1..=n).product()
}