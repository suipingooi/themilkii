from django.urls import path
import stickers.views

urlpatterns = [
    path('listing', stickers.views.sticker_list, name='stickerlist'),
    path('add', stickers.views.sticker_add, name='add_sticker'),
    path('delete/<sticky_id>', stickers.views.sticker_del, name='del_sticker'),
    path('edit/<sticky_id>', stickers.views.sticker_edit, name='edit_sticker'),
]
