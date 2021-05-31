from django.db import models
import uuid


class Drink(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    quantity = models.FloatField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
class Operation(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    data = models.DateTimeField()
    operation = models.CharField(max_length=10)
    amount = models.IntegerField()
    price = models.FloatField()
