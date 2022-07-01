#[derive(Clone, Eq, Hash, PartialEq, Debug)]
pub struct RubixCube {
    top_face: Vec<Vec<bool>>,
    bottom_face: Vec<Vec<bool>>,
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
            let bottom_row = &self.bottom_face[index];

            let mut replacement_top: Vec<bool> = Vec::new();
            let mut replacement_bottom: Vec<bool> = Vec::new();

            for elem in top_row.iter().rev() {
                replacement_bottom.push(*elem)
            }

            for elem in bottom_row.iter().rev() {
                replacement_top.push(*elem)
            }

            self.top_face[index] = replacement_top;
            self.bottom_face[index] = replacement_bottom
        } else {
            let mut replacement_top: Vec<bool> = Vec::new();
            let mut replacement_bottom: Vec<bool> = Vec::new();

            for elem in self.top_face.iter().rev() {
                replacement_bottom.push(elem[index])
            }

            for elem in self.bottom_face.iter().rev() {
                replacement_top.push(elem[index])
            }

            for (idx, elem) in replacement_bottom.iter().enumerate() {
                self.bottom_face[idx][index] = *elem
            }

            for (idx, elem) in replacement_top.iter().enumerate() {
                self.top_face[idx][index] = *elem
            }
        }
    }
}