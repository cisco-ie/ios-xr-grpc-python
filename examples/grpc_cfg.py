'''
Note:
This is an example to show replace and merge configs work with a get command.
The example is using XRdocs vagrant topology for all the configurations
'''

import sys
sys.path.insert(0, '../')
from lib.cisco_grpc_client import CiscoGRPCClient
import json
from time import sleep

class Example:
    def __init__(self):
        self.client = CiscoGRPCClient('11.1.1.10', 57777, 10, 'vagrant', 'vagrant')
    def get(self):
        path = '{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}'
        result = self.client.getconfig(path)
        print result

    def replace(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.replaceconfig(path)
        print result # If this is sucessful, then there should be no errors.

    def merge(self):
        path = open('snips/bgp_merge.json').read()
        result = self.client.mergeconfig(path)
        print result # If this is sucessful, then there should be no errors.

    def delete(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.deleteconfig(path)
        print result # If this is sucessful, then there should be no errors.

def main():
    '''
    This example does not use TLS, if you want to use TLS please refer to the example with tls
    Here is a workflow of the example that uses all the different types.
    '''
    example = Example()
    #We are going to start with a replace config, to add a base BGP config
    example.replace()
    #Lets see what the bgp is on the router to ensure the the config got placed in there. \n'
    #This config should be the same as the starting snip\n'
    example.get()
    #Let us use merge to add another neighbor.
    example.merge()
    #The resulting config should be the first config plus the second
    example.get()
    #If we were to replace the config wtih the starting config we would see only the starting config
    example.replace()
    example.get()
    #If we were to delete the config using the starting json, we would see that bgp is no longer active.
    example.delete()
    example.get()

if __name__ == '__main__':
    main()
