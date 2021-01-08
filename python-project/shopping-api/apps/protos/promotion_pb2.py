# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: promotion.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='promotion.proto',
  package='discount',
  syntax='proto3',
  serialized_options=b'Z\023promotion;promotion',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fpromotion.proto\x12\x08\x64iscount\"\x1a\n\x04User\x12\x12\n\ndate_birth\x18\x01 \x01(\x03\"%\n\x05Order\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.discount.User\"5\n\x08\x44iscount\x12\x12\n\npercentage\x18\x01 \x01(\x02\x12\x15\n\rdiscount_name\x18\x02 \x01(\t\"2\n\tDiscounts\x12%\n\tdiscounts\x18\x01 \x03(\x0b\x32\x12.discount.Discount2M\n\x0f\x44iscountService\x12:\n\x12\x41vailableDiscounts\x12\x0f.discount.Order\x1a\x13.discount.DiscountsB\x15Z\x13promotion;promotionb\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='discount.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_birth', full_name='discount.User.date_birth', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=55,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='discount.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='discount.Order.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=57,
  serialized_end=94,
)


_DISCOUNT = _descriptor.Descriptor(
  name='Discount',
  full_name='discount.Discount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentage', full_name='discount.Discount.percentage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discount_name', full_name='discount.Discount.discount_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=96,
  serialized_end=149,
)


_DISCOUNTS = _descriptor.Descriptor(
  name='Discounts',
  full_name='discount.Discounts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='discounts', full_name='discount.Discounts.discounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=151,
  serialized_end=201,
)

_ORDER.fields_by_name['user'].message_type = _USER
_DISCOUNTS.fields_by_name['discounts'].message_type = _DISCOUNT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['Discount'] = _DISCOUNT
DESCRIPTOR.message_types_by_name['Discounts'] = _DISCOUNTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'promotion_pb2'
  # @@protoc_insertion_point(class_scope:discount.User)
  })
_sym_db.RegisterMessage(User)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'promotion_pb2'
  # @@protoc_insertion_point(class_scope:discount.Order)
  })
_sym_db.RegisterMessage(Order)

Discount = _reflection.GeneratedProtocolMessageType('Discount', (_message.Message,), {
  'DESCRIPTOR' : _DISCOUNT,
  '__module__' : 'promotion_pb2'
  # @@protoc_insertion_point(class_scope:discount.Discount)
  })
_sym_db.RegisterMessage(Discount)

Discounts = _reflection.GeneratedProtocolMessageType('Discounts', (_message.Message,), {
  'DESCRIPTOR' : _DISCOUNTS,
  '__module__' : 'promotion_pb2'
  # @@protoc_insertion_point(class_scope:discount.Discounts)
  })
_sym_db.RegisterMessage(Discounts)


DESCRIPTOR._options = None

_DISCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='DiscountService',
  full_name='discount.DiscountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=203,
  serialized_end=280,
  methods=[
  _descriptor.MethodDescriptor(
    name='AvailableDiscounts',
    full_name='discount.DiscountService.AvailableDiscounts',
    index=0,
    containing_service=None,
    input_type=_ORDER,
    output_type=_DISCOUNTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOUNTSERVICE)

DESCRIPTOR.services_by_name['DiscountService'] = _DISCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
