from django.shortcuts import render

def index_view(request):
    context = {'heading': 'Welcome to Cow Talks'}
    return render(request, 'index.html', context)

def history_view(request):
    context = {'text': 'Cows previous talks'}
    return render(request, 'history.html', context)
