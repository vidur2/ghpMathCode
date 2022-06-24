/*
PSET 1 Problem 1
Vidur Modgil, Max Wang, Eric Sun, Kevin Yuan
*/

// Constant initialization
const MAX_NUM: u128 = 9;

// Imports
use std::collections::HashSet;

fn main() {

    // Initialization of vector with values of digits and changing values
    let mut stack: Vec<u128> = Vec::new();

    for i in 1..MAX_NUM+1 { stack.push(i) };

    let mut current_possibility: u128;

    // Initialization of final output vec
    let mut answer_vec = Vec::new();

    // Keeps on going until stack runs out of values
    while stack.len() > 0 {

        // Gets the first element out of the stack
        current_possibility = stack.pop().unwrap();

        // Chacks all digits
        for i in 1..MAX_NUM + 1 {

            // Checks if string only contains uinque digits
            let current_possibility_str = current_possibility.clone().to_string();
            let valid = check_if_unique(&current_possibility_str);

            // Checking modulo
            if valid {
                let value = (current_possibility_str.len() + 1) as u128; 
                let test_value = current_possibility * 10 + i;

                if test_value % value == 0 && value == MAX_NUM {
                    answer_vec.push(test_value)
                } 
                // If above 9, return
                else if test_value % value == 0 {
                    stack.push(test_value)
                }
            }
        }
    }

    // Printing out answer
    for answer in answer_vec.iter() {
        println!("{}", answer);
    }
}


// Function to check if string is unique
fn check_if_unique(input: &str) -> bool {


    // HashSets are unique
    let mut check_set: HashSet<char> = HashSet::new();

    // Checks if char not in hashset, if in hashset break
    for char_ in input.chars() {
        if check_set.contains(&char_) {
            return false
        } 

        check_set.insert(char_);
    }

    // Return true if runs
    return true
}