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
    data = [
        {"id": 1, "name": "中原工学院", "address": "河南省郑州市"},
        {"id": 2, "name": "山西大学", "address": "山西省太原市"},
        {"id": 3, "name": "太原理工大学", "address": "山西省太原市"},
        {"id": 4, "name": "北京邮电大学", "address": "北京市"},
        {"id": 5, "name": "西北农林科技大学", "address": "陕西省"},
        {"id": 6, "name": "长春工业大学", "address": "吉林省长春市"},
    ]
    return render(request, 'techResource.html', data)



def test(request):
    context= {}
    context['hello'] = 'Hello Worldhtml!'
    return render(request, 'hello.html', context)
