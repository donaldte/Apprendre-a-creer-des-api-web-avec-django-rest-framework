from rest_framework  import serializers
from django.contrib.auth.models import User


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    


class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    has_perms = serializers.BooleanField(read_only=True)
    number = serializers.CharField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'id', 'has_perms', 'number', 'user_product')

    def get_user_product(self, obj):
        user = obj 
        request = self.context.get('request')
        product = user.product_set.all()[:3]
        return ProductInlineSerializer(product, many=True, context={'request':request}).data