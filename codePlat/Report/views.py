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
from .forms import ReportForm
from TechResource.models import SciAchi
from Report.forms import ReportFormExpert,changeSciAchiForm,ChangeExpertForm
from Report.models import report,report_expert,report_comment
from UserComment.models import Comment
import Notification.views as Notification_views
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



#处理成果类举报通过(修改）
def agree_resource_report(request,report_id):
    #被处理的举报
    report=models.report.objects.filter(report_id=report_id)
    resource=get_object_or_404(SciAchi,resource_id=report.report_resource_id.resource_id)
    if request.method == "POST":
        changeForm=changeSciAchiForm(request.POST)
        if changeForm.is_valid():
            type = changeForm.cleaned_data['Reporttype']
            content = changeForm.cleaned_data['changeContent']
            if type=='标题错误':
                resource.name=content
                resource.save()
            if type=='作者错误':
                resource.author = content
                resource.save()
            if type=='关键词错误':
                resource.keywordSeq = content
                resource.save()
            if type=='发表年份错误':
                resource.publishYear = content
                resource.save()
            if type=='摘要错误':
                resource.abstract = content
                resource.save()
            report.report_status=2
            report.save()
            #修改完以后自动给相关用户发消息
            Notification_views.agree_SciAchi_report_agree(request,report.report_resource_id.resource_id,report.report_user.user_id)
            return HttpResponse(json.dumps("修改成功"),content_type='application/json')
        return HttpResponse(json.dumps("表格出了点问题"),content_type='application/json')
    changeForm = changeSciAchiForm
    return HttpResponse(json.dumps("哈哈"), content_type='application/json')

#处理成果类举报通过(删除）
def agree_resource_report_delete(request,report_id):
    report=models.report.objects.filter(report_id=report_id)
    resource_id=report.report_resource_id.resource_id
    resource=SciAchi.objects.filter(resource_id=resource_id)
    resource.delete()
    report.report_status = 2
    report.save()
    Notification_views.agree_SciAchi_report_delete(request, report.report_resource_id.resource_id,
                                                  report.report_user.user_id)
    return HttpResponse(json.dumps("成果已经被删除"),content_type='application/json')



#处理成果类举报不通过
def notagree_resource_report(request,report_id):
    report=models.report.objects.filter(report_id=report_id)
    report.report_status = 3
    report.save()
    Notification_views.notagree_SciAchi_report(request, report.report_resource_id.resource_id,
                                                  report.report_user.user_id)
    return HttpResponse(json.dumps("举报已经被驳回"), content_type='application/json')


#处理专家类举报通过（修改）
def agree_expert_report(request,report_id):
    #被处理的举报
    report=models.report.objects.filter(report_id=report_id)
    expert=get_object_or_404(ExpertUser,expert_id=report.report_expert_id.expert_id)
    if request.method == "POST":
        changeForm=ChangeExpertForm(request.POST)
        if changeForm.is_valid():
            type = changeForm.cleaned_data['Reporttype']
            content = changeForm.cleaned_data['changeContent']
            if type=='姓名错误':
                expert.name=content
                expert.save()
            if type=='所在机构错误':
                expert.institution = content
                expert.save()
            if type=='论文发表数量错误':
                expert.paper_number = content
                expert.save()
            if type=='H指数':
                expert.H_index= content
                expert.save()
            if type=='G指数':
                expert.G_index = content
                expert.save()
            if type=='领域错误':
                expert.field = content
                expert.save()
            report.report_status=2
            report.save()
            #修改完以后自动给相关用户发消息
            Notification_views.agree_expert_report_agree(request,report.report_expert_id.expert_id,report.report_user.user_id)
            return HttpResponse(json.dumps("修改成功"),content_type='application/json')
        return HttpResponse(json.dumps("表格出了点问题"),content_type='application/json')
    changeForm = ChangeExpertForm
    return HttpResponse(json.dumps("哈哈"), content_type='application/json')

#处理专家类举报通过（删除）
def agree_expert_report_delete(request,report_id):
    report=models.report_expert.objects.filter(report_id=report_id)
    expert_id=report.report_expert_id.expert_id
    expert=SciAchi.objects.filter(expert_id=expert_id)
    expert.delete()
    report.report_status = 2
    report.save()
    Notification_views.agree_expert_report_delete(request, report.report_expert_id.expert_id,
                                                  report.report_user.user_id)
    return HttpResponse(json.dumps("成果已经被删除"),content_type='application/json')


#处理专家类举报不通过
def notagree_expert_report(request,report_id):
    report=models.report_expert.objects.filter(report_id=report_id)
    report.report_status = 3
    report.save()
    Notification_views.notagree_SciAchi_report(request, report.report_expert_id.expert_id,
                                                  report.report_user.user_id)
    return HttpResponse(json.dumps("举报已经被驳回"), content_type='application/json')


#处理评论类举报通过
def agree_comment_report(request,report_id):
    report_forcomment=models.report.objects.filter(report_id=report_id)
    Comment_id=report_forcomment.report_comment_id.Comment_id
    comment=Comment.objects.filter(Comment_id=Comment_id)
    user_id=comment.report_user.user_id
    comment.delete()
    report_forcomment.report_status=2
    report_forcomment.save()
    Notification_views.reported_comment_delete(request,Comment_id,user_id)
    return HttpResponse(json.dumps("删除评论成功"),content_type='application/json')


#处理评论类举报不通过
def not_agree_comment_report(request,report_id):
    report_forcomment=models.report.objects.filter(report_id=report_id)
    Comment_id=report_forcomment.report_comment_id.Comment_id
    comment=Comment.objects.filter(Comment_id=Comment_id)
    user_id=comment.report_user.user_id
    report_forcomment.report_status=3
    report_forcomment.save()
    Notification_views.reported_comment_delete(request,Comment_id,user_id)
    return HttpResponse(json.dumps("删除评论成功"),content_type='application/json')