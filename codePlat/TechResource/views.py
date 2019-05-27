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
from django.forms.models import model_to_dict

def ajax_submit(request):
    ret = {'status': True, 'error': ""}
    print(request.POST)
    j_ret = json.dumps(ret)
    return HttpResponse(j_ret)

def list_all(request):
    json_list=[]
    data = SciAchi.objects.all()
    from django.forms.models import model_to_dict
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    from django.http import HttpResponse
    return HttpResponse(json.dumps(json_list),content_type='application/json')

    # temp=list(data)
    # return render(request, 'techResource.html', {'data': json.dumps(temp)})

def list_one(self,request,resource_id):
   # data=get_object_or_404(SciAchi,resource_id=resource_id)
    data=[1,2,3,4]
    temp=list(data)
    return render(request, 'techDetail.html', {'data': json.dumps(temp)})

def testVue(request):
    data = SciAchi.objects.all()
    return render(request, 'index.html', {'data': data})
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

