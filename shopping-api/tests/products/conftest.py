import pytest


@pytest.fixture
def product_data():
    return {
        "title": "Car Toy",
        "description": "Is a toy",
        "price": "500.00",
        "currency": "BRL",
    }
