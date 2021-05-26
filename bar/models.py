from django.db import models
import uuid

class Drink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    quantity = models.FloatField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)