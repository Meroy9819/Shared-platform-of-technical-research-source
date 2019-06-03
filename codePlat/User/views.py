from User.models import NormalUser, ExpertUser, Administrator, ConfirmString
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from . import models
from .forms import UserForm, RegisterForm,ChangePwForm,ChangeIntro
import hashlib
import json
import codePlat
import datetime
from django.core.mail import EmailMultiAlternatives
from Like.models import LikeResources
#from Report.models import report
from User.models import NormalUser
from rest_framework import status
from django.http import HttpResponse
from django.forms.models import model_to_dict
from Like.models import LikeResources,LikeExpert
from VisitHistory.views import add_visit_resource_history,add_visit_expert_history
from UserComment.models import Comment
from TechResource.models import SciAchi
import codePlat.settings as settings
from User.models import PicTest
#from Report.models import report
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
                if user.passwd == hash_code(password):  # 哈希值和数据库内的值进行比对
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
    return HttpResponse()

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
            phonenumber=register_form.cleaned_data['phonenumber']
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

                new_user = models.NormalUser()
                new_user.name = username
                new_user.passwd = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.phonenumber=phonenumber
                new_user.corresponding_expert_id=0
                new_user.corrsponding_admin_id=0
                new_user.point=0
                new_user.introduction="No yet"
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
# def like_resource(request,resource_id):
#     #判断用户是否登录
#     username = request.session.get('username', '')
#     if not username:
#         return HttpResponseRedirect('/login/')
#     #判断是否收藏
#     try:
#         now_user=NormalUser.objects.get(name=username)
#     except:
#         message = '不存在当前用户'
#         return render(request, 'shoucang.html', locals())
#     try:
#         queryset=LikeResources.objects.get(liker_user=now_user,like_resource_id=resource_id)
#         message = '你已经收藏过该资源'
#         return render(request, 'shoucang.html', locals())
#     except:
#         #往数据库存储收藏信息
#         thislikeinfor = LikeResources(
#             liker_user=now_user,
#             like_resource_id=resource_id
#         )
#         thislikeinfor.save()
#         message = '收藏成功'
#         return render(request, 'shoucang.html', locals())

#用户举报信息
# def report_resource(request,resource_id):
#     #判断用户是否登录
#     username = request.session.get('username', '')
#     if not username:
#         return HttpResponseRedirect('/login/')
#     try:
#         now_user=NormalUser.objects.get(name=username)
#     except:
#         message = '不存在当前用户'
#         return render(request, 'shoucang.html', locals())
#     try:
#         queryset=LikeResources.objects.get(liker_user=now_user,like_resource_id=resource_id)
#         message = '你已经举报过该资源'
#         return render(request, 'shoucang.html', locals())
#     except:
#         #往数据库存储收藏信息
#         thisreportinfor = report(
#             report_user=now_user,
#             report_resource_id=resource_id
#         )
#         thisreportinfor.save()
#         message = '举报成功'
#         return render(request, 'shoucang.html', locals())

#普通用户主页展示信息

def show_user(request):
    #如果尚未登录，则跳转到登录页
    if not request.session.get('is_login', None)!=True:
        #return redirect("/login/login.html")
        print (request.session.get('username',''))
        return HttpResponse(json.dumps("ewt"),content_type='application/json')
    #取出当前用户对象
    #json化所有用户信息
    ret={}
    json_list = []
    user_name=request.GET.get('username','')
    data=NormalUser.objects.filter(username=user_name)
    import base64
    for item in data:
        json_list.append({"id": item.user_id,
                          "img": str(item.image),
                          "name": item.username,
                          "user_type":item.user_type,
                          "introduction":item.introduction ,
                          "sex":item.sex,
                          "email":item.email,
                          "注册时间":str(item.c_time),
                          "手机号":item.phonenumber,

                          })
    #用户对应的评论信息
    comment_user=get_object_or_404(NormalUser,username=user_name)
    all_comment=Comment.objects.filter(CommentUSerid=comment_user)
    for item in all_comment:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    #用户的收藏成果列表
    liker_user=get_object_or_404(NormalUser,username=user_name)
    all_likes=LikeResources.objects.filter(liker_user=liker_user)
    for item in all_likes:
        item_temp=model_to_dict(item)
        json_dict = model_to_dict(item_temp)
        json_list.append(json_dict)
        resource_id=item_temp.like_resource_id.resource_id
        resource=SciAchi.objects.filter(resource_id=resource_id)
        json_dict = model_to_dict(resource)
        json_list.append(json_dict)
    #用户的收藏专家列表
    liker_user=get_object_or_404(NormalUser,username=user_name)
    all_likes=LikeExpert.objects.filter(liker_user=liker_user)
    for item in all_likes:
        item_temp=model_to_dict(item)
        json_dict = model_to_dict(item_temp)
        json_list.append(json_dict)
        expert_id=item_temp.like_expert_id.expert_id
        expert=ExpertUser.objects.filter(expert_id=expert_id)
        json_dict = model_to_dict(expert)
        json_list.append(json_dict)
    #用户的举报成果列表
    report_user=get_object_or_404(NormalUser,username=user_name)
    all_report=report.objects.filter(report_user=report_user)
    for item in all_report:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    #用户的举报专家列表
    all_report=report_expert.objects.filter(report_user=report_user)
    for item in all_report:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    #用户的举报评论列表
    all_report=report_comment.objects.filter(report_user=report_user)
    for item in all_report:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    #用户的访问成果记录
    all_history=VisitResourceHistory.objects.filter(visit_user=report_user)
    for item in all_history:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    #用户的访问专家记录
    all_history=VisitExpertHistory.objects.filter(visit_user=report_user)
    for item in all_history:
        json_dict = model_to_dict(item)
        json_list.append(json_dict)
    ret['data']=json_list
    return HttpResponse(json.dumps(ret), content_type='application/json')
#专家主页展示
def show_expert(request,expert_id):
    add_visit_expert_history(request,expert_id)
    json_list=[]
    #专家的所有个人信息
    expert=get_object_or_404(ExpertUser,expert_id=expert_id)
    json_dict = model_to_dict(expert)
    json_list.append(json_dict)
    return HttpResponse(json.dumps(json_list), content_type='application/json')

#用户修改密码
def change_password(request):
    #如果用户没有登录
    if not request.session.get('is_login', None):
        return HttpResponse(json.dumps('请先登录'),content_type='application/type')
    if request.method == "POST":
        username=request.session.get('username','')
        changepw_form = ChangePwForm(request.POST)
        message = "请检查填写的内容！"
        if changepw_form.is_valid():
            pw1 = changepw_form.cleaned_data['pw1']
            pw2 = changepw_form.cleaned_data['pw2']
            pw3=changepw_form.cleaned_data['pw3']
            try:
                user = models.NormalUser.objects.get(username=username)
                pw_origin=user.passwd
                if hash_code(pw1)==pw_origin:
                    if hash_code(pw2)==hash_code(pw3):
                        user.passwd=hash_code(pw2)
                        user.save()
                        request.session['is_login'] = False
                        return HttpResponse(json.dumps("修改密码成功"),content_type='application/json')
                    else:
                        return HttpResponse(json.dumps("两次输入的密码不相同"),content_type='application/json')
                else:
                    return HttpResponse(json.dumps("原密码输入错误"), content_type='application/json')
            except:
                return HttpResponse(json.dumps("用户不存在"), content_type='application/json')
        return HttpResponse(json.dumps("表格错误"), content_type='application/json')
        changepw_form = ChangePwForm
    return HttpResponse(json.dumps("欢迎修改密码。。"), content_type='application/json')

#用户修改简介
def change_introduction(request):
    #如果用户没有登录
    if not request.session.get('is_login', None):
        return HttpResponse(json.dumps('请先登录'),content_type='application/type')
    if request.method == "POST":
        username=request.session.get('username','')
        changeintro_form = ChangeIntro(request.POST)
        message = "请检查填写的内容！"
        if changeintro_form.is_valid():
            intro=changeintro_form.cleaned_data['intro']
            try:
                user = models.NormalUser.objects.get(username=username)
                user.introduction=intro
                user.save()
            except:
                return HttpResponse(json.dumps("用户不存在"), content_type='application/json')
        return HttpResponse(json.dumps("表格错误"), content_type='application/json')
        changeintro_form = ChangeIntro
    return HttpResponse(json.dumps("欢迎修改个人简介"), content_type='application/json')

def show_upload(request):
    return render(request, 'test/upload.html')



def upload_handle(request):
    pic = request.FILES['pic']
    save_path = '{}/media/{}'.format(settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # 数据库中保存上传记录
    PicTest.objects.create(goods_pic='media/{}'.format(pic.name))
    return redirect('/show_imgs')


def show_imgs(request):
    pics = PicTest.objects.all()
    return render(request,'test/show_imgs.html', {'pics': pics})


import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.six import BytesIO
#显示二维码
def generate_qrcode(request, data):
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    return HttpResponse(image_stream, content_type="image/png")
