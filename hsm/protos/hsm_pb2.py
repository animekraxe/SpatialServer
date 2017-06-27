# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/hsm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/hsm.proto',
  package='hsm',
  syntax='proto3',
  serialized_pb=_b('\n\x10protos/hsm.proto\x12\x03hsm\"(\n\x05Vec3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"3\n\x05Vec4D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"*\n\x04\x46\x61\x63\x65\x12\n\n\x02v1\x18\x01 \x01(\r\x12\n\n\x02v2\x18\x02 \x01(\r\x12\n\n\x02v3\x18\x03 \x01(\r\"e\n\tTransform\x12\x1f\n\x0btranslation\x18\x01 \x01(\x0b\x32\n.hsm.Vec3D\x12\x1c\n\x08rotation\x18\x02 \x01(\x0b\x32\n.hsm.Vec4D\x12\x19\n\x05scale\x18\x03 \x01(\x0b\x32\n.hsm.Vec3D\"O\n\x17\x44\x65viceToMarkerTransform\x12!\n\ttransform\x18\x01 \x01(\x0b\x32\x0e.hsm.Transform\x12\x11\n\tmarker_id\x18\x02 \x01(\r\"[\n\x04Mesh\x12\x1c\n\x08vertices\x18\x01 \x03(\x0b\x32\n.hsm.Vec3D\x12\x18\n\x05\x66\x61\x63\x65s\x18\x02 \x03(\x0b\x32\t.hsm.Face\x12\x1b\n\x07normals\x18\x03 \x03(\x0b\x32\n.hsm.Vec3D\"\x1d\n\x08MeshInfo\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\"&\n\tImageInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x65xt\x18\x02 \x01(\t\"\xfd\x01\n\nAPIRequest\x12\x12\n\nclient_key\x18\x01 \x01(\r\x12$\n\x0b\x63lient_type\x18\x02 \x01(\x0e\x32\x0f.hsm.ClientType\x12\x1b\n\x06method\x18\x03 \x01(\x0e\x32\x0b.hsm.Method\x12\x11\n\tblob_size\x18\x04 \x01(\x04\x12 \n\tmesh_info\x18\x64 \x01(\x0b\x32\r.hsm.MeshInfo\x12#\n\nimage_info\x18\xc8\x01 \x01(\x0b\x32\x0e.hsm.ImageInfo\x12>\n\x17\x64\x65vice_marker_transform\x18\xac\x02 \x01(\x0b\x32\x1c.hsm.DeviceToMarkerTransform\")\n\x0b\x41PIResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t*3\n\nClientType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06MOBILE\x10\x01\x12\x0c\n\x08HOLOLENS\x10\x02*L\n\x06Method\x12\x0e\n\nSEND_IMAGE\x10\x00\x12\r\n\tSEND_MESH\x10\x01\x12#\n\x1fSEND_DEVICE_TO_MARKER_TRANSFORM\x10\x02\x62\x06proto3')
)

_CLIENTTYPE = _descriptor.EnumDescriptor(
  name='ClientType',
  full_name='hsm.ClientType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLOLENS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=811,
  serialized_end=862,
)
_sym_db.RegisterEnumDescriptor(_CLIENTTYPE)

ClientType = enum_type_wrapper.EnumTypeWrapper(_CLIENTTYPE)
_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='hsm.Method',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEND_IMAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_MESH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_DEVICE_TO_MARKER_TRANSFORM', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=864,
  serialized_end=940,
)
_sym_db.RegisterEnumDescriptor(_METHOD)

Method = enum_type_wrapper.EnumTypeWrapper(_METHOD)
UNKNOWN = 0
MOBILE = 1
HOLOLENS = 2
SEND_IMAGE = 0
SEND_MESH = 1
SEND_DEVICE_TO_MARKER_TRANSFORM = 2



_VEC3D = _descriptor.Descriptor(
  name='Vec3D',
  full_name='hsm.Vec3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='hsm.Vec3D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='hsm.Vec3D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='hsm.Vec3D.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=25,
  serialized_end=65,
)


_VEC4D = _descriptor.Descriptor(
  name='Vec4D',
  full_name='hsm.Vec4D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='hsm.Vec4D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='hsm.Vec4D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='hsm.Vec4D.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='hsm.Vec4D.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=67,
  serialized_end=118,
)


_FACE = _descriptor.Descriptor(
  name='Face',
  full_name='hsm.Face',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v1', full_name='hsm.Face.v1', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v2', full_name='hsm.Face.v2', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v3', full_name='hsm.Face.v3', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=120,
  serialized_end=162,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='hsm.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='hsm.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='hsm.Transform.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='hsm.Transform.scale', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=164,
  serialized_end=265,
)


_DEVICETOMARKERTRANSFORM = _descriptor.Descriptor(
  name='DeviceToMarkerTransform',
  full_name='hsm.DeviceToMarkerTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='hsm.DeviceToMarkerTransform.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='marker_id', full_name='hsm.DeviceToMarkerTransform.marker_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=267,
  serialized_end=346,
)


_MESH = _descriptor.Descriptor(
  name='Mesh',
  full_name='hsm.Mesh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='hsm.Mesh.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faces', full_name='hsm.Mesh.faces', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='hsm.Mesh.normals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=348,
  serialized_end=439,
)


_MESHINFO = _descriptor.Descriptor(
  name='MeshInfo',
  full_name='hsm.MeshInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hsm.MeshInfo.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=441,
  serialized_end=470,
)


_IMAGEINFO = _descriptor.Descriptor(
  name='ImageInfo',
  full_name='hsm.ImageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hsm.ImageInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ext', full_name='hsm.ImageInfo.ext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=472,
  serialized_end=510,
)


_APIREQUEST = _descriptor.Descriptor(
  name='APIRequest',
  full_name='hsm.APIRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_key', full_name='hsm.APIRequest.client_key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='hsm.APIRequest.client_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='hsm.APIRequest.method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blob_size', full_name='hsm.APIRequest.blob_size', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mesh_info', full_name='hsm.APIRequest.mesh_info', index=4,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_info', full_name='hsm.APIRequest.image_info', index=5,
      number=200, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_marker_transform', full_name='hsm.APIRequest.device_marker_transform', index=6,
      number=300, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=513,
  serialized_end=766,
)


_APIRESPONSE = _descriptor.Descriptor(
  name='APIResponse',
  full_name='hsm.APIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='hsm.APIResponse.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='hsm.APIResponse.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=768,
  serialized_end=809,
)

_TRANSFORM.fields_by_name['translation'].message_type = _VEC3D
_TRANSFORM.fields_by_name['rotation'].message_type = _VEC4D
_TRANSFORM.fields_by_name['scale'].message_type = _VEC3D
_DEVICETOMARKERTRANSFORM.fields_by_name['transform'].message_type = _TRANSFORM
_MESH.fields_by_name['vertices'].message_type = _VEC3D
_MESH.fields_by_name['faces'].message_type = _FACE
_MESH.fields_by_name['normals'].message_type = _VEC3D
_APIREQUEST.fields_by_name['client_type'].enum_type = _CLIENTTYPE
_APIREQUEST.fields_by_name['method'].enum_type = _METHOD
_APIREQUEST.fields_by_name['mesh_info'].message_type = _MESHINFO
_APIREQUEST.fields_by_name['image_info'].message_type = _IMAGEINFO
_APIREQUEST.fields_by_name['device_marker_transform'].message_type = _DEVICETOMARKERTRANSFORM
DESCRIPTOR.message_types_by_name['Vec3D'] = _VEC3D
DESCRIPTOR.message_types_by_name['Vec4D'] = _VEC4D
DESCRIPTOR.message_types_by_name['Face'] = _FACE
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['DeviceToMarkerTransform'] = _DEVICETOMARKERTRANSFORM
DESCRIPTOR.message_types_by_name['Mesh'] = _MESH
DESCRIPTOR.message_types_by_name['MeshInfo'] = _MESHINFO
DESCRIPTOR.message_types_by_name['ImageInfo'] = _IMAGEINFO
DESCRIPTOR.message_types_by_name['APIRequest'] = _APIREQUEST
DESCRIPTOR.message_types_by_name['APIResponse'] = _APIRESPONSE
DESCRIPTOR.enum_types_by_name['ClientType'] = _CLIENTTYPE
DESCRIPTOR.enum_types_by_name['Method'] = _METHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vec3D = _reflection.GeneratedProtocolMessageType('Vec3D', (_message.Message,), dict(
  DESCRIPTOR = _VEC3D,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.Vec3D)
  ))
_sym_db.RegisterMessage(Vec3D)

Vec4D = _reflection.GeneratedProtocolMessageType('Vec4D', (_message.Message,), dict(
  DESCRIPTOR = _VEC4D,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.Vec4D)
  ))
_sym_db.RegisterMessage(Vec4D)

Face = _reflection.GeneratedProtocolMessageType('Face', (_message.Message,), dict(
  DESCRIPTOR = _FACE,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.Face)
  ))
_sym_db.RegisterMessage(Face)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.Transform)
  ))
_sym_db.RegisterMessage(Transform)

DeviceToMarkerTransform = _reflection.GeneratedProtocolMessageType('DeviceToMarkerTransform', (_message.Message,), dict(
  DESCRIPTOR = _DEVICETOMARKERTRANSFORM,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.DeviceToMarkerTransform)
  ))
_sym_db.RegisterMessage(DeviceToMarkerTransform)

Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), dict(
  DESCRIPTOR = _MESH,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.Mesh)
  ))
_sym_db.RegisterMessage(Mesh)

MeshInfo = _reflection.GeneratedProtocolMessageType('MeshInfo', (_message.Message,), dict(
  DESCRIPTOR = _MESHINFO,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.MeshInfo)
  ))
_sym_db.RegisterMessage(MeshInfo)

ImageInfo = _reflection.GeneratedProtocolMessageType('ImageInfo', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEINFO,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.ImageInfo)
  ))
_sym_db.RegisterMessage(ImageInfo)

APIRequest = _reflection.GeneratedProtocolMessageType('APIRequest', (_message.Message,), dict(
  DESCRIPTOR = _APIREQUEST,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.APIRequest)
  ))
_sym_db.RegisterMessage(APIRequest)

APIResponse = _reflection.GeneratedProtocolMessageType('APIResponse', (_message.Message,), dict(
  DESCRIPTOR = _APIRESPONSE,
  __module__ = 'protos.hsm_pb2'
  # @@protoc_insertion_point(class_scope:hsm.APIResponse)
  ))
_sym_db.RegisterMessage(APIResponse)


# @@protoc_insertion_point(module_scope)