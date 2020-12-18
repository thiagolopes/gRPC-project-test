from django.db import models

from apps.commons.models import BaseUUIDModel

CURRENCY_CHOICES = (("BRL", "BRL"), ("USD", "USD"))


class ProductModel(BaseUUIDModel):
    title = models.CharField(max_length=64, unique=True, help_text="Product Title")
    description = models.TextField(help_text="Product description", default="")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Product price")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
