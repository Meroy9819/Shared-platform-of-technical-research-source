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
from VisitHistory.views import add_visit_resource_history,add_visit_expert_history
from .forms import SciAchiForm
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
    add_visit_resource_history(request,resource_id)
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

#上传一个科技成果
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

# def create_SciAchi(request):
#     #如果没有登录
#     if not request.session.get('is_login', None):
#         return HttpResponse(json.dumps("您尚未登录"),content_type='application/type')
#     if request.method == "POST":
#         sciachi_form = SciAchiForm(request.POST)
#         message = "请检查填写的内容！"
#         if sciachi_form.is_valid():  # 获取数据
#             create_name = sciachi_form.cleaned_data['create_name']
#             passw = register_form.cleaned_data['password1']
#             password2 = register_form.cleaned_data['password2']
#             email = register_form.cleaned_data['email']
#             sex = register_form.cleaned_data['sex']
#             phonenumber = register_form.cleaned_data['phonenumber']
#             if password1 != password2:  # 判断两次密码是否相同
#                 message = "两次输入的密码不同！"
#                 return render(request, 'login/register.html', locals())
#             else:
#                 same_name_user = models.NormalUser.objects.filter(name=username)
#                 if same_name_user:  # 用户名唯一
#                     message = '用户已经存在，请重新选择用户名！'
#                     return render(request, 'login/register.html', locals())
#                 same_email_user = models.NormalUser.objects.filter(email=email)
#                 if same_email_user:  # 邮箱地址唯一
#                     message = '该邮箱地址已被注册，请使用别的邮箱！'
#                     return render(request, 'login/register.html', locals())
#
#                 new_user = models.NormalUser()
#                 new_user.name = username
#                 new_user.passwd = hash_code(password1)  # 使用加密密码
#                 new_user.email = email
#                 new_user.sex = sex
#                 new_user.phonenumber = phonenumber
#                 new_user.corresponding_expert_id = 0
#                 new_user.corrsponding_admin_id = 0
#                 new_user.point = 0
#                 new_user.introduction = "No yet"
#                 new_user.save()
#
#                 code = make_confirm_string(new_user)
#                 send_email(email, code)
#
#                 message = '请前往注册邮箱，进行邮件确认！'
#                 return render(request, 'login/confirm.html', locals())  # 跳转到等待邮件确认页面。
#     register_form = RegisterForm
#     return render(request, 'login/register.html', locals())
#
