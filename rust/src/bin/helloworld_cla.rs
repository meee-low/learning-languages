use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    // dbg!(args);
    if args.len() >= 2 {
        println!("Hello, {}!", args[1])
    }
    else {
        println!("Hello, world!")
    }
}