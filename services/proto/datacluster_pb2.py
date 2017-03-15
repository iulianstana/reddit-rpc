# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datacluster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datacluster.proto',
  package='cluster',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64\x61tacluster.proto\x12\x07\x63luster\"\xa6\x01\n\rRedditMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\tsubreddit\x18\x03 \x01(\t\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.cluster.RedditMessage.message_type\"+\n\x0cmessage_type\x12\x0e\n\nsubmission\x10\x00\x12\x0b\n\x07\x63omment\x10\x01\"\x14\n\x05Reply\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\x32K\n\x0b\x44\x61taCluster\x12<\n\x10\x41\x64\x64RedditMessage\x12\x16.cluster.RedditMessage\x1a\x0e.cluster.Reply\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REDDITMESSAGE_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='message_type',
  full_name='cluster.RedditMessage.message_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='submission', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='comment', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=154,
  serialized_end=197,
)
_sym_db.RegisterEnumDescriptor(_REDDITMESSAGE_MESSAGE_TYPE)


_REDDITMESSAGE = _descriptor.Descriptor(
  name='RedditMessage',
  full_name='cluster.RedditMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cluster.RedditMessage.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='cluster.RedditMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subreddit', full_name='cluster.RedditMessage.subreddit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='cluster.RedditMessage.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REDDITMESSAGE_MESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=197,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='cluster.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='cluster.Reply.ack', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=219,
)

_REDDITMESSAGE.fields_by_name['type'].enum_type = _REDDITMESSAGE_MESSAGE_TYPE
_REDDITMESSAGE_MESSAGE_TYPE.containing_type = _REDDITMESSAGE
DESCRIPTOR.message_types_by_name['RedditMessage'] = _REDDITMESSAGE
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY

RedditMessage = _reflection.GeneratedProtocolMessageType('RedditMessage', (_message.Message,), dict(
  DESCRIPTOR = _REDDITMESSAGE,
  __module__ = 'datacluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.RedditMessage)
  ))
_sym_db.RegisterMessage(RedditMessage)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), dict(
  DESCRIPTOR = _REPLY,
  __module__ = 'datacluster_pb2'
  # @@protoc_insertion_point(class_scope:cluster.Reply)
  ))
_sym_db.RegisterMessage(Reply)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class DataClusterStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.AddRedditMessage = channel.unary_unary(
          '/cluster.DataCluster/AddRedditMessage',
          request_serializer=RedditMessage.SerializeToString,
          response_deserializer=Reply.FromString,
          )


  class DataClusterServicer(object):

    def AddRedditMessage(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DataClusterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AddRedditMessage': grpc.unary_unary_rpc_method_handler(
            servicer.AddRedditMessage,
            request_deserializer=RedditMessage.FromString,
            response_serializer=Reply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'cluster.DataCluster', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDataClusterServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddRedditMessage(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDataClusterStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def AddRedditMessage(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AddRedditMessage.future = None


  def beta_create_DataCluster_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('cluster.DataCluster', 'AddRedditMessage'): RedditMessage.FromString,
    }
    response_serializers = {
      ('cluster.DataCluster', 'AddRedditMessage'): Reply.SerializeToString,
    }
    method_implementations = {
      ('cluster.DataCluster', 'AddRedditMessage'): face_utilities.unary_unary_inline(servicer.AddRedditMessage),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_DataCluster_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('cluster.DataCluster', 'AddRedditMessage'): RedditMessage.SerializeToString,
    }
    response_deserializers = {
      ('cluster.DataCluster', 'AddRedditMessage'): Reply.FromString,
    }
    cardinalities = {
      'AddRedditMessage': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'cluster.DataCluster', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
