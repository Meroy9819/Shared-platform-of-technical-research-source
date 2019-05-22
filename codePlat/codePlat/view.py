from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context= {}
    context['hello'] = 'Hello Worldhhhhhh!'
    return render(request, 'helloworld.html', context)