from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def add(request):
    #需要传值：?a=2&b=5
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def index1(request):
    context= {}
    context['hello'] = 'Hello Worldfd!'
    return render(request, 'testlearn.html', context)



def test(request):
    context= {}
    context['hello'] = 'Hello Worldhtml!'
    return render(request, 'hello.html', context)
