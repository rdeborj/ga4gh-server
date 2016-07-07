# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/metadata.proto

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
  name='ga4gh/metadata.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x14ga4gh/metadata.proto\x12\x05ga4gh\"U\n\x0cOntologyTerm\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x13\n\x0bsource_name\x18\x03 \x01(\t\x12\x16\n\x0esource_version\x18\x04 \x01(\t\"8\n\x07\x44\x61taset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ONTOLOGYTERM = _descriptor.Descriptor(
  name='OntologyTerm',
  full_name='ga4gh.OntologyTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.OntologyTerm.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term', full_name='ga4gh.OntologyTerm.term', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_name', full_name='ga4gh.OntologyTerm.source_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_version', full_name='ga4gh.OntologyTerm.source_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=116,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='ga4gh.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.Dataset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.Dataset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.Dataset.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=118,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['OntologyTerm'] = _ONTOLOGYTERM
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET

OntologyTerm = _reflection.GeneratedProtocolMessageType('OntologyTerm', (_message.Message,), dict(
  DESCRIPTOR = _ONTOLOGYTERM,
  __module__ = 'ga4gh.metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.OntologyTerm)
  ))
_sym_db.RegisterMessage(OntologyTerm)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), dict(
  DESCRIPTOR = _DATASET,
  __module__ = 'ga4gh.metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Dataset)
  ))
_sym_db.RegisterMessage(Dataset)


# @@protoc_insertion_point(module_scope)
