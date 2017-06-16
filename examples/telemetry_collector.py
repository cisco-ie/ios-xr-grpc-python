""" Basic collector for telemetry.
Initiate a gRPC dial-in telemetry channel, subscribe to a stream,
and output to display. Converts from protobuf to JSON for display.
"""

from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient
import json


def print_connectivity(connectivity):
    print connectivity


# Change client details to match your environment.
client = CiscoGRPCClient('localhost', 57777, 10, 'vagrant', 'vagrant')
subscription_id = 'sub1'
recv_count = 0
# Handle connectivity changes.
client.connectivityhandler(print_connectivity)
# Iterate over subscription recvs.
for segment in client.getsubscription(subscription_id, unmarshal=True):
    # unmarshal is an optional argument, default is unmarshal = True
    # If unmarshal is false, out is in gpb k/v
    recv_count += 1
    print(json.dumps(segment, indent=4, separators=(',', ': ')))
    print('End Telemetry Segment')
    print(str(recv_count) + ' Segments Received')
