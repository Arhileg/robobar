from django.urls import path

from .views import index, by_drink, DrinkCreateView

urlpatterns = [
    path('add/', DrinkCreateView.as_view(), name='add'),
    path('<str:drink_id>/', by_drink, name='by_drink'),
    path('', index, name='index'),
]
