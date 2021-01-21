from apps.commons.stubs import BaseStub
from apps.stubs.promotion_pb2 import Order, User
from apps.stubs.promotion_pb2_grpc import DiscountServiceServicer, DiscountServiceStub

from django.conf import settings


class DiscountStub(BaseStub, DiscountServiceServicer):
    stub_class = DiscountServiceStub

    def AvailableDiscounts(self, user_date_birth):
        order = Order(user=User(date_birth=user_date_birth))
        return self.client.AvailableDiscounts(order)


if settings.DEBUG is False:
    pass
    # TODO instance here a channel with TLS

discount_stub = DiscountStub()
