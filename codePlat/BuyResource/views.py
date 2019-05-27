from django.shortcuts import render
from .models import BuyResources
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
from .models import BuyResources
# Create your views here.
# 创建交易信息
def create_transaction(request,resource_id):
    #如果用户没有登录
    if request.session.get('is_login', None)!=True:
        return redirect("/login/login.html")
    username=request.session.get('username','')
    buy_user=get_object_or_404(NormalUser,name=username)
    buy_resource=get_object_or_404(SciAchi,resource_id=resource_id)
    new_buy=BuyResources()
    new_buy.buyer_id=buy_user
    new_buy.buy_resource_id=buy_resource
    new_buy.save()
    return HttpResponse("购买成功", content_type='application/json')