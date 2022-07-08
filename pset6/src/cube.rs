
#[derive(Copy, Clone, Eq, Hash, PartialEq)]
pub struct Cube {
    x: i8,
    y: i8,
    z: i8
}
impl Cube {
    pub fn new(x: i8, y: i8, z: i8) -> Self {
        return Self { x, y, z }
    }

    pub fn step(&self) -> Vec<Self> {
        let mut neighbors: Vec<Self> = Vec::new();

        if self.x - 1 >= 0 {
            neighbors.push(Self::new(self.x - 1, self.y, self.z));
        } 
        if self.x + 1 < 5 {
            neighbors.push(Self::new(self.x + 1, self.y, self.z));
        }
        if self.y - 1 >= 0 {
            neighbors.push(Self::new(self.x, self.y - 1, self.z));
        } 
        if self.y + 1 < 5 {
            neighbors.push(Self::new(self.x, self.y + 1, self.z));
        } 
        if self.z - 1 >= 0 {
            neighbors.push(Self::new(self.x, self.y, self.z- 1));
        } 
        if self.z + 1 < 5 {
            neighbors.push(Self::new(self.x, self.y, self.z + 1));
        }

        return neighbors
    }
}