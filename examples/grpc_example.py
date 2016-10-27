""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
"""
import sys
sys.path.insert(0, '../')
from lib.cisco_grpc_client import CiscoGRPCClient
import json

def main():
    '''
    To not use tls we need to do 2 things.
    1. Comment the variables creds and options out
    2. Remove creds and options CiscoGRPCClient
    ex: client = CiscoGRPCClient('11.1.1.10', 57777, 10, 'vagrant', 'vagrant')
    '''
    creds = open('ems.pem').read()
    options='ems.cisco.com'
    client = CiscoGRPCClient('11.1.1.10', 57777, 10, 'vagrant', 'vagrant', creds, options)
    #Test 1: Test Get config json requests
    path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
    result = client.getconfig(path)
    print json.dumps(json.loads(result))

if __name__ == '__main__':
    main()
