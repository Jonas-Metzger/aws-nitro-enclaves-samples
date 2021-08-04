#!/bin/bash

DOCKER_IMAGE_NAME=att-doc-retriever-sample
EIF_FILE=att_doc_retriever_sample.eif
RS_CARGO_PATH=rs/Cargo.toml

# Build Rust app
cargo build --release --target=x86_64-unknown-linux-musl --manifest-path ${RS_CARGO_PATH}

# Build docker container
docker build -t ${DOCKER_IMAGE_NAME} -f Dockerfile ..

# Build Enclave image
nitro-cli build-enclave --docker-uri ${DOCKER_IMAGE_NAME} --output-file ${EIF_FILE}

