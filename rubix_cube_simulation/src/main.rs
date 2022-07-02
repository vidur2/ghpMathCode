mod rubix_cube;

use crate::rubix_cube::RubixCube;
use std::collections::{HashSet, VecDeque};

fn main() {
    let mut queue: VecDeque<RubixCube> = VecDeque::new();
    let mut visited: HashSet<Vec<Vec<bool>>> = HashSet::new();
    queue.push_back(RubixCube::new());

    while queue.len() != 0 {
        let current = queue.pop_front().unwrap();
        let leaves = current.step();

        visited.insert(current.top_face);

        for leaf in leaves.iter() {
            if !visited.contains(&leaf.top_face) {
                queue.push_back(leaf.clone());
            }
        }

    }

    let poss = RubixCube::generate_all_possibilities();
    let mut not_found: Vec<Vec<Vec<bool>>> = Vec::new();

    for face in poss.iter() {
        let top_face = face.clone();
        
        if !visited.contains(&top_face) {
            not_found.push(top_face);
        }
    }

    for face in not_found {
        for row in face {
            println!("{:?}", row);
        }

        println!("\n");
    }
}
