from django.shortcuts import render
from django.http import HttpResponse
from .generate import generate_web


def index(request):
    """
    if(request.GET.get('genbtn')):
       output = {'shitpost': generate_web()}
       return render(request, 'index.html', context=output)

    else:
       output = {'shitpost': ""}
       return render(request, 'index.html', context=output)
    """
    return render(request, 'index.html', {})

#TODO need to find a way to update the output to screen
"""
def out_gen(request):
    if(request.GET.get('genbtn')):
        return render(request, 'index.html', {'shitpost': generate_web()})
"""
