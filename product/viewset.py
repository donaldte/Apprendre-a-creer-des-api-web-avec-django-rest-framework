from .models import Product
from .serializer import ProductSerializer
from rest_framework import mixins, viewsets


class ProductViewset(viewsets.ModelViewSet):
    """"
    get -> list -> QuerySet
    get -> retrieve 
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListRestrieveViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    