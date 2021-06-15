from django.shortcuts import render, reverse, redirect
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