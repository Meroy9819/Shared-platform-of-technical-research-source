from django.shortcuts import render
from .models import Notification_report_comment
from User.models import NormalUser
from UserComment.models import Comment
from django.shortcuts import HttpResponse
import json

#创建评论被举报的通知
def create_notofication_report_comment(request,commentuserid,commentid):
    user=NormalUser.objects.filter(user_id=commentuserid)
    comment=Comment.objects.filter(Comment_id=commentid)
    new_notification=Notification_report_comment()
    new_notification.notification_message="你的评论被举报"
    new_notification.notification_status=1
    new_notification.notification_receiver=user
    new_notification.comment=comment
    new_notification.save()
    return HttpResponse()


#阅读了评论被举报的消息
def read_comment_report(request,notification_id):
    if not request.session.get('is_login', None):
        return HttpResponse(json.dumps('请先登录'), content_type='application/json')
    data=Notification_report_comment.objects.filter(notification_comment_id=notification_id)
    data.report_status=2
    data.save()
    return HttpResponse(json.dumps('通知已经更改为已读'),content_type='application/json')


#删除评论被举报的消息
def delete_comment_report(request,notification_id):
    if not request.session.get('is_login', None):
        return HttpResponse(json.dumps('请先登录'), content_type='application/json')
    data=Notification_report_comment.objects.filter(notification_comment_id=notification_id).delete()
    return HttpResponse(json.dumps('通知已经更改为已读'),content_type='application/json')


