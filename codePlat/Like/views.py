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
from Report.models import report
from User.models import NormalUser
from rest_framework import status
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Like.models import LikeResources
from BuyResource.models import BuyResources
from Report.models import report
from TechResource.models import SciAchi
# Create your views here.
#接受收藏
def create_like(request,resource_id):
    #如果用户没有登录
    if request.session.get('is_login', None)!=True:
        return redirect("/login/login.html")
    username=request.session.get('username','')
    liker_user=get_object_or_404(NormalUser,name=username)
    like_resource=get_object_or_404(SciAchi,resource_id=resource_id)
    new_like=LikeResources()
    new_like.liker_user=liker_user
    new_like.like_resource_id=like_resource
    new_like.save()
    return HttpResponse("收藏成功", content_type='application/json')
