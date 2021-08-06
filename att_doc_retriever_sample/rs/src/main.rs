use nsm_io::Request;
use serde_bytes::ByteBuf;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let key_arg = &args[1];
    let data_arg = &args[2];
    
    let nsm_fd = nsm_driver::nsm_init();

    let public_key = ByteBuf::from(key_arg);
    let user_data = ByteBuf::from(data_arg);

    let request = Request::Attestation {
        public_key: Some(public_key),
        user_data: Some(user_data),
        nonce: None,
    };

    let response = nsm_driver::nsm_process_request(nsm_fd, request);
    println!("{:?}", response);

    nsm_driver::nsm_exit(nsm_fd);
}

