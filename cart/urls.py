from django.urls import path
import cart.views

urlpatterns = [
    path('', cart.views.view_cart, name='cart_read'),
    path('add/<sticky_id>', cart.views.add_to_cart, name='cart_add'),
]
