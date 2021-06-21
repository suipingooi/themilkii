def basket(request):
    cart = request.session.get('basket', {})
    return {
        'basket': cart,
        'num_items': len(cart)
    }