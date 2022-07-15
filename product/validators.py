from .models import Product
from rest_framework import serializers

from rest_framework.validators import UniqueValidator


# def validate_product_name(value):
#         qs = Product.objects.filter(name__iexact=value)
#         if qs.exists():
#            raise serializers.ValidationError(f"Le produit {value} existe deja en db")
#         return value        


validators_unique_product_name = UniqueValidator(queryset=Product.objects.all())