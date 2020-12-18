from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.commons.models import BaseUUIDModel


class ClientModel(AbstractUser, BaseUUIDModel):
    birth_date = models.DateField(help_text="Birth date")

    REQUIRED_FIELDS = [
        "birth_date",
    ]
