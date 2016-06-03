# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/read_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import reads_pb2 as ga4gh_dot_reads__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/read_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=b'\n\x18ga4gh/read_service.proto\x12\x05ga4gh\x1a\x11ga4gh/reads.proto\"|\n\x1aSearchReadGroupSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rbio_sample_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"d\n\x1bSearchReadGroupSetsResponse\x12,\n\x0fread_group_sets\x18\x01 \x03(\x0b\x32\x13.ga4gh.ReadGroupSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"3\n\x16GetReadGroupSetRequest\x12\x19\n\x11read_group_set_id\x18\x01 \x01(\t\"\x85\x01\n\x12SearchReadsRequest\x12\x16\n\x0eread_group_ids\x18\x01 \x03(\t\x12\x14\n\x0creference_id\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"X\n\x13SearchReadsResponse\x12(\n\nalignments\x18\x01 \x03(\x0b\x32\x14.ga4gh.ReadAlignment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf8\x01\n\x0bReadService\x12\\\n\x13SearchReadGroupSets\x12!.ga4gh.SearchReadGroupSetsRequest\x1a\".ga4gh.SearchReadGroupSetsResponse\x12\x45\n\x0fGetReadGroupSet\x12\x1d.ga4gh.GetReadGroupSetRequest\x1a\x13.ga4gh.ReadGroupSet\x12\x44\n\x0bSearchReads\x12\x19.ga4gh.SearchReadsRequest\x1a\x1a.ga4gh.SearchReadsResponseb\x06proto3'
  ,
  dependencies=[ga4gh_dot_reads__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHREADGROUPSETSREQUEST = _descriptor.Descriptor(
  name='SearchReadGroupSetsRequest',
  full_name='ga4gh.SearchReadGroupSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchReadGroupSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchReadGroupSetsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bio_sample_id', full_name='ga4gh.SearchReadGroupSetsRequest.bio_sample_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchReadGroupSetsRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchReadGroupSetsRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=54,
  serialized_end=178,
)


_SEARCHREADGROUPSETSRESPONSE = _descriptor.Descriptor(
  name='SearchReadGroupSetsResponse',
  full_name='ga4gh.SearchReadGroupSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_group_sets', full_name='ga4gh.SearchReadGroupSetsResponse.read_group_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchReadGroupSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=180,
  serialized_end=280,
)


_GETREADGROUPSETREQUEST = _descriptor.Descriptor(
  name='GetReadGroupSetRequest',
  full_name='ga4gh.GetReadGroupSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_group_set_id', full_name='ga4gh.GetReadGroupSetRequest.read_group_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=282,
  serialized_end=333,
)


_SEARCHREADSREQUEST = _descriptor.Descriptor(
  name='SearchReadsRequest',
  full_name='ga4gh.SearchReadsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_group_ids', full_name='ga4gh.SearchReadsRequest.read_group_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='ga4gh.SearchReadsRequest.reference_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.SearchReadsRequest.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.SearchReadsRequest.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchReadsRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchReadsRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=336,
  serialized_end=469,
)


_SEARCHREADSRESPONSE = _descriptor.Descriptor(
  name='SearchReadsResponse',
  full_name='ga4gh.SearchReadsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alignments', full_name='ga4gh.SearchReadsResponse.alignments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchReadsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=471,
  serialized_end=559,
)

_SEARCHREADGROUPSETSRESPONSE.fields_by_name['read_group_sets'].message_type = ga4gh_dot_reads__pb2._READGROUPSET
_SEARCHREADSRESPONSE.fields_by_name['alignments'].message_type = ga4gh_dot_reads__pb2._READALIGNMENT
DESCRIPTOR.message_types_by_name['SearchReadGroupSetsRequest'] = _SEARCHREADGROUPSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchReadGroupSetsResponse'] = _SEARCHREADGROUPSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetReadGroupSetRequest'] = _GETREADGROUPSETREQUEST
DESCRIPTOR.message_types_by_name['SearchReadsRequest'] = _SEARCHREADSREQUEST
DESCRIPTOR.message_types_by_name['SearchReadsResponse'] = _SEARCHREADSRESPONSE

SearchReadGroupSetsRequest = _reflection.GeneratedProtocolMessageType('SearchReadGroupSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREADGROUPSETSREQUEST,
  __module__ = 'ga4gh.read_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReadGroupSetsRequest)
  ))
_sym_db.RegisterMessage(SearchReadGroupSetsRequest)

SearchReadGroupSetsResponse = _reflection.GeneratedProtocolMessageType('SearchReadGroupSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREADGROUPSETSRESPONSE,
  __module__ = 'ga4gh.read_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReadGroupSetsResponse)
  ))
_sym_db.RegisterMessage(SearchReadGroupSetsResponse)

GetReadGroupSetRequest = _reflection.GeneratedProtocolMessageType('GetReadGroupSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREADGROUPSETREQUEST,
  __module__ = 'ga4gh.read_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetReadGroupSetRequest)
  ))
_sym_db.RegisterMessage(GetReadGroupSetRequest)

SearchReadsRequest = _reflection.GeneratedProtocolMessageType('SearchReadsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREADSREQUEST,
  __module__ = 'ga4gh.read_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReadsRequest)
  ))
_sym_db.RegisterMessage(SearchReadsRequest)

SearchReadsResponse = _reflection.GeneratedProtocolMessageType('SearchReadsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREADSRESPONSE,
  __module__ = 'ga4gh.read_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchReadsResponse)
  ))
_sym_db.RegisterMessage(SearchReadsResponse)


# @@protoc_insertion_point(module_scope)
