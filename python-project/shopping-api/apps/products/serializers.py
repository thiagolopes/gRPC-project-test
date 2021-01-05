from rest_framework import serializers

from apps.products.models import ProductModel

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
    # discount = DiscountSerializer(default={"percentage": 0, "discount": 0}, read_only=True)
    discount = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = PRODUCT_FIELDS + ("discount",)
        read_only_fields = [
            "id",
        ]

    def get_discount(self, obj):
        return {"percentage": 0, "discount": 0.0}
