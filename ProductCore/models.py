from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
