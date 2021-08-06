# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

FROM python:3.7.9-alpine3.12

# Copy the Rust compiled binary which retrieves the Attestation document to container
COPY att_doc_retriever_sample/rs/target/x86_64-unknown-linux-musl/release/att_doc_retriever_sample att_doc_retriever_sample/

# Copy the python client-server handler logic to the container
COPY att_doc_retriever_sample/py/att_doc_retriever_sample.py att_doc_retriever_sample/

# Copy the client-server logic from the vsock sample to the container
COPY vsock_sample/py/vsock-sample.py vsock_sample/py/

#    3 is the CID for the parent instance
# 5010 is the socket port
CMD ["/usr/local/bin/python3", "att_doc_retriever_sample/att_doc_retriever_sample.py", "enclave", "3", "5010"]

