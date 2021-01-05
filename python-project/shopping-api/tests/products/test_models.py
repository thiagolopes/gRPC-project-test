import uuid

import pytest

from apps.products.models import ProductModel

pytestmark = pytest.mark.django_db


def test_product_model_creation():
    product = ProductModel.objects.create(title="Car Toy", description="Toy", currency="BRL", price=101.10)

    assert ProductModel.objects.count() == 1
    assert str(product) == "Car Toy"
    assert isinstance(product.pk, uuid.UUID)
