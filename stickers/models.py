from django.db import models
from pyuploadcare.dj.models import ImageField
from django.core.validators import MinValueValidator

# from django import forms

# Create your models here.


def valiPrice(price):
    if price > 0:
        return float(price)


class sticker(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(
        blank=False, max_digits=5, decimal_places=2,
        validators=[MinValueValidator(1.00), valiPrice])
    photo = ImageField(blank=False, manual_crop="")

    def __str__(self):
        return self.name
