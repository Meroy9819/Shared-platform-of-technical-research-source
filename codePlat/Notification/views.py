from django.shortcuts import render
from .models import Notification_report_comment
from User.models import NormalUser
from UserComment.models import Comment
from django.shortcuts import HttpResponse,get_object_or_404
import json

#创建评论被举报的通知
#通知用户，他的评论被人举报
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
    data=Notification_report_comment.objects.filter(notification_comment_id=notification_id)
    if data.report_status==1:
        HttpResponse(json.dumps('您尚未阅读过此消息'), content_type='application/json')
    else:
        return HttpResponse(json.dumps('通知已经被删除'),content_type='application/json')

#通知用户，被举报的评论已经被管理员删除
#通知举报人：你的举报已通过
#通知评论人：你的评论已经被删除
#user_id 是举报人的id
def reported_comment_delete(request,Comment_id,user_id):
    report_user=get_object_or_404(NormalUser,user_id=user_id)
    reported_comment=get_object_or_404(Comment,Comment_id=Comment_id)

    new_notification1=Notification_report_comment()
    new_notification1.notification_message="您举报的评论已经被删除"
    new_notification1.notification_receiver=report_user
    new_notification1.notification_comment_from=reported_comment
    new_notification1.notification_status=1
    new_notification1.save()

    reporter=reported_comment.report_user
    new_notification2 =Notification_report_comment()
    new_notification2.notification_message="您的评论因被人举报，经审核后，已经被删除"
    new_notification2.notification_receiver=reporter
    new_notification2.notification_comment_from=reported_comment
    new_notification2.notification_status=1
    new_notification2.save()
    return HttpResponse(json.dumps("评论删除通知发送成功"),content_type='application/json')


#通知用户，被举报的评论未被管理员认可，仍旧保留
#通知举报人：你的举报已被驳回
#通知评论人：你的评论仍旧保留
#user_id 是举报人的id
def reported_comment_delete(request,Comment_id,user_id):
    report_user=get_object_or_404(NormalUser,user_id=user_id)
    reported_comment=get_object_or_404(Comment,Comment_id=Comment_id)
#通知举报人
    new_notification1=Notification_report_comment()
    new_notification1.notification_message="您举报的评论经管理员审核，符合国家法律法规条例，内容健康向上，举报予以驳回"
    new_notification1.notification_receiver=report_user
    new_notification1.notification_comment_from=reported_comment
    new_notification1.notification_status=1
    new_notification1.save()
#通知被举报用户
    reporter=reported_comment.report_user
    new_notification2 =Notification_report_comment()
    new_notification2.notification_message="您的评论虽然被人举报，但是经过正义的管理员审核，认为并无不妥之处，故予以保留"
    new_notification2.notification_receiver=reporter
    new_notification2.notification_comment_from=reported_comment
    new_notification2.notification_status=1
    new_notification2.save()
    return HttpResponse(json.dumps("评论被驳回通知发送成功"),content_type='application/json')


