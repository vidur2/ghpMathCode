mod tlc_struct;
use tlc_struct::Tlc;

use std::{collections::{HashSet, VecDeque}, rc::Rc};

fn main() {
    let mut visited: HashSet<Rc<Tlc>> = HashSet::new();
    let mut queue: VecDeque<Rc<Tlc>> = VecDeque::from([Rc::new(Tlc::new(String::from("TC")))]);
    let mut current;

    loop {

        current = queue.pop_back().unwrap();
        println!("{:?}", current);

        let reffed = Rc::clone(&current);

        if reffed.as_ref() == &Tlc::new(String::from("TC")) {
            break;
        }

        let reffed = Rc::clone(&current);
        let new_str_possibilities = Rc::as_ref(&reffed).clone().check_all();

        for str_ in new_str_possibilities {
            if !visited.contains(&str_) {
                let reference = Rc::new(str_); 
                queue.push_front(Rc::clone(&reference));
                visited.insert(Rc::clone(&reference));
            }
        }
    }

    println!("Found");
}
