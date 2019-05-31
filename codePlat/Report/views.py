from django.shortcuts import render
from User.models import NormalUser, ExpertUser, Administrator, ConfirmString
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from . import models
import json
import datetime
from Report.models import report
from User.models import NormalUser
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Report.models import report,report_comment,report_expert
from .forms import ReportForm
from TechResource.models import SciAchi
from Report.forms import ReportFormExpert
#举报某成果
def create_report(request,resource_id):
    #如果用户没有登录
    if request.session.get('is_login', None)!=True:
        return redirect("/login/login.html")
    if request.method == "POST":
        report_form=ReportForm(request.POST)
        message = "请检查填写的内容！"
        report_user_name = request.session.get('username', '')
        user_temp=get_object_or_404(NormalUser,name=report_user_name)
        resource_temp=get_object_or_404(SciAchi,resource_id=resource_id)
        if report_form.is_valid():  # 获取数据
            new_report=report()
            new_report.report_error=report_form.cleaned_data['Reporttype']
            new_report.report_context=report_form.cleaned_data['ReportContent']
            new_report.report_user=user_temp
            new_report.report_resource_id=resource_temp
            new_report.save()
            return HttpResponse("举报成功", content_type='application/json')
    report_form = ReportForm
    return HttpResponse("哈哈哈哈", content_type='application/json')


#举报某专家
def create_report_expert(request,expert_id):
    #如果用户没有登录
    if request.session.get('is_login', None)!=True:
        return redirect("/login/login.html")
    if request.method == "POST":
        report_form=ReportForm(request.POST)
        message = "请检查填写的内容！"
        report_user_name = request.session.get('username', '')
        user_temp=get_object_or_404(NormalUser,name=report_user_name)
        expert_temp=get_object_or_404(ExpertUser,expert_id=expert_id)
        if report_form.is_valid():  # 获取数据
            new_report=report_expert()
            new_report.report_error=report_form.cleaned_data['Reporttype']
            new_report.report_context=report_form.cleaned_data['ReportContent']
            new_report.report_user=user_temp
            new_report.report_resource_id=expert_temp
            new_report.save()
            return HttpResponse("举报成功", content_type='application/json')
    report_form = ReportFormExpert
    return HttpResponse("哈哈哈哈", content_type='application/json')


#展示成果类的未处理举报信息
def show_resource_report_not(request):
    ret={}
    json_list=[]
    data=models.report.objects.filter(report_status=1)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')

#展示成果类的已处理举报信息
def show_resource_report_ok(request):
    ret={}
    json_list=[]
    data=report.objects.filter(report_status=2)
    data1=report.objects.filter(report_status=3)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    for item in data1:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')


#展示专家类的未处理举报信息
def show_expert_report_not(request):
    ret={}
    json_list=[]
    data=models.report_expert.objects.filter(report_status=1)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')

#展示专家类的已处理举报信息
def show_resource_expert_ok(request):
    ret={}
    json_list=[]
    data=models.report_expert.objects.filter(report_status=2)
    data1=models.report_expert.objects.filter(report_status=3)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    for item in data1:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')

#展示已处理评论举报
def show_resource_comment_ok(request):
    ret={}
    json_list=[]
    data=models.report_comment.objects.filter(report_status=2)
    data1=models.report_comment.objects.filter(report_status=3)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    for item in data1:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')
#展示未处理评论举报
def show_comment_report_not(request):
    ret={}
    json_list=[]
    data=models.report_comment.objects.filter(report_status=1)
    for item in data:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret),content_type='application/json')
#处理成果类举报通过
def agree_resource_report(request,report_id):
    report=report.objects.filter(report_id=report_id)


#处理成果类举报不通过
#处理专家类举报通过
#处理专家类举报不通过
#处理评论类举报通过
#处理评论类举报不通过