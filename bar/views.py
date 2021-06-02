from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import DrinkForm
from .models import Drink, Operation


class DrinkCreateView(CreateView):
    """docstring for ."""
    template_name = 'create.html'
    form_class = DrinkForm
    success_url = reverse_lazy('index')

def index(request):
    drinks = Drink.objects.order_by('name')
    return render(request, 'index.html', {'drinks': drinks})

def operations(request):
    operations = Operation.objects.order_by('data')
    return render(request, 'operations.html', {'operations': operations})
