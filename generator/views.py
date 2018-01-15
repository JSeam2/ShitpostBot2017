from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    output = {'shitpost': 'hi'}
    return render(request, 'index.html', context=output)
