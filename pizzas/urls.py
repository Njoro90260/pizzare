"""Defines url patterns for pizzas"""

from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page for the project
    path('', views.index, name='index'),
    # page for pizza types
    path('pizzas/', views.pizzas, name='pizzas'),
    # path for the Toppings for the toppings
    path('toppings/<int:pizza_id>/', views.toppings, name='toppings'),
]