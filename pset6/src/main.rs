use std::collections::HashSet;

use cube::Cube;

mod cube;

fn main() {
    let cube = Cube::new(2,2, 2);

    let mut stack: Vec<Cube> = Vec::new();
    let mut visited: HashSet<Cube> = HashSet::new();

    stack.push(cube);

    while stack.len() > 0 {
        let current = stack.pop().unwrap();
        visited.insert(current);

        let cube_arr = current.step();
        for cube in cube_arr.iter() {
            if !visited.contains(cube) {
                stack.push(cube.clone());
            }
        }
    }

    println!("{}", visited.len())
}
