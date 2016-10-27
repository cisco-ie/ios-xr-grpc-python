"""
This module needs to be able to do a few things using gRPC Openconfig modules.
1. Get information on policy and bgp neighbors.
2. Apple to apply single or multiple policies to an interfaces.
3. Get a policy from box a and apply it to box b.
4. It needs to use templating to create new policies and apply to upload them in the end.
"""
import json
from collections import OrderedDict
import sys
sys.path.insert(0, '../')
from lib.cisco_grpc_client import CiscoGRPCClient


class RoutePolicy(object):
    """Class to manipulate route policy and bgp neighbors using openconfig
    """
    def __init__(self, host, port, username, password):
        """This class creates a grpc client for the functions to use.
            :param host: The ip address for the device.
            :param port: The port for the device.
            :param user: Username for device login.
            :param password: Password for device login.
            :type host: str
            :type port: int
            :type password: str
            :type username: str
        """
        self.client = CiscoGRPCClient(host, port, 10, username, password)

    def get_policies(self):
        """sends a gRPC request and returns openconfig json of policies
            :return: Json string of policies
            :rtype: json object
        """
        path = '{"openconfig-routing-policy:routing-policy": [null]}'
        result = self.client.getconfig(path)
        policies = json.loads(result, object_pairs_hook=OrderedDict)
        return policies

    def list_policies(self):
        """Prints a list policies names for a router
        """
        bgp_policies = self.get_policies()
        policy_definitions = bgp_policies['openconfig-routing-policy:routing-policy']['policy-definitions']['policy-definition']
        print '\nPolicy Names:\n'
        for policy in policy_definitions:
            print 'Name: %s' % policy['name']

    def detail_policy(self, policy_name):
        """Prints the full json of a policy in Openconfig and returns it
            :param policy_name: Policy Name on the box (case sensative).
            :type policy_name: str
            :return: Json string of policy
            :rtype: str
        """
        bgp_policies = self.get_policies()
        policy_definitions = bgp_policies['openconfig-routing-policy:routing-policy']['policy-definitions']['policy-definition']
        for policy in policy_definitions:
            if policy_name == policy['name']:
                print json.dumps(policy, indent=4, separators=(',', ': '))
                inner = json.dumps(policy)
        template = '{"openconfig-routing-policy:routing-policy": {"policy-definitions": {"policy-definition": [%s]}}}' % inner
        return json.dumps(json.loads(template, object_pairs_hook=OrderedDict), indent=4, separators=(',', ': '))

    def get_neighbors(self):
        """sends a gRPC request and returns openconfig json of BGP
            :return: Json string of policies
            :rtype: json object
        """
        path = '{"openconfig-bgp:bgp": [null]}'
        result = self.client.getconfig(path)
        bgp = json.loads(result, object_pairs_hook=OrderedDict)
        return bgp

    def list_neighbors(self):
        """Prints a list bgp neighbors for a router
        """
        bgp = self.get_neighbors()
        bgp_neighbors = bgp['openconfig-bgp:bgp']['neighbors']['neighbor']
        print "\nNeighbor's\n"
        for neighbor in bgp_neighbors:
            print 'Neighbor: %s AS: %s' % (neighbor['neighbor-address'], neighbor['config']['peer-as'])

    def detail_neighbor(self, neighbor_address):
        """Prints the full json of a neighbor in Openconfig format
            :param policy_name: Neighbor Address on the box.
            :type policy_name: str
        """
        bgp = self.get_neighbors()
        bgp_neighbors = bgp['openconfig-bgp:bgp']['neighbors']['neighbor']
        for neighbor in bgp_neighbors:
            if neighbor_address == neighbor['neighbor-address']:
                print json.dumps(neighbor, indent=4, separators=(',', ': '))
                inner = json.dumps(neighbor)
        template = '{"openconfig-bgp:bgp": {"neighbors": {"neighbor" :  [%s]}}}' % inner
        return json.dumps(json.loads(template, object_pairs_hook=OrderedDict), indent=4, separators=(',', ': '))

    def is_int(self, num):
        """Helper function to see if value is a integer.
        Used to figure if its an AS or Neighbor Address
        :param num: A number or str
        :type: int or str
        :rtype boolean
        """
        try:
            int(num)
            return True
        except ValueError:
            return False

    def merge_config(self, config):
        """gRPC merge call to push config changes to Router
        :param config: yang structured config in json
        :type config: str
        :return error if applicable
        :rtype str
        """
        try:
            response = self.client.mergeconfig(config)
            if response.errors:
                err = json.loads(response.errors)
                return json.dumps(err, indent=4, separators=(',', ': '))
        except ValueError as err:
            return err

    def neighbor_policy(self, neighbor_address, policy, direction):
        """Function to update a neighbors or AS policy
        :param neighbor_address: neighbor address or AS for policy
        :param policy: name of policy to be applied
        :param direction: export-policy or import-policy
        :type neighbor_address: str or int
        :type policy: str
        :type direction: str
        :returns: Prints neighbors it is applied to, and new bgp neighbor config
        """
        updated_neighbors = []
        bgp = self.get_neighbors()
        bgp_neighbors = bgp['openconfig-bgp:bgp']['neighbors']['neighbor']
        for neighbor in bgp_neighbors:
            if self.is_int(neighbor_address):
                val = neighbor['config']['peer-as']
            else:
                val = neighbor['neighbor-address']
            if val in neighbor_address:
                if len(policy) > 1 and isinstance(policy, list):
                    policy = self.multiple_policies(policy, neighbor_address)
                # Change the policy to drop.
                ipvs = neighbor['afi-safis']['afi-safi']
                for ipv in ipvs:
                    curr_policy = ipv['apply-policy']['config'][direction]
                    ipv['apply-policy']['config']['export-policy'] = policy
                    ip_type = ipv['afi-safi-name']
                    # Add the removed neighbors to list.
                    updated_neighbors.append((neighbor['neighbor-address'], ip_type, curr_policy))
        updated_neighbors = json.dumps(updated_neighbors)
        print updated_neighbors
        bgp_config = json.dumps(bgp)
        err = self.merge_config(bgp_config)
        if not err:
            print err
        print '\nNew Neighbor Detail:\n'
        self.detail_neighbor(neighbor_address)

    def multiple_policies(self, policies, neighbor):
        """Creates a new policy that applies list of policies to it.
        :param policies: list of policies that you want applied to a single policy
        :param neighbor: the neighbor you are going to apply these policies (used for naming)
        :type policies: list
        :type neighbor: str
        :return:  Name of the policy that is created
        :rtype: str
        """
        policy_name = neighbor.replace('.', '_')
        policy_name = 'multi_policy_' + policy_name
        shell = '{"openconfig-routing-policy:routing-policy": {"policy-definitions": {"policy-definition": [{"name": "%s","statements": {"statement": []}}]}}}' % policy_name
        shell = json.loads(shell, object_pairs_hook=OrderedDict)
        conditions = shell['openconfig-routing-policy:routing-policy']['policy-definitions']['policy-definition'][0]['statements']['statement']
        for policy in policies:
            policy_nm = 'Policy_' + policy
            json_policy = '{"name": "%s", "conditions": {"call-policy": "%s"}}' % (policy_nm, policy)
            json_policy = json.loads(json_policy, object_pairs_hook=OrderedDict)
            conditions.append(json_policy)
        multi_policy = json.dumps(shell)
        print self.merge_config(multi_policy)
        return policy_name

def main():
    """
    Testing and demoing functions in class
    """
    # Create a class object for route policy manipulation
    route = RoutePolicy('localhost', 57777, 'vagrant', 'vagrant')
    # List  Policies from Router
    route.list_policies()
    print '\nnext function\n'
    # Get the full json object of the policy, allows for manipulation
    policy = route.detail_policy('TEST')
    print '\nnext function\n'
    # List BGP neighbors
    route.list_neighbors()
    print '\nnext function\n'
    # Get the full json object of the BGP neighbor, allows for manipulation
    route.detail_neighbor('11.1.1.2')
    print '\nnext function\n'
    # Apply multiple policies to a single neighbor interface
    route.neighbor_policy('11.1.1.2', ['TEST', 'SEND-MED-IGP'], 'export-policy')
    print '\nnext function\n'
    # Store policy in json file to modify
    policy_file = open('policy.json', 'w')
    policy_file.write(policy)
    policy_file.close()
    # Merge policy from file to router
    policy_file = open('policy.json', 'r')
    route.merge_config(policy_file.read())
    policy_file.close()

if __name__ == '__main__':
    main()
