import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2
import nxos_grpc_pb2 as nxos__grpc__pb2


class gRPCConfigOperStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_stream(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/GetConfig',
        request_serializer=nxos__grpc__pb2.GetConfigArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.GetConfigReply.FromString,
        )
    self.Get = channel.unary_stream(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/Get',
        request_serializer=nxos__grpc__pb2.GetArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.GetReply.FromString,
        )
    self.GetOper = channel.unary_stream(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/GetOper',
        request_serializer=nxos__grpc__pb2.GetOperArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.GetOperReply.FromString,
        )
    self.EditConfig = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/EditConfig',
        request_serializer=nxos__grpc__pb2.EditConfigArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.EditConfigReply.FromString,
        )
    self.DeleteConfig = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/DeleteConfig',
        request_serializer=nxos__grpc__pb2.DeleteConfigArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.DeleteConfigReply.FromString,
        )
    self.CopyConfig = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/CopyConfig',
        request_serializer=nxos__grpc__pb2.CopyConfigArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.CopyConfigReply.FromString,
        )
    self.StartSession = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/StartSession',
        request_serializer=nxos__grpc__pb2.SessionArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.SessionReply.FromString,
        )
    self.CloseSession = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/CloseSession',
        request_serializer=nxos__grpc__pb2.CloseSessionArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.CloseSessionReply.FromString,
        )
    self.KillSession = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/KillSession',
        request_serializer=nxos__grpc__pb2.KillArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.KillReply.FromString,
        )
    self.Lock = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/Lock',
        request_serializer=nxos__grpc__pb2.LockArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.LockReply.FromString,
        )
    self.UnLock = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/UnLock',
        request_serializer=nxos__grpc__pb2.UnLockArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.UnLockReply.FromString,
        )
    self.Commit = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/Commit',
        request_serializer=nxos__grpc__pb2.CommitArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.CommitReply.FromString,
        )
    self.Validate = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/Validate',
        request_serializer=nxos__grpc__pb2.ValidateArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.ValidateReply.FromString,
        )
    self.Abort = channel.unary_unary(
        '/NXOSExtensibleManagabilityService.gRPCConfigOper/Abort',
        request_serializer=nxos__grpc__pb2.AbortArgs.SerializeToString,
        response_deserializer=nxos__grpc__pb2.AbortReply.FromString,
        )


class gRPCConfigOperServicer(object):

  def GetConfig(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOper(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EditConfig(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteConfig(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CopyConfig(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSession(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseSession(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KillSession(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Lock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnLock(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Commit(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Validate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Abort(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_gRPCConfigOperServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_stream_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=nxos__grpc__pb2.GetConfigArgs.FromString,
          response_serializer=nxos__grpc__pb2.GetConfigReply.SerializeToString,
      ),
      'Get': grpc.unary_stream_rpc_method_handler(
          servicer.Get,
          request_deserializer=nxos__grpc__pb2.GetArgs.FromString,
          response_serializer=nxos__grpc__pb2.GetReply.SerializeToString,
      ),
      'GetOper': grpc.unary_stream_rpc_method_handler(
          servicer.GetOper,
          request_deserializer=nxos__grpc__pb2.GetOperArgs.FromString,
          response_serializer=nxos__grpc__pb2.GetOperReply.SerializeToString,
      ),
      'EditConfig': grpc.unary_unary_rpc_method_handler(
          servicer.EditConfig,
          request_deserializer=nxos__grpc__pb2.EditConfigArgs.FromString,
          response_serializer=nxos__grpc__pb2.EditConfigReply.SerializeToString,
      ),
      'DeleteConfig': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteConfig,
          request_deserializer=nxos__grpc__pb2.DeleteConfigArgs.FromString,
          response_serializer=nxos__grpc__pb2.DeleteConfigReply.SerializeToString,
      ),
      'CopyConfig': grpc.unary_unary_rpc_method_handler(
          servicer.CopyConfig,
          request_deserializer=nxos__grpc__pb2.CopyConfigArgs.FromString,
          response_serializer=nxos__grpc__pb2.CopyConfigReply.SerializeToString,
      ),
      'StartSession': grpc.unary_unary_rpc_method_handler(
          servicer.StartSession,
          request_deserializer=nxos__grpc__pb2.SessionArgs.FromString,
          response_serializer=nxos__grpc__pb2.SessionReply.SerializeToString,
      ),
      'CloseSession': grpc.unary_unary_rpc_method_handler(
          servicer.CloseSession,
          request_deserializer=nxos__grpc__pb2.CloseSessionArgs.FromString,
          response_serializer=nxos__grpc__pb2.CloseSessionReply.SerializeToString,
      ),
      'KillSession': grpc.unary_unary_rpc_method_handler(
          servicer.KillSession,
          request_deserializer=nxos__grpc__pb2.KillArgs.FromString,
          response_serializer=nxos__grpc__pb2.KillReply.SerializeToString,
      ),
      'Lock': grpc.unary_unary_rpc_method_handler(
          servicer.Lock,
          request_deserializer=nxos__grpc__pb2.LockArgs.FromString,
          response_serializer=nxos__grpc__pb2.LockReply.SerializeToString,
      ),
      'UnLock': grpc.unary_unary_rpc_method_handler(
          servicer.UnLock,
          request_deserializer=nxos__grpc__pb2.UnLockArgs.FromString,
          response_serializer=nxos__grpc__pb2.UnLockReply.SerializeToString,
      ),
      'Commit': grpc.unary_unary_rpc_method_handler(
          servicer.Commit,
          request_deserializer=nxos__grpc__pb2.CommitArgs.FromString,
          response_serializer=nxos__grpc__pb2.CommitReply.SerializeToString,
      ),
      'Validate': grpc.unary_unary_rpc_method_handler(
          servicer.Validate,
          request_deserializer=nxos__grpc__pb2.ValidateArgs.FromString,
          response_serializer=nxos__grpc__pb2.ValidateReply.SerializeToString,
      ),
      'Abort': grpc.unary_unary_rpc_method_handler(
          servicer.Abort,
          request_deserializer=nxos__grpc__pb2.AbortArgs.FromString,
          response_serializer=nxos__grpc__pb2.AbortReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NXOSExtensibleManagabilityService.gRPCConfigOper', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
