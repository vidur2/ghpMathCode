use std::collections::HashMap;

fn main() {
    let mut store: HashMap<u64, u64> = HashMap::new();
    let mut count_str = String::new();

    println!("Enter count below:");
    std::io::stdin().read_line(&mut count_str).unwrap();
    println!("\n\n");

    let count: i32 = count_str.trim().parse().unwrap();

    for i in 5..count {
        let current = i as f64;
        let new = current.log2();

        if new.fract() == 0.0 {
            let cloned_store = store.clone();
            let number_value = cloned_store.get(&(new as u64));

            match number_value {
                Some(val) => {
                    store.insert(new as u64, val + 1);
                }
                None => {
                    store.insert(new as u64, 1);
                }
            }
        }

        let mut number = new as u64;
        while number != 1 {
            number = if number % 2 == 1 {
                3 * number + 1
            } else {
                number / 2
            };
            let new = (number as f64).log2();

            if new.fract() == 0.0 {
                let cloned_store = store.clone();
                let number_value = cloned_store.get(&(new as u64));

                match number_value {
                    Some(val) => {
                        store.insert(new as u64, val + 1);
                    }
                    None => {
                        store.insert(new as u64, 1);
                    }
                }
            }
        }
    }

    println!("Results of the form 2^base");
    println!("{:?}", store)
}
