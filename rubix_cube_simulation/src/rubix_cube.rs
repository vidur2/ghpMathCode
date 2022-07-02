use std::{collections::HashSet, hash::Hash};

#[derive(Clone, Eq, Hash, PartialEq, Debug)]
pub struct RubixCube {
    pub top_face: Vec<Vec<bool>>,
    pub bottom_face: Vec<Vec<bool>>,
}

impl RubixCube {
    pub fn new() -> Self {
        Self {
            top_face: vec![
                vec![true, true, true],
                vec![true, true, true],
                vec![true, true, true],
            ],
            bottom_face: vec![
                vec![false, false, false],
                vec![false, false, false],
                vec![false, false, false],
            ],
        }
    }

    pub fn generate_all_possibilities() -> HashSet<Vec<Vec<bool>>> {
        let mut ret_possibilities: HashSet<Vec<Vec<bool>>> = HashSet::new();
        let mut stack: Vec<Vec<Vec<bool>>> = vec![Self::new().top_face];

        while stack.len() != 0 {
            let current = stack.pop().unwrap();
            ret_possibilities.insert(current.clone());
            for i in 0..3 {
                for j in 0..3 {
                    if i != 1 || j != 1  {
                        let mut mut_current = current.clone();
                        mut_current[i][j] = !mut_current[i][j];

                        if !ret_possibilities.contains(&mut_current) {
                            stack.push(mut_current)
                        }
                    }
                }
            }
        }
        return ret_possibilities;
    }

    pub fn step(&self) -> Vec<Self> {
        let mut ret_vec: Vec<Self> = Vec::new();

        let mut cloned_ref = self.clone();
        cloned_ref.transform_rubix_cube(true, 0);
        ret_vec.push(cloned_ref);
        let mut cloned_ref = self.clone();
        cloned_ref.transform_rubix_cube(true, 2);
        ret_vec.push(cloned_ref);
        let mut cloned_ref = self.clone();
        cloned_ref.transform_rubix_cube(false, 0);
        ret_vec.push(cloned_ref);
        let mut cloned_ref = self.clone();
        cloned_ref.transform_rubix_cube(false, 2);
        ret_vec.push(cloned_ref);

        return ret_vec;
    }

    fn transform_rubix_cube(&mut self, row: bool, index: usize) {
        if row {
            let top_row = &self.top_face[index];
            let bottom_row = &self.bottom_face[2 - index];

            let mut replacement_top: Vec<bool> = Vec::new();
            let mut replacement_bottom: Vec<bool> = Vec::new();

            for elem in top_row.iter() {
                replacement_bottom.push(*elem)
            }

            for elem in bottom_row.iter() {
                replacement_top.push(*elem)
            }

            self.top_face[index] = replacement_top;
            self.bottom_face[2 - index] = replacement_bottom
        } else {
            let mut replacement_top: Vec<bool> = Vec::new();
            let mut replacement_bottom: Vec<bool> = Vec::new();

            for elem in self.top_face.iter().rev() {
                replacement_bottom.push(elem[index])
            }

            for elem in self.bottom_face.iter().rev() {
                replacement_top.push(elem[2 - index])
            }

            for (idx, elem) in replacement_bottom.iter().enumerate() {
                self.bottom_face[idx][2 - index] = *elem
            }

            for (idx, elem) in replacement_top.iter().enumerate() {
                self.top_face[idx][index] = *elem
            }
        }
    }
}
