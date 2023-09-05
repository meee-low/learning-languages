use std::io;

fn main() {
    println!("What's your name?");
    let mut name = String::new();
    // Reads the input from stdin.
    let stdin = io::stdin();
    // Sets the input to name. Ignore the Result (it's just the number of bytes read or a panic if error)
    stdin.read_line(&mut name).unwrap();
    // Print ignoring the '\n' at the end from pressing Enter.
    println!("Hello, {}!", name.trim());
}