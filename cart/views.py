from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from stickers.models import sticker
# Create your views here.


def add_to_cart(request, sticky_id):
    cart = request.session.get('basket', {})
    sticky = get_object_or_404(sticker, pk=sticky_id)

    if sticky_id not in cart:
        cart[sticky_id] = {
            'id': sticky_id,
            'item': sticky.name + " | " + sticky.description,
            'price': float(sticky.price),
            'quantity': 1,
            'total': float(sticky.price),
            'photo': str(sticky.photo),
        }
    else:
        cart[sticky_id]['quantity'] += 1
        cart[sticky_id]['total'] += float(sticky.price)

    request.session['basket'] = cart

    messages.info(request, 'Item added into your basket')
    return redirect(reverse('stickerlist'))


def view_cart(request):
    cart = request.session.get('basket', {})
    return render(request, 'cart/basket_view-template.html', {
        'cart': cart,
    })
