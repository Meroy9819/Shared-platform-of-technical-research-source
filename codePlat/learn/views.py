from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')




def test(request):
    context= {}
    context['hello'] = 'Hello Worldhtml!'
    return render(request, 'hello.html', context)
