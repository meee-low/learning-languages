struct LinkedList<T: std::fmt::Debug> {
    head: Option<Box<Node<T>>>
}
struct Node<T: std::fmt::Debug> {
    value: T,
    next: Option<Box<Node<T>>>
}

impl<T: std::fmt::Debug> LinkedList<T> {
    pub fn new() -> Self {
        LinkedList { head: None }
    }
    pub fn append(&mut self, value: T) {
        match &mut self.head {
            Some(node) => node.append(value),
            None => self.head = Some(Box::new(Node::new(value)))
        }
    }

    pub fn show(&self) {
        match &self.head {
            Some(ref head_node_box) => {
                println!("{:?}", head_node_box.value);
                let curr_node = head_node_box;
                while let Some(next_node) = &curr_node.next {
                    println!("{:?}", next_node.value);
                }
            }
            None => {println!("Empty list");}
        }
    }
}

impl<T: std::fmt::Debug> Node<T> {
    fn new(value: T) -> Self {
        Node{value, next: None}
    }

    fn append(&mut self, value: T) {
        match &mut self.next {
            Some(node) => node.append(value),
            None => self.next = Some(Box::new(Node::new(value)))
        }
    }
}

fn main() {
    let mut ll = LinkedList::new();
    for i in 1..=5 {
        ll.append(i);
    }
    ll.show();
}