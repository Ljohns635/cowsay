from django.shortcuts import render, HttpResponseRedirect, reverse
from cow_app.models import CowText
from cow_app.forms import CowTextForm
import subprocess

def index_view(request):
    context = {}
    if request.method == 'POST':
        form = CowTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowText.objects.create(
                speak = data['speak']
            )
            return HttpResponseRedirect(request.path_info)
           
    form = CowTextForm()
    context.update({'form': form})
    return render(request, 'index.html', context)


def history_view(request):
    words = CowText.objects.all().order_by('-id')[:10][::-1]
    context = {'text': 'Cows previous talks', 'words': words }
    return render(request, 'history.html', context)


    

