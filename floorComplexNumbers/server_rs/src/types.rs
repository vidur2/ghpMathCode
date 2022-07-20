use pyo3::{Py, PyAny};
use serde::{Serialize, Deserialize};

#[derive(Deserialize)]
pub struct GetGraph {
    pub interval: f32,
    pub range: u8,
    pub email: String
}