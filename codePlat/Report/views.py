from django.shortcuts import render
from User.models import NormalUser, ExpertUser, Administrator, ConfirmString
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from . import models
import hashlib
import json
import codePlat
import datetime
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from Like.models import LikeResources
from Report.models import report
from User.models import NormalUser
from rest_framework import status
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Like.models import LikeResources
from Report.models import report
from .forms import ReportForm
from TechResource.models import SciAchi
#举报某资源
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
            new_report=models.report()
            new_report.report_context=report_form.cleaned_data['ReportContent']
            new_report.report_user=user_temp
            new_report.report_resource_id=resource_temp
            new_report.save()
            return HttpResponse("举报成功", content_type='application/json')
    report_form = ReportForm
    return HttpResponse("哈哈哈哈", content_type='application/json')
