from django.urls import path

from .views import DrinkCreateView, index, operations

urlpatterns = [
    path('add/', DrinkCreateView.as_view(), name='add'),
    path('operations/', operations, name='operations'),
    path('', index, name='index'),
]
