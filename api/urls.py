from django.urls import path
from .views import api_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', api_view, name='api_view'),
    path('auth', obtain_auth_token),
]
