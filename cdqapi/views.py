from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Quote
from .tools import get_random_dog_pic_url, get_random_cat_pic_url
from random import choice
import datetime

@api_view(['GET',])
@renderer_classes([JSONRenderer,])
def inspire(request):
    primary_keys = Quote.objects.values_list('pk', flat=True)
    random_pk = choice(primary_keys)
    randomized_quote = Quote.objects.get(pk=random_pk)
    return Response({
        'quote': f"{randomized_quote.text} - {randomized_quote.author}",
        'cat_pic': get_random_cat_pic_url(),
        'dog_pic': get_random_dog_pic_url(),
        'timestamp' : datetime.datetime.now()
    })
        
