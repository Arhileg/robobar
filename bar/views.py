from django.shortcuts import render

from .models import Drink

def index(request):
    drinks = Drink.objects.order_by('name')
    return render(request, 'index.html', {'drinks': drinks})
