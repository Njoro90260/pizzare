from django.db import models

# Create your models here.

#register a model pizza with a field name which will hold name values,
#such as Hawaiian and Meat Lovers.
class Pizza(models.Model):
    """The kind of pizza a person likes."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Topping(models.Model):
    """The toppings for the pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name