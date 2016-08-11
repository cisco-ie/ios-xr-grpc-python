import grpc
from grpc.beta import implementations
import ems_grpc_pb2

class CiscoGRPCClient(object):
    def __init__(self, host, port, timeout, user, password, creds=None, options=None):
        """This class creates grpc calls using python.
            :param username: Username for device login
            :param password: Password for device login
            :param host: The ip address for the device
            :param port: The port for the device
            :param timeout: how long before the rpc call timesout
            :param creds: Input of the pem file
            :param options: TLS server name
            :type password: str
            :type username: str
            :type server: str
            :type port: int
            :type timeout:int
            :type creds: str
            :type options: str
        """
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

    def __repr__(self):
        return '%s(Host = %s, Port = %s, User = %s, Password = %s, Timeout = %s)' % (
            self.__class__.__name__,
            self._host,
            self._port,
            self._metadata[0][1],
            self._metadata[1][1],
            self._timeout
        )

    def getconfig(self, path):
        """Get grpc call
            :param data: JSON
            :type data: str
            :return: Return the response object
            :rtype: Response stream object
        """
        message = ems_grpc_pb2.ConfigGetArgs(yangpathjson=path)
        responses = self._stub.GetConfig(message,self._timeout, metadata = self._metadata)
        objects = ''
        for response in responses:
            objects += response.yangjson
        return objects

    def mergeconfig (self, yangjson):
        """Merge grpc call equivalent  of PATCH RESTconf call
            :param data: JSON
            :type data: str
            :return: Return the response object
            :rtype: Response object
        """
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response = self._stub.MergeConfig(message, self._timeout, metadata = self._metadata)
        return response

    def deleteconfig (self, yangjson):
        """delete grpc call
            :param data: JSON
            :type data: str
            :return: Return the response object
            :rtype: Response object
        """
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response = self._stub.DeleteConfig(message, self._timeout, metadata = self._metadata)
        return response

    def replaceconfig (self, yangjson):
        """Replace grpc call equivalent of PUT in restconf
            :param data: JSON
            :type data: str
            :return: Return the response object
            :rtype: Response object
        """
        message = ems_grpc_pb2.ConfigArgs(yangjson= yangjson)
        response= self._stub.ReplaceConfig(message, self._timeout, metadata = self._metadata)
        return response
    def getoper (self, path):
        """ Get Oper call
            :param data: JSON
            :type data: str
            :return: Return the response object
            :rtype: Response stream object
        """
        message = ems_grpc_pb2.GetOperArgs(yangpathjson=path)
        responses = self._stub.GetOper(message,self._timeout, metadata = self._metadata)
        objects = ''
        for response in responses:
            objects += response.yangjson
        return objects

    def showcmdtextoutput (self, cli):
        """ Get of CLI show commands in text
            :param data: cli show
            :type data: str
            :return: Return the response object
            :rtype: str
        """
        stub = ems_grpc_pb2.beta_create_gRPCExec_stub(self._channel)
        message = ems_grpc_pb2.ShowCmdArgs(cli = cli)
        response = stub.ShowCmdTextOutput(message, self._timeout, metadata = self._metadata)
        objects = ''
        for response in responses:
            objects += response.output
        return objects

    def showcmdjsonoutput (self, cli):
        """ Get of CLI show commands in json
            :param data: cli show
            :type data: str
            :return: Return the response object
            :rtype: str
        """
        stub = ems_grpc_pb2.beta_create_gRPCExec_stub(self._channel)
        message = ems_grpc_pb2.ShowCmdArgs(cli = cli)
        response = stub.ShowCmdJSONOutput(message, self._timeout, metadata = self._metadata)
        objects = ''
        for response in responses:
            objects += response.jsonoutput
        return objects




