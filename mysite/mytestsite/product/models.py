#models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
