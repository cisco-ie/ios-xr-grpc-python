import sys
sys.path.insert(0, '../')
from lib.cisco_grpc_client import CiscoGRPCClient
import json

def main():
    #creds = open('ems.pem').read()
    #options='ems.cisco.com'
    client = CiscoGRPCClient('11.1.1.10', 57777, 10, 'vagrant', 'vagrant')
    #Test 1: Test Get config json requests
    path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
    result = client.getconfig(path)
    print json.dumps(json.loads(result))

if __name__ == '__main__':
    main()
