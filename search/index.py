from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from product.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    #should_index = "is_public"
    fields = [
        'name',
        'content',
        'price',
        'public',
        'user'
        
    ]
    tags = "get_tags_list"

    settings = {
        'searchableAttributes':['name', 'content'],
        'attributesForFaceting':['user', 'public']
    }


