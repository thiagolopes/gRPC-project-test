from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("apps.products.routes")),
    path("", include("apps.clients.routes")),
]
