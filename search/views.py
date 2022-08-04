from product.models import Product
from product.serializer import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response

from . import client

class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user =None
        if request.user.is_authenticated:
            user = request.user.username
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag')
        query = request.GET.get('q')
        print(query, tag, user, public)
        if not query:
            return Response("Aucun produit trouve", status=404)
        result = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(result)    



class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        result = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user=self.request.user
                result = qs.search(q, user)
        return result
