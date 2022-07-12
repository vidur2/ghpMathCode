use std::collections::{HashSet, VecDeque};

use cube::Cube;

mod cube;

fn main() {
    let cube = Cube::new(2, 2, 2);

    let mut stack: VecDeque<Cube> = VecDeque::new();
    let mut visited: HashSet<Cube> = HashSet::new();
    let mut future: Vec<Cube> = Vec::new();

    let mut matrix: [[i8; 125]; 125] = [[0i8; 125]; 125];

    stack.push_back(cube);
    future.push(cube);

    while stack.len() > 0 {
        let current = stack.pop_front().unwrap();
        visited.insert(current);

        let (cube_arr, deg) = current.step();
        let column = index(&current, &future);
        matrix[column as usize][column as usize] = deg as i8;

        for cube in cube_arr.iter() {
            if !visited.contains(cube) {
                stack.push_back(cube.clone());
            }

            if index(cube, &future) == -1 {
                future.push(cube.clone())
            }

            let row = index(&cube, &future);

            matrix[column as usize][row as usize] = -1
        }
    }

    println!("{:?}", matrix)
}

fn index(cube: &Cube, hash_set: &Vec<Cube>) -> isize {
    for (idx, cube_check) in hash_set.iter().enumerate() {
        if cube == cube_check {
            return idx as isize;
        }
    }

    return -1;
}
