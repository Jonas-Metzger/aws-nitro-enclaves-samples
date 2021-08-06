#!/usr/local/bin/env python3

# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


import argparse
import inspect
import socket
import subprocess as sp
import sys
import time

from os import path

# import module outside of subtree
current_dir = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
vsock_dir = path.join(path.dirname(path.dirname(current_dir)), 'vsock_sample/py')
sys.path.insert(0, vsock_dir)
vs = __import__('vsock-sample')

# Binary executed
PUBLIC_KEY = 'my public key'
USER_DATA = 'more stuff'
RS_BINARY = './att_doc_retriever_sample/att_doc_retriever_sample'


def client_handler(args):
    client = vs.VsockStream()
    endpoint = (args.cid, args.port)
    client.connect(endpoint)

    # Execute binary and send the output to client
    proc = sp.Popen([RS_BINARY, PUBLIC_KEY, USER_DATA], stdout=sp.PIPE)
    out, err = proc.communicate()

    client.send_data(out)


def server_handler(args):
    server = vs.VsockListener()
    server.bind(args.port)
    server.recv_data()


def main():
    parser = argparse.ArgumentParser(prog='vsock-sample')
    parser.add_argument("--version", action="version",
                        help="Prints version information.",
                        version='%(prog)s 0.1.0')
    subparsers = parser.add_subparsers(title="options")

    client_parser = subparsers.add_parser("client", description="Client",
                                          help="Connect to a given cid and port.")
    client_parser.add_argument("cid", type=int, help="The remote endpoint CID.")
    client_parser.add_argument("port", type=int, help="The remote endpoint port.")
    client_parser.set_defaults(func=client_handler)

    server_parser = subparsers.add_parser("server", description="Server",
                                          help="Listen on a given port.")
    server_parser.add_argument("port", type=int, help="The local port to listen on.")
    server_parser.set_defaults(func=server_handler)

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

