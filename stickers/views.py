from django.shortcuts import render
from .models import sticker

# Create your views here.


def sticker_list(request):
    stickers = sticker.objects.all().order_by('-id')
    return render(request, 'stickers/sticker_read-template.html', {
        'stickers': stickers
    })