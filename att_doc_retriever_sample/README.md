# Attestation Document Retriever Sample

This is a sample application which retrieves an attestation document from an Enclave.
The attestation document is requested from the enclave using a Rust application which
is called by a python client that sends the results via vsock to a python server that
runs on the parent instance.

## EC2 Instance
The cheapest supported instance type is c5a.xlarge. See  https://docs.aws.amazon.com/enclaves/latest/user/getting-started.html. We use the 
AWS Nitro Enclaves Developer AMI (https://aws.amazon.com/marketplace/pp/prodview-37z6ersmwouq2). We require the following commands before we can run the build.sh:

```
curl --proto '=https' --tlsv1.2 -sSfy https://sh.rustup.rs | sh 
rustup target add x86_64-unknown-linux-musl
sudo yum install git
```

Then git clone this repo and proceed.

## Build

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

