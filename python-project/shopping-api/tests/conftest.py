import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from apps.clients.models import ClientModel


@pytest.fixture
def client():
    user = ClientModel.objects.create_user("test_user", "test@test.com", "123123123", birth_date="2020-10-10")
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    return client


@pytest.fixture
def client_not_authenticated():
    return APIClient()


@pytest.fixture
def discounts_data():
    return [
        {"percentage": 0.1, "discountName": "discount one"},
        {"percentage": 0.05, "discountName": "discount two"},
    ]
