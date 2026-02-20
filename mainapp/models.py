from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.CharField(max_length=150)
    rating = models.FloatField(blank=True, null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.name
