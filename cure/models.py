from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)