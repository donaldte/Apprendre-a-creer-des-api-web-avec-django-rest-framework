from .models import Product
from django.http import JsonResponse

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def api_view(request):
    # request != requests
    # request c'est instance de HttpRequest
    if request.method != "POST":
        return Response({'detail': 'method get not allowed'}, status=405)
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
       data = model_to_dict(query, fields=('name', 'price'))
        # serialization: Mettre des donnees sur forme de dict
    return Response(data)    