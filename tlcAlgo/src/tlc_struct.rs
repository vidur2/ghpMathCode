use std::sync::{Mutex, Arc};

#[derive(Clone, PartialEq, Eq, Hash, Debug)]
pub struct Tlc(String);

impl Tlc {
    pub fn new(data: String) -> Self {
        return Self(data)
    }

    pub fn check_all(self) -> Vec<Self> {

        let ret_vec: Arc<Mutex<Vec<Self>>> = Arc::new(Mutex::new(Vec::new()));

        if self.0.ends_with("L") {
            ret_vec.lock().unwrap().push(self.clone().append_c());
        }
        ret_vec.lock().unwrap().push(self.clone().repeat_seq());

        let ret_vec_sing = Arc::clone(&ret_vec);

        let inner = self.clone();
        for i in inner.replace_lll().iter() {
            ret_vec_sing.lock().unwrap().push(i.clone());
        };

        let ret_vec_sing  = Arc::clone(&ret_vec);

        let inner = self.clone();
        for i in inner.remove_cc() {
            ret_vec_sing.lock().unwrap().push(i.clone())
        }

        return ret_vec.lock().unwrap().clone();
    }

    fn append_c(self) -> Self {
        let mut scoped = self.0.clone();
        scoped.push('C');
        return self.clone()
    }

    fn repeat_seq(self) -> Self {
        let (_t, rest) = self.0.split_at(1);
        return Self(String::from("T") + rest + rest)
    }

    fn replace_lll(self) -> Vec<Self> {

        let indeces: Vec<(usize, &str)> = self.0.match_indices("LLL").collect();
        let mut ret_val: Vec<Self> = Vec::new();

        for (index, _value) in indeces.iter() {
            let mut added_val = self.0.clone();
            added_val.replace_range(index..&(index + 3), "C");
            let check = Tlc::new(added_val.clone());

            ret_val.push(check);
        }

        return ret_val;
    }

    fn remove_cc(self) -> Vec<Self> {
        let indeces: Vec<(usize, &str)> = self.0.match_indices("CC").collect();
        let mut ret_val: Vec<Self> = Vec::new();

        for (index, _value) in indeces.iter() {
            let mut added_val = self.0.clone();
            added_val.replace_range(index..&(index + 2), "");
            let check = Tlc::new(added_val.clone());

            ret_val.push(check)
        }

        return ret_val;
    }
}