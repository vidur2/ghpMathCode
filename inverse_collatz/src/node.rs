#[derive(Debug)]
pub struct Node {
    pub data: u128,
    pub level: u128
}

impl Node {
    pub fn new(data: u128, level: u128) -> Node {
        return Node {
            data,
            level
        }
    }

    pub fn generate_next(&self) -> (Node, Node) {
        let (low, high) = ((self.data - 1)/3, 2 * self.data);

        return (Node::new(low, self.level + 1), Node::new(high, self.level + 1))
    }
}