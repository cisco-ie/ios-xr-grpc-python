""" Basic collector for telemetry.
Initiate a gRPC dial-in telemetry channel, subscribe to a stream,
and output to display. Converts from protobuf to JSON for display.
"""

import sys
sys.path.insert(0, '../')
from lib.cisco_grpc_client import CiscoGRPCClient
import json

client = CiscoGRPCClient('10.200.96.16', 57400, 100, 'mdt', 'f33dm3d4t4')
subscription_id = 'sub1'
recv_count = 0
for segment in client.get_subscription(subscription_id):
	recv_count += 1
	print json.dumps(segment, indent=4, separators=(',', ': '))
	print 'End Telemetry Segment'
	print str(recv_count) + ' Segments Received'

