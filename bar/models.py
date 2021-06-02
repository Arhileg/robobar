from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Drink(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('1.0'))])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.name

class Operation(models.Model):
    OPER_KINDS = (
        ('a', 'arrive'),
        ('s', 'sale'),
    )
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    data = models.DateTimeField()
    operation = models.CharField(max_length=1, choices=OPER_KINDS, default='a')
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return '{} = {} : {}'.format(self.operation, self.drink, self.amount)
