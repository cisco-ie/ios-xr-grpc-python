import grpc
from grpc.beta import implementations
import ems_grpc_pb2

class CiscoGRPCClient(object):
    def __init__(self, host, port, timeout, user, password, creds=None, options=None):
        if creds != None:
            self._target = '%s:%d' % (host, port)
            self._creds = implementations.ssl_channel_credentials(creds)
            self._options = options
            channel = grpc.secure_channel(
            self._target, self._creds, (('grpc.ssl_target_name_override', self._options,),))
            self._channel = implementations.Channel(channel)
        else:
            self._host = host
            self._port = port
            self._channel = implementations.insecure_channel(self._host, self._port)
        self._stub = ems_grpc_pb2.beta_create_gRPCConfigOper_stub(self._channel)
        self._timeout = int(timeout)
        self._metadata = [('username', user), ('password', password)]

    def getconfig(self, path):
        message = ems_grpc_pb2.ConfigGetArgs(yangpathjson=path)
        responses = self._stub.GetConfig(message,self._timeout, metadata = self._metadata)
        objects = ''
        for response in responses:
            objects += response.yangjson
        return objects

    def get_subscription(self, subid):
        sub_args = ems_grpc_pb2.CreateSubsArgs(ReqId=1, encode=3, subidstr=subid)
        stream = self._stub.CreateSubs(sub_args, timeout=self._timeout, metadata=self._metadata)
        self._channel.subscribe(self.connectivity_handler, True)
        for segment in stream:
            yield segment

    def connectivity_handler(self, result):
        print result

    def mergeconfig (self, yangjson):
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response = self._stub.MergeConfig(message, self._timeout, metadata = self._metadata)
        return response

    def deleteconfig (self, yangjson):
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response = self._stub.DeleteConfig(message, self._timeout, metadata = self._metadata)
        return response

    def replaceconfig (self, yangjson):
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response= self._stub.ReplaceConfig(message, self._timeout, metadata = self._metadata)
        return response
