# Basic collector for telemetry.
# TBDone

from cisco_grpc_client_insecure import CiscoGRPCClient
import json
import time

client = CiscoGRPCClient('192.168.1.2', 57777, 100, 'vagrant', 'vagrant')
path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'
result = client.getconfig(path)
print result
print 'getconfig() printed, waiting 3 seconds.'
time.sleep(3)
path = '1'
recv_count = 0
for segment in client.get_subscription(path):
	recv_count += 1
	print segment
	print 'End Telemetry Segment'
	print str(recv_count) + ' Segments Received'

