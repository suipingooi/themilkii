from django import forms
from .models import sticker


class StickForm(forms.ModelForm):
    class Meta:
        model = sticker
        fields = {
            'name',
            'description',
            'price',
            'photo',
        }
    field_order = [
        'name',
        'description',
        'price',
        'photo',
    ]
