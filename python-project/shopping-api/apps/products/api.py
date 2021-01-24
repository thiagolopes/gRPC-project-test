from functools import partial

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.products.models import ProductModel
from apps.products.serializers import ProductDiscoutSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = [
        "get",
        "post",
        "delete",
        "head",
        "options",
    ]

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    serializer_class_authenticated = ProductDiscoutSerializer

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return partial(self.serializer_class_authenticated, context={"request": self.request})
        return self.serializer_class
