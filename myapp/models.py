from django.db import models

class Products(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()