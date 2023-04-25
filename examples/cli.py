#!/usr/bin/env python
"""
GRPC Client with command line options

Usage:
    client.py -i <router_IP> -p <port> -u <user> -pw <password> -r <rpc> [--file <json_file>]
    client.py (-h | --help)

Options:
    -h --help    Show this help
    --version	 Show version
    -i           IP address of the router which the client will connect to
    -p           Router gRPC server will be running on some TCP port, generally 57400
    -u           Username to connect with
    -pw          User's password
    -r           RPC call to make.  Valid RPCS: get-oper, get-config, merge-config, replace-config
    --file	 Optional json file for filtered namespace requests.  Client is expecting these files to be stored in json/ folder

Example:
python cli.py -i 192.168.122.214 -p 57400 -u cisco -pw cisco -r get-oper --file json/get-oper-mpls-te.json

Note: Version 1.0 supports get-oper, get-config, and merge-config RPCs, replace-config hopefully coming soon
"""
import sys
sys.path.append('../')
from grpc.framework.interfaces.face.face import AbortionError
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient
from docopt import docopt


def main():

    __version__ = 'GRPC_Client 1.0'
    arguments = docopt(__doc__, version=__version__)

    IP = arguments['<router_IP>']
    TCP_PORT = int(arguments['<port>'])
    user = arguments['<user>']
    password = arguments['<password>']
    RPC = arguments['<rpc>']

    client = CiscoGRPCClient(IP, TCP_PORT, 600, user, password)

    if RPC == "get-oper":

        if arguments['--file']:
            file = arguments['--file']
            path = open(file).read()
        else:
            path = 'Error'
            print(
                'get-oper argument must include --file option and json file to filter yang operational namespace')
        try:
            err, result = client.getoper(path)
            if err:
                print(err)
            print(result)
        except AbortionError:
            print(
                'Unable to connect to local box, check your gRPC destination.')

    if RPC == "get-config":

        if arguments['--file']:
            file = arguments['--file']
            path = open(file).read()
        else:
            path = ""

        try:
            err, result = client.getconfig(path)
            if err:
                print(err)
            print(result)
        except AbortionError:
            print(
                'Unable to connect to local box, check your gRPC destination.')

    if RPC == "merge-config":

        if arguments['--file']:
            file = arguments['--file']
            path = open(file).read()
        else:
            path = 'Error'
            print(
                'get-oper argument must include --file option and json file to filter yang operational namespace')
        try:
            err = client.mergeconfig(path)
            if err:
                print(err)
            # print result
        except AbortionError:
            print(
                'Unable to connect to local box, check your gRPC destination.')

    if RPC == "replace-config":

        if arguments['--file']:
            file = arguments['--file']
            path = open(file).read()
        else:
            path = 'Error'
            print(
                'get-oper argument must include --file option and json file to filter yang operational namespace')
        try:
            err = client.replaceconfig(path)
            if err:
                print(err)
        except AbortionError:
            print(
                'Unable to connect to local box, check your gRPC destination.')

    if RPC == "delete-config":

        if arguments['--file']:
            file = arguments['--file']
            path = open(file).read()
        else:
            path = 'Error'
            print(
                'get-oper argument must include --file option and json file to filter yang operational namespace')
        try:
            err = client.deleteconfig(path)
            if err:
                print(err)
            # print result
        except AbortionError:
            print(
                'Unable to connect to local box, check your gRPC destination.')

if __name__ == '__main__':
    main()
