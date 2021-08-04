# Attestation Document Retriever Sample

This is a sample application which retrieves an attestation document from an Enclave.
The attestation document is requested from the enclave using a Rust application which
is called by a python client that sends the results via vsock to a python server that
runs on the parent instance.

## Build

Use the steps from https://docs.aws.amazon.com/enclaves/latest/user/getting-started.html to set up a parent instance that can run
the generated enclave image.

Run the `build.sh` script to build the Rust application, the docker container and the enclave image.
`$ ./build.sh`

## Run

Start server on parent instance
`$ python3 py/att_doc_retriever_sample.py server 5010`

Using the nitro tools, run the enclave providing the enclave image form the build step.
`$ nitro-cli run-enclave --cpu-count 2 --memory 512 --eif-path att_doc_retriever_sample.eif --debug-mode`

On the parent instance you should see the Attestation Document sent from the enclave
```
$ python3 py/att_doc_retriever_sample.py server 5010
Attestation { document: ...
```

