import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(help_text="Product Title", max_length=64, unique=True)),
                ("description", models.TextField(default="", help_text="Product description")),
                ("price", models.DecimalField(decimal_places=2, help_text="Product price", max_digits=8)),
                ("currency", models.CharField(choices=[("BRL", "BRL"), ("USD", "USD")], max_length=3)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
