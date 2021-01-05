import uuid

import pytest

from apps.products.serializers import DiscountSerializer, ProductDiscoutSerializer, ProductSerializer

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "data, expected",
    [
        [{"percentage": 40.0, "discount": 10.0}, {"percentage": 40.0, "discount": 10.0}],
        [{}, {"percentage": 0, "discount": 0}],
    ],
)
def test_discount_serializer(data, expected):
    discount = DiscountSerializer(data=data)

    assert discount.is_valid() is True
    assert discount.data == expected


def test_discount_serializer_less_zero():
    discount = DiscountSerializer(data={"percentage": -10, "discount": -1})

    assert discount.is_valid() is False
    assert discount.errors["percentage"][0] == "Ensure this value is greater than or equal to 0."


def test_product_serializer(product_data):
    product = ProductSerializer(data=product_data)

    assert product.is_valid() is True
    assert product.data == product_data


def test_product_with_discount_serializer(product_data):
    product_discount = ProductDiscoutSerializer(data=product_data)

    assert product_discount.is_valid() is True
    assert product_discount.data == {
        "title": "Car Toy",
        "description": "Is a toy",
        "price": "500.00",
        "currency": "BRL",
        "discount": {"percentage": 0, "discount": 0},
    }
