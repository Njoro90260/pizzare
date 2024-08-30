from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.

def index(request):
    """Home page."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
    """Show the toppings for the pizzas."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza)
    context = {'pizza':pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza_toppings.html', context)


