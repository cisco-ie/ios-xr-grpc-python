""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
"""
import json
from grpc.framework.interfaces.face.face import AbortionError
import sys
sys.path.insert(0, '../')
from lib.nexus_grpc_client import CiscoGRPCClient

def main():
    '''
    To not use tls we need to do 2 things.
    1. Comment the variables creds and options out
    2. Remove creds and options CiscoGRPCClient
    ex: client = CiscoGRPCClient('11.1.1.10', 57777, 10, 'vagrant', 'vagrant')
    '''
    #creds = open('ems.pem').read()
    #options = 'ems.cisco.com'
    client = CiscoGRPCClient('10.200.97.136', 50051, 10, 'admin', 'sp1l4b')
    #Test 1: Test Get config json requests
    path = '{"rpc":{"get-config":{"source":"running"}}}'
    try:
        err, result = client.getconfig(path)
        if err:
            print err
        print json.dumps(json.loads(result))
    except AbortionError:
        print AbortionError
        print(
            'Unable to connect to local box, check your gRPC destination.'
            )

if __name__ == '__main__':
    main()
