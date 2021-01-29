from decimal import Decimal

from django.utils.functional import cached_property
from rest_framework import serializers
from django.conf import settings

from apps.commons.utils import ftod
from apps.products.models import ProductModel
from apps.stubs.promotion import discount_stub

PRODUCT_FIELDS = (
    "id",
    "title",
    "description",
    "price",
    "currency",
)


class DiscountsSerializer:
    def __init__(self, discounts, price, max_discount_percentage=None):
        self.discounts = discounts
        self.price = price
        self.max_discount_percentage = max_discount_percentage

        if self.max_discount_percentage is not None:
            self.max_discount_percentage = Decimal(str(max_discount_percentage))

        if not self.discounts:
            self.discounts = []

    def _amount(self, discount):
        return self.price * ftod(discount)

    @cached_property
    def overflow_discount_percentage(self):
        if self.max_discount_percentage is not None:
            s = sum(ftod(d["percentage"]) for d in self.discounts)
            if s > self.max_discount_percentage:
                return self.max_discount_percentage - s
        return 0

    @property
    def validated_data(self):
        discounts = self.discounts

        data = [
            {"percentage": ftod(d["percentage"]), "amount": self._amount(d["percentage"])} for d in discounts
        ]

        if self.overflow_discount_percentage:
            data.append(
                {
                    "percentage": self.overflow_discount_percentage,
                    "amount": self._amount(self.overflow_discount_percentage),
                }
            )

        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = PRODUCT_FIELDS
        read_only_fields = [
            "id",
        ]


class ProductDiscoutSerializer(serializers.ModelSerializer):
    discounts = serializers.SerializerMethodField()
    discount_stub_class = discount_stub

    class Meta:
        model = ProductModel
        fields = PRODUCT_FIELDS + ("discounts",)
        read_only_fields = [
            "id",
        ]

    @cached_property
    def promotions_avalible(self):
        date = self.context["request"].user.birth_date.isoformat()
        return self.discount_stub_class.AvailableDiscounts(date)

    def get_discounts(self, obj):
        discounts_data = self.promotions_avalible.get("discounts", None)
        discounts = DiscountsSerializer(discounts_data, obj.price, settings.MAX_DISCOUNT_PERCENTAGE_ALLOWED)
        return discounts.validated_data
