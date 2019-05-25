from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
#from label.models import label
from TechResource.models import SciAchi
from TechResource.serializers import SciAchiSerializer
from User.serializers import NormalUserSerializer
from User.serializers import ExpertSerializer
from collections import OrderedDict
from django.shortcuts import render, get_object_or_404,render_to_response,HttpResponse
import json
from django.http import HttpResponse
from django.forms.models import model_to_dict

def ajax_submit(request):
    ret = {'status': True, 'error': ""}
    print(request.POST)
    j_ret = json.dumps(ret)
    return HttpResponse(j_ret)

#展示所有在数据库中的论文
def list_all(request):
    json_list=[]
    data = SciAchi.objects.all()
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    #HttpResponse.setHeader("Access-Control-Allow-Origin", "*");
    return HttpResponse(json.dumps(json_list),content_type='application/json')

    # temp=list(data)
    # return render(request, 'techResource.html', {'data': json.dumps(temp)})

#展示一个指定了resource_id的论文
#包括论文数据和评论数据
def list_one(self,request,resource_id):
    #科技资源数据
    json_list = []
    data=get_object_or_404(SciAchi,resource_id=resource_id)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    #评论数据
    paper = SciAchi.objects.get(resource_id=resource_id)
    all_comment=paper.Comment_set().all()
    for item in all_comment:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    return HttpResponse(json.dumps(json_list), content_type='application/json')

def test(request):
    return render(request, 'ajax.html')

def ajax(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print("ok")
        status = 1
        result = "sucuss"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result,
            "name": name
        }))

def create(request):
    sciAchi_serializer = SciAchiSerializer(data=request.data)
    if sciAchi_serializer.is_valid():
        thissciAchi = SciAchi(
            name=request.data.get("name"),
            sciAchiUrl=request.data.get("path"),
            abstract=request.data.get("abstract"),
            keywordSeq=request.data.get("keyword"),
            price=request.data.get("value"),
         )
        thissciAchi.save()
        return Response(thissciAchi.resource_id, status=status.HTTP_201_CREATED)
    return Response(sciAchi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

