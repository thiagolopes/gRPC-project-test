import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .factories import ProductFactory
from apps.clients.models import ClientModel
from apps.products.models import ProductModel

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("batch_number", [3, 4, 2])
def test_product_list(client, batch_number):
    ProductFactory.create_batch(batch_number)
    url = reverse("products:products-list")
    req = client.get(url)

    assert req.status_code == status.HTTP_200_OK
    assert req.data["count"] == batch_number


def test_product_fetch_authenticated(client):
    product = ProductFactory.create()
    url = reverse("products:products-detail", args=[product.pk])
    req = client.get(url)

    assert req.status_code == status.HTTP_200_OK
    assert req.data["id"] == str(product.pk)
    assert "discount" in req.data


def test_product_fetch_unauthenticated(client_not_authenticated):
    product = ProductFactory.create()
    url = reverse("products:products-detail", args=[product.pk])
    req = client_not_authenticated.get(url)

    assert req.status_code == status.HTTP_200_OK
    assert req.data["id"] == str(product.pk)
    assert "discount" not in req.data


def test_product_create(client, product_data):
    url = reverse("products:products-list")
    req = client.post(url, product_data)

    assert req.status_code == status.HTTP_201_CREATED
    assert req.data["title"] == product_data["title"]


def test_product_delete(client, product_data):
    product = ProductFactory.create()
    url = reverse("products:products-detail", args=[product.pk])

    assert ProductModel.objects.count() == 1

    req = client.delete(url)

    assert req.status_code == status.HTTP_204_NO_CONTENT
    assert ProductModel.objects.count() == 0


@pytest.mark.parametrize(
    "method_not_allowed",
    [
        "patch",
        "put",
    ],
)
def test_product_invalid_methods(client, method_not_allowed):
    product = ProductFactory.create()
    url = reverse("products:products-detail", args=[product.pk])

    assert getattr(client, method_not_allowed)(url).status_code == status.HTTP_405_METHOD_NOT_ALLOWED
