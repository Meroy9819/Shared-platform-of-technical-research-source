from django.db import models
from User.models import NormalUser
from UserComment.models import Comment
from TechResource.models import SciAchi
from Apply.models import Apply,Verification
# Create your models here.
class Notification_report_comment(models.Model):
    notification_comment_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #被举报评论来源
    notification_comment_from=models.ForeignKey(Comment,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username + ":   " + self.report_expert_id.name

    class Meta:
        verbose_name = "评论通知"
        verbose_name_plural = "评论通知"


class Notification_report_SciAchi(models.Model):
    notification_sciachi_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #被举报评论来源
    notification_sciachi_from=models.ForeignKey(SciAchi,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username + ":   " + self.report_expert_id.name

    class Meta:
        verbose_name = "成果通知"
        verbose_name_plural = "成果通知"


class Notification_report_expert(models.Model):
    notification_expert_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #被举报评论来源
    notification_expert_from=models.ForeignKey(SciAchi,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username + ":   " + self.report_expert_id.name

    class Meta:
        verbose_name = "专家通知"
        verbose_name_plural = "专家通知"

class Notification_apply_expert(models.Model):
    notification_applyexpert_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #对应的申请信息
    notification_apply_from=models.ForeignKey(Apply,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username

    class Meta:
        verbose_name = "申请成为专家通知"
        verbose_name_plural = "申请成为专家通知"

class Notification_apply_expert(models.Model):
    notification_applyexpert_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #对应的申请信息
    notification_apply_from=models.ForeignKey(Apply,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username

    class Meta:
        verbose_name = "申请成为专家通知"
        verbose_name_plural = "申请成为专家通知"


class Notification_verification_expert(models.Model):
    notification_verifiyxpert_id=models.AutoField(primary_key=True,)
    notification_message=models.CharField(max_length=100)
    #谁收到这个通知
    notification_receiver=models.ForeignKey(NormalUser,on_delete=True)
    #对应的申请信息
    notification_verification_from=models.ForeignKey(Apply,on_delete=True)
    #表示通知的状态
    #1 表示未读
    #2 表示已读
    notification_status=models.IntegerField(default=1)
    notification_sendtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_receiver.username

    class Meta:
        verbose_name = "申请成为专家通知"
        verbose_name_plural = "申请成为专家通知"