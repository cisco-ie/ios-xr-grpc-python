""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
    """
    import json
    from grpc.framework.interfaces.face.face import AbortionError
    from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient

    def main():
            '''
        To not use tls we need to do 2 things.
        1. Comment the variables creds and options out
        2. Remove creds and options CiscoGRPCClient
        ex: client = CiscoGRPCClient('10.1.1.30', 57777, 10, 'vagrant', 'vagrant')
        '''
        creds = open('ems.pem').read()
        options = 'ems.cisco.com'
        client = CiscoGRPCClient('127.0.0.1', 57777, 10, 'vagrant', 'vagrant',creds,options)
        policy_file = open('example.cfg', 'r')
        new_policy = policy_file.read()
        policy_file.close()
        result = client.commitreplace(new_policy)
        print result

    if __name__ == '__main__':
        main()
