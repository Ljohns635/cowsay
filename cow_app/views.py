from django.shortcuts import render
from cow_app.models import CowText

def index_view(request):
    context = {'heading': 'Welcome to Cow Talks'}
    return render(request, 'index.html', context)

def history_view(request):
    words = CowText.objects.all().order_by('-id')[:10][::-1]
    context = {'text': 'Cows previous talks', 'words': words }
    return render(request, 'history.html', context)
