from uuid import uuid4

import factory
from factory import fuzzy

from apps.products.models import ProductModel


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductModel

    title = factory.Faker("name")
    description = factory.Faker("texts", nb_texts=1)
    price = factory.Faker("random_number", digits=2)
