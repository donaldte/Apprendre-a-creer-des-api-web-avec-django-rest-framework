from django.shortcuts import get_object_or_404, render
from .models import Product

from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import  generics, mixins

from api.mixins import StaffEditorPermissionsMixin, UserQuerrySetMixin

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListCreateProductView(
    StaffEditorPermissionsMixin, 
    generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content, user=self.request.user)

      

class UpdateProductView(
    StaffEditorPermissionsMixin, 
    UserQuerrySetMixin,
    generics.UpdateAPIView):  

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)     

class DeleteProductView(
    StaffEditorPermissionsMixin, 
    UserQuerrySetMixin,
    generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='past')



class ProductMixinsView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)  

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)             

        

def documentation(request):
    return render(request, 'v1/product.html')        