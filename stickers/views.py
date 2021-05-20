from django.shortcuts import render, HttpResponse

# Create your views here.


def product_listing(request):
    return HttpResponse('stickerlist')
