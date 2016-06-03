# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/bio_metadata_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import bio_metadata_pb2 as ga4gh_dot_bio__metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/bio_metadata_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=b'\n ga4gh/bio_metadata_service.proto\x12\x05ga4gh\x1a\x18ga4gh/bio_metadata.proto\"c\n\x18SearchIndividualsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"\\\n\x19SearchIndividualsResponse\x12&\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x11.ga4gh.Individual\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"y\n\x17SearchBioSamplesRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"Y\n\x18SearchBioSamplesResponse\x12$\n\nbiosamples\x18\x01 \x03(\x0b\x32\x10.ga4gh.BioSample\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc9\x02\n\x12\x42ioMetadataService\x12V\n\x11SearchIndividuals\x12\x1f.ga4gh.SearchIndividualsRequest\x1a .ga4gh.SearchIndividualsResponse\x12S\n\x10SearchBioSamples\x12\x1e.ga4gh.SearchBioSamplesRequest\x1a\x1f.ga4gh.SearchBioSamplesResponse\x12\x43\n\rGetIndividual\x12\x1f.ga4gh.SearchIndividualsRequest\x1a\x11.ga4gh.Individual\x12\x41\n\x0cGetBioSample\x12\x1f.ga4gh.SearchIndividualsRequest\x1a\x10.ga4gh.BioSampleb\x06proto3'
  ,
  dependencies=[ga4gh_dot_bio__metadata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHINDIVIDUALSREQUEST = _descriptor.Descriptor(
  name='SearchIndividualsRequest',
  full_name='ga4gh.SearchIndividualsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchIndividualsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchIndividualsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchIndividualsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchIndividualsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=69,
  serialized_end=168,
)


_SEARCHINDIVIDUALSRESPONSE = _descriptor.Descriptor(
  name='SearchIndividualsResponse',
  full_name='ga4gh.SearchIndividualsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='ga4gh.SearchIndividualsResponse.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchIndividualsResponse.next_page_token', index=1,
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
  serialized_start=170,
  serialized_end=262,
)


_SEARCHBIOSAMPLESREQUEST = _descriptor.Descriptor(
  name='SearchBioSamplesRequest',
  full_name='ga4gh.SearchBioSamplesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchBioSamplesRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchBioSamplesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.SearchBioSamplesRequest.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchBioSamplesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchBioSamplesRequest.page_token', index=4,
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
  serialized_start=264,
  serialized_end=385,
)


_SEARCHBIOSAMPLESRESPONSE = _descriptor.Descriptor(
  name='SearchBioSamplesResponse',
  full_name='ga4gh.SearchBioSamplesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosamples', full_name='ga4gh.SearchBioSamplesResponse.biosamples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchBioSamplesResponse.next_page_token', index=1,
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
  serialized_start=387,
  serialized_end=476,
)

_SEARCHINDIVIDUALSRESPONSE.fields_by_name['individuals'].message_type = ga4gh_dot_bio__metadata__pb2._INDIVIDUAL
_SEARCHBIOSAMPLESRESPONSE.fields_by_name['biosamples'].message_type = ga4gh_dot_bio__metadata__pb2._BIOSAMPLE
DESCRIPTOR.message_types_by_name['SearchIndividualsRequest'] = _SEARCHINDIVIDUALSREQUEST
DESCRIPTOR.message_types_by_name['SearchIndividualsResponse'] = _SEARCHINDIVIDUALSRESPONSE
DESCRIPTOR.message_types_by_name['SearchBioSamplesRequest'] = _SEARCHBIOSAMPLESREQUEST
DESCRIPTOR.message_types_by_name['SearchBioSamplesResponse'] = _SEARCHBIOSAMPLESRESPONSE

SearchIndividualsRequest = _reflection.GeneratedProtocolMessageType('SearchIndividualsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchIndividualsRequest)
  ))
_sym_db.RegisterMessage(SearchIndividualsRequest)

SearchIndividualsResponse = _reflection.GeneratedProtocolMessageType('SearchIndividualsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSRESPONSE,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchIndividualsResponse)
  ))
_sym_db.RegisterMessage(SearchIndividualsResponse)

SearchBioSamplesRequest = _reflection.GeneratedProtocolMessageType('SearchBioSamplesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchBioSamplesRequest)
  ))
_sym_db.RegisterMessage(SearchBioSamplesRequest)

SearchBioSamplesResponse = _reflection.GeneratedProtocolMessageType('SearchBioSamplesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESRESPONSE,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchBioSamplesResponse)
  ))
_sym_db.RegisterMessage(SearchBioSamplesResponse)


# @@protoc_insertion_point(module_scope)
