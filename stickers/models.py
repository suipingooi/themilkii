from django.db import models
# from pyuploadcare.dj.models import ImageField
# from django import forms

# Create your models here.


class sticker(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(blank=False, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
