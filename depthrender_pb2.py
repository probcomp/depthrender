# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depthrender.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depthrender.proto',
  package='depthrender',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64\x65pthrender.proto\x12\x0b\x64\x65pthrender\"k\n\x17RenderDepthImageRequest\x12\x14\n\x0cnum_vertices\x18\x01 \x01(\x05\x12\x15\n\rnum_triangles\x18\x02 \x01(\x05\x12\x10\n\x08vertices\x18\x03 \x01(\x0c\x12\x11\n\ttriangles\x18\x04 \x01(\x0c\"K\n\x15RenderDepthImageReply\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65pth_image\x18\x03 \x01(\x0c\x32m\n\x0b\x44\x65pthRender\x12^\n\x10RenderDepthImage\x12$.depthrender.RenderDepthImageRequest\x1a\".depthrender.RenderDepthImageReply\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_RENDERDEPTHIMAGEREQUEST = _descriptor.Descriptor(
  name='RenderDepthImageRequest',
  full_name='depthrender.RenderDepthImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_vertices', full_name='depthrender.RenderDepthImageRequest.num_vertices', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_triangles', full_name='depthrender.RenderDepthImageRequest.num_triangles', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='depthrender.RenderDepthImageRequest.vertices', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='triangles', full_name='depthrender.RenderDepthImageRequest.triangles', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=34,
  serialized_end=141,
)


_RENDERDEPTHIMAGEREPLY = _descriptor.Descriptor(
  name='RenderDepthImageReply',
  full_name='depthrender.RenderDepthImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='depthrender.RenderDepthImageReply.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='depthrender.RenderDepthImageReply.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth_image', full_name='depthrender.RenderDepthImageReply.depth_image', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=143,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['RenderDepthImageRequest'] = _RENDERDEPTHIMAGEREQUEST
DESCRIPTOR.message_types_by_name['RenderDepthImageReply'] = _RENDERDEPTHIMAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RenderDepthImageRequest = _reflection.GeneratedProtocolMessageType('RenderDepthImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENDERDEPTHIMAGEREQUEST,
  '__module__' : 'depthrender_pb2'
  # @@protoc_insertion_point(class_scope:depthrender.RenderDepthImageRequest)
  })
_sym_db.RegisterMessage(RenderDepthImageRequest)

RenderDepthImageReply = _reflection.GeneratedProtocolMessageType('RenderDepthImageReply', (_message.Message,), {
  'DESCRIPTOR' : _RENDERDEPTHIMAGEREPLY,
  '__module__' : 'depthrender_pb2'
  # @@protoc_insertion_point(class_scope:depthrender.RenderDepthImageReply)
  })
_sym_db.RegisterMessage(RenderDepthImageReply)


DESCRIPTOR._options = None

_DEPTHRENDER = _descriptor.ServiceDescriptor(
  name='DepthRender',
  full_name='depthrender.DepthRender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=220,
  serialized_end=329,
  methods=[
  _descriptor.MethodDescriptor(
    name='RenderDepthImage',
    full_name='depthrender.DepthRender.RenderDepthImage',
    index=0,
    containing_service=None,
    input_type=_RENDERDEPTHIMAGEREQUEST,
    output_type=_RENDERDEPTHIMAGEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEPTHRENDER)

DESCRIPTOR.services_by_name['DepthRender'] = _DEPTHRENDER

# @@protoc_insertion_point(module_scope)
