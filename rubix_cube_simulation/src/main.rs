mod rubix_cube;

use crate::rubix_cube::RubixCube;
use std::collections::{HashSet, VecDeque};

fn main() {
    let mut queue: VecDeque<RubixCube> = VecDeque::new();
    let mut visited: HashSet<RubixCube> = HashSet::new();
    let mut counter = 0;
    queue.push_back(RubixCube::new());

    while queue.len() != 0 {
        let current = queue.pop_front().unwrap();
        let leaves = current.step();

        visited.insert(current);

        for leaf in leaves.iter() {
            if !visited.contains(leaf) {
                queue.push_back(leaf.clone());
            }
        }

        counter += 1;
    }

    println!("{}", counter);
}
