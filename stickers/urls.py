from django.urls import path
import stickers.views

urlpatterns = [
    path('stickers', stickers.views.sticker_list, name='stickerlist'),
]