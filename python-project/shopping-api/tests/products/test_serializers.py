import uuid
from decimal import Decimal
from unittest.mock import Mock

import grpc
import pytest

from apps.products.serializers import DiscountsSerializer, ProductDiscoutSerializer, ProductSerializer

pytestmark = pytest.mark.django_db


def test_discount_serializer_empty():
    discount = DiscountsSerializer([], 100)

    assert discount.validated_data == []


def test_discount_serializer_with_discounts(discounts_data):
    discount = DiscountsSerializer(discounts_data, 100)

    assert discount.validated_data == [
        {"amount": Decimal("10.0"), "percentage": Decimal("0.1"), "description": "discount one"},
        {"amount": Decimal("5.0"), "percentage": Decimal("0.05"), "description": "discount two"},
    ]


def test_discount_serializer_with_discounts_and_max_discount(discounts_data):
    discount = DiscountsSerializer(discounts_data, 100, 0.05)

    assert discount.validated_data == [
        {"amount": Decimal("10.00"), "percentage": Decimal("0.1"), "description": "discount one"},
        {"amount": Decimal("5.00"), "percentage": Decimal("0.05"), "description": "discount two"},
        {
            "amount": Decimal("-10.00"),
            "percentage": Decimal("-0.10"),
            "description": "Value maximum discount reaching",
        },
    ]


def test_discount_serializer_overflow_discount_percentage(discounts_data):
    discount = DiscountsSerializer(discounts_data, 100, 0.05)
    assert discount.overflow_discount_percentage == Decimal("-0.10")


def test_product_serializer(product_data):
    product = ProductSerializer(data=product_data)

    assert product.is_valid() is True
    assert product.data == product_data


def test_product_with_discount_serializer_without_discount(product_data):
    stub_mock, request_mock = Mock(), Mock()
    stub_mock.AvailableDiscounts.return_value = {}

    product_discount = ProductDiscoutSerializer(data=product_data, context={"request": request_mock})
    product_discount.discount_stub_class = stub_mock

    assert product_discount.is_valid() is True
    product_discount.save()
    assert product_discount.data == {
        "id": product_discount.data["id"],
        "title": "Car Toy",
        "description": "Is a toy",
        "price": "500.00",
        "discounts": [],
        "currency": "BRL",
    }
    request_mock.user.birth_date.isoformat.assert_called()
    stub_mock.AvailableDiscounts.assert_called()


def test_product_with_discount_serializer_without_grpc_error(product_data, caplog):
    stub_mock, request_mock = Mock(), Mock()
    stub_mock.AvailableDiscounts.side_effect = grpc.RpcError

    product_discount = ProductDiscoutSerializer(data=product_data, context={"request": request_mock})
    product_discount.discount_stub_class = stub_mock

    assert product_discount.is_valid() is True
    product_discount.save()
    assert product_discount.data == {
        "id": product_discount.data["id"],
        "title": "Car Toy",
        "description": "Is a toy",
        "price": "500.00",
        "discounts": [],
        "currency": "BRL",
    }
    request_mock.user.birth_date.isoformat.assert_called()
    stub_mock.AvailableDiscounts.assert_called()
    assert "grpc_discount_calls_error" in caplog.text
