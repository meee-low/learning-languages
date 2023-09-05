fn main() {
    // fizzbuzzv1();
    fizzbuzzv2();
}

fn fizzbuzzv1() {
    for i in 1..=100 {
        let mut s = "".to_string();
        if i % 3 == 0 {
            s += "Fizz";
        }
        if i % 5 == 0 {
            s += "Buzz";
        }
        if s.len() == 0 {
            s = i.to_string();
        }
        println!("{}", s);
    }
}

fn fizzbuzzv2() {
    use std::collections::BTreeMap;
    // BTreeMap instead of HashMap for preserving order of insertion.
    let mut substitutions = BTreeMap::new();
    substitutions.insert(3, "Fizz");
    substitutions.insert(5, "Buzz");
    substitutions.insert(7, "Bazz");

    for i in 1..=100 {
        let mut s = "".to_string();
        for (k, v) in substitutions.iter() {
            if i % k == 0 { s += *v }
        }
        if s.len() == 0 { s = i.to_string() }
        println!("{}", s);
    }
}