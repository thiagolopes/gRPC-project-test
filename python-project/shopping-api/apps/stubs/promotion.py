from unittest.mock import Mock

from django.conf import settings

from apps.commons.stubs import BaseStub
from apps.stubs.promotion_pb2 import Order, User
from apps.stubs.promotion_pb2_grpc import DiscountServiceServicer, DiscountServiceStub


class DiscountStub(BaseStub, DiscountServiceServicer):
    stub_class = DiscountServiceStub

    def AvailableDiscounts(self, user_date_birth):
        order = Order(user=User(date_birth=user_date_birth))
        return self.client.AvailableDiscounts(order)


discount_stub = DiscountStub()

if settings.DEBUG is True:
    discount_stub = DiscountStub(channel=Mock())
