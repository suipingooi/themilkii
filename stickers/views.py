from django.shortcuts import render

# Create your views here.


def product_listing(request):
    return render(request, 'stickers/sticker_read-template.html')