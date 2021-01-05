from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.products.api import ProductViewSet

app_name = "products"

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = router.urls
