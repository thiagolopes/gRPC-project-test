from django.utils.functional import cached_property
from rest_framework import serializers

from apps.products.models import ProductModel
from apps.stubs.promotion import discount_stub

PRODUCT_FIELDS = (
    "id",
    "title",
    "description",
    "price",
    "currency",
)


class DiscountSerializer(serializers.Serializer):
    percentage = serializers.FloatField(min_value=0, max_value=100, default=0.0)
    discount = serializers.FloatField(min_value=0, default=0.0)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = PRODUCT_FIELDS
        read_only_fields = [
            "id",
        ]


class ProductDiscoutSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    discount_stub_class = discount_stub

    class Meta:
        model = ProductModel
        fields = PRODUCT_FIELDS + ("discount",)
        read_only_fields = [
            "id",
        ]

    @cached_property
    def promotions_avalibe(self):
        date = self.context["request"].user.birth_date.isoformat()
        return self.discount_stub_class.AvailableDiscounts(date)

    def get_discount(self, obj):
        promotions = self.promotions_avalibe
        discount = DiscountSerializer(data={})
        discount.is_valid()
        return discount.validated_data
