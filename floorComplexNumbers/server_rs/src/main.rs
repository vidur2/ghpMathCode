mod types;

use std::{net::TcpListener, io::Read};
use std::thread;

use pyo3::prelude::*;
use types::GetGraph;

fn main() {
    let listener = TcpListener::bind("0.0.0.0:5001").unwrap();

    for stream in listener.incoming() {
        let mut stream = stream.unwrap();

        thread::spawn(move || {
            let mut buff: [u8; 1024] = [0u8; 1024];

            stream.read(&mut buff).expect("Could not read stream");

            if buff.starts_with(b"POST /get_graph HTTP/1.1") {
                let body_str = String::from_utf8(buff.to_vec()).unwrap();
                let parsed = parse_body(body_str);
                let body_inf: GetGraph = serde_json::from_str(&parsed).unwrap();
                run_py(body_inf).unwrap();
            }
            
        });
    }
}

fn run_py(params: GetGraph) -> PyResult<()> {
    Python::with_gil(|py| {
        let dcolor = PyModule::import(py, "dcolorUse")?;
        dcolor.getattr("calcRoots")?.call1((params.range, params.interval))?;
        let smtp_stuff = PyModule::import(py, "smtpStuff")?;
        smtp_stuff.getattr("sendMail")?.call1((params.email,))?;
        Ok(())
    })
}

fn parse_body(body: String) -> String {
    let split_string: Vec<&str> = body.split("Content-Length: ").collect();
    if split_string.len() > 1 {
        let content_len = split_string[1];
        let content_len_split: Vec<&str> = content_len.split("\n").collect();
        let content_len_int: usize = content_len_split[0]
            .trim()
            .parse()
            .expect("Could not cast to integer");
        let split_body: Vec<&str> = body.split("\n").collect();
        println!("{}", split_body[split_body.len() - 1]);
        String::from(split_body[split_body.len() - 1])
            .split_at(content_len_int)
            .0
            .to_string()
    } else {
        println!("{}", split_string[0]);
        return String::from(split_string[0]);
    }
}
