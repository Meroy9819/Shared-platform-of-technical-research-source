from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from . import models
import json
from User.models import NormalUser
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Like.models import LikeResources,LikeExpert
from User.models import ExpertUser
from TechResource.models import SciAchi

# Create your views here.
#接受收藏
def create_like(request,resource_id):
    #如果用户没有登录
    if not request.session.get('is_login', None):
        return redirect("/login/login.html")
    #取当前用户名
    username=request.session.get('username','')
    liker_user=get_object_or_404(NormalUser,name=username)
    like_resource=get_object_or_404(SciAchi,resource_id=resource_id)
    #查询是否数据库中已经有收藏信息
    query_like=LikeResources.objects.get(liker_user=liker_user,like_resource_id=like_resource)
    if query_like:
        message="你已经收藏过该资源"
        return HttpResponse(json.dumps(message),content_type='application/json')
    new_like=LikeResources()
    new_like.liker_user=liker_user
    new_like.like_resource_id=like_resource
    new_like.save()
    return HttpResponse("收藏成功", content_type='application/json')

#取消收藏
def delete_like(request,resource_id):
    user=request.session.get('username','')
    user=get_object_or_404(NormalUser,name=user)
    resource=get_object_or_404(SciAchi,resource_id=resource_id)
    ok=models.LikeResources.objects.filter(liker_user=user,like_resource_id=resource).delete()
    if ok:
        return HttpResponse(json.dumps("删除成功"),content_type='application/json')
    else:
        return HttpResponse(json.dumps("取消收藏失败"),content_type='application/json')

#接受收藏专家
def create_like_expert(request,expert_id):
    #如果用户没有登录
    if not request.session.get('is_login', None):
        return redirect("/login/login.html")
    #取当前用户名
    username=request.session.get('username','')
    liker_user=get_object_or_404(NormalUser,name=username)
    like_expert=get_object_or_404(ExpertUser,expert_id=expert_id)
    #查询是否数据库中已经有收藏信息
    query_like=LikeExpert.objects.get(liker_user=liker_user,like_expert_id=like_expert)
    if query_like:
        message="你已经收藏过该专家"
        return HttpResponse(json.dumps(message),content_type='application/json')
    new_like=LikeExpert()
    new_like.liker_user=liker_user
    new_like.like_resource_id=like_expert
    new_like.save()
    return HttpResponse("收藏成功", content_type='application/json')

#取消收藏
def delete_like_expert(request,expert_id):
    user=request.session.get('username','')
    user=get_object_or_404(NormalUser,name=user)
    expert=get_object_or_404(ExpertUser,expert_id=expert_id)
    ok=models.LikeExpert.objects.filter(liker_user=user,like_expert_id=expert).delete()
    if ok:
        return HttpResponse(json.dumps("删除成功"),content_type='application/json')
    else:
        return HttpResponse(json.dumps("取消收藏失败"),content_type='application/json')
