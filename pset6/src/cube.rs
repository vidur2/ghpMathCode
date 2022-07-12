#[derive(Copy, Clone, Eq, Hash, PartialEq, Debug)]
pub struct Cube {
    x: i8,
    y: i8,
    z: i8,
}
impl Cube {
    pub fn new(x: i8, y: i8, z: i8) -> Self {
        return Self { x, y, z };
    }

    pub fn step(&self) -> (Vec<Self>, usize) {
        let mut neighbors: Vec<Self> = Vec::new();
        let mut conns: usize = 0;

        if self.x - 1 >= 0 {
            neighbors.push(Self::new(self.x - 1, self.y, self.z));
            conns += 1
        }
        if self.x + 1 < 5 {
            neighbors.push(Self::new(self.x + 1, self.y, self.z));
            conns += 1
        }
        if self.y - 1 >= 0 {
            neighbors.push(Self::new(self.x, self.y - 1, self.z));
            conns += 1
        }
        if self.y + 1 < 5 {
            neighbors.push(Self::new(self.x, self.y + 1, self.z));
            conns += 1
        }
        if self.z - 1 >= 0 {
            neighbors.push(Self::new(self.x, self.y, self.z - 1));
            conns += 1
        }
        if self.z + 1 < 5 {
            neighbors.push(Self::new(self.x, self.y, self.z + 1));
            conns += 1
        }

        return (neighbors, conns);
    }
}
