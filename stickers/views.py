from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import sticker
from .forms import StickForm
from django.contrib import messages
# Create your views here.


def sticker_list(request):
    stickers = sticker.objects.all().order_by('-id')
    return render(request, 'stickers/sticker_read-template.html', {
        'stickers': stickers
    })


def sticker_add(request):
    if request.method == 'POST':
        stick_form = StickForm(request.POST)
        if stick_form.is_valid():
            stick_form.save()
            messages.success(request, 'New Sticker Pack Added')
            return redirect(reverse(sticker_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'stickers/sticker_add-template.html', {
                'form': stick_form
            })
    else:
        stick_form = StickForm()
        return render(request, 'stickers/sticker_add-template.html', {
            'form': stick_form
        })


def sticker_del(request, sticky_id):
    sticky_to_delete = get_object_or_404(sticker, pk=sticky_id)
    if request.method == "POST":
        sticky_to_delete.delete()
        messages.success(request, 'Sticker Pack Entry Deleted')
        return redirect(sticker_list)
    else:
        messages.warning(request, 'DELETE action cannot be undone')
        return render(request, 'stickers/sticker_del-template.html', {
            'sticky': sticky_to_delete,
        })


def sticker_edit(request, sticky_id):
    sticky_to_edit = get_object_or_404(sticker, pk=sticky_id)
    if request.method == "POST":
        stick_form = StickForm(request.POST, instance=sticky_to_edit)
        if stick_form.is_valid():
            stick_form.save()
            messages.success(request, 'Sticker Pack Entry Listing Updated')
            return redirect(reverse(sticker_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'stickers/sticker_edit-template.html', {
                'form': stick_form,
                'sticky': sticky_to_edit
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        stick_form = StickForm(instance=sticky_to_edit)
        return render(request, 'stickers/sticker_edit-template.html', {
            'form': stick_form,
            'sticky': sticky_to_edit
        })
