from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.clients.models import ClientModel

admin.site.register(ClientModel, UserAdmin)
