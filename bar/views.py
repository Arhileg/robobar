from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import DrinkForm
from .models import Drink

class DrinkCreateView(CreateView):
    """docstring for ."""
    template_name = 'create.html'
    form_class = DrinkForm
    success_url = '/bar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[]
        return context

def index(request):
    drinks = Drink.objects.order_by('name')
    return render(request, 'index.html', {'drinks': drinks})

def by_drink(request, drink_id):
    drink = Drink.objects.filter(pk=drink_id)
    return render(request, 'by_drink.html', {'drink': drink})
