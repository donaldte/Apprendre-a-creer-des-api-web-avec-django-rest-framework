from django.urls import path

from .views import DetailProductView, ListCreateProductView, ListProductView, ProductMixinsView, UpdateProductView, DeleteProductView

urlpatterns = [
   # path('<int:pk>/', DetailProductView.as_view()),
   # path('<int:pk>/update', UpdateProductView.as_view()),
   # path('<int:pk>/delete', DeleteProductView.as_view()),
   # path('create/', CreateProductView.as_view()),
   # path('list/', ListProductView.as_view()),
   path('create-list/',  ListCreateProductView.as_view()),
   path('<int:pk>/detail', ProductMixinsView.as_view(), name='product-detail'),
   path('<int:pk>/update', ProductMixinsView.as_view(), name="product-update"),
   path('<int:pk>/update', ProductMixinsView.as_view()),
   path('<int:pk>/delete', ProductMixinsView.as_view()),
   path('list/', ProductMixinsView.as_view()),
     
]
