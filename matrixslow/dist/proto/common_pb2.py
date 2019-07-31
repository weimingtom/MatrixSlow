# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63ommon.proto\"\'\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnode_type\x18\x02 \x01(\t\"$\n\x06Matrix\x12\r\n\x05value\x18\x01 \x03(\x02\x12\x0b\n\x03\x64im\x18\x02 \x03(\x05\"Q\n\rNodeGradients\x12\x14\n\x05nodes\x18\x01 \x03(\x0b\x32\x05.Node\x12\x1a\n\tgradients\x18\x02 \x03(\x0b\x32\x07.Matrix\x12\x0e\n\x06\x61\x63\x63_no\x18\x03 \x01(\x05\"L\n\x16VariableWeightsReqResp\x12\x18\n\tvariables\x18\x01 \x03(\x0b\x32\x05.Node\x12\x18\n\x07weights\x18\x02 \x03(\x0b\x32\x07.Matrixb\x06proto3')
)




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_type', full_name='Node.node_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=55,
)


_MATRIX = _descriptor.Descriptor(
  name='Matrix',
  full_name='Matrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Matrix.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim', full_name='Matrix.dim', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=93,
)


_NODEGRADIENTS = _descriptor.Descriptor(
  name='NodeGradients',
  full_name='NodeGradients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='NodeGradients.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradients', full_name='NodeGradients.gradients', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_no', full_name='NodeGradients.acc_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=176,
)


_VARIABLEWEIGHTSREQRESP = _descriptor.Descriptor(
  name='VariableWeightsReqResp',
  full_name='VariableWeightsReqResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variables', full_name='VariableWeightsReqResp.variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='VariableWeightsReqResp.weights', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=254,
)

_NODEGRADIENTS.fields_by_name['nodes'].message_type = _NODE
_NODEGRADIENTS.fields_by_name['gradients'].message_type = _MATRIX
_VARIABLEWEIGHTSREQRESP.fields_by_name['variables'].message_type = _NODE
_VARIABLEWEIGHTSREQRESP.fields_by_name['weights'].message_type = _MATRIX
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Matrix'] = _MATRIX
DESCRIPTOR.message_types_by_name['NodeGradients'] = _NODEGRADIENTS
DESCRIPTOR.message_types_by_name['VariableWeightsReqResp'] = _VARIABLEWEIGHTSREQRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  })
_sym_db.RegisterMessage(Node)

Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), {
  'DESCRIPTOR' : _MATRIX,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:Matrix)
  })
_sym_db.RegisterMessage(Matrix)

NodeGradients = _reflection.GeneratedProtocolMessageType('NodeGradients', (_message.Message,), {
  'DESCRIPTOR' : _NODEGRADIENTS,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:NodeGradients)
  })
_sym_db.RegisterMessage(NodeGradients)

VariableWeightsReqResp = _reflection.GeneratedProtocolMessageType('VariableWeightsReqResp', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLEWEIGHTSREQRESP,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:VariableWeightsReqResp)
  })
_sym_db.RegisterMessage(VariableWeightsReqResp)


# @@protoc_insertion_point(module_scope)