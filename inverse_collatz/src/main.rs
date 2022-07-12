use std::collections::VecDeque;
use node::Node;

mod node;



fn main() {
    let mut queue: VecDeque<Node> = VecDeque::new();

    queue.push_back(Node::new(1, 0));
    
    while queue.len() != 0 {
        let current = queue.pop_front().unwrap();
        println!("{:?}", current);

        let (low, high) = current.generate_next();

        if low.data > 0 {
            queue.push_back(low);
            queue.push_back(high);
        } else {
            queue.push_back(high);
        }
    }
}