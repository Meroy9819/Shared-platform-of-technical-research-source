from User.models import NormalUser, ExpertUser, Administrator, ConfirmString
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from . import models
from .forms import UserForm, RegisterForm
import hashlib
import json
import codePlat
import datetime
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from .models import LikeResources
from User.models import NormalUser
from rest_framework import status

#加密密码
def hash_code(s, salt='codeplat_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

#主页
def index(request):
    pass
    return render(request, 'login/index.html')

#用户登录
def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.NormalUser.objects.get(name=username)
                if not user.has_confirmed:
                    message = "该用户还未通过邮件确认！"
                    return render(request, 'login/login.html', locals())
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm
    return render(request, 'login/login.html', locals())

#用户注册
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form =RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            phonenumber=register_form.changed_data['phonenumber']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.NormalUser.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.NormalUser.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                    # 当一切都OK的情况下，创建新用户

                new_user = models.NormalUser()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.phonenumber=phonenumber
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往注册邮箱，进行邮件确认！'
                return render(request, 'login/confirm.html', locals())  # 跳转到等待邮件确认页面。
    register_form = RegisterForm
    return render(request, 'login/register.html', locals())

#用户注册验证
def make_confirm_string(NormalUser):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(NormalUser.name, now)
    ConfirmString.objects.create(code=code, user=NormalUser)
    return code


#发送验证邮件
def send_email(email, code):
    subject = '来自最棒的妙妙的测试邮件'
    from_email='miaoran9819@163.com'
    to=email
    text_content = '请回答：妙妙是不是最棒！'
    #服务器来了以后的注册地址
    html_content = '<p>欢迎注册<a href="http://{}/confirm/?code={}" target="blank>www.xxx.com</a>我滴网站</a>，hhhhhhhhhhhhhhh</p>'.format(
            '127.0.0.1', code, codePlat.settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("<h1>邮件发送成功!</h1>")

#用户注册条件判断
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())
    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(codePlat.settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())

#用户登出
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()

    return redirect('/index/')

#显示主页，用于测试
def base(request):
    pass
    return render(request,'login/base.html')

#用户收藏资源
def like_resource(request,resource_id):
    #判断用户是否登录
    username = request.session.get('username', '')
    if not username:
        return HttpResponseRedirect('/login/')
    #判断是否收藏
    try:
        now_user=NormalUser.objects.get(name=username)
    except:
        return HttpResponse("不存在当前用户", status=status.HTTP_406_NOT_ACCEPTABLE)
    try:
        queryset=LikeResources.objects.get(liker_user=now_user,like_resource_id=resource_id)
        return HttpResponse("你已经收藏过该资源")
    except:
        #往数据库存储收藏信息
        thislikeinfor = LikeResources(
            liker_user=now_user,
            like_resource_id=resource_id
        )
        thislikeinfor.save()

