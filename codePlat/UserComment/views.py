from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from rest_framework import viewsets, response
from TechResource.models import SciAchi
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from TechResource.models import SciAchi
from .forms import CommentForm
from User.models import NormalUser
from .models import Comment
from . import models
import json

#创建评论
def create_comment(request,resource_id):
    #如果用户没有登录的话，直接跳转回主页
    if not request.session.get('is_login', None):
        #取前端传来的表格
        return redirect("/index/")
    haha="1"
    #message=request.method
    #return render(request,'comment/comment.html', locals())
    if request.method == "POST":
        haha = "2"
        comment_form = CommentForm(request.POST)
        message="请检查填写的内容"
        if comment_form.is_valid():  # 获取数据
            haha = "3"
            CommentTitle=comment_form.cleaned_data['CommentTitle']
            CommentContent=comment_form.cleaned_data['CommentTitle']
            try:
                paper=SciAchi.objects.get(resource_id=resource_id)
            except:
                message = '无相应编号的论文'
                return render(request, 'comment/comment.html', locals())
            try:
                username=request.session.get['username']
                user=NormalUser.objects.get(name=username)
            except:
                message = '无相应编号的用户'
                return render(request, 'comment/comment.html', locals())
            new_comment=CommentForm()
            new_comment.CommentContent=CommentContent
            new_comment.CommentTitle=CommentTitle
            new_comment.CommentUSerid=user
            new_comment.CommentResourceid=paper
            new_comment.save()
            message='评论成功'
            return render(request, 'comment/comment.html', locals())
    comment_form = CommentForm
    message="no 2"
    return render(request, 'comment/comment.html', locals())

def comment_success(request):
    message="hahahahcommentsuccess"
    return render(request,"comment/commentsuccess.html",locals())

def delete_comment(request,Comment_id):
    comment=get_object_or_404(Comment,Comment_id=Comment_id)
    if comment:
        delete_ok=models.Comment.objects.filter(Comment_id=Comment_id).delete()
        if delete_ok:
            message="删除评论成功"
            return HttpResponse(json.dumps(message),content_type='application/json')
        else:
            message="删除评论失败"
            return HttpResponse(json.dumps(message),content_type='application/json')
    else:
        message="没有该条评论"
        return HttpResponse(json.dumps(message),content_type='application/json')


