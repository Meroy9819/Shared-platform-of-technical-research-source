from django.shortcuts import render
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
from User.models import NormalUser
from rest_framework import status
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Like.models import LikeResources
from BuyResource.models import BuyResources
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
    liker_user=get_object_or_404(NormalUser,name=user)
    resource=get_object_or_404(SciAchi,SciAchi,resource_id=resource_id)
    ok=models.LikeResources.objects.filter(liker_user=user,like_resource_id=resource).delete()
    if ok:
        return HttpResponse(json.dumps("删除成功"),content_type='application/json')
    else:
        return HttpResponse(json.dumps("取消收藏失败"),content_type='application/json')

