import unittest
from cisco_grpc_client import CiscoGRPCClient
import json


class CiscoGRPCClientcase(unittest.TestCase):
    def setUp(self):
        self.client = CiscoGRPCClient('192.168.1.2', 57777, 10, 'vagrant', 'vagrant')
        self.maxDiff = None
        path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
        self._result = self.client.getconfig(path)
    def test_get(self):
        path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
        self._result = self.client.getconfig(path)
        try:
            json_object = json.loads(self._result)
        except ValueError, e:
            self.assertTrue(False, e)
        self.assertTrue(True)
    def test_replace(self):
        yangjsonreplace = '{"Cisco-IOS-XR-ip-static-cfg:router-static": {"default-vrf": {"address-family": {"vrfipv4": {"vrf-unicast": {"vrf-prefixes": {"vrf-prefix": [{"prefix": "0.0.0.0", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 0}, {"prefix": "1.2.3.5", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 32}]}}}}}}}'
        response = self.client.replaceconfig(yangjsonreplace)
        self.assertEqual(response.errors, u'')
    def test_merge(self):
        yangjsonmerge = '{"Cisco-IOS-XR-ip-static-cfg:router-static": {"default-vrf": {"address-family": {"vrfipv4": {"vrf-unicast": {"vrf-prefixes": {"vrf-prefix": [{"prefix": "1.2.3.6", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 32}]}}}}}}}'
        response = self.client.mergeconfig(yangjsonmerge)
        self.assertEqual(response.errors, u'')
        path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
        result = self.client.getconfig(path)
        result = json.dumps(json.loads(result))
        test_result = '{"Cisco-IOS-XR-ip-static-cfg:router-static": {"default-vrf": {"address-family": {"vrfipv4": {"vrf-unicast": {"vrf-prefixes": {"vrf-prefix": [{"prefix": "0.0.0.0", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 0}, {"prefix": "1.2.3.5", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 32}, {"prefix": "1.2.3.6", "vrf-route": {"vrf-next-hop-table": {"vrf-next-hop-next-hop-address": [{"next-hop-address": "10.0.2.2"}]}}, "prefix-length": 32}]}}}}}}}'
        self.assertEqual(result, test_result)
    def tearDown(self):
        response = self.client.replaceconfig(self._result)
if __name__ == '__main__':
    unittest.main()
